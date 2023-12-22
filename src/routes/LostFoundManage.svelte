<script>
    import { onMount } from 'svelte';
    import { user } from '../components/store.js';
    import { get } from 'svelte/store';
  
    let foundItems = [];
    let lostItems = [];
  
    // Function to fetch all found items
    const fetchFoundItems = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/all_found_items');
        if (!response.ok) {
          throw new Error('Failed to fetch found items data');
        }
        foundItems = await response.json();
      } catch (error) {
        console.error(error.message);
      }
    };
  
    // Function to fetch all lost items
    const fetchLostItems = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/all_lost_items');
        if (!response.ok) {
          throw new Error('Failed to fetch lost items data');
        }
        lostItems = await response.json();
      } catch (error) {
        console.error(error.message);
      }
    };
  
    const deleteItem = async (ItemID) => {
      try {
        const response = await fetch(`http://localhost:8000/api/deleteItem?id=${ItemID}`, {
          method: 'DELETE',
        });
  
        if (!response.ok) {
          throw new Error('Failed to delete item');
        }
  
        // Refresh the lost and found items after deleting
        fetchFoundItems();
        fetchLostItems();
      } catch (error) {
        console.error(error.message);
      }
    };
  
    const markItemFound = async (ItemID) => {
      try {
        const response = await fetch(`http://localhost:8000/api/markItemFound?id=${ItemID}`, {
          method: 'POST',
        });
  
        if (!response.ok) {
          throw new Error('Failed to mark item as found');
        }
  
        // Refresh the lost and found items after marking as found
        fetchFoundItems();
        fetchLostItems();
      } catch (error) {
        console.error(error.message);
      }
    };
  
    // Fetch found and lost items when the component is mounted
    onMount(() => {
      fetchFoundItems();
      fetchLostItems();
    });
  </script>
  
  <main>
    <!-- ... (existing HTML code) ... -->
  
    <!-- Lost Items Section with Delete and Mark as Found Buttons -->
    <section class="lost-items-section">
      <h1 class="section-title">Lost Items</h1>
  
      {#if lostItems.length > 0}
        <ul class="lost-items-list">
          {#each lostItems as { ItemID, QalamID, ItemDescription, DateReported }}
            <li class="lost-item" key={ItemID}>
              <div class="QalamID">{QalamID}</div>
              <div class="item-description">{ItemDescription}</div>
              <div class="date-reported">Date Reported: {DateReported}</div>
              <button class = "btn" on:click={() => deleteItem(ItemID)}>Delete</button>
              <button class = "btn" on:click={() => markItemFound(ItemID)}>Item Found</button>
            </li>
          {/each}
        </ul>
      {:else}
        <p class="no-items-message">No lost items reported.</p>
      {/if}
    </section>
  </main>
 


  <style>
    /* Additional CSS for the LostFound component */
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
  
    .found-items-section,
    .lost-items-section,
    .report-item-section {
      margin-bottom: 40px;
    }
  
    .section-title {
      font-size: 28px;
      font-weight: bold;
      color: #555; /* Medium-dark text color */
      margin-bottom: 20px;
    }
  
    .found-items-list,
    .lost-items-list {
      list-style: none;
      padding: 0;
    }
  
    .found-item,
    .lost-item {
      background-color: #f9f9f9; /* Light background color for each item */
      border-radius: 8px;
      padding: 15px;
      margin-bottom: 15px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .item-description {
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 8px;
      color: #333; /* Dark text color */
    }
  
    .date-reported {
      font-size: 14px;
      color: #666; /* Medium text color */
    }
  
    .no-items-message {
      font-size: 16px;
      color: #777; /* Light text color */
    }
  
    .additional-info {
      text-align: center;
    }
  
    .additional-title {
      font-size: 24px;
      font-weight: bold;
      color: #555; /* Medium-dark text color */
      margin-bottom: 10px;
    }
  
    .additional-text {
      font-size: 16px;
      color: #777; /* Light text color */
    }
  
    .btn {
      background-color: #e4dbdb;
        font-size: 14;
        margin: 10px;
        width: 160px; /* Adjust the width as needed */
    }
    .btn:hover {
    background-color: #0056b3;
  }
  
  </style>