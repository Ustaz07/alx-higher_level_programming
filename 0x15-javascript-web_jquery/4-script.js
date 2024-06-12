// Wait for the document to be fully loaded
$(document).ready(function(){
    // Attach a click event listener to the DIV#toggle_header element
    $('#toggle_header').click(function(){
        // Toggle the classes 'red' and 'green' on the <header> element
        $('header').toggleClass('red green');
    });
});
