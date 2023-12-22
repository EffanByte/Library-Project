<!-- BookDetail.svelte -->

<script>
    import { onMount } from 'svelte';
    import { push, params,  } from 'svelte-spa-router';
    import axios from 'axios';  // assuming axios is installed, otherwise use fetch
    import { selectedBookID, user, loggedIn } from '../components/store.js';
    
    let issueing = false;
    let selectedDuration = 0    ;
    let issueAmount = 0;
    let fineMessage = '';
    let book = null;
    let delay=''
    let bookID;
    let due_date = null
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
        issueing = true;
        }
        else
        alert("Please log in to borrow a book");
    }

  function handleDurationSelection(event) {
    selectedDuration = event.target.value;
    
    // Calculate due date based on the selected duration
    if (selectedDuration) {
      const durationInDays = parseInt(selectedDuration); // Parse duration as an integer
      const currentDate = new Date();
      due_date = new Date(currentDate.getTime() + durationInDays * 24 * 60 * 60 * 1000);
      
      // Format the due_date to "YYYY-MM-DD"
      const year = due_date.getFullYear();
      const month = String(due_date.getMonth() + 1).padStart(2, '0');
      const day = String(due_date.getDate()).padStart(2, '0');
      due_date = `${year}-${month}-${day}`;
    }
  }
    async function IssueBook() {
        try {

            // Call your backend API to issue the book
            console.log("Test 1")
            const response = await fetch(`http://localhost:8000/api/issueBook`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },

                body: JSON.stringify({
                    QalamID: $user.id, // Assuming you have user information in your store
                    BookID: bookID,
                    JobID: 1, // Assuming you have job information in your store
                    DueDate: due_date, // Placeholder, you need to calculate the actual due date
                }),
            });
            console.log($user.id)
            console.log(bookID)
            console.log(due_date)
            if (response.ok) {
                // If the API call is successful, remove the book from the local list or update its status
                // (You need to implement the logic to update your local data store)
                console.log("Test3")
                // Close the modal
                selectedDuration = 0;
                issueAmount = 0;
                fineMessage = '';
                closePopup();
            }
        } catch (error) {
            console.error('Error issuing book:', error);
            // Handle error (display a message, log, etc.)
        }
        closePopup();
       
    }
/*function displayIssue(){
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
        issueing = false;
        selectedDuration = 0;
        issueAmount = 0;
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
            <button class="btn btn-primary" on:click={OpenModal}>Issue Book</button>
            {:else if `${book.TypeID}` == 1}
            <button class = "btn btn-secondary" on:click = {viewPDF}>View PDF</button>
            {/if}
        </div>
    {:else}
        <p>Loading...</p>
    {/if}

    <!-- Issueing modal section -->
    {#if issueing}
    <div class="modal fade show" style="display: block;" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Issue Book</h5>
                    <button type="button" class="close" on:click={closePopup}>
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Select duration:</p>
                    <select on:change = {handleDurationSelection}>
                        <option value="" disabled selected>Select duration</option>
                        <option value="7">One week</option>
                        <option value="14">Two weeks</option>
                        <option value="30">One month</option>
                        <option value="90">three months</option>
                    </select>
                    {#if selectedDuration}
                        <p>{fineMessage}</p>
                    {/if}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" on:click={closePopup}>Close</button>
                    <button type="button" class="btn btn-primary" disabled={!selectedDuration} on:click = {IssueBook}>Issue</button>
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