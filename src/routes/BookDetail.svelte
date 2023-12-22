<!-- BookDetail.svelte -->

<script>
    import { onMount } from 'svelte';
    import { push, params,  } from 'svelte-spa-router';
    import axios from 'axios';  // assuming axios is installed, otherwise use fetch
    import { selectedBookID, user, loggedIn } from '../components/store.js';
    let renting = false;
    let selectedDuration = '';
    let rentAmount = 0;
    let fineMessage = '';
    let book = null;
    let delay=''
    
    let bookID;
selectedBookID.subscribe(value => {
    bookID = value;
    if (bookID) {
        getBookDetails(bookID);
    }
    else {
        console.error('Book ID is missing from the URL parameters.');
    }
});

    onMount(async () => {
       // console.log("hello")
       
    const bookIDFromParams = $params.bookID;
    console.log("Current Book ID:", bookIDFromParams);
    if (bookIDFromParams) {
        getBookDetails(bookIDFromParams);
    } else {
        console.error('Book ID is missing from the URL parameters.');
    }

       /* console.log('Book ID:', bookID)
        if (bookID)
        {   
            await getBookDetails(bookID);
        }  */  
        /*unsubscribe = pdfDataStore.subscribe(data => {
        if (data) {
            pdfDataUri = `data:application/pdf;base64,${data}`;
            PDFObject.embed(pdfDataUri, '.container');
            }
        });*/
        getBookDetails();
        
    });

    $: if (book && book.PDF) {
    pdfDataStore.set(book.PDF);
}


    /*onDestroy(() => {
    if (unsubscribe) {
        unsubscribe();
    }
});*/

function viewPDF() {
    if (book && book.PDF) {
        //console.log("Setting PDF in store:", book.PDF); // Log the PDF data being set
        pdfDataStore.set(null);
        pdfDataStore.set(book.PDF);
        push('/BookPDF');
    } else {
        console.log("No PDF data available for this book.");
    }
}


    function OpenModal() {
        if ($loggedIn.is == true){
        renting = true;
        }
        else
        alert("Please log in to borrow a book");
    }

    function handleDurationSelection(event) {
        selectedDuration = event.target.value;
        // Calculate rent amount and fine message based on the selected duration
        // This is a placeholder, replace with actual calculation logic
        if (selectedDuration === '1 week') {
            rentAmount = 5;
            fineMessage = 'Fine: $10 if late.';
        } else if (selectedDuration === '2 weeks') {
            rentAmount = 30;
            fineMessage = 'Fine: $30 if late.';
        } else if (selectedDuration === '1 month') {
            rentAmount = 50;
            fineMessage = 'Fine: $50 if late.';
        } else if (selectedDuration === '3 months') {
            rentAmount = 100;
            fineMessage = 'Fine: $100 if late.';
        }


    }
/*function displayRent(){
     if (delay === 'one week') {
           
            fineMessage = 'Fine: $10 if late.';
        } else if (delay === 'two weeks') {
           
            fineMessage = 'Fine: $30 if you are two weeks late to return the book.';
        } else if (selectedDuration === 'one month') {
            
            fineMessage = 'Fine: $50 if you are a month late to return the book.';
        } else if (selectedDuration === 'three months') {
            
            fineMessage = 'Fine: $100 and a warning letter if you are three months late to return the book.';
        }
}*/
    function closePopup() {
        renting = false;
        selectedDuration = '';
        rentAmount = 0;
        fineMessage = '';
    }


    async function getBookDetails(id) {
    try {
        const response = await axios.get(`http://localhost:8000/api/books/${id}`);
        book = response.data;
        if (book && book.PDF) {
            pdfDataStore.set(book.PDF); // Update the store with the new PDF data
            console.log("pdfDataStore set in BookDetail.svelte");
        } else {
            console.error('PDF data is missing for this book.');
        }
    } catch (error) {
        console.error('Error fetching book details:', error);
    }
}

    
</script>



<main>
    <!-- Book details section -->
    {#if book}
        <div class="contB">
            <div class="cont1">
                <img src={`data:image/jpeg;base64,${book.coverImage}`} alt={`Cover of ${book.Title}`} class="book-cover" />

                <div class="book-info">
                    <h2>{book.Title}</h2>
                    <p>Author: {book.Author}</p>
                    <p>Rating: {9.5}</p>
                </div>
            </div>
            <div class="book-description">
                <h3>Description</h3>
                <p>{book.Description}</p>
            </div>
            {#if `${book.TypeID}` == 2}
            <button class="btn btn-primary" on:click={OpenModal}>Rent Book</button>
            {:else if `${book.TypeID}` == 1}
            <button class = "btn btn-secondary" on:click = {viewPDF}>View PDF</button>
            {/if}
        </div>
    {:else}
        <p>Loading...</p>
    {/if}

    <!-- Renting modal section -->
    {#if renting}
    <div class="modal fade show" style="display: block;" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Rent Book</h5>
                    <button type="button" class="close" on:click={closePopup}>
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Select duration:</p>
                    <select on:change={handleDurationSelection}>
                        <option value="" disabled selected>Select duration</option>
                        <option value="one week">One week</option>
                        <option value="two weeks">Two weeks</option>
                        <option value="one month">One month</option>
                        <option value="three months">three months</option>
                    </select>
                    {#if selectedDuration}
                        <p>Rent amount: ${rentAmount}</p>
                        <p>{fineMessage}</p>
                    {/if}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" on:click={closePopup}>Close</button>
                    <button type="button" class="btn btn-primary" disabled={!selectedDuration}>Rent</button>
                </div>
            </div>
        </div>
    </div>
    <div class="modal-backdrop fade show"></div>
    {/if}

</main>

<style>
    .contB {
        background-color: white;
        margin: 10vh;
        min-height: 100vh;
        padding: 5vh;
display:flex;
        flex-direction: column;
    }
.cont1{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}
    .book-cover {
        width: 150px; /* Adjust as needed */
        height: auto;
        margin-right: 20px;
    }

    .book-info {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .book-description {
        margin-top: 20px;
    }

    @media (min-width: 600px) {
        .book-description {
            clear: both;
            margin-left: 170px; /* Adjust based on the width of the book cover */
        }
    }
</style>