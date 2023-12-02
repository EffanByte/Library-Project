<script>

    import 'bootstrap/dist/js/bootstrap.bundle.min.js';
	import 'bootstrap/dist/css/bootstrap.min.css';
    import Navbar from "./components/navbar.svelte";
    import BookDetail from './routes/BookDetail.svelte';
    import LibrarianHome from './routes/LibrarianHome.svelte';
    import Router from 'svelte-spa-router';
    import Catalogue from './components/Catalogue.svelte';
    import Login from './components/Login.svelte';
    import BackG from './components/BackG.svelte';
    import SignUp from './components/Sign.svelte';
    import UserManage from './routes/UserManage.svelte';
    import BookManage from './routes/BookManage.svelte';
    import RentManage from './routes/RentManage.svelte';
    import RoomManage from './routes/RoomManage.svelte';
    import Profile from './routes/Profile.svelte';
    const routes = {

        '/': Catalogue,
        '/book/:id': BookDetail, 
        '/Librarian': LibrarianHome, 
        '/Librarian/BookManagement': BookManage,
        '/Librarian/UserManagement': UserManage,
        '/Librarian/RoomManagement': RoomManage,
        '/Librarian/RentManagement': RentManage,
        '/User/:user': Profile
    };
    let showLogin = false;
    let showSignup = false;
    function handleLoginEvent() {
        showLogin = true;   
    }
    function handleSignupEvent(){
showSignup = true;
    }
    let books = [
        {id: 1, title: 'Book 1',coverUrl: 'cover1.jpg',}
        ,
        {id: 2,  title: 'Book 2',coverUrl: 'cover2.jpg' }
    ]

</script>
<main>
    <Navbar on:login = {handleLoginEvent} on:signup = {handleSignupEvent}/>
    <BackG />
    <Login show = {showLogin} on:close = {showLogin = false} />
    <SignUp show = {showSignup} on:close = {showSignup = false} />
<Router {routes}/>
</main>
