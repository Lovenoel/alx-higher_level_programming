#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:

// Import the request module to handle HTTP requests
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the Star Wars API to get movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Iterate over each character URL to get the character details
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      // Parse the character details and print the name
      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
