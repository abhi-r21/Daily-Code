// Create PATCH /users

import http from "node:http";

const server = http.createServer((req, res) => {
  if(req.method === "PATCH" && req.url === "/users") {
    res.end("Users partially updated");
    return;
  }
});

server.listen(3001, () => {
  console.log("Server is running in port 3001")
});