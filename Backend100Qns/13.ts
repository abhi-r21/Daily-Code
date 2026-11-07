//Create DELETE /users

import http from "node:http";

const server = http.createServer((req, res) => {
  if(req.method === "DELETE" && req.url === "/users") {
    res.end("Users deleted");
    return;
  }
});

server.listen(3000, () => {
  console.log("Server is running in port 3000")
});

