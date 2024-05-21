#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs'); // Importing the file system module
const filePath = process.argv[2]; // Getting the file path from command line arguments

// Reading the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Printing the error object if an error occurred
    console.error(err);
  } else {
    // Printing the content of the file
    console.log(data);
  }
});
