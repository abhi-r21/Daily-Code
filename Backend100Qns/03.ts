//Question: Create an endpoint that returns a JSON object.

import http from "node:http";

const server = http.createServer((req, res) =>{
  res.writeHead(200, {
    "content-type": "application/json",
  });

  res.end(JSON.stringify({
    message: "Hello",
    success: true,
  }));
});

server.listen(3000);