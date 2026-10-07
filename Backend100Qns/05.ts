//Question: Return the URL requested by the client.

import http from "node:http";

const server = http.createServer((req, res)=>{
  res.end(`URL: $(req.url)`);
});

server.listen(3000);