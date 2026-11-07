//Question: Accept a POST request to /users.

import http from "node:http";

const server = http.createServer((req, res) => {
  if(req.method === "POST" && req.url === "/users") {
    res.writeHead(201, {
      "content-type": "text/plain"
    });
    res.end("Users created");
    return;
  };

  res.writeHead(404, {
    "content-type": "text/plain"
  });
  res.end("route not found")
});

server.listen(3001, () =>{
  console.log("server is running")
});