#!/usr/bin/node

const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading file ${sourceFile1}: ${err}`);
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading file ${sourceFile2}: ${err}`);
      return;
    }

    const concatenatedContent = data1 + '\n' + data2;

    fs.writeFile(destinationFile, concatenatedContent, (err) => {
      if (err) {
        console.error(`Error writing to file ${destinationFile}: ${err}`);
        return;
      }
      console.log(`Concatenation successful! Result saved to ${destinationFile}`);
    });
  });
});
