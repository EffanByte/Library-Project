<script>
    import BookCard from "./BookCard.svelte";
console.log("test");
    let showModal = false;
    function handleLoginEvent() {
        showModal = true;
        showModal = !!showModal;
    }
    let books = [
    { id: 1, title: 'Book 1', coverUrl: 'testcover.jpeg'},
    { id: 2, title: 'Book 2', coverUrl: 'testcover.jpeg'}
];

</script>

<main>
<div class = "heading">Browse The Catalogue here</div>
<div class="container">
    <div class="row">
        {#each books as book}
            <div class="col-md-6 col-lg-4">
                <BookCard {book} />
            </div>
        {/each}
    </div>
</div>
<footer> Testing here</footer>
</main>