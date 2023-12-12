<script>

    let rentedBooks = [
        { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },
                { bookID: '001', name: 'Book 1', issuedBy: 'User A', dueDate: '2023-07-15' },
        { bookID: '002', name: 'Book 2', issuedBy: 'User B', dueDate: '2023-07-20' },

    ];
    // THE PLAN IS TO DISPLAY AT MOST 50 ENTERIES HERE. OTHERWISE USE ONE OF THE SORTING ALGOS TO RETRIEVE THE PROPER ANSWER
    let Sorted = "Recently Added";
    let selectedOption = 'Time'; // Default selection
    let parameter = ''; // Variable to store textarea input

    function extendDueDate(bookID) {
        console.log('Extending due date:', bookID);
        // Add logic to handle the due date extension
    }
    
    function returnBook(bookID) {
        console.log('Returning book:', bookID);
        // Add logic to handle the book return
    }
</script>

<div class="container">
    <div class="table-container">
        <h1>Sorted by {Sorted}</h1>
        <table class="mytable">
            <thead>
                <tr>
                    <th>BookID</th>
                    <th>Name</th>
                    <th>Issued by</th>
                    <th>Due Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {#each rentedBooks as book}
                    <tr>
                        <td>{book.bookID}</td>
                        <td>{book.name}</td>
                        <td>{book.issuedBy}</td>
                        <td>{book.dueDate}</td>
                        <td><button on:click={() => returnBook(book.bookID)}>Return Book</button>
                            <button on:click= {() => extendDueDate(book.bookID)}>Extend Due Date</button>
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
    <div class = "column">
<div class="container mt-3">
        <div class="mb-3">
        <label for="options" class="form-label">Sort by</label>
        <select id="options" class="form-select" bind:value={Sorted}>
            <option value="Time">Date</option>
            <option value="User">User</option>
            <option value="Recently Added">Recently Added</option>
            <option value="BookID">BookID</option>
        </select>
    </div>
    <div class="mb-3">
        <label for="options" class="form-label">Filter By:</label>
        <select id="options" class="form-select" bind:value={selectedOption}>
            <option value="Time">Date</option>
            <option value="User">User</option>
            <option value="Recently Added">Recently Added</option>
            <option value="BookID">BookID</option>
        </select>
    </div>

    <div class="mb-3">
        <label for="parameter">Filter</label>
        <textarea id="parameter" class="form-control" bind:value={parameter} rows="3"></textarea>
    </div>
</div>
    </div>
</div>


<style>

    .table-container {
        width: 100%;
        max-height: 30vh; /* 30% of the viewport height */
        overflow-y: auto;
    }

    .mytable {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    /* Additional styles for button and other elements */
</style>
