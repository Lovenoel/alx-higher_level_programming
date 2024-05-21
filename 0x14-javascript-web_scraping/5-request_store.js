#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file

const request = require('request'); // Importing the request module
const fs = require('fs'); // Importing the file system module
const url = process.argv[2]; // Getting the URL to request from command line arguments
const filePath = process.argv[3]; // Getting the file path to store the response from command line arguments

// Making a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    // Printing the error object if an error occurred
    console.error(error);
  } else {
    // Writing the body of the response to the file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        // Printing the error object if an error occurred during writing
        console.error(err);
      }
    });
  }
});
