const express = require("express");

const app = express();

app.get("/multiply/:a/:b", function(req, res) {
  const a = parseInt(req.params.a);
  const b = parseInt(req.params.b);

  const ans = a * b;

  res.json({
    ans: ans
  })
})

app.listen(3000);