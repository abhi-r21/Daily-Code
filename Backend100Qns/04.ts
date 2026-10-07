//Question: Return the HTTP method used by the client.

import http from "node:http";

const server = http.createServer((req, res)=>{
  res.end(`Method: $(req.method)`);
});

server.listen(3000);