const http = require('http');
const fs = require('fs');

const DB_FILE = process.argv[2];

/**
 * Reads student database CSV asynchronously and returns formatted string.
 * @param {string} path - Path to the CSV file.
 * @returns {Promise<string>} Formatted list of students.
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
      return;
    }

    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Filter out empty lines and trailing carriage returns
      const lines = data
        .split('\n')
        .map((line) => line.trim())
        .filter((line) => line.length > 0);

      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      // Skip header row (firstname,lastname,age,field)
      const studentRecords = lines.slice(1);
      const fields = {};

      for (const record of studentRecords) {
        const student = record.split(',');
        if (student.length >= 4) {
          const firstname = student[0];
          const field = student[3];

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      }

      let totalStudents = 0;
      for (const list of Object.values(fields)) {
        totalStudents += list.length;
      }

      let output = `Number of students: ${totalStudents}`;
      for (const [field, list] of Object.entries(fields)) {
        output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
      }

      resolve(output);
    });
  });
}

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(DB_FILE)
      .then((data) => {
        res.end(data);
      })
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    res.end();
  }
});

app.listen(1245);

module.exports = app;
