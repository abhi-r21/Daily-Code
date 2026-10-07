//Question: Print the method and URL whenever a request arrives.

import http from "node:http";

const server = http.createServer((req, res)=>{
  console.log(req.method, req.url);

  res.end("Request Received");
});

server.listen(3000);

