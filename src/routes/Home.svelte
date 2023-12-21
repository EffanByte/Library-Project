<script>
    import { onMount } from 'svelte';
    import { push } from "svelte-spa-router";
    import {user, loggedIn, pdfDataStore } from "../components/store.js";
    import { createEventDispatcher } from 'svelte';
    import { get } from 'svelte/store';
    import PDFObject from "pdfobject";


    let greeting;
    let lastReadBook = [];
    let lastReadBookCoverImage = '';

    onMount(() => {
        updateGreeting();
        getLastReadBook();
    });

    
    function updateGreeting() {
        const hour = new Date().getHours();
        if (hour < 12) {
            greeting = 'Good Morning';
        } else if (hour < 18) {
            greeting = 'Good Afternoon';
        } else {
            greeting = 'Good Evening';
        }
    }

function gotoCatalogue()
{
    push("/Catalogue");
}
function gotoRoom(){
    //push("/Room");
    if ($user.username) 
    {
        push("/Room");
    }
    else
    {
        alert("Please sign in first!");
    }
}
function gotoLost(){
    push("/LostFound");
 
}
function gotoComplaint(){
    if ($user.username) 
    {
        push("/Complaint")
    }
    else
    {
        alert("Please sign in first!");
    }
    
}




async function getLastReadBook() {
    console.log("Entered getLastReadBook()");
    const loggedInUser = get(user);
    console.log(user);
    if (user.username != '' && user.id != 0) {
        console.log("Entered first if condition")
        try {
            // Ensure that loggedInUser.id is an integer.
            const userId = parseInt(loggedInUser.id, 10);
            // Check if userId is a valid integer.
            if (isNaN(userId)) {
                throw new Error('Invalid user ID');
            }

            // Fetch the last book read data using the user ID.
            const response = await fetch(`http://localhost:8000/api/getLastBookRead?id=${userId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch last read book');
            }

            const lastBookReadData = await response.json();
            lastReadBook = lastBookReadData;
            if (lastBookReadData && lastBookReadData.coverImage) {
                lastReadBookCoverImage = `data:image/jpeg;base64,${lastBookReadData.coverImage}`;
            }
        } catch (error) {
            console.error('Error:', error.message);
        }
    }
}


   /*function openLastReadBookPDF() {
        if (lastReadBook && lastReadBook.PDF) {
            const pdfData = `data:application/pdf;base64,${lastReadBook.PDF}`;
            window.open(pdfData);
        }

    }*/

    /*function openLastReadBookPDF() {
    if (lastReadBook && lastReadBook.PDF) {
        const pdfData = `data:application/pdf;base64,${lastReadBook.PDF}`;
        PDFObject.embed(pdfData, ".pdf-container"); // Use a dedicated container for the PDF
    }
}*/
function openLastReadBookPDF() {
    if (lastReadBook && lastReadBook.PDF) {
        pdfDataStore.set(lastReadBook.PDF); // Set the PDF data in the store
        push('/BookPDF'); // Navigate to the BookPDF route
    }
}

    $: if ($user && $user.id) {
  getLastReadBook();
}



</script>

<div class="container">
    <div class="row">
        <div class="col-md-6 mt-3">
            <div class="greeting mb-4">
                {#if $user.username == ''}
                    <h2>{greeting}, Guest!</h2>
                {:else}
                    <h2>{greeting}, {$user.username}!</h2>
                {/if}
            </div>
        </div>
        {#if $user.username != ''}
        <div class="col-md-6">
            <div class="d-flex flex-column align-items-center justify-content-center mt-4 spa">
                <img src={lastReadBookCoverImage} alt="Last Read Book" class="effimg">
                <button on:click={openLastReadBookPDF} class="btn btn-primary mt-2 mb-3">Continue Reading Last Book</button>
            </div>
        </div>
    {/if}
    
        </div>

        

    <div class="row">
    <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="bookimg.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Browse Catalogue</h5>
        <p class="card-text">Check out all the books in our library here.</p>
        <button on:click={gotoCatalogue} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
        <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="conferenceimg.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Room Rental</h5>
        <p class="card-text">Rent a conference room for all your meetings.</p>
        <button on:click = {gotoRoom} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
  <div class="col-lg-4 mb-4">
  <div class="card">
      <img src="https://images.unsplash.com/photo-1516214104703-d870798883c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=60" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Lost and Found</h5>
        <p class="card-text">Lost an item? Check the list to see if we found it.</p>
       <button on:click={gotoLost} class="btn btn-outline-success btn-sm">Go</button>
      </div>
      </div>
    </div>
    <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="complaint.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">File a Complaint</h5>
        <p class="card-text">Tell us about your complaints.</p>
       <button on:click = {gotoComplaint} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
  </div>
</div>

<style>
    .effimg{
        aspect-ratio: 11/16;
        height: 30vh;
    }
    .greeting h2 {
        /* Add styling for the greeting text */
        color: #4a4e69; /* Example color */
        font-weight: bold;
    }


    .card {
        transition: transform 0.3s ease-in-out;
    }

    .card:hover {
        transform: scale(1.05);
    }

    .pdf-container {
    width: 100%; /* Full width of the container */
    height: 600px; /* Adjust the height as needed */
}

</style>
