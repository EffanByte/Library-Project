<script>
    // Import statements if needed
    let bookType;
    // Functions for each feature - keep them empty for now
    function addBook() {
        // Logic for adding a book
    }

    function updateBook() {
        // Logic for updating a book
    }

    function removeBook() {
        // Logic for removing a book
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
                    <input type="text" class="form-control" id="bookName" required>
                </div>
                <div class="mb-3">
                    <label for="bookAuthor" class="form-label">Author</label>
                    <input type="text" class="form-control" id="bookAuthor" required>
                </div>
                <div class="mb-3">
                    <label for="bookGenre" class="form-label">Genre</label>
                    <input type="text" class="form-control" id="bookGenre" required>
                </div>
                <div class="mb-3">
                    <label for="bookDescription" class="form-label">Description</label>
                    <textarea class="form-control" id="bookDescription" rows="3"></textarea>
                </div>
                <div class="mb-3">
                    <label for="bookType" class="form-label">Book Type</label>
                    <select id="bookType" bind:value={bookType} class="form-control">
                        <option value="1">eBook</option>
                        <option value="2">Physical Book</option>
                    </select>
                </div>
                <div class="drop-area" on:drop={handleDrop} on:dragover={handleDragOver}>
                    {#if droppedImage}
                        <img src={droppedImage} alt="Dropped image" class="preview-image" />
                    {:else}
                        <p>Drop image here or click to upload</p>
                    {/if}
                    <input type="file" class="file-input" accept="image/*">
                </div>
                <button type="submit" class="btn btn-primary">Add Book</button>
            </form>
        </div>
        <div class="col">
        </div>

        <div class="col">
        </div>
    </div>
</div>

<style>
    .book-management-container {
        text-align: center;
        padding: 20px;
    }

    .actions {
        margin-top: 30px;
    }

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
