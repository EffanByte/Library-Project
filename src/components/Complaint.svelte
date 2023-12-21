<script>
  import { onMount } from 'svelte';
  import { user } from '../components/store.js';  // Import your user store
  import { get } from 'svelte/store';

  let complaint_description = '';

  async function submitComplaint() {
    try {
      const loggedInUser = get(user);
      console.log(user);

      const response = await fetch(`http://localhost:8000/api/submitComplaints?id=${loggedInUser.id}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          complaint_description,
        }),
      });

      if (response.ok) {
        const result = await response.json();
        console.log(result.message);
        alert("Complaint Registered Successfully!");
      } else {
        console.error('Failed to submit complaint');
      }
    } catch (error) {
      console.error(error.message);
    }
  }

</script>

<div class="row justify-content-center mt-5">
  <div class="col-md-8">
    <div class="card">
      <div class="card-header">
        <h2 class="mb-0 text-white">Submit a Complaint</h2>
      </div>
      <div class="card-body">
        <form on:submit|preventDefault={submitComplaint}>
          <div class="mb-3">
            <label for="complaint_description" class="form-label">Complaint Details</label>
            <textarea class="form-control" id="complaint_description" rows="4" placeholder="Describe your complaint" bind:value={complaint_description} required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit Complaint</button>
        </form>
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

  .form-control {
    background-color: #FFCCCC; /* Red pastel form input background color */
  }

  /* Additional CSS for the submit button */
  .btn-primary {
    background-color: #FF6666; /* Red pastel submit button background color */
    border-color: #FF6666;
  }

  .btn-primary:hover {
    background-color: #FF4747; /* Darker red pastel on hover */
    border-color: #FF4747;
  }
</style>