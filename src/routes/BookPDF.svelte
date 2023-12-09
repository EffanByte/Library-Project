<script>
    import { onMount } from 'svelte';
    import PDFObject from "pdfobject";

    onMount(() => {
        console.log(PDFObject.pdfobjectversion);
        PDFObject.embed("Assignment 2.pdf", ".container"); //placeholder values
    });
</script>

<div class = container ></div>


<style>
    .container {
        width: 100%; /* Full width of the parent container */
        height: 600px; /* Adjust the height as needed */
    }
</style>