//Question: Return "About page" when /about is requested.

import http from "node:http";

const server = http.createServer((req, res) => {
  if (req.url === "/about") {
    res.writeHead(200, {
      "content-type": "application/json",
    });
    res.end("About page");
    return;
  }
});

server.listen(3000, () => {
  console.log("Server is running")
})