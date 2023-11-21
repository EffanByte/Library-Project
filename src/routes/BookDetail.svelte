<script>
    import { onMount } from 'svelte';
    export let params;

    let bookId;
    let book;

    bookId = params.id;
    console.log(bookId);
    onMount(async () => {
        // Fetch or compute the book details here using bookId
        // For example, you might have a function `getBookDetails(id)`
      //  book = await getBookDetails(bookId);
    });
    if (bookId) {
        book = {
            title: "Testing",
            author: "Effan pro",
            rating: 5,
            description: "Effan's code works",
            coverUrl: "testcover.jpeg"
        }
    }
</script>

{#if book}
<div class="contB">
    <div class = "cont1">
    <img src={book.coverUrl} alt={`Cover of ${book.title}`} class="book-cover" />

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
</div>
{:else}
    <p>Loading...</p>
{/if}

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
