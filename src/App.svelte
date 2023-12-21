

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
    import BookPDF from './routes/BookPDF.svelte';
    import Home from './routes/Home.svelte'
    import Complaint from './components/Complaint.svelte';
    import RoomUser from './components/Room.svelte'
    import LostFound from './components/LostFound.svelte';
    import ComplaintManage from './routes/ComplaintManage.svelte';
    import LostFoundLibrarian from './routes/LostFoundManage.svelte';
    const routes = {

        '/': Home,
        '/book/:bookID': BookDetail,
        '/Librarian': LibrarianHome, 
        '/Librarian/BookManagement': BookManage,
        '/Librarian/UserManagement': UserManage,
        '/Librarian/RoomManagement': RoomManage,
        '/Librarian/RentManagement': RentManage,
        '/Librarian/ComplaintManagement': ComplaintManage,
        '/User/:user': Profile,
        '/PDF/:typeID': BookPDF,
        '/UserHome/:user': Home,
        '/Catalogue': Catalogue,
        '/Complaint': Complaint,
        '/Room': RoomUser,
        '/LostFound': LostFound,     
        '/Librarian/LostAndFoundManagement': LostFoundLibrarian,   
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
