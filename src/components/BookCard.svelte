<script>
    import { link } from 'svelte-spa-router';
    export let book; // Receiving book data as a prop
</script>

<!-- Assuming each book object has a unique identifier `id` -->
    <a use:link href={`/book/${book.id}`}>
    <div class="card" style="width: 18rem;">
        <img src={book.coverUrl} class="card-img-top" alt={`Cover of ${book.title}`} />
        <div class="card-body">
            <h5 class="card-title">{book.title}</h5>
        </div>
    </div>
</a>

<style>
    .card {
        margin-top: 5vh;
        cursor: pointer; /* Optional: to show it's clickable */
        border: 2px black solid;
    }   
    a {
        text-decoration: none; /* Optional: to prevent default link styling */
        color: inherit; /* Optional: to maintain the color of the content */
    }
</style>