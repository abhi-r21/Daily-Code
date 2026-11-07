// Question: Prefix your API routes with /api

import http from "node:http";

const server = http.createServer((req, res) => {
  if(req.method === "GET" && req.url === "/api/users") {
    res.end("Users API");
  }
});

server.listen(3000, () => {
  console.log("server is running")
});