<script>
    import { push } from "svelte-spa-router";
    import {user } from "../components/store.js";
    let name = $user.username;
function gotoCatalogue(){
    push("/Catalogue");
}
function gotoRoom(){
    push("/Room");
}
function gotoLost(){
    push("/Lost");
}
function gotoComplaint(){
    push("/Complaint");
}
</script>

<div class="container">
    <div class="row">
        <div class="col-md-6 mt-3">
            <div class="greeting">
                {#if $user.username == ''}
            <h2>Good Afternoon, Guest!</h2>
            {:else}
                 <h2>Good Afternoon, {$user.username}!</h2>
                {/if}
            </div>
        </div>
<div class="col-md-6">
            <!-- Move the image and button to the top right side -->
            <div class="d-flex flex-column align-items-center justify-content-center mt-4 spa">
                <img src="librarybg.jpg" alt="Last Read Book" class="effimg">
                <button class="btn btn-primary mt-2 mb-3">Continue Reading Last Book</button>
            </div>
        </div>
    </div>

    <div class="row">
    <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="bookimg.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Browse Catalogue</h5>
        <p class="card-text">Check out all the books in our library here.</p>
        <button on:click={gotoCatalogue} class="btn btn-outline-success btn-sm">Go</button>
      </div>
     </div>
    </div>
        <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="conferenceimg.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Room Rental</h5>
        <p class="card-text">Rent a conference room for all your meetings.</p>
       <a href="" class="btn btn-outline-success btn-sm">Go</a>
      </div>
     </div>
    </div>
  <div class="col-lg-4 mb-4">
  <div class="card">
      <img src="https://images.unsplash.com/photo-1516214104703-d870798883c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=60" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">Lost and Found</h5>
        <p class="card-text">Lost an item? Check the list to see if we found it.</p>
       <a href="" class="btn btn-outline-success btn-sm">Go</a>
      </div>
      </div>
    </div>
    <div class="col-lg-4 mb-4">
    <div class="card">
      <img src="complaint.jpg" alt="" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">File a Complaint</h5>
        <p class="card-text">Tell us about your complaints.</p>
       <a href="" class="btn btn-outline-success btn-sm">Go</a>
      </div>
     </div>
    </div>
  </div>
</div>

<style>
    .effimg{
        aspect-ratio: 11/16;
        height: 30vh;
    }
    .greeting h2 {
        /* Add styling for the greeting text */
        color: #4a4e69; /* Example color */
        font-weight: bold;
    }


    .card {
        transition: transform 0.3s ease-in-out;
    }

    .card:hover {
        transform: scale(1.05);
    }

</style>
