$(document).ready(function(){
    // Make an AJAX request to fetch data from the URL
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(response) {
            // Update the content of DIV#hello with the fetched translation of "hello"
            $('#hello').text(response.hello);
        }
    });
});
