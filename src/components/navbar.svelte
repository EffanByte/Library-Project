<script>
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();
    function openLogin() {
        dispatch('login');
    }
    function openSignup(){
        dispatch('signup');
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

        <!-- Login and Signup Buttons -->
        <div class="d-flex">
            <button class="btn btn-outline-primary" type="button" on:click={openLogin}>Login</button>
            <button class="btn btn-primary" type="button" style="margin-left: 10px;" on:click = {openSignup}>Sign Up</button>
        </div>
    </div>
</nav>