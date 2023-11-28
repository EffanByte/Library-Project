<!-- BookDetail.svelte -->

<script>
    import { onMount } from 'svelte';

    let renting = false;
    let selectedDuration = '';
    let rentAmount = 0;
    let fineMessage = '';
    let book = null;
    let delay=''
    

    // Simulating book data retrieval using onMount
    onMount(async () => {
        // Fetch or compute book details here using bookId
        // For example, you might have a function getBookDetails(id)
        const bookId = 123; // Replace this with actual book ID or parameter
;        book = await getBookDetails(bookId);
    });

    function rentBook() {
        renting = true;
    }

    function handleDurationSelection(event) {
        selectedDuration = event.target.value;
        // Calculate rent amount and fine message based on the selected duration
        // This is a placeholder, replace with actual calculation logic
        if (selectedDuration === 'one week') {
            rentAmount = 5;
            fineMessage = 'Fine: $10 if late.';
        } else if (selectedDuration === 'two weeks') {
            rentAmount = 30;
            fineMessage = 'Fine: $30 if late.';
        } else if (selectedDuration === 'one month') {
            rentAmount = 50;
            fineMessage = 'Fine: $50 if late.';
        } else if (selectedDuration === 'three months') {
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
        // Simulating book details retrieval from an API
        // Replace this with actual API fetch logic
        return {
            title: "Testing",
            author: "Effan pro",
            rating: 5,
            description: "Effan's code works",
            coverUrl: "testcover.jpeg"
        };
    }
</script>

<main>
    <!-- Book details section -->
    {#if book}
        <div class="contB">
            <div class="cont1">
                <img src={book.coverUrl} alt="Cover of ${book.title}" class="book-cover" />
                <div class="book-info">
                    <h2>{book.title}</h2>
                    <p>Author: {book.author}</p>
                    <p>Rating: {book.rating}</p>
                </div>
            </div>
            <div class="book-description">
                <h3>Description</h3>
                <p>{book.description}</p>
            </div>
            <button class="btn btn-primary" on:click={rentBook}>Rent Book</button>
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