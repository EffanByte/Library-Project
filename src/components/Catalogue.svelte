<script>
    import BookCard from "./BookCard.svelte";
console.log("test");
    let showModal = false;
    let books = [];
    function handleLoginEvent() {
        showModal = true;
        showModal = !!showModal;
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

    <div class="container my-3">
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
Sort By
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li><a class="dropdown-item" href="#">Option 1</a></li>
                <li><a class="dropdown-item" href="#">Option 2</a></li>
                <li><a class="dropdown-item" href="#">Option 3</a></li>
                <li><a class="dropdown-item" href="#">Option 4</a></li>
                <li><a class="dropdown-item" href="#">Option 5</a></li>
            </ul>
        </div>
    <!-- Add a filter icon later-->
        <!-- Horizontal Divider -->
        <hr class="my-4">

        <div class="row">
            {#each books as book}
                <div class="col-md-6 col-lg-4">
                    <BookCard {book} />
                </div>
            {/each}
        </div>
    </div>

    <footer> Testing here</footer>
</main>

