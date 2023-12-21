<script>
  import { onMount } from 'svelte';
  import { user } from '../components/store.js';
  import { get } from 'svelte/store';

  let foundItems = [];
  let lostItems = [];
  let lostItemDescription = '';
  let lostDateReported = '';
  let foundItemDescription = '';
  let foundDateReported = '';

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

  const reportFoundItem = async () => {
    try {
      const loggedInUser = get(user);

      const response = await fetch(`http://localhost:8000/api/reportFoundItem?id=${loggedInUser.id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          foundItemDescription,
          foundDateReported
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to report found item');
      }

      // Refresh the found items after reporting
      fetchFoundItems();

      // Clear the input fields
      ItemDescription = '';
      DateReported = '';
    } catch (error) {
      console.error(error.message);
    }
  };

  const reportLostItem = async () => {
    try {
      const loggedInUser = get(user);

      const response = await fetch(`http://localhost:8000/api/reportLostItem?id=${loggedInUser.id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          lostItemDescription,
          lostDateReported
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to report lost item');
      }

      // Refresh the lost items after reporting
      fetchLostItems();

      // Clear the input fields
      ItemDescription = '';
      DateReported = '';
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
  <div class="container h-100">
    <div class="heading">Lost and Found</div>

    <!-- Found Items Section -->
    <section class="found-items-section">
      <h1 class="section-title">Found Items</h1>

      {#if foundItems.length > 0}
        <ul class="found-items-list">
          {#each foundItems as { ID, QalamID, ItemDescription, DateReported }}
            <li class="found-item" key={ID}>
              <div class="QalamID">{QalamID}</div>
              <div class="item-description">{ItemDescription}</div>
              <div class="date-reported">Date Reported: {DateReported}</div>
            </li>
          {/each}
        </ul>
      {:else}
        <p class="no-items-message">No found items reported.</p>
      {/if}
    </section>

    <!-- Lost Items Section -->
    <section class="lost-items-section">
      <h1 class="section-title">Lost Items</h1>

      {#if lostItems.length > 0}
        <ul class="lost-items-list">
          {#each lostItems as { ID, QalamID, ItemDescription, DateReported }}
            <li class="lost-item" key={ID}>
              <div class="QalamID">{QalamID}</div>
              <div class="item-description">{ItemDescription}</div>
              <div class="date-reported">Date Reported: {DateReported}</div>
            </li>
          {/each}
        </ul>
      {:else}
        <p class="no-items-message">No lost items reported.</p>
      {/if}
    </section>

    <!-- Report Item Section -->
    <section class="report-item-section">
      <h2 class="additional-title">Report a Lost or Found Item</h2>
      <form on:submit|preventDefault={reportFoundItem}>
        <label for="ItemDescription1">Item Description:</label>
        <input type="text" bind:value={foundItemDescription} id="ItemDescription1" required>
       c
        <label for="DateReported1">Date Reported:</label>
        <input type="date" bind:value={foundDateReported} id="DateReported1" required>

        <button type="submit">Report Found Item</button>
      </form>

      <form on:submit|preventDefault={reportLostItem}>
        <label for="ItemDescription2">Item Description:</label>
        <input type="text" bind:value={lostItemDescription} id="ItemDescription2" required>

        <label for="DateReported2">Date Reported:</label>
        <input type="date" bind:value={lostDateReported} id="DateReported2" required>

        <button type="submit">Report Lost Item</button>
      </form>
    </section>
  </div>cd 
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
</style>
