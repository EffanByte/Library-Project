<script>
    export let book; // Receiving book data as a prop
</script>

<div class="card" style="width: 18rem;">
    <img src={book.coverUrl} class="card-img-top" alt={`Cover of ${book.title}`} />
    <div class="card-body">
        <h5 class="card-title">{book.title}</h5>
    </div>
</div>

<style>
    .card{
        margin: 2vh;
        
    }
</style>