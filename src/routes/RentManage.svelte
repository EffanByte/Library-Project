<script>
  import { onMount } from 'svelte';
  import { get } from 'svelte/store';

  let issuedBooks = [];

  // Function to fetch all issued books from the library
  const fetchIssuedBooksLibrary = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/allIssuedBooksLibrary');
      if (!response.ok) {
        throw new Error('Failed to fetch issued books data');
      }
      issuedBooks = await response.json();
    } catch (error) {
      console.error(error.message);
    }
  };

  // Fetch issued books when the component is mounted
  onMount(() => {
    fetchIssuedBooksLibrary();
  });
</script>

<style>
  /* Add your custom styles here */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #f2f2f2;
  }
</style>

<!-- Display the issued books in a table -->
<div>
  <h2>Issued Books</h2>
  <table>
    <thead>
      <tr>
        <th>BookID</th>
        <th>Name</th>
        <th>IssuedBy</th>
      </tr>
    </thead>
    <tbody>
      {#each issuedBooks as { BookID, Title, IssuedBy }}
        <tr>
          <td>{BookID}</td>
          <td>{Title}</td>
          <td>{IssuedBy}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
