<script>
  import { onMount } from 'svelte';
  import { get } from 'svelte/store';
  import axios from 'axios'
  let issuedBooks = [];
  // Function to fetch all issued books from the library
  const fetchIssuedBooksLibrary = async () => {

  };

  // Fetch issued books when the component is mounted
  onMount(async () => {
    try {
          try {
      const response = await fetch('http://localhost:8000/api/allIssuedBooksLibrary');
      if (!response.ok) {
        throw new Error('Failed to fetch issued books data');
      }
      issuedBooks = await response.json();
    } catch (error) {
      console.error(error.message);
    }
    console.log(issuedBooks)
    console.log(issuedBooks.length)
      // For each issued book, fetch the title from the books table
      for (let i = 0; i < issuedBooks.length; i++) {
        const bookID = issuedBooks[i].BookID;
        const bookResponse = await axios.get(`http://localhost:8000/api/books/${bookID}`);
        const bookTitle = bookResponse.data.Title;
        console.log(bookTitle)
        // Add the Title attribute to the issuedBooks array
        issuedBooks[i].Title = bookTitle;
      }
    } catch (error) {
      console.error('Error fetching issued books:', error);
    }
  });

  </script>
  <main>
    <div class="container h-100">
      <div class="heading">Issued Books from the Library</div>
  
      {#if issuedBooks.length> 0}
        <ul class="issued-books-list">
          {#each issuedBooks as { BookID, Title, DueDate }}
            <li class="issued-book" key={BookID}>
              <div class="book-id">BookID: {BookID}</div>
              <div class="title">{Title}</div>
              <div class="DueDate">{DueDate}  </div>
            </li>
          {/each}
        </ul>
      {:else}
        <p class="no-books-message">No books issued from the library.</p>
      {/if}
    </div>
  </main>
  
  <style>
    /* Additional CSS for the IssuedBooksLibrary component */
    main {
      padding: 40px 0;
    }
  
    .container {
      max-width: 800px;
      margin: 0 auto;
      background-color: white;
    }
  
    .heading {
      font-size: 36px;
      font-weight: bold;
      text-align: center;
      margin-bottom: 20px;
      color: #333; /* Dark text color */
    }
  
    .issued-books-list {
      list-style: none;
      padding: 0;
    }
  
    .issued-book {
      background-color: #f9f9f9; /* Light background color for each book */
      border-radius: 8px;
      padding: 15px;
      margin-bottom: 15px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .book-id {
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 8px;
      color: #333; /* Dark text color */
    }
  
    .title {
      font-size: 16px;
      margin-bottom: 8px;
      color: #555; /* Medium-dark text color */
    }
  
    .issued-by {
      font-size: 14px;
      color: #666; /* Medium text color */
    }
  
    .no-books-message {
      font-size: 16px;
      color: #777; /* Light text color */
    }
  </style>