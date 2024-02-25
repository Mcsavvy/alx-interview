#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
async function req (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}
request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const url of data.characters) {
    try {
      const person = await req(url);
      console.log(person.name);
    } catch (err) {
      console.error(err);
    }
  }
});
