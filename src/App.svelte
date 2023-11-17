<script>
	import 'bootstrap/dist/js/bootstrap.bundle.min.js';
	 import 'bootstrap/dist/css/bootstrap.min.css';
   import Navbar from "./components/navbar.svelte";
   import BackG from "./components/BackG.svelte";
   import BookCard from './components/BookCard.svelte';

    let books = [
        { title: 'Book 1',coverUrl: 'cover1.jpg' }
        ,
        { title: 'Book 2',coverUrl: 'cover1.jpg' }
        ,
        { title: 'Book 3',coverUrl: 'cover1.jpg' },
        { title: 'Book 4',coverUrl: 'cover1.jpg' }
        ,
        { title: 'Book 5',coverUrl: 'cover1.jpg' }
        ,
        { title: 'Book 6',coverUrl: 'cover1.jpg' }
        
    ];
</script>
<main>
<Navbar />
<BackG/>
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