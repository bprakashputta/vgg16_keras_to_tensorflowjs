const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const PORT = 3000 || process.env.PORT;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (request, response) => {
    return response.send('Hello');
});

app.listen(PORT, (err) => {
    if (err) throw err;

    console.log('listening on port', PORT);
});