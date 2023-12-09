<script>
    import { createEventDispatcher } from "svelte";
    import { loggedIn, user } from './store.js';
    import { push } from 'svelte-spa-router';
    import axios from 'axios';

    const dispatch = createEventDispatcher();

    export let show;
    let Email = '';
    let Name = '';
    let Password = '';
    let isLibrarian = true;

    async function handleLogin() {
        try {
            const response = await axios.post('http://localhost:8000/api/login', {
                Email,
                Name,
                Password
            });

            if (response.status === 200) {
                // Assuming the backend response contains the user and a flag for librarian status
                loggedIn.set({ is: true }); // Updating store value
                user.set({ username: response.data.name }); // Updating user store

                close();

                if (response.data.isLibrarian) {
                    push('/Librarian/');
                } else {
                    //push('/User'); // Redirect to a different page for non-librarians
                    push('/Librarian/'); // redirecting to librarian page by default temporarily
                }
            } else {
                alert("Invalid credentials");
            }
        } catch (error) {
            console.error("Login error:", error.response?.data || error.message);
            alert("Login failed. Please try again.");
        }
    }

    function close() {
        show = false;
        dispatch('close');
    }
</script>

{#if show}
<div class="modal show" tabindex="-1" role="dialog" style="display: block;">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" on:click={close}>
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form on:submit|preventDefault={handleLogin}>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="text" class="form-control" id="email" bind:value={Email}>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" class="form-control" id="password" bind:value={Password}>
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>
        </div>
    </div>
</div>
<div class="modal-backdrop show"></div>
{/if}

<style>
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1050;
        display: none;
        overflow: hidden;
        outline: 0;
    }

    .show {
        display: block;
    }

    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1040;
        width: 100vw;
        height: 100vh;
        background-color: #000;
        opacity: .5;
    }
    button {
        margin-top: 10px;
    }
</style>