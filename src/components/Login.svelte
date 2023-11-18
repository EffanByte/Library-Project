<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    export let show;
    let username = '';
    let password = '';
    
    function handleLogin() {
        // Implement your login logic here
        console.log(username, password);
        close(); 
    }
    function close(){
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
                        <label for="username">Username</label>
                        <input type="text" class="form-control" id="username" bind:value={username}>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" class="form-control" id="password" bind:value={password}>
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
</style>