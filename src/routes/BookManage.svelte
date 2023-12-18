<script>
    import axios from 'axios';
    let BooktoAdd = {
            Title: '',
            Genre: '',
            Description: "",
            TypeID: 0
        }

    let bookToUpdate = {
        BookID: 0,
        Title: '',
        Genre: '',
        Description: "",
        TypeID: 0
    }  
    
       // Reactive variables for selected book type text
    let selectedBookTypeText = '';
    let selectedUpdateBookTypeText = '';


    async function addBook() {
    // First, check if the book exists
    await checkIfBookExists(BooktoAdd.Title);

    // Now, use the bookexists variable to decide the next step
    if (bookexists) {
        alert("A book with this title already exists.");
        return;
    }
    const formData = new FormData();
    formData.append('Title', BooktoAdd.Title);
    formData.append('Author', BooktoAdd.Author);
    formData.append('Genre', BooktoAdd.Genre);
    formData.append('Description', BooktoAdd.Description);
    formData.append('TypeID', BooktoAdd.TypeID);

    // Assuming droppedImage is a file object from file input
    if (droppedImage) {
        formData.append('coverImage', droppedImage);
    }

    // Add PDF file to formData if available
    // For example, if you have a file input for PDF
    // if (selectedPdfFile) {
    //     formData.append('PDF', selectedPdfFile);
    // }

    try {
        const response = await axios.post('http://localhost:8000/api/books', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        if (response.status === 201) {
            alert('Book added successfully');
            // Reset the form or additional logic here
        }
    } catch (error) {
        console.error('Error adding book:', error.response?.data || error.message);
        alert('Error adding book');
    }
}


async function updateBook() {
    try {
        let formData = new FormData();
        formData.append('Title', bookToUpdate.Title);
        formData.append('Genre', bookToUpdate.Genre);
        formData.append('TypeID', bookToUpdate.TypeID);
        formData.append('Description', bookToUpdate.Description);
        if (droppedPDF) {
            formData.append('PDF', droppedPDF);
        }

        const response = await axios.put(`http://localhost:8000/api/books/update/${bookToUpdate.BookID}`, formData);
        if (response.status === 200) {
            alert('Book and PDF updated successfully');
        }
    } catch (error) {
        console.error('Error updating book and PDF:', error.response?.data || error.message);
        alert('Error updating book and PDF');
    }
}

    function removeBook() {
        // Logic for removing a book
    }

    let bookTitleToUpdate = ''; 


    let bookexists = null; // if book does not exist in database

    
    async function checkIfBookExists() {
        try {
            const response = await axios.post('http://localhost:8000/api/books/check', {
                Title: bookTitleToUpdate
        });

        if (response.status === 200 && response.data.exists) {
            bookexists = true;
            bookToUpdate = response.data.book; // Populate the fields with the existing book data
        } else {
            bookexists = false;
        }
    } catch (error) {
        console.error('Error fetching book:', error.response?.data || error.message);
        bookexists = false;
        }
    }


let droppedImage = null;

// Function to handle the dropping of the image
function handleImageDrop(event) 
{
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

let droppedPDF = null;
  // Reactive statement to check if the selected book type is eBook (1)
  $: isEbookSelected = () => {
        return BooktoAdd.TypeID === 1 || bookToUpdate.TypeID === 1;
    };


function handlePDFDrop(event) {
    event.preventDefault();
    if (event.dataTransfer.files && event.dataTransfer.files[0]) {
        const file = event.dataTransfer.files[0];
        // Check if the file is a PDF
        if (file.type !== 'application/pdf') {
            alert('Please drop a PDF file');
            return;
        }
        droppedPDF = file;
    }
}

let fileInput; // This will hold the reference to the file input element

let filePDFInput; // Reference to the file input for PDFs

// This function is called when the drop area is clicked
function openFileDialog() {
  if (fileInput) {
    fileInput.click(); // Simulate a click on the hidden file input
  }
}

// This function simulates a click on the file input for PDFs
function openFilePDFDialog() {
  filePDFInput.click();
}

// This function is called when a key is pressed while the image drop area is focused
function handleKeydown(event) {
  // Check if the Enter key or Spacebar was pressed
  if (event.key === 'Enter' || event.key === ' ') {
    openFileDialog();
  }
}

// This function is called when a key is pressed while the PDF drop area is focused
function handlePDFKeydown(event) {
  // Check if the Enter key or Spacebar was pressed
  if (event.key === 'Enter' || event.key === ' ') {
    openFilePDFDialog();
  }
}



function handleBookTypeChange(event) {
        BooktoAdd.TypeID = parseInt(event.target.value);
    }

    function handleUpdateBookTypeChange(event) {
        bookToUpdate.TypeID = parseInt(event.target.value);
    }

</script>

<div class="container book-management">
    <div class="row">
        <div class="col">
            <h2>Add Book</h2>
            <form on:submit|preventDefault={addBook}>
                <div class="mb-3">
                    <label for="bookName" class="form-label">Title</label>
                    <input type="text" class="form-control" id="Title" bind:value={BooktoAdd.Title} required>
                </div>
                <div class="mb-3">
                    <label for="bookAuthor" class="form-label">Author</label>
                    <input type="text" class="form-control" id="bookAuthor" bind:value={BooktoAdd.Author} required>
                </div>
                <div class="mb-3">
                    <label for="bookGenre" class="form-label">Genre</label>
                    <input type="text" class="form-control" id="bookGenre" bind:value={BooktoAdd.Genre} required>
                </div>
                <div class="mb-3">
                    <label for="bookDescription" class="form-label">Description</label>
                    <textarea class="form-control" id="bookDescription" bind:value={BooktoAdd.Description} rows="3"></textarea>
                </div>
                <div class="mb-3">
                    <label for="bookType" class="form-label">Book Type</label>
                    <select id="bookType" bind:value={BooktoAdd.TypeID} on:change={handleBookTypeChange} class="form-control">
                        <option value="1" >eBook</option>
                        <option value="2" >Physical Book</option>
                    </select>
                </div>
                <label for="image-drop-area" class="form-label">Upload Image</label>
               <!-- <div class="drop-area" on:drop={handleImageDrop} on:dragover={handleDragOver}>
                    {#if droppedImage}
                        <div src={droppedImage} alt="Dropped image" class="preview-image" />
                    {:else}
                        <p>Drop image here or click to upload</p>
                    {/if}
                    <input type="file" class="file-input" accept="image/*">
                </div>-->

                <!-- This is your drop area -->
                <div class="drop-area" 
                role = "button"
                on:click={openFileDialog} 
                on:keydown={handleKeydown} 
                on:drop={handleImageDrop} 
                on:dragover={handleDragOver}
                tabindex="0"> <!-- Make the div focusable -->
               {#if droppedImage}
                 <img src={droppedImage} alt="Dropped image" class="preview-image" />
               {:else}
                 <p>Drop image here or click to upload</p>
               {/if}
               <input type="file" class="file-input" accept="image/*" bind:this={fileInput}>
           </div>
           
  

        {#if isEbookSelected()}
        <!-- This is your drop area for PDFs -->
        <label for="pdf-drop-area" class="form-label">Upload PDF</label>
        <div class="drop-area" 
            role= "button"
            on:click={openFilePDFDialog} 
            on:keydown={handlePDFKeydown} 
            on:drop={handlePDFDrop} 
            on:dragover={handleDragOver}
            tabindex="0"> <!-- Make the div focusable -->
            {#if droppedPDF}
                <p>PDF: {droppedPDF.name}</p>
                {:else}
                    <p>Drop PDF here or click to upload</p>
                    <input type="file" id="pdf-drop-area" class="file-input" accept="application/pdf" on:change="{(e) => droppedPDF = e.target.files[0]}">
                {/if}
                     </div>
                {/if}

                <button type="submit" class="btn btn-primary">Add Book</button>
            </form>
        </div>

 
<div class="col">
            <h2>Update Book</h2>
            <div class="mb-3">
                <label for="bookTitleToUpdate" class="form-label">Title</label>
                <input type="text" bind:value={bookTitleToUpdate} class="form-control" id="bookTitleToUpdate">
                <button on:click={checkIfBookExists} class="btn btn-secondary mt-2">Check Book</button>
            </div>
{#if bookTitleToUpdate}
{#if bookexists}
                <form on:submit|preventDefault={updateBook}>
                    <!-- Display BookID (Read-only) -->
                    <div class="mb-3">
                        <label for="bookID" class="form-label">Book ID (Non-Updateable)</label>
                        <input type="text" class="form-control" id="bookID" value={bookToUpdate.BookID} readonly>
                    </div>
                 <!-- <form on:submit|preventDefault={updateBook}> -->
                    <div class="mb-3">
                        <label for="updateName" class="form-label">New Name</label>
                        <input type="text" bind:value={bookToUpdate.Title} class="form-control" id="updateName">
                    </div>
                    <div class="mb-3">
                        <label for="updateGenre" class="form-label">Genre</label>
                        <input type="text" bind:value={bookToUpdate.Genre} class="form-control" id="updateGenre">
                    </div>

                    <div class="mb-3">
                        <label for="updateBookType" class="form-label">Book Type</label>
                        <select id="updateBookType" bind:value = {bookToUpdate.TypeID} on:change={handleUpdateBookTypeChange} class="form-control">
                            <option value="1" >eBook</option>
                            <option value="2" >Physical Book</option>
                        </select>
                    </div>
        
                    <!--<div class="mb-3">
                        <label for="updateBookType" class="form-label">Book Type</label>
                        <select id="updateBookType" bind:value={bookToUpdate.TypeID} on:change={handleUpdateBookTypeChange} class="form-control">
                            <option value="1">eBook</option>
                            <option value="2">Physical Book</option>
                        </select>
                    </div>-->
                    <div class="mb-3">
                        <label for="updateDescription" class="form-label">Description</label>
                        <textarea class="form-control" bind:value={bookToUpdate.Description} id="updateDescription" rows="3"></textarea>
                    </div>
                    {#if isEbookSelected()}
                        <div class="drop-area" on:drop={handlePDFDrop} on:dragover={handleDragOver}>
                            {#if droppedPDF}
                                <p>PDF: {droppedPDF.name}</p>
                            {:else}
                                <p>Drop PDF here or click to upload</p>
                            <input type="file" class="file-input" accept="application/pdf" on:change="{(e) => droppedPDF = e.target.files[0]}">
                            {/if}
                        </div>
                    {/if}

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
    .file-input {
  display: none; /* This hides the file input */
}

</style>
