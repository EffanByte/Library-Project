<script>
    import BookCard from "./BookCard.svelte";
    import Select from "svelte-select";
  import { goto } from '$app/navigation';
    let books = [];
        let currentPage = 1;
    const booksPerPage = 5;
    let totalBooks = 0;
    let selectedSortOption = '';
    // Computed paginated books
    $: paginatedBooks = books.slice((currentPage - 1) * booksPerPage, currentPage * booksPerPage);
    $: totalBooks = books.length;
    $: totalPages = Math.ceil(totalBooks / booksPerPage);
    let searchQuery = '';
    let searchResults = [];
    // Function to change page
    function changePage(page) {
        currentPage = page;
    }



  function sortByTitle(a, b) {
    const titleA = a.Title.toLowerCase();
    const titleB = b.Title.toLowerCase();
    return titleA.localeCompare(titleB);
  }

  // Sorting based on author
  function sortByAuthor(a, b) {
    const authorA = a.Author.toLowerCase();
    const authorB = b.Author.toLowerCase();
    return authorA.localeCompare(authorB);
  }

  // Sorting based on genre
  function sortByGenre(a, b) {
    const genreA = a.Genre.toLowerCase();
    const genreB = b.Genre.toLowerCase();
    return genreA.localeCompare(genreB);
  }
function sortBooks() {
  let sortedBooks = books; // Create a copy of the books array

  switch (selectedSortOption) {
    case 'name':
      console.log(searchResults)
      sortedBooks.sort(sortByTitle);
      break;
    case 'author':
      sortedBooks.sort(sortByAuthor);
      break;
    case 'genre':
      sortedBooks.sort(sortByGenre);
      break;
    default:
      break;
  }

  books = sortedBooks; // Update the original books array with the sorted copy
}


// Function to load books from the Flask API
async function loadBooks() {
        const response = await fetch('http://localhost:8000/api/books');
        if (response.ok) {
            books = await response.json();
        } else {
            console.error('Failed to load books');
        }
    }
    // calling function
    loadBooks();

        $: {
    // This reactive statement will re-run whenever sortTrigger changes
    // It ensures that the books are re-rendered when the sorting function is applied
    console.log("Re-rendering books:", books);

  }
    // Update searchResults based on the searchQuery
  $: searchResults = books.filter(book => book.Title.toLowerCase().includes(searchQuery.toLowerCase())).slice(0, 5);
  function handleSearchResultClick(book) {  
    // Navigate to the book details page or perform any other action
    goto(`/book/${book.BookID}`);
  }
  console.log(searchResults); 
</script>

<main>
    <div class="heading">Browse The Catalogue here</div>

    <div class="container sort">
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
    Sort By
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <li>
      <select bind:value={selectedSortOption} on:change={sortBooks} class="form-select">
        <option value="">-- Select an option --</option>
        <option value="name">Name</option>
        <option value="author">Author</option>
        <option value="genre">Genre</option>
      </select>
    </li>
  </ul>
</div>

 <!-- Search Bar -->
    <div class>
      <label for="search" class="form-label">Search by Title</label>
      <input type="text" id="search" bind:value={searchQuery} class="form-control" placeholder="Enter book title...">
    </div>

    <!-- Search Results Dropdown -->
    {#if searchResults.length > 0}
      <Select
        label="Search Results"
        value={null}
        items = {searchResults}
        labelField="Title"
        on:change={({ detail }) => handleSearchResultClick(detail.value)}
      />
    {/if}
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

