<script>
  import { onMount } from 'svelte';
  import { push } from 'svelte-spa-router';

  let complaints = [];

  onMount(async () => {
    try {
      const response = await fetch(`http://localhost:8000/api/complaints`);
      
      if (response.ok) {
        complaints = await response.json();
      } else {
        console.error('Failed to fetch complaints');
      }
    } catch (error) {
      console.error(error.message);
    }
  });


</script>

<div class="row justify-content-center mt-5">
  <div class="col-md-8">
    <div class="card">
      <div class="card-header">
        <h2 class="mb-0 text-white">Complaint Management</h2>
      </div>
      <div class="card-body">
        {#if complaints.length > 0}
          <ul class="list-group">
            {#each complaints as complaint (complaint.id)}
              <li class="list-group-item" >
                {complaint.complaint_description}
              </li>
            {/each}
          </ul>
        {:else}
          <p>No complaints available.</p>
        {/if}
      </div>
    </div>
  </div>
</div>

<style>
  /* Additional CSS for the red pastel background */
  body {
    background-color: #F5A9A9; /* Red pastel background color */
  }

  /* Additional CSS for the card styling */
  .card {
    border: none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #FFCCCC; /* Red pastel card background color */
  }

  .card-header {
    background-color: #FF6666; /* Red pastel header background color */
    color: white;
  }

  .list-group-item {
    cursor: pointer;
    background-color: #FFCCCC; /* Red pastel list item background color */
  }

  /* Additional CSS for the hover effect on list items */
  .list-group-item:hover {
    background-color: #FF9999; /* Darker red pastel on hover */
  }
</style>
