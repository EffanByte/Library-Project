<script>
    import { push } from 'svelte-spa-router';
    export let book; // Receiving book data as a prop
    function navigateToBook(BookID) {
        push(`/book/${BookID}`);
    }
</script>

<div class="system">
        <div class="bookslider-img" style="background: url({book.coverUrl});">
        </div>
    <div class="blookslider-data">
            <h5 class = "Card-title">{book.Title}</h5>
            <p>By: {book.Author}</p>
            <button class="btn btn-primary" on:click={() => navigateToBook(book.BookID)}>Go to Book</button>
        </div>
        
    </div>

<style>
    a {
        text-decoration: none; /* Optional: to prevent default link styling */
        color: inherit; /* Optional: to maintain the color of the content */
    }
.system{
        width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    border-radius:5px;
    padding: 7px;
}
     .system:hover{
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.25);
  -webkit-transform: all .3s ease-in-out;
  -ms-transform: all .3s ease-in-out;
  transform: all .3s ease-in-out;
  position: relative;
}   
.blookslider-data{
  width: 65%;
  padding-left: 10px;   
}

.bookslider-img{
  width: 130px;
  height: 200px;
  background-position: center center;
  
  background-repeat: no-repeat !important;
  background-size: cover !important;

}
</style>