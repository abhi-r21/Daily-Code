//Question: Create a Node.js HTTP server that responds "Hello World" to every request.

import http from "node:http";

const server = http.createServer((req, res) => {
  res.end("Hello world");
});

server.listen(3000, () => {
  console.log("Server is running in port 3000");
});