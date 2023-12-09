<script>
    // Dummy data for demonstration
    let userName = "John Doe";
    let cmsId = "123456";
    let userEmail = "johndoe@example.com";
    let booksRead = ["Book Title 1", "Book Title 2", "Book Title 3"];
    let booksRented = [
        { title: "Rented Book 1", returnBy: "2023-07-20" },
        { title: "Rented Book 2", returnBy: "2023-08-15" }
    ];
    let lateFees = "No pending late fees";

    // Functions to fetch user data, books read, rented books, etc.
    function fetchBooksRead() {
        // Fetch and return array of books the user has read
    }

    function fetchBooksRented() {
        // Fetch and return array of books the user is currently renting
    }
</script>

<div class="container my-4">
    <div class="text-center">
        <h3>{userName}</h3>
    </div>
    <h4 class="mt-4">About Me</h4>
    <p>CMS ID: {cmsId}</p>
    <p>Email: {userEmail}</p>

    <h4 class="mt-4">Currently Rented/Bought Books</h4>
    <ul class="list-group">
        {#each booksRented as book}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                {book.title}
                <span class="badge bg-primary rounded-pill">Return by: {book.returnBy}</span>
            </li>
        {/each}
    </ul>

    <div class="alert alert-info mt-4" role="alert">
        Late Fees: {lateFees}
    </div>
</div>
