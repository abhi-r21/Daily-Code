//Question: Return different responses for GET and POST.

import http from "node:http";

const server = http.createServer((req, res) => {
  if(req.method === "GET") {
    res.end("GET request");
    return;
  }
  if(req.method === "POST") {
    res.end("POST request");
    return;
  }

  res.writeHead(405);
  res.end("Method not allowed")
});

server.listen(3000, () => {
  console.log("server is runnning")
})