const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(database)
    .then(() => res.end())
    .catch((err) => res.end(err.message));
});

app.listen(1245);

module.exports = app;
