#!/usr/bin/node

const fs = require('fs');

// Extract file paths from command line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

// Read content from sourceFile1
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading file ${sourceFile1}: ${err}`);
    return;
  }

  // Read content from sourceFile2
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading file ${sourceFile2}: ${err}`);
      return;
    }

    // Remove leading and trailing whitespace from each file's content
    const trimmedData1 = data1.trim();
    const trimmedData2 = data2.trim() + '\n';

    // // Concatenate the trimmed content from both files
    const concatenatedContent = trimmedData1 + '\n' + trimmedData2;

    fs.writeFile(destinationFile, concatenatedContent, (err) => {
      if (err) {
        console.error(`Error writing to file ${destinationFile}: ${err}`);
        return;
      }
      console.log(`Concatenation successful! Result saved to ${destinationFile}`);
    });
  });
});
