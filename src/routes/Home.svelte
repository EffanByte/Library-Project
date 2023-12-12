<script>
    import { push } from "svelte-spa-router";

function gotoCatalogue(){
    push("/Catalogue");
}
</script>

<div class="container">
    <div class="row">
        <div class="col-md-6">
            <div class="greeting">
                <h2>Good Afternoon, User!</h2>
            </div>
        </div>
        <div class="col-md-6 text-end">
            <div class="last-read">
                <img src="path/to/last-read-book.jpg" alt="Last Read Book" class="img-fluid mb-2">
                <button class="btn btn-primary">Continue Reading Last Book</button>
            </div>
        </div>
    </div>

    <div class="row mt-4">
        <div class="col-md-3">
            <div class="card"  on:click={gotoCatalogue}>
                <img src="path/to/image.jpg" class="card-img-top" alt="Browse the Catalogue">
                <div class="card-body">
                    <p class="card-text">Browse the Catalogue</p>
                </div>
            </div>
        </div>
        <div class="col-md-3" on:click={() => {/* Navigate to Book a Room */}}>
            <div class="card">
                <img src="path/to/image.jpg" class="card-img-top" alt="Book a Room">
                <div class="card-body">
                    <p class="card-text">Book a Room</p>
                </div>
            </div>
        </div>
        <div class="col-md-3" on:click={() => {/* Navigate to Lost & Found */}}>
            <div class="card">
                <img src="path/to/image.jpg" class="card-img-top" alt="Lost & Found">
                <div class="card-body">
                    <p class="card-text">Lost & Found</p>
                </div>
            </div>
        </div>
        <div class="col-md-3" on:click={() => {/* Navigate to Register a Complaint */}}>
            <div class="card">
                <img src="path/to/image.jpg" class="card-img-top" alt="Register a Complaint">
                <div class="card-body">
                    <p class="card-text">Register a Complaint</p>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .greeting h2 {
        /* Add styling for the greeting text */
        color: #4a4e69; /* Example color */
        font-weight: bold;
    }

    .last-read img {
        /* Styling for the book image */
        max-width: 200px; /* Adjust as needed */
    }

    .card {
        cursor: pointer;
        transition: transform 0.3s ease-in-out;
    }

    .card:hover {
        transform: scale(1.05);
    }

    .custom-horizontal-container {
    width: 100%; /* Full width of the parent element */
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
    aspect-ratio: 16 / 9; /* Example aspect ratio for horizontal layout */
    overflow: hidden; /* Ensures content doesn't overflow the set aspect ratio */
}
</style>
