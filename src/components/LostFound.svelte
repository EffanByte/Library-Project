<!-- LostFound.svelte -->

<script>
  import { onMount } from 'svelte';

  let lostItems = [];

  // Simulate fetching data from a server
  const fetchLostItems = async () => {
    // Make a fetch request to your server or API
    // Replace this with actual API endpoint
    const response = await fetch('/api/lostitems');
    const data = await response.json();

    // Update lostItems with the retrieved data
    lostItems = data;
  };

  // Fetch lost items when the component is mounted
  onMount(() => {
    fetchLostItems();
  });
</script>

<main>
  <div class="container h-100">
    <div class="heading">Lost and Found</div>

    <section class="lost-items-section">
      <h1 class="section-title">Lost and Found Items</h1>

      {#if lostItems.length > 0}
        <ul class="lost-items-list">
          {#each lostItems as { id, ItemDescription, DateLost }}
            <li class="lost-item" key={id}>
              <div class="item-description">{ItemDescription}</div>
              <div class="date-lost">Date Lost: {DateLost}</div>
            </li>
          {/each}
        </ul>
      {:else}
        <p class="no-items-message">No lost items found.</p>
      {/if}
    </section>

    <section class="additional-info">
      <h2 class="additional-title">Look at our Lost & Found!</h2>
      <p class="additional-text">Visit the librarian if you find something that belongs to you!</p>
    </section>
  </div>
</main>

<style>
  /* Additional CSS for the LostFound component */
  main {
    padding: 40px 0;
  }

  .container-me{
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

  .lost-items-section {
    margin-bottom: 40px;
  }

  .section-title {
    font-size: 28px;
    font-weight: bold;
    color: #555; /* Medium-dark text color */
    margin-bottom: 20px;
  }

  .lost-items-list {
    list-style: none;
    padding: 0;
  }

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

  .date-lost {
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
