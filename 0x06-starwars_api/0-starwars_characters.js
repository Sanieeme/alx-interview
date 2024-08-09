#!/usr/bin/node

// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
    console.error('Please provide a valid movie ID.');
    process.exit(1);
}

function fetchStarWarsCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    request(url, { json: true }, (err, res, body) => {
        if (err) {
            console.error('Error fetching movie details:', err);
            return;
        }

        if (!body || !body.characters) {
            console.error('Invalid movie ID or no characters found.');
            return;
        }

        body.characters.forEach(characterUrl => {
            request(characterUrl, { json: true }, (err, res, body) => {
                if (err) {
                    console.error('Error fetching character details:', err);
                    return;
                }
                console.log(body.name);
            });
        });
    });
}

fetchStarWarsCharacters(movieId);
