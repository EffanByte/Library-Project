<script>
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';
  let complaints = [];
  let selectedComplaint = null;
  let isModalOpen = false;
    const dispatch = createEventDispatcher();

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

  function openModal(complaint) {
    selectedComplaint = complaint;
    isModalOpen = true; // Set the flag to open the modal
  }
    function closeModal() {
    selectedComplaint = null;
    isModalOpen = false; // Set the flag to close the modal
  }
    async function markAsResolved() {
    // Call your backend API to mark the complaint as resolved
    // Example: await fetch(`http://localhost:8000/api/markAsResolved?id=${selectedComplaint.id}`, { method: 'POST' });

    // Remove the complaint from the local list
    complaints = complaints.filter(c => c.id !== selectedComplaint.id);

    // Close the modal
    closeModal();
  }
</script>

{#if isModalOpen}
<div class="modal show" tabindex="-1" role="dialog" style="display: block;">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Complaint Details</h5>
          <button type="button" class="close" aria-label="Close" on:click={() => selectedComplaint = null}>
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>{selectedComplaint.complaint_description}</p>
          <button class="btn btn-danger" on:click={markAsResolved}>Mark as Resolved</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal-backdrop show"></div>
  {/if}
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
              <li class="list-group-item" on:click={() => openModal(complaint)}>
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
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1050;
        display: none;
        overflow: hidden;
        outline: 0;
    }

    .show {
        display: block;
    }

    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1040;
        width: 100vw;
        height: 100vh;
        background-color: #000;
        opacity: .5;
    }
    button {
        margin-top: 10px;
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
