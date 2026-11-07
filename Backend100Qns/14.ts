//Create PUT /users

import http from "node:http";

const server = http.createServer((req, res) =>{
  if(req.method === "PUT" && req.url === "/users") {
    res.end("Users updated");
    return;
  }
});

server.listen(3000, () => {
  console.log("server is running");
});