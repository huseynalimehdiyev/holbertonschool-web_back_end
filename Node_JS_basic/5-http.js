const http = require('http');
const fs = require('fs');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    fs.readFile(database, 'utf8', (error, data) => {
      if (error) {
        res.statusCode = 500;
        res.end('Cannot load the database');
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const columns = student.split(',');
        const firstname = columns[0];
        const field = columns[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      let result = 'This is the list of our students\n';
      result += `Number of students: ${students.length}\n`;

      Object.keys(fields).forEach((field) => {
        result += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });

      res.end(result.trim());
    });
    return;
  }

  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
