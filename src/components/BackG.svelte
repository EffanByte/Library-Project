<script>    
     import {backgroundColor} from "./store.js";
console.log(backgroundColor);
     function updateBG(){
     const currentPath = window.location.href;
     console.log(currentPath);
     if (currentPath == 'http://localhost:8080/#/' || currentPath== 'http://localhost:8080/'){
backgroundColor.set('#C6DEF1');
     }
     else if (currentPath == 'http://localhost:8080/#/Librarian/'){
        backgroundColor.set("#F7D9C4")
     }
     else if (currentPath == 'http://localhost:8080/#/Catalogue'){
        backgroundColor.set('#C9E4DE');
     }
     else if (currentPath == 'http://localhost:8080/#/Complaint'){
      backgroundColor.set('#FF6961');
     }
          else if (currentPath == 'http://localhost:8080/#/LostFound'){
      backgroundColor.set('#836953');
     }
    }
       window.addEventListener('popstate', updateBG);
       updateBG();
</script>

<div class = "background-image" style = "background-color: {$backgroundColor}"></div>


<style>
    .background-image {
    position: fixed;
    /* Fixed position */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* Path to your image */
    background-size: cover;
    /* or use 'contain' based on your requirement */
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    /* This makes the background static */
    z-index: -1;
        transition: background-color 1s;
    /* Ensures the background stays behind other content */
}

</style>