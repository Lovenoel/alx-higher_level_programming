#!/usr/bin/node
// Script that displays the status code of a GET request

const request = require('request'); // Importing the request module
const url = process.argv[2]; // Getting the URL to request from command line arguments

// Making a GET request to the provided URL
request(url, (error, response) => {
  if (error) {
    // Printing the error object if an error occurred
    console.error(error);
  } else {
    // Printing the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
