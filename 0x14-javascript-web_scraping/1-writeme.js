#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs'); // Importing the file system module
const filePath = process.argv[2]; // Getting the file path from command line arguments
const content = process.argv[3]; // Getting the string to write from command line arguments

// Writing the string to the file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Printing the error object if an error occurred
    console.error(err);
  }
});
