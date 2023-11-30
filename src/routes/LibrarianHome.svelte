<script>
    import ScrollBar from '../components/ScrollBar.svelte';
</script>
<ScrollBar></ScrollBar>

<div class="container mt-4 dashboard">
    <div class="row">
        <!-- Repeat this structure for each card -->
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card h-100">
                <img src="path/to/image.jpg" class="card-img-top" alt="Feature">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">Feature Title</h5>
                    <p class="card-text flex-grow-1">Brief description of the feature.</p>
                    <a href="#" class="btn btn-primary mt-2 align-self-start">Learn More</a>
                </div>
            </div>
        </div>
        <div class="col-md-6 col-lg-3 mb-4">
            <div class="card">
                <img src="path/to/user-management-image.jpg" class="card-img-top" alt="User Management">
                <div class="card-body">
                    <h5 class="card-title">User Management</h5>
                    <p class="card-text">Manage user accounts, permissions, and data.</p>
                    <a href="#" class="btn btn-primary">Manage Users</a>
                </div>
            </div>
        </div>
                <div class="col-md-6 col-lg-3 mb-4">
            <div class="card">
                <img src="path/to/loan-management-image.jpg" class="card-img-top" alt="Loan Management">
                <div class="card-body">
                    <h5 class="card-title">Loan Management</h5>
                    <p class="card-text">Track and manage book loans and returns.</p>
                    <a href="#" class="btn btn-primary">Manage Loans</a>
                </div>
            </div>
        </div>
                <div class="col-md-6 col-lg-3 mb-4">
            <div class="card">
                <img src="path/to/room-reservation-image.jpg" class="card-img-top" alt="Room Reservation System">
                <div class="card-body">
                    <h5 class="card-title">Room Reservation System</h5>
                    <p class="card-text">Manage reservations for study rooms and spaces.</p>
                    <a href="#" class="btn btn-primary">Manage Reservations</a>
                </div>
            </div>
        </div>

    </div>
</div>

<style>
    .dashboard {
        padding-bottom: 30px; /* Adds space at the bottom of the container */
    }

    .card {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Subtle shadow for depth */
        border-radius: 10px; /* Rounded corners */
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
