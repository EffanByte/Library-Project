<script>
  let email = '';
  let dateOfComplaint = '';
  let complaintDetails = '';

  function submitComplaint() {
    // Here, you can handle the submission of the complaint data
    // For now, let's just log the data to the console
    console.log('Email:', email);
    console.log('Date of Complaint:', dateOfComplaint);
    console.log('Complaint Details:', complaintDetails);
  }
</script>

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

<div class="row justify-content-center mt-5">
  <div class="col-md-8">
    <div class="card">
      <div class="card-header">
        <h2 class="mb-0 text-white">Submit a Complaint</h2>
      </div>
      <div class="card-body">
        <form on:submit|preventDefault={submitComplaint}>
            <div class="mb-3">
              <label for="email" class="form-label">Email address</label>
              <input type="email" class="form-control" id="email" placeholder="Your email" bind:value={email} required>
            </div>
            <div class="mb-3">
              <label for="dateOfComplaint" class="form-label">Date of Complaint</label>
              <input type="date" class="form-control" id="dateOfComplaint" bind:value={dateOfComplaint} required>
            </div>
            <div class="mb-3">
              <label for="complaintDetails" class="form-label">Complaint Details</label>
              <textarea class="form-control" id="complaintDetails" rows="4" placeholder="Describe your complaint" bind:value={complaintDetails} required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit Complaint</button>
          </form>
        </div>
      </div>
    </div>
  </div>