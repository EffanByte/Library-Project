<script>
    import { createEventDispatcher } from 'svelte';
    import axios from 'axios';

    export let show;
    const dispatch = createEventDispatcher();

    let name = '';
    let email = '';
    let password = '';
    let confirmPassword = '';
    let userId = '';
    let validationError = '';  // New variable to store validation error message

    async function handleSignUp() {
        // Reset previous validation error
        validationError = '';

        if (password !== confirmPassword) {
            validationError = "Passwords do not match";
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/api/signup', {
                Name: name,
                Email: email,
                Password: password,
                QalamID: userId
            });

            if (response.status === 201) {
                console.log("Signed up successfully:", response.data);
                // Handle successful sign up, e.g., redirect to login or dashboard
                close()
            }
        } catch (error) {
            console.error("Sign up error:", error.response?.data || error.message);
            // Set validationError based on the error received
            validationError = error.response?.data?.error || "An error occurred during sign up";
            //alert(error.response?.data?.error);
            console.error("Sign up error response:", error.response);

        }
    }

    function close() {
        show = false;
        dispatch('close');
    }
</script>

{#if show}
<div class="modal show" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Sign Up</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" on:click={close}>
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form on:submit|preventDefault={handleSignUp}>
                    {#if validationError}
                        <div class="alert alert-danger" role="alert">
                            {validationError}
                        </div>
                    {/if}
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" class="form-control" id="name" bind:value={name}>
                    </div>
                    <div class="form-group">
                        <label for="userId">ID</label>
                        <input type="text" class="form-control" id="userId" bind:value={userId}>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" class="form-control" id="email" bind:value={email}>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" class="form-control" id="password" bind:value={password}>
                    </div>
                    <div class="form-group">
                        <label for="confirmPassword">Confirm Password</label>
                        <input type="password" class="form-control" id="confirmPassword" bind:value={confirmPassword}>
                    </div>
                    <button type="submit" class="btn btn-primary">Sign Up</button>
                </form>
            </div>
        </div>
    </div>
</div>
<div class="modal-backdrop show"></div>
{/if}

<style>
    .modal {
        /* Your modal styling */
    }
    .show {
        display: block;
    }
    .modal-backdrop {
        /* Your modal backdrop styling */
    }
</style>












<!--
<script>
    import { createEventDispatcher } from 'svelte';
    import axios from 'axios';

    export let show;
    const dispatch = createEventDispatcher();

    let name = '';
    let email = '';
    let password = '';
    let confirmPassword = '';
    let userId = '';

    async function handleSignUp() {
        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }
        
        try {
            const response = await axios.post('http://localhost:8000/api/signup', {
                Name: name,
                Email: email,
                Password: password,
                QalamID: userId
            });

            if (response.status === 200) {
                console.log("Signed up successfully:", response.data);
                // Handle successful sign up, e.g., redirect to login or dashboard
            }
        } catch (error) {
            console.error("Sign up error:", error.response?.data || error.message);
            // Handle error, e.g., show an error message to the user
        }

        close();
    }

    function close() {
        show = false;
        dispatch('close');
    }
</script>

{#if show}
<div class="modal show" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Sign Up</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" on:click={close}>
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form on:submit|preventDefault={handleSignUp}>
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" class="form-control" id="name" bind:value={name}>
                    </div>
                     <div class="form-group">
                        <label for="userId">ID</label>
                        <input type="text" class="form-control" id="userId" bind:value={userId}>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" class="form-control" id="email" bind:value={email}>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" class="form-control" id="password" bind:value={password}>
                    </div>
                    <div class="form-group">
                        <label for="confirmPassword">Confirm Password</label>
                        <input type="password" class="form-control" id="confirmPassword" bind:value={confirmPassword}>
                    </div>
                    <button type="submit" class="btn btn-primary">Sign Up</button>
                </form>
            </div>
        </div>
    </div>
</div>
<div class="modal-backdrop show"></div>
{/if}

<style>
    .modal {
        /* Your modal styling */
    }
    .show {
        display: block;
    }
    .modal-backdrop {
        /* Your modal backdrop styling */
    }
</style>


-->

