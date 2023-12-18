<script>
<<<<<<< HEAD
    import { push } from "svelte-spa-router";
    import {user } from "../components/store.js";
    
=======
    import { onMount } from 'svelte';
    import { push } from "svelte-spa-router";
    import {user } from "../components/store.js";


    let greeting;

    onMount(() => {
        updateGreeting();
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
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a

function gotoCatalogue(){
    push("/Catalogue");
}
function gotoRoom(){
    push("/Room");
}
function gotoLost(){
    push("/LostFound");
}
function gotoComplaint(){
    push("/Complaint");
}
</script>

<div class="container">
    <div class="row">
        <div class="col-md-6 mt-3">
            <div class="greeting mb-4">
<<<<<<< HEAD
                {#if $user.role == ''}
            <h2>Good Afternoon, Guest!</h2>
            {:else}
                 <h2>Good Afternoon, {$user.username}!</h2>
                {/if}
            </div>
        </div>
        {#if $user.role != ''}
=======
                {#if $user.username == ''}
                    <h2>{greeting}, Guest!</h2>
                {:else}
                    <h2>{greeting}, {$user.username}!</h2>
                {/if}
            </div>
        </div>
        {#if $user.username != ''}
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
        <div class="col-md-6">
            <!-- Move the image and button to the top right side -->
            <div class="d-flex flex-column align-items-center justify-content-center mt-4 spa">
                <img src="librarybg.jpg" alt="Last Read Book" class="effimg">
                <button class="btn btn-primary mt-2 mb-3">Continue Reading Last Book</button>
            </div>
        </div>
        {/if}
    </div>

    <div class="row">
    <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="bookimg.jpg" alt="" class="card-img-top">
      <div class="card-body">
<<<<<<< HEAD

=======
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
        <h5 class="card-title">Browse Catalogue</h5>
        <p class="card-text">Check out all the books in our library here.</p>
        <button on:click={gotoCatalogue} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
<<<<<<< HEAD
    {#if $user.role != ""}
    <div class="col-lg-4 mb-4">
        <div class="card">
            <img src="conferenceimg.jpg" alt="" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Room Rental</h5>
                <p class="card-text">Rent a conference room for all your meetings.</p>
=======
        <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="conferenceimg.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Room Rental</h5>
        <p class="card-text">Rent a conference room for all your meetings.</p>
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
        <button on:click = {gotoRoom} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
<<<<<<< HEAD
    {/if}
=======
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
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
<<<<<<< HEAD
        {#if $user.role != ""}
=======
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
    <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="complaint.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">File a Complaint</h5>
<<<<<<< HEAD
        <p class="card-text">Tell us about your complaints so that we can fix them.</p>
=======
        <p class="card-text">Tell us about your complaints.</p>
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
       <button on:click = {gotoComplaint} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
<<<<<<< HEAD
    {/if}
  </div>
          {#if $user.role == ""}
          <h2 class = "text-center">Login to access all the library features!</h2>
          {/if}
=======
  </div>
>>>>>>> cd9df86e7b9cbbde8217a7644acea378924b4c4a
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

</style>
