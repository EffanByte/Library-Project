<script>
  import axios from 'axios';
  import {onMount} from "svelte";
  let booktoAdd = {
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

  let droppedImage = null;
  let droppedPDF = null;

  function handleImageChange(event) {
    const files = event.target.files;
    if (files && files[0]) {
      droppedImage = files[0];
    }
  }

  function handlePDFChange(event) {
    const files = event.target.files;
    if (files && files[0] && files[0].type === 'application/pdf') {
      droppedPDF = files[0];
    } else {
      alert('Please select a PDF file');
    }
  }  

  async function addBook() {
  try {
    // First, check if the book exists
    await checkIfBookExists(booktoAdd.Title);

    // Now, use the bookexists variable to decide the next step
    if (bookexists) {
      alert("A book with this title already exists.");
      return;
    }

    const formData = new FormData();
    formData.append('Title', booktoAdd.Title);
    formData.append('Author', booktoAdd.Author);
    formData.append('Genre', booktoAdd.Genre);
    formData.append('Description', booktoAdd.Description);
    formData.append('TypeID', booktoAdd.TypeID);

    if (droppedImage) {
      formData.append('coverImage', droppedImage);
    }

    if (droppedPDF) {
      formData.append('PDF', droppedPDF);
    }

    // Make the POST request to add the book
    const response = await axios.post('http://localhost:8000/api/books', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    if (response.status === 201) {
      alert('Book added successfully');
      // Reset the form or additional logic here
      // You might want to clear the form and reset any state variables
      booktoAdd = { Title: '', Genre: '', Description: "", TypeID: 0 };
      droppedImage = null;
      droppedPDF = null;
      // Update the UI accordingly
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

    if (droppedImage) {
      formData.append('coverImage', droppedImage);
    }

    if (droppedPDF) {
      formData.append('PDF', droppedPDF);
    }

    const response = await axios.put(
      `http://localhost:8000/api/books/${bookToUpdate.BookID}`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
    );

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







function handleBookTypeChange(event) {
      booktoAdd.TypeID = event.target.value;

  }

function handleUpdateBookTypeChange(event) {
  bookToUpdate.TypeID = parseInt(event.target.value, 10);
  console.log(bookToUpdate.TypeID);
  console.log(booktoAdd.TypeID)
  
}

$: isEbookSelectedInUpdatePDF = bookToUpdate.TypeID == 1;
$: isEbookSelectedInAddPDF = booktoAdd.TypeID == 1;

let inputPDF = document.getElementById("input-pdf");


function uploadPDF(event) {
// This function will be called when a PDF is selected using the input element
if (event.target.files && event.target.files[0]) {
  const file = event.target.files[0];
  if (file.type !== 'application/pdf') {
    alert('Please select a PDF file');
    return;
  }
  droppedPDF = file; // Assign the selected file to droppedPDF
}
}

  onMount(() => {
  inputPDF = document.getElementById("input-pdf");
});


</script>



<div class="container book-management">
  <div class="row">
      <div class="col">
          <h2>Add Book</h2>
          <form on:submit|preventDefault={addBook}>
              <div class="mb-3">
                  <label for="bookName" class="form-label">Title</label>
                  <input type="text" class="form-control" id="Title" bind:value={booktoAdd.Title} required>
              </div>
              <div class="mb-3">
                  <label for="bookAuthor" class="form-label">Author</label>
                  <input type="text" class="form-control" id="bookAuthor" bind:value={booktoAdd.Author} required>
              </div>
              <div class="mb-3">
                  <label for="bookGenre" class="form-label">Genre</label>
                  <input type="text" class="form-control" id="bookGenre" bind:value={booktoAdd.Genre} required>
              </div>
              <div class="mb-3">
                  <label for="bookDescription" class="form-label">Description</label>
                  <textarea class="form-control" id="bookDescription" bind:value={booktoAdd.Description} rows="3"></textarea>
              </div>
              <div class="mb-3">
                  <label for="bookType" class="form-label">Book Type</label>
                  <select type="bookType" id = "bookType" bind:value={booktoAdd.TypeID} on:change={handleBookTypeChange} class="form-control">
                      <option value= 1 >eBook</option>
                      <option value= 2 >Physical Book</option>
                  </select>
              </div>
            

              <!-- This is your drop area -->
              <div class="mb-3">
                <label for="input-image" class="form-label">Upload Image</label>
                <input type="file" accept="image/*" id="input-image" on:change={handleImageChange} class="file-input" />
                <label for="input-image" class="btn btn-secondary">Choose File</label>
                {#if droppedImage}
                  <!-- Display the selected image file name -->
                  <p>{droppedImage.name}</p>
                {/if}
              </div>
         


            {#if isEbookSelectedInAddPDF}
              <div class="mb-3">
              <label for="input-pdf" class="form-label">Upload PDF</label>
              <input type="file" accept="application/pdf" id="input-pdf" on:change={handlePDFChange} class="file-input" />
              <label for="input-pdf" class="btn btn-secondary">Choose File</label>
            {#if droppedPDF}
              <!-- Display the selected PDF file name -->
              <p>{droppedPDF.name}</p>
            {/if}
          </div>
          {/if}


              <button type="submit" class="btn btn-primary">Add Book</button>
          </form>
      </div>

  <!---<div class = "drop-area">
      <label for = "input-pdf">
          <input type = "file" accept="application/pdf" id = "input-pdf">
      </label>

  </div>-->


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
                      <select name = "updateBookType" id="updateBookType" bind:value = {bookToUpdate.TypeID} class="form-control">
                          <option value= 1 >eBook</option>
                          <option value= 2 >Physical Book</option>
                      </select>
                  </div>
                  <div class="mb-3">
                      <label for="updateDescription" class="form-label">Description</label>
                      <textarea class="form-control" bind:value={bookToUpdate.Description} id="updateDescription" rows="3"></textarea>
                    
                         <!-- This is your drop area -->
                     <div class="mb-3">
                      <label for="input-image" class="form-label">Upload Image</label>
                      <input type="file" accept="image/*" id="input-image" on:change={handleImageChange} class="file-input" />
                      <label for="input-image" class="btn btn-secondary">Choose File</label>
                      {#if droppedImage}
                        <!-- Display the selected image file name -->
                        <p>{droppedImage.name}</p>
                      {/if}
                      </div>
                      {#if isEbookSelectedInUpdatePDF}
                      <div class="mb-3">
                      <label for="input-pdf" class="form-label">Upload PDF</label>
                      <input type="file" accept="application/pdf" id="input-pdf" on:change={handlePDFChange} class="file-input" />
                      <label for="input-pdf" class="btn btn-secondary">Choose File</label>
                    {#if droppedPDF}
                      <!-- Display the selected PDF file name -->
                      <p>{droppedPDF.name}</p>
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
    

  .file-input {
      display: none;
  }

  /* Additional styling can be added here */
  .file-input {
display: none; /* This hides the file input */
}

.btn:hover {
  background-color: #0056b3;
}

</style>







