<!-- UserManagement.svelte -->
<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  let users = [];



  onMount(() => {
    fetchUsers();
  });

  // Function to fetch all users
  async function fetchUsers() {
    try {
      const response = await fetch('http://localhost:8000/api/allUsers');
      if (!response.ok) {
        throw new Error('Failed to fetch users data');
      }
      users = [...await response.json()];

      
    } catch (error) {
      console.error(error.message);
    }
  }

  let editingUser = null;

// Function to prepare and show edit form
function editUser(user) {
  editingUser = { ...user }; // Clone the user object to prevent direct mutation
}


// Function to submit edited user details
async function submitEdit() {
  if (editingUser.Email == '' || editingUser.Name == '')
  {
    alert("Error. Fields cannot be empty.");
  }
  try {
    const response = await axios.put(`http://localhost:8000/api/users/${editingUser.QalamID}`, {
      Email: editingUser.Email,
      Name: editingUser.Name
    });
    if (response.status === 200) {
      // Update the local users array with the new details
      users = users.map(user => {
        return user.QalamID === editingUser.QalamID ? { ...editingUser } : user;
      });
      editingUser = null; // Reset editing user
      alert('User updated successfully');
    }
  } catch (error) {
    console.error('Error updating user:', error.response?.data || error.message);
    alert('Error updating user:', error.message);
  }
}

function cancelEdit() {
    editingUser = null; // Reset editing user to null
  }

  // Function to handle delete user click
  async function deleteUser(user) {
    // Call the API to delete the user or implement the logic here
    console.log("Delete user", user);
  }



function addUser()
{

}
  
</script>



<main>
  <div class="heading">User Management</div>
  <div class="container">
    <div class="row mt-4">
      <div class="col-md-12">
        <h2 class="text-center">Users</h2>
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Qalam ID</th>
              <th>Email</th>
              <th>Name</th>
              <th>Actions</th> <!-- Added header for actions -->
            </tr>
          </thead>
          <tbody>
            {#each users as user}
              <tr>
                <td>{user.QalamID}</td>
                <td>{user.Email}</td>
                <td>{user.Name}</td>
                <td>
                  <!-- Edit and Delete buttons -->
                  <button on:click={() => editUser(user)} class="btn btn-secondary btn-sm">Edit</button>
                  <button on:click={() => deleteUser(user)} class="btn btn-danger btn-sm">Delete</button>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
      {#if editingUser}
      <div class="edit-form">
        <h2>Edit User</h2>
        <input type="text" bind:value={editingUser.Email} placeholder="Email"/>
        <input type="text" bind:value={editingUser.Name} placeholder="Name"/>
        <button on:click={submitEdit} class="btn btn-success btn-sm">Done</button>
        <button on:click={cancelEdit} class="btn btn-secondary btn-sm">Cancel</button>
      </div>
    {/if}
    </div>

    <!-- Form to add a new user -->
    <div class="row mt-4">
      <div class="col-md-12">
        <h2 class="text-center">Add New User</h2>
        <form on:submit|preventDefault={addUser}>
          <!-- Your form inputs here -->
          <button type="submit" class="btn btn-primary">Add User</button>
        </form>
      </div>
    </div>
  </div>
</main>

<style>
  .btn {
    margin-left: 5px; /* Spacing between buttons */
  }
  /* Additional styling if needed */
  .edit-form {
    margin-top: 20px;
    text-align: center;
  }
  .edit-form input {
    margin-right: 10px;
    padding: 5px;
  }
</style>