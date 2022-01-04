import express from "express";
const PORT = 4000;

const app = express();
const handleHome = (req, res) => {
  console.log("rotoRldi");
  res.send("<h1> rotoRl </h1>");
  return res.end();
};
app.get("/", handleHome);

const handleListen = () => {
  console.log(`server listenting on port http://localhost:${PORT}`);
};
app.listen(PORT, handleListen);
