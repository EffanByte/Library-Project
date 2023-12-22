<script>
    import { createEventDispatcher } from 'svelte';
    import {user, loggedIn, isLibrarian} from "./store.js";
    import { push } from 'svelte-spa-router';
    import { onMount, onDestroy } from 'svelte';
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
    let homepage = "/#/";
    function handleOutsideClick(event) {
        // Check if the click is outside the navbar or dropdown
        if (showDropdown && !event.target.closest('.navbar')) {
            toggleDropdown();
        }
    }

  onMount(() => {
      window.addEventListener('click', handleOutsideClick);
  });

  onDestroy(() => {
      window.removeEventListener('click', handleOutsideClick);
  });

</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <!-- Logo -->
    {#if $user.role === 'Supervisor'}
    <a class="navbar-brand"  href= "/#/Librarian">
      Virtual Library
    </a>
    {:else}
        <a class="navbar-brand"  href= "/#/">
      Virtual Library
    </a>
    {/if}
{#if $isLibrarian.is == true}
    <div class="navbar-center">
    </div>
    {/if}
    {#if $loggedIn.is == true}
      <!-- Check if the user is logged in -->
      <div class="user-area" style="cursor: pointer" on:click={toggleDropdown}>
        
        Hello, {$user.username}!
        {#if showDropdown}
          <!-- Dropdown toggle -->
          <div class="dropdown-container" on:click={toggleDropdown}>
            <div class="dropdown-item" on:click={goToProfile}>Profile</div>
            <div class="dropdown-item" on:click={logout}>Log Out</div>
          </div>
        {/if}
      </div>
    {:else}
      <div class="d-flex">
        <button class="btn btn-outline-primary" type="button" on:click={openLogin}>Login</button>
        <button class="btn btn-primary" type="button" style="margin-left: 10px;" on:click={openSignup}>Sign Up</button>
      </div>
    {/if}

  <!-- New navbar element -->

</div>
</nav>

<style>
.dropdown-container {
      position: relative; /* Required for absolute positioning of children */
      cursor: pointer;
      /* Additional styling */
  }

  .dropdown-container {
      position: absolute;
      right: 0;
      background-color: #f9f9f9;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      z-index: 1;
  }

  .dropdown-item {
      padding: 12px 16px;
      text-decoration: none;
      display: block;
      color: black;
  }

  .dropdown-item:hover {  
      background-color: #f1f1f1;
  }

  /* Optional: Style to remove the bottom border for the last item */
  .dropdown-item:last-child {
      border-bottom: none;
  }
  </style>