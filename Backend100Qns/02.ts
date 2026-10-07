//Question: Return an HTML heading instead of plain text.
import http from "node:http";

const server = http.createServer((req, res)=>{
  res.writeHead(200, {
    "Content-Type": "text/html",
  });

  res.end("<h1>Hello from Node.js</h1>");
});

server.listen(3000);