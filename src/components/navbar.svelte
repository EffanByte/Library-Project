<script>
    import { createEventDispatcher } from 'svelte';
    import {user, loggedIn} from "./store.js";
    import { push } from 'svelte-spa-router';
    const dispatch = createEventDispatcher();
    
     let showDropdown = false;
        function toggleDropdown() {
            console.log(showDropdown);
        showDropdown = !showDropdown;
    }
        function logout() {
        loggedIn.set({is: false});
        user.set({ username: '',});
        push('/');
        showDropdown = false;
    }
        function goToProfile() {
            console.log($user.username);
        push(`/user/${user.username}`);
        showDropdown = false;
    }
    function openLogin() {
        dispatch('login');
    }
    function openSignup(){
        dispatch('signup');
    }
    function handleKeydown(){
    }
</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <!-- Logo -->
        <a class="navbar-brand" href="/#/">
            Library Management
        </a>

        <!-- Toggler for Mobile View -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
            <!-- Tagline -->
            <div class="navbar-nav">
                <span class="nav-link"></span>
            </div>
        </div>
{#if $loggedIn.is == true} <!-- Check if the user is logged in -->
    <div class="user-area" style = "cursor: pointer"on:click={toggleDropdown}>
        Hello, {$user.username}!
        {#if showDropdown} <!-- Dropdown toggle -->
<div class = "dropdown-container" on:click = {toggleDropdown}>
<div class="dropdown-item" on:click={goToProfile}>Profile</div>
<div class="dropdown-item" on:click = {logout}>Log Out</div>    
</div>
        {/if}
    </div>
{:else}
    <div class="d-flex">
        <button class="btn btn-outline-primary" type="button" on:click = {openLogin}>Login</button>
        <button class="btn btn-primary" type="button" style="margin-left: 10px;" on:click={openSignup}>Sign Up</button>
    </div>
{/if}
</nav>

<style>
.dropdown-container {
        position: relative; /* Required for absolute positioning of children */
        cursor: pointer;
        /* Additional styling */
    }

    .dropdown-menu {
        display: none; /* Hide by default */
        position: absolute;
        right: 0; /* Align to the right side of .dropdown-container */
        top: 100%; /* Position right below the navbar */
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        width: 200px; /* Or as needed */
        z-index: 1000;
    }

    .dropdown-container:hover .dropdown-menu,
    .dropdown-container:focus .dropdown-menu {
        display: block; /* Show on hover or focus */
    }

    .dropdown-item {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }

    .dropdown-item:hover {
        background-color: #f6f6f6;
    }

    /* Optional: Style to remove the bottom border for the last item */
    .dropdown-item:last-child {
        border-bottom: none;
    }
    </style>