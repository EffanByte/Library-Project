<!-- UserList.svelte -->

<script>
    import { onMount } from 'svelte';
    import { link } from 'svelte-spa-router';
  
    let users = [];
    let selectedUser = null;
  
    async function fetchUsers() {
      try {
        const response = await fetch('/api/users/all/books');
        const data = await response.json();
        users = data.users;
      } catch (error) {
        console.error('Error fetching users:', error.message);
      }
    }
  
    function handleUserSelection(userId) {
      selectedUser = users.find(user => user.id === userId);
    }
  
    onMount(() => {
      fetchUsers();
    });
  </script>
  
  <main>
    <h1>List of Users</h1>
    <ul class="user-list">
      {#each users as user}
        <li>
          <span>{user.name}</span>
          <button class="details-btn" on:click={() => handleUserSelection(user.id)}>View Details</button>
        </li>
      {/each}
    </ul>
  
    {#if selectedUser}
      <div class="user-details">
        <h2>User Details</h2>
        <p>User ID: {selectedUser.id}</p>
        <p>Name: {selectedUser.name}</p>
  

        <!--
        Additional User Details - Commented out
        <h3>Additional Details</h3>
        <p>Email: {selectedUser.email || 'N/A'}</p>
        <p>Membership Status: {selectedUser.membershipStatus || 'N/A'}</p>
        <p>Join Date: {selectedUser.joinDate || 'N/A'}</p>
        <p>Contact Information: {selectedUser.contactInfo || 'N/A'}</p>
      -->


        <h3>Books Rented</h3>
        {#if selectedUser.booksRented.length > 0}
          <ul class="books-list">
            {#each selectedUser.booksRented as book}
              <li>{book.title}</li>
            {/each}
          </ul>
        {:else}
          <p>No books rented by this user.</p>
        {/if}
           
      </div>
     
    {/if}


     
  </main>
   


  <style>
    .user-list {
      list-style: none;
      padding: 0;
    }
  
    .user-list li {
      margin-bottom: 10px;
    }
  
    .details-btn {
      background-color: #3498db;
      color: #fff;
      border: none;
      padding: 5px 10px;
      cursor: pointer;
    }
  
    .user-details {
      margin-top: 20px;
      border: 1px solid #ccc;
      padding: 10px;
    }
  
    .books-list {
      list-style: none;
      padding: 0;
    }
  
    .books-list li {
      margin-bottom: 5px;
    }
  </style>