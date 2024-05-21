#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const request = require('request'); // Importing the request module
const url = process.argv[2]; // Getting the API URL from command line arguments

// Making a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    // Printing the error object if an error occurred
    console.error(error);
  } else {
    // Parsing the response body
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Iterating through the tasks and counting completed tasks for each user
    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    // Printing the count of completed tasks by user ID
    console.log(completedTasks);
  }
});
