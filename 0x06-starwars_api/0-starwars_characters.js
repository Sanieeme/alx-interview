#!/usr/bin/node

// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, async (err, res, body) => {
  if (err) {
    console.error('Error fetching movie details:', err);
    return;
  }

  if (!body || !body.characters) {
    console.error('Invalid movie ID or no characters found.');
    return;
  }

  try {
    // Fetch characters in order
    for (const characterUrl of body.characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (err, res, characterBody) => {
          if (err) {
            console.error('Error fetching character details:', err);
            reject(err);
            return;
          }
          console.log(characterBody.name);
          resolve();
        });
      });
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
});

