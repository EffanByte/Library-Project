<script>
    import { link } from 'svelte-spa-router';
    import {user} from '../components/store.js';
    import ScrollBar from '../components/ScrollBar.svelte';
    
</script>
{#if $user.role == "Supervisor"}
<ScrollBar></ScrollBar>
{/if}
    <div class="row justify-content-center mt-5 mx-auto col-10">
        <!-- Repeat this structure for each card -->
        {#if $user.role == "Supervisor" || $user.role == "Ebooks_manager" || $user.role == "Archivist" || $user.role == "Technical_Services_Librarian"}
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="BookMNG.webp" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">Manage Books</h5>
                    <p class="card-text flex-grow-1">Add, update or delete books.</p>
                    <a href={`/Librarian/BookManagement/`} class="btn btn-primary mt-2 align-self-start" use:link >Click Here</a>
                </div>
            </div>
        </div>
        {/if}
        {#if $user.role == "Supervisor" || $user.role == "Technical_Services_Librarian" || $user.role == "Ebooks_Librarian"}
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="RentMNG.png" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">Issued Books Management</h5>
                    <p class="card-text flex-grow-1">Check the status of all the issued books.</p>
                    <a href={`/Librarian/RentManagement/`} class="btn btn-primary mt-2 align-self-start" use:link>Click Here</a>
                </div>
            </div>
        </div>
        {/if}

                {#if $user.role == "Supervisor"}
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="UserMNG.jpg" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">

                    <h5 class="card-title">User Management</h5>
                    <p class="card-text flex-grow-1">Add, Update and Remove Users and assign them roles.</p>
                    <a href={`/Librarian/UserManagement/`} class="btn btn-primary mt-2 align-self-start" use:link >Click Here</a>
                </div>
            </div>
        </div>
        {/if}
        {#if $user.role == "Supervisor" || $user.role == "Technical_Services_Librarian"}
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="RoomMNG.jpg" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">Room Management</h5>
                    <p class="card-text flex-grow-1">View Room Bookings and Edit them.</p>
                    <a href={`/Librarian/RoomManagement/`} class="btn btn-primary mt-2 align-self-start" use:link>Click Here</a>
                </div>
            </div>
        </div>
        {/if}
                {#if $user.role == "Supervisor" || $user.role == "Technical_Services_Librarian"}
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="RoomMNG.jpg" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">View Complaints</h5>
                    <p class="card-text flex-grow-1">View Complaints and Fix them</p>
                    <a href={`/Librarian/ComplaintManagement/`} class="btn btn-primary mt-2 align-self-start" use:link>Click Here</a>
                </div>
            </div>
        </div>
        {/if}

        
        {#if $user.role == "Supervisor" || $user.role == "Technical_Services_Librarian"}
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="lostfnd.jpg" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">Lost and Found</h5>
                    <p class="card-text flex-grow-1">Manage Lost and Found items here</p>
                    <a href={`/Librarian/LostAndFoundManagement/`} class="btn btn-primary mt-2 align-self-start" use:link>Click Here</a>
                </div>
            </div>
        </div>
        {/if}
    </div>
    
<style>

    .card {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Subtle shadow for depth */
        border-radius: 10px; /* Rounded corners */
        transition: transform 0.3s ease-in-out;
    }

    .card-img-top {
        height: 180px; /* Fixed height for images */
        object-fit: cover; /* Ensures images cover the area nicely */
        border-top-left-radius: 10px; /* Rounded corners for image */
        border-top-right-radius: 10px;
    }

    .card-body {
        padding: 15px; /* Inner spacing for card content */
    }

    .card-title {
        font-size: 1.2rem; /* Uniform title size */
    }

    .card-text {
        font-size: 0.9rem; /* Consistent text size */
    }

   

    .card:hover {
        transform: scale(1.05);
    }


    .btn-primary {
        background-color: #0056b3; /* Example primary color */
        /* Additional button styling if needed */
    }
     


    @media (max-width: 576px) {
        .card-img-top {
            height: 160px; /* Smaller image height on smaller screens */
        }
    }
</style>
