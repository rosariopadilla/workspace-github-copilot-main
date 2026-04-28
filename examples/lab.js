const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

// Endpoint principal
app.get('/', (req, res) => {
    res.send('Hola mundo desde mi API');
});

// Endpoint para obtener la hora del sistema
app.get('/time', (req, res) => {
    const now = new Date();
    const response = {
        time: now.toISOString()
    };

    // Logging estructurado del acceso al endpoint /time
    const logEntry = {
        timestamp: now.toISOString(),
        severity: 'INFO',
        message: 'Time endpoint accessed',
        context: {
            service: 'basic-express-api',
            endpoint: '/time',
            method: 'GET',
            requestId: req.headers['x-request-id'] || null
        }
    };
    console.log(JSON.stringify(logEntry));
});

module.exports = app;
