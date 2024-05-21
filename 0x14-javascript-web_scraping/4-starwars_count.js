#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request'); // Importing the request module
const url = process.argv[2]; // Getting the API URL from command line arguments

// Making a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    // Printing the error object if an error occurred
    console.error(error);
  } else {
    // Parsing the response body
    const films = JSON.parse(body).results;
    // Filtering the films to find those that include Wedge Antilles (character ID 18)
    const wedgeCount = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
    // Printing the count of movies where Wedge Antilles is present
    console.log(wedgeCount);
  }
});
