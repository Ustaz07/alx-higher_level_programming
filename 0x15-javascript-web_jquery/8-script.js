$(document).ready(function(){
    // Make an AJAX request to fetch data from the URL
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        success: function(response) {
            // Loop through the results array and append each movie title to the UL#list_movies
            response.results.forEach(function(movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        }
    });
});
