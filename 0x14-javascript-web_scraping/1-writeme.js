const request = require('request');
const fs = require('fs');

// Function to fetch data from a URL and write it to a file
function fetchDataAndWriteToFile(url, filePath) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        fs.writeFile(filePath, body, 'utf8', err => {
          if (err) {
            reject(err);
          } else {
            resolve();
          }
        });
      }
    });
  });
}

// Usage example
const url = 'https://example.com';
const filePath = 'example.html';

fetchDataAndWriteToFile(url, filePath)
  .then(() => console.log('File written successfully'))
  .catch(error => console.error('Error:', error));
