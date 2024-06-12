// Wait for the document to be fully loaded before executing the script
$(document).ready(function() {
    // Add a click event listener to the <div> element with id "red_header"
    $('#red_header').click(function() {
      // Select the <header> element using JQuery and change its text color to red
      $('header').css('color', '#FF0000');
    });
  });
