<script>
	import 'bootstrap/dist/js/bootstrap.bundle.min.js';
	 import 'bootstrap/dist/css/bootstrap.min.css';
   import Navbar from "./components/navbar.svelte";
   import BackG from "./components/BackG.svelte";
   import BookCard from './components/BookCard.svelte';

    let books = [
        { title: 'Book 1',coverUrl: 'cover1.jpg' }
        ,
        { title: 'Book 1',coverUrl: 'cover1.jpg' }
        ,
        { title: 'Book 1',coverUrl: 'cover1.jpg' }
    ];
</script>

<main>
<Navbar />
<BackG/>
<div class = "heading">Browse The Catalogue here</div>
<div class = "container">{#each books as book}
        <BookCard {book} />
    {/each}</div>  
<footer> Testing here</footer>
</main>