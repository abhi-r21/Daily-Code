//Question: Return 404 for routes that don't exist.

import http from "node:http";

const server = http.createServer((req, res) => {
  res.writeHead(404);
  res.end("Rount not found")
});

server.listen(3000, () => {
  console.log("Server is running")
});