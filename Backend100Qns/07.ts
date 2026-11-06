//Question: Create /health that returns { status: "ok" }.

import http from "node:http";

const server = http.createServer((req, res) => {
  if (req.url === "/health") {
    res.writeHead(200, {
      "Content-Type": "application/json",
    });
    
    res.end(JSON.stringify({
      status: "ok",
    }));
  };
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
