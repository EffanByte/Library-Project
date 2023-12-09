<script>
    import BookCard from "./BookCard.svelte";
console.log("test");
    let books = [];
        let currentPage = 1;
    const booksPerPage = 5;
    let totalBooks = 0;

    // Computed paginated books
    $: paginatedBooks = books.slice((currentPage - 1) * booksPerPage, currentPage * booksPerPage);
    $: totalBooks = books.length;
    $: totalPages = Math.ceil(totalBooks / booksPerPage);

    // Function to change page
    function changePage(page) {
        currentPage = page;
    }
// Function to load books from the Flask API
async function loadBooks() {
        const response = await fetch('http://localhost:8000/api/books');
        if (response.ok) {
            books = await response.json();
            console.log(books);
        } else {
            console.error('Failed to load books');
        }
    }
    // calling function
    loadBooks();

</script>

<main>
    <div class="heading">Browse The Catalogue here</div>

    <div class="container sort">
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
Sort By
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li><a class="dropdown-item" href="#">Date Added</a></li>
                <li><a class="dropdown-item" href="#">Name</a></li>
                <li><a class="dropdown-item" href="#">Author</a></li>
                <li><a class="dropdown-item" href="#">Availability</a></li>
            </ul>
        </div>
    <!-- Add a filter icon later-->
        <!-- Horizontal Divider -->
        <hr class="my-4">

            <div class="row">
                {#each paginatedBooks as book}
                    <div class="col-md-6 col-lg-4">
                    <BookCard {book} />
                    </div>
                {/each}
            </div>
<nav aria-label="Page navigation" class = "">
    <ul class="pagination justify-content-center">
        <li class="page-item {currentPage === 1 ? 'disabled' : ''}">
            <a class="page-link" href="#" aria-label="Previous" on:click|preventDefault={() => changePage(currentPage - 1)}>
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>

        {#each Array(totalPages) as _, index (index)}
            <li class="page-item {currentPage === index + 1 ? 'active' : ''}">
                <a class="page-link" href="#" on:click|preventDefault={() => changePage(index + 1)}>{index + 1}</a>
            </li>
        {/each}

        <li class="page-item {currentPage === totalPages ? 'disabled' : ''}">
            <a class="page-link" href="#" aria-label="Next" on:click|preventDefault={() => changePage(currentPage + 1)}>
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    </ul>
</nav>


    </div>

    <footer> Testing here</footer>
</main>

