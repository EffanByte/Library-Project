<script>

    import 'bootstrap/dist/js/bootstrap.bundle.min.js';
	import 'bootstrap/dist/css/bootstrap.min.css';
    import Navbar from "./components/navbar.svelte";
    import BookDetail from './routes/BookDetail.svelte';
    import Router from 'svelte-spa-router';
    import Catalogue from './components/Catalogue.svelte';
    import Login from './components/Login.svelte';
    import BackG from './components/BackG.svelte';
    const routes = {
        '/': Catalogue,
        '/book/:id': BookDetail, //Dynamic route for books. Understand this later
    };
    let showModal = false;
    function handleLoginEvent() {
        showModal = true;
        showModal = !!showModal;
    }
    let books = [
        {id: 1, title: 'Book 1',coverUrl: 'cover1.jpg',}
        ,
        {id: 2,  title: 'Book 2',coverUrl: 'cover2.jpg' }
    ]

</script>
<main>
    <Navbar on:login = {handleLoginEvent}/>
    <BackG />
    <Login show = {showModal} on:close = {showModal = false} />
<Router {routes}/>
</main>