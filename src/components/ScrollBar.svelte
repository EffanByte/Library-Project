<script>
    // Dummy items array
    const items = [
        { id: 1, cover: 'booknews.png', text: "User Affan just issued Effan's Book"},
        { id: 2, cover: 'avatar2.avif', text: "User Affan just signed up" },
        { id: 1, cover: 'booknews.png', text: 'User Hamza Riaz just submitted a complaint' },
        { id: 2, cover: 'booknews.png', text: 'User Arham booked room #101' },
        { id: 1, cover: 'avatarimg.png', text: 'User Arham just signed up' },
        { id: 2, cover: 'booknews.png', text: "User Hamza's complaint has been resolved" },
        { id: 1, cover: 'avatarimg.png', text: 'User Shah just signed up' },
        { id: 2, cover: 'avatar2.avif', text: 'User Hamza just Signed up' },


        // ... more items
    ];
</script>

<div class="container-fluid mt-4 px-4">
    <div class="d-flex flex-row flex-nowrap overflow-auto scrollbar">
        {#each items as item}
             <div class="col-md-4 mb-3">
                <div class="card">
                <img class="img-fluid" alt="100%x280" src="{item.cover}">
                    <div class="card-body">
                        <h4 class="card-title">{item.text}</h4>
                    </div>
                </div>
            </div>
        {/each}
    </div>
</div>

<style>
    .scrollbar::-webkit-scrollbar {
        height: 8px;
    }
    .card-title{
        font-size: 15px;
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
    .card {
        width: 150px;
        display: flex;
        flex-direction: row;
    }

    .card-body {
        padding: 1rem; /* Inner card spacing */
    }
    img {
        max-height: 20vh
    }
</style>