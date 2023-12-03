<script>
    import { link } from 'svelte-spa-router';
    let books = [/* array of books */];
</script>

{#each books as book}
    <a use:link href={`/book/${book.BookID}`}>{book.Title}</a>
{/each}