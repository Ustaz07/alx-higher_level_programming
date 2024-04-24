#!/usr/bin/node

// Import the dict object from the 101-data.js file
const { dict } = require('./101-data');

// Function to swap keys and values in a dictionary
function swapKeysAndValues (obj) {
  const result = {};
  for (const key in obj) {
    const value = obj[key];
    if (!result[value]) {
      result[value] = [key];
    } else {
      result[value].push(key);
    }
  }
  return result;
}

// Create a new dictionary with occurrences as keys and lists of user ids as values
const sortedDict = swapKeysAndValues(dict);

// Print the new dictionary
console.log(sortedDict);
