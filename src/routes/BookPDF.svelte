<script>
    import { onMount } from 'svelte';
    import PDFObject from 'pdfobject';
    import { pdfDataStore } from "../components/store.js";

let pdfDataUri;

onMount(() => {
    pdfDataStore.subscribe(data => {
        if (data) {
            pdfDataUri = `data:application/pdf;base64,${data}`;
            PDFObject.embed(pdfDataUri, '.container');
        }
    });
});
</script>

<div class="container"></div>





<style>
    .container {
        width: 100%; /* Full width of the parent container */
        height: 600px; /* Adjust the height as needed */
    }
</style>