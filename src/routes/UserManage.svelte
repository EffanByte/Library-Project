<!-- UserManagement.svelte -->

<script>
    const roles = ['head librarian', 'technical services librarian', 'ebooks manager', 'student', 'archivist'];
  let users = [

  ];

  let newUser = {
    qalamId: '',
    name: '',
    email: '',
    password: '',
    role: 'head librarian', // Default role
  };

  function addUser() {
    // Validate and add the new user
    if (newUser.name.trim() !== '' && newUser.email.trim() !== '' && newUser.password.trim() !== '') {
      users = [...users, { id: users.length + 1, ...newUser }];
      // Reset the newUser object
      newUser = { qalamId: '', name: '', email: '', password: '', role: 'head librarian' };
    }
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
              <th>ID</th>
              <th>Qalam ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Role</th>
            </tr>
          </thead>
          <tbody>
            {#each users as user}
              <tr>
                <td>{user.id}</td>
                <td>{user.qalamId}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.role}</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </div>

    <div class="row mt-4">
      <div class="col-md-12">
        <h2 class="text-center">Add New User</h2>
        <form on:submit|preventDefault={addUser}>
          <div class="mb-3">
            <label for="qalamId">Qalam ID:</label>
            <input type="text" class="form-control" id="qalamId" bind:value={newUser.qalamId} required>
          </div>
          <div class="mb-3">
            <label for="name">Name:</label>
            <input type="text" class="form-control" id="name" bind:value={newUser.name} required>
          </div>
          <div class="mb-3">
            <label for="email">Email:</label>
            <input type="email" class="form-control" id="email" bind:value={newUser.email} required>
          </div>
          <div class="mb-3">
            <label for="password">Password:</label>
            <input type="password" class="form-control" id="password" bind:value={newUser.password} required>
          </div>
          <div class="mb-3">
            <label for="role">Role:</label>
            <select id="role" bind:value={newUser.role} class="form-control">
              {#each roles as role}
                <option value={role}>{role}</option>
              {/each}
            </select>
          </div>
          <button type="submit" class="btn btn-primary">Add User</button>
        </form>
      </div>
    </div>
  </div>
</main>

<style>
  /* Additional styling if needed */
</style>
