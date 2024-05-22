#!/usr/bin/node
//  Script that prints all characters of a Star Wars movie:

// Import the 'request' module for making HTTP requests
const request = require('request');

// Function to print characters of a Star Wars movie in the right order
function printCharactersInOrder (movieId) {
  // Construct the URL for the Star Wars movie API
  const url = `https://swapi.dev/api/films/${movieId}/`;

  // Make a GET request to the API
  request(url, (error, response, body) => {
    // Check if there is no error and the response status is OK (200)
    if (!error && response.statusCode === 200) {
      // Parse the response body into JSON
      const filmData = JSON.parse(body);
      // Extract the list of character URLs from the film data
      const characters = filmData.characters;
      // Create an array to hold character names in the right order
      const characterNames = filmData.characters.map(characterUrl => null);

      let count = 0;
      // Iterate over each character URL
      characters.forEach((characterUrl, index) => {
        // Make a GET request to the character URL
        request(characterUrl, (error, response, body) => {
          // Checks for no error and the response status is OK(200)
          if (!error && response.statusCode === 200) {
            // Parse the character data into JSON
            const characterData = JSON.parse(body);
            // Store the character's name at the it's index
            characterNames[index] = characterData.name;
            count++;

            // If all character names have been fetched,print them
            if (count === characters.length) {
              characterNames.forEach(name => {
                console.log(name);
              });
            }
          } else {
            // Log an error message if there was an issue fetching character data
            console.log('Error fetching character data:', error);
          }
        });
      });
    } else {
      // Log an error message if there was an issue fetching movie data
      console.log('Error fetching movie data:', error);
    }
  });
}

// Parse command line argument for movie ID
const args = process.argv.slice(2);
const movieId = parseInt(args[0]);

// Call the function with the provided movie ID
printCharactersInOrder(movieId);
