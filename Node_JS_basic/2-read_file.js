const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n').filter((line) => line.trim() !== '');
  const students = lines.slice(1); // remove header
  const fields = {};

  students.forEach((student) => {
    const [firstname, , , field] = student.split(',');
    if (!fields[field]) fields[field] = [];
    fields[field].push(firstname);
  });

  console.log(`Number of students: ${students.length}`);
  for (const field in fields) {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  }
}

module.exports = countStudents;
