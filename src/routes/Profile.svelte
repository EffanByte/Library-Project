<script>
    import { onMount } from 'svelte';
    import { user } from '../components/store.js';  // Import your user store
    import { get } from 'svelte/store';

    let profileData = {
        userName: "",
        cmsId: 0,
        userEmail: "",
        booksRented: [],  // Assuming you will populate this from another source
        lateFees: ""      // Assuming you will populate this from another source
    };

    // Function to fetch user data
    async function fetchUserData() {
        try {
            const loggedInUser = get(user);
            // Make a request to your server to get user information
            const response = await fetch(`http://localhost:8000/api/profile?id=${loggedInUser.id}`);
            if (!response.ok) {
                throw new Error('Failed to fetch user data');
            }
            const userData = await response.json();
            profileData = {  // Reassign profileData to a new object to be reactive
                userName: userData.Name,
                cmsId: userData.QalamID,
                userEmail: userData.Email,
                booksRented: profileData.booksRented,  
                lateFees: profileData.lateFees
            };
        } catch (error) {
            console.error(error.message);
        }
    }

    onMount(() => {
        fetchUserData();
    });
</script>


<div class="container my-4">
    <div class="text-center">
        <h3>{profileData.userName}</h3>
    </div>
    <h4 class="mt-4">About Me</h4>
    <p>CMS ID: {profileData.cmsId}</p>
    <p>Email: {profileData.userEmail}</p>

    <h4 class="mt-4">Currently Rented/Bought Books</h4>
    <ul class="list-group">
        {#each profileData.booksRented as book}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                {book.title}
                <span class="badge bg-primary rounded-pill">Return by: {book.returnBy}</span>
            </li>
        {/each}
    </ul>

    <div class="alert alert-info mt-4" role="alert">
        Late Fees: {profileData.lateFees}
    </div>
</div>