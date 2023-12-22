import { writable } from 'svelte/store';

// Creating a writable store for loggedIn
export const loggedIn = writable({ is: false });
// Creating a writable store for user data
export const user = writable({id: 0,username: '', role: ''} );
// Creating a writable store book chosen when going from BookCard.Svelte -> BookDetail.svelte (TEPORARY WORKAROUND)
export const selectedBookID = writable(null);
export const isLibrarian = writable({ is: true });
export const backgroundColor = writable('#C6DEF1');
export const userroles = writable("guest");
export const pdfDataStore = writable('');




