// Question: Create routes:
// GET /
// GET /users
// GET /products
// GET /about

import http from "node:http";

const server = http.createServer((req, res) => {
  if(req.method === "GET" && req.url === "/"){
  res.end("Home");
  return;
  }
  if(req.method === "GET" && req.url === "/users") {
    res.end("Users");
    return;
  }
  if(req.method === "GET" && req.url === "/products") {
    res.end("Products");
    return;
  }
  if(req.method === "GET" && req.url === "/about") {
    res.end("About");
    return;
  }
});

server.listen(3000, () => {
  console.log("Server is running")
});