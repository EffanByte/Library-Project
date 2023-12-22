<script>
    import { onMount } from 'svelte';
    import PDFObject from 'pdfobject';
    import { pdfDataStore } from "../components/store.js";

    let pdfDataUri;

    $: if (pdfDataUri) {
        PDFObject.embed(pdfDataUri, '.container');
    }

    onMount(() => {
        const unsubscribe = pdfDataStore.subscribe(data => {
            if (data) {
                pdfDataUri = `data:application/pdf;base64,${data}`;
                console.log("PDF set in BookPDF.Svelte");
            }
        });

        return unsubscribe; // Cleanup subscription on component destruction
    });
</script>

<div class="container"></div>





<style>
    .container {
        width: 100%; /* Full width of the parent container */
        height: 600px; /* Adjust the height as needed */
    }
</style>