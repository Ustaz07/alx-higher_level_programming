#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesFilms = films.filter(film =>
    film.characters.some(character => character.includes('/18/'))
  );

  console.log(wedgeAntillesFilms.length);
});
