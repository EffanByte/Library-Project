import { writable } from 'svelte/store';

// Creating a writable store for loggedIn
export const loggedIn = writable({ is: false });
// Creating a writable store for user data
export const user = writable({username: ''} );