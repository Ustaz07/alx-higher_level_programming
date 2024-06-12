$(document).ready(function(){
    // Make an AJAX request to fetch data from the URL
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: function(response) {
            // Update the content of DIV#character with the fetched character name
            $('#character').text(response.name);
        }
    });
});
