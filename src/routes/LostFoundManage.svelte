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
              <button on:click={() => deleteItem(ItemID)}>Delete</button>
              <button on:click={() => markItemFound(ItemID)}>Item Found</button>
            </li>
          {/each}
        </ul>
      {:else}
        <p class="no-items-message">No lost items reported.</p>
      {/if}
    </section>
  </main>
 