<script>
    // Dummy items array
    const items = [
        { id: 1, cover: 'path/to/cover1.jpg', text: 'Item 1' },
        { id: 2, cover: 'path/to/cover2.jpg', text: 'Item 2' },
        { id: 1, cover: 'path/to/cover1.jpg', text: 'Item 1' },
        { id: 2, cover: 'path/to/cover2.jpg', text: 'Item 2' },
        { id: 1, cover: 'path/to/cover1.jpg', text: 'Item 1' },
        { id: 2, cover: 'path/to/cover2.jpg', text: 'Item 2' },
        { id: 1, cover: 'path/to/cover1.jpg', text: 'Item 1' },
        { id: 2, cover: 'path/to/cover2.jpg', text: 'Item 2' },
        { id: 1, cover: 'path/to/cover1.jpg', text: 'Item 1' },
        { id: 2, cover: 'path/to/cover2.jpg', text: 'Item 2' },



        // ... more items
    ];
</script>

<div class="container-fluid mt-4 px-4">
    <div class="d-flex flex-row flex-nowrap overflow-auto scrollbar">
        {#each items as item}
            <div class="card card-item shadow-sm">
                <img src={item.cover} class="card-img-top" alt={`Cover of ${item.text}`}>
                <div class="card-body">
                    <p class="card-text">Some description or detail about the item.</p>
                    <!-- Add more content or buttons if needed -->
                </div>
            </div>
        {/each}
    </div>
</div>

<style>
    .scrollbar::-webkit-scrollbar {
        height: 8px;
    }

    .scrollbar::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }

    .scrollbar::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 4px;
    }

    .scrollbar::-webkit-scrollbar-thumb:hover {
        background: #555;
    }

    .card-item {
        flex: 0 0 auto; /* Prevents cards from shrinking */
        width: 200px; /* Fixed width for each card */
        margin-right: 15px; /* Space between cards */
        border-radius: 0.75rem; /* Rounded corners */
    }

    .card-img-top {
        height: 150px; /* Consistent height for images */
        object-fit: cover; /* Ensures images cover the card top area */
        border-top-left-radius: 0.75rem; /* Align image border with card */
        border-top-right-radius: 0.75rem;
    }

    .card-body {
        padding: 1rem; /* Inner card spacing */
    }
</style>
