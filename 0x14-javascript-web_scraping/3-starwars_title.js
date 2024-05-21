#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request'); // Importing the request module
const movieId = process.argv[2]; // Getting the movie ID from command line arguments
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // Constructing the URL for the API request

// Making a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    // Printing the error object if an error occurred
    console.error(error);
  } else {
    // Parsing and printing the title of the movie
    console.log(JSON.parse(body).title);
  }
});
