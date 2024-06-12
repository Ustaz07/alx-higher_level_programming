$(document).ready(function(){
    $('#btn_translate').click(function(){
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();
        
        // Make an AJAX request to fetch translation
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            type: 'GET',
            data: { lang: languageCode },
            success: function(response) {
                // Update the content of DIV#hello with the fetched translation
                $('#hello').text(response.hello);
            },
            error: function() {
                // Display an error message if translation fails
                $('#hello').text('Error: Translation not found');
            }
        });
    });
});
