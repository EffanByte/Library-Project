<script>
  import BookCard from "./BookCard.svelte";
  import {push} from 'svelte-spa-router';
  import {selectedBookID} from "../components/store.js";
  let books = [];
  let currentPage = 1;
  const booksPerPage = 5;
  let totalBooks = 0;
  let selectedSortOption = "";
  // Computed paginated books
  $: paginatedBooks = books.slice(
    (currentPage - 1) * booksPerPage,
    currentPage * booksPerPage,
  );
  $: totalBooks = books.length;
  $: totalPages = Math.ceil(totalBooks / booksPerPage);
  let searchQuery = "";
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
      case "name":
        console.log(searchResults);
        sortedBooks.sort(sortByTitle);
        break;
      case "author":
        sortedBooks.sort(sortByAuthor);
        break;
      case "genre":
        sortedBooks.sort(sortByGenre);
        break;
      default:
        break;
    }

    books = sortedBooks; // Update the original books array with the sorted copy
  }

  // Function to load books from the Flask API
  async function loadBooks() {
    const response = await fetch("http://localhost:8000/api/books");
    if (response.ok) {
      books = await response.json();
    } else {
      console.error("Failed to load books");
    }
  }
  // calling function
  loadBooks();

  $: {
    // This reactive statement will re-run whenever sortTrigger changes
    // It ensures that the books are re-rendered when the sorting function is applied
  }
  // Update searchResults based on the searchQuery
  $: searchResults = books
    .filter((book) =>
      book.Title.toLowerCase().includes(searchQuery.toLowerCase()),
    )
    .slice(0, 5);
    function navigateToBook(bookID) {
        selectedBookID.set(bookID); // TEMPORARY WORKAROUND TO MAKE BookDetail.svelte work
        setLastReadBookIfNeeded(bookID);
        push(`/book/${bookID}`);

    }
   // const loggedInUser = get(user);

    async function setLastReadBookIfNeeded(bookID) {
      const loggedInUser = get(user);
    if (loggedInUser && loggedInUser.id) {
        try {
            // Call your API to set the last read book
            const response = await axios.post('http://localhost:8000/api/setLastBookRead', {
                userId: loggedInUser.id,
                bookId: bookID
            });
            if (response.status !== 200) {
                throw new Error(response.data.error || 'Failed to set last read book');
            }
        } catch (error) {
            console.error('Error setting last read book:', error.message);
        }
    }
}

</script>

<main>
  <div class="heading">Browse The Catalogue here</div>

  <div class="container sort">
<div class="custom-dropdown">
    <span class="dropdown-text">Sort By</span>
    <div class="dropdown-content">
      <select
        bind:value={selectedSortOption}
        on:change={sortBooks}
        class="form-select"
      >
        <option value="">-- Select an option --</option>
        <option value="name">Name</option>
        <option value="author">Author</option>
        <option value="genre">Genre</option>
      </select>
    </div>
  </div>

    <!-- Search Bar -->
    <div class>
      <label for="search" class="form-label">Search by Title</label>
      <input
        type="text"
        id="search"
        bind:value={searchQuery}
        class="form-control"
        placeholder="Enter book title..."
      />
    </div>

<!-- Search Results Dropdown -->
{#if searchQuery !== '' && searchResults.length > 0}
  <div class="search-results">
    {#each searchResults as search}
      <div class="search-result">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div on:click={navigateToBook(search.BookID)}>{search.Title}</div>
      </div>
    {/each}
  </div>
{/if}

    <!-- Add a filter icon later-->
    <!-- Horizontal Divider -->
    <hr class="my-4" />

    <div class="row">
      {#each paginatedBooks as book}
        <div class="col-md-6 col-lg-4">
          <BookCard {book} />
        </div>
      {/each}
    </div>
    <nav aria-label="Page navigation" class="">
      <ul class="pagination justify-content-center">
        <li class="page-item {currentPage === 1 ? 'disabled' : ''}">
          <a
            class="page-link"
            href="#"
            aria-label="Previous"
            on:click|preventDefault={() => changePage(currentPage - 1)}
          >
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>

        {#each Array(totalPages) as _, index (index)}
          <li class="page-item {currentPage === index + 1 ? 'active' : ''}">
            <a
              class="page-link"
              href="#"
              on:click|preventDefault={() => changePage(index + 1)}
              >{index + 1}</a
            >
          </li>
        {/each}

        <li class="page-item {currentPage === totalPages ? 'disabled' : ''}">
          <a
            class="page-link"
            href="#"
            aria-label="Next"
            on:click|preventDefault={() => changePage(currentPage + 1)}
          >
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</main>

<style>
  .custom-dropdown {
    position: relative;
    display: inline-block;
    cursor: pointer;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
  }

  .custom-dropdown:hover .dropdown-content {
    display: block;
  }
</style>