// TLS Server Node.js 
// G. Isaza oct 2017

var express = require('express');
//var express = require('tls');
var app = express();
var https = require('https');
//var http = require('http');
var fs = require('fs');

// This line is from the Node.js HTTPS documentation.
var options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem'),
  passphrase: 'testing' 
  //passphrase: passphrase
};

// Create an HTTP service.
//http.createServer(app).listen(80);
// Create an HTTPS service identical to the HTTP service.
//https.createServer(options, app).listen(443);

https.createServer(options, function (req, res) {
  res.writeHead(200);
  res.end("hello world\n");
}).listen(443);
