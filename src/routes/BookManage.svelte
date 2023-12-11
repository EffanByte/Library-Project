<script>

   let BooktoAdd = {
        Name: '',
        Genre: '',
        Description: '',
        typeID: ''
    }
    function addBook() {
        // Logic for adding a book
    }
    function updateBook() {
        // Logic to update the book
    }

    function removeBook() {
        // Logic for removing a book
    }

    let bookNameToUpdate = ''; 

    let bookToUpdate = {
        Name: '',
        genre: '',
        typeID: '',
        Description: "",

    }
    let bookexists = null; // if book does not exist in database

    async function checkIfBookExists() {
bookexists = true; // HARD CODED RIGHT NOW
        // Replace with your API call or database check

        if (bookToUpdate) {
            // Book exists, populate the fields
        } else {
            // Handle book not found
        }
    }


        let droppedImage = null;

    // Function to handle the dropping of the image
    function handleDrop(event) {
        event.preventDefault();
        if (event.dataTransfer.files && event.dataTransfer.files[0]) {
            const file = event.dataTransfer.files[0];
            // Perform validation if necessary (e.g., check file type)

            const reader = new FileReader();
            reader.onload = (e) => {
                droppedImage = e.target.result; // This is the base64 encoded image
            };
            reader.readAsDataURL(file);
        }
    }
        function handleDragOver(event) {
        event.preventDefault();
    }
</script>

<div class="container book-management">
    <div class="row">
        <div class="col">
            <h2>Add Book</h2>
            <form on:submit|preventDefault={addBook}>
                <div class="mb-3">
                    <label for="bookName" class="form-label">Name</label>
                    <input type="text" class="form-control" id="bookName" bind:value={BooktoAdd.name} required>
                </div>
                <div class="mb-3">
                    <label for="bookAuthor" class="form-label">Author</label>
                    <input type="text" class="form-control" id="bookAuthor" bind:value={BooktoAdd.author} required>
                </div>
                <div class="mb-3">
                    <label for="bookGenre" class="form-label">Genre</label>
                    <input type="text" class="form-control" id="bookGenre" bind:value={BooktoAdd.genre} required>
                </div>
                <div class="mb-3">
                    <label for="bookDescription" class="form-label">Description</label>
                    <textarea class="form-control" id="bookDescription" bind:value={BooktoAdd.description} rows="3"></textarea>
                </div>
                <div class="mb-3">
                    <label for="bookType" class="form-label">Book Type</label>
                    <select id="bookType" bind:value={BooktoAdd.typeID} class="form-control">
                        <option value="1">eBook</option>
                        <option value="2">Physical Book</option>
                    </select>
                </div>
                <div class="drop-area" on:drop={handleDrop} on:dragover={handleDragOver}>
                    {#if droppedImage}
                        <div src={droppedImage} alt="Dropped image" class="preview-image" />
                    {:else}
                        <p>Drop image here or click to upload</p>
                    {/if}
                    <input type="file" class="file-input" accept="image/*">
                </div>
                <button type="submit" class="btn btn-primary">Add Book</button>
            </form>
        </div>
<div class="col">
            <h2>Update Book</h2>
            <div class="mb-3">
                <label for="bookNameToUpdate" class="form-label">Book Name</label>
                <input type="text" bind:value={bookNameToUpdate} class="form-control" id="bookNameToUpdate">
                <button on:click={checkIfBookExists} class="btn btn-secondary mt-2">Check Book</button>
            </div>
{#if bookNameToUpdate}
{#if bookexists}
                <form on:submit|preventDefault={updateBook}>
                    <div class="mb-3">
                        <label for="updateName" class="form-label">New Name</label>
                        <input type="text" bind:value={bookToUpdate.name} class="form-control" id="updateName">
                    </div>
                    <div class="mb-3">
                        <label for="updateGenre" class="form-label">Genre</label>
                        <input type="text" bind:value={bookToUpdate.genre} class="form-control" id="updateGenre">
                    </div>
                    <div class="mb-3">
                        <label for="updateBookType" class="form-label">Book Type</label>
                        <select id="updateBookType" bind:value={bookToUpdate.typeID} class="form-control">
                            <option value="1">eBook</option>
                            <option value="2">Physical Book</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="updateDescription" class="form-label">Description</label>
                        <textarea class="form-control" bind:value={bookToUpdate.description} id="updateDescription" rows="3"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Update Book</button>
                </form>
                {:else if bookexists == false}
                <div style = color:red>This book was not found</div>
                     <!-- else if content here -->
                {/if}

                {/if}
        </div>

        <div class="col">
        </div>
    </div>
</div>

<style>




    .btn {
        margin: 10px;
        width: 150px; /* Adjust the width as needed */
    }
        .drop-area {
        border: 2px dashed #ccc;
        padding: 20px;
        text-align: center;
        cursor: pointer;
    }

    .preview-image {
        max-width: 100%;
        height: auto;
        margin-top: 10px;
    }

    .file-input {
        display: none;
    }

    /* Additional styling can be added here */
</style>
