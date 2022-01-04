import express from "express";

const PORT = 4000;

const app = express();

const logger = (req, res, next) => {
  console.log(`${req.method} ${res.url}`);
  next();
};
const handleProtected = (req, res) => {
  return res.send("welcome to the private lounge");
};
const privateMiddleware = (req, res, next) => {
  const url = req.url;
  if (url === "/protected") {
    return res.send("<h1>Not Allowed</h1>");
  }
  console.log("Allowed, you may continue.");
  next();
};
const handleHome = (req, res) => {
  return res.send("i love middleware");
};
app.use(logger);
app.use(privateMiddleware);
app.get("/", handleHome);
app.get("/protected", handleProtected);
const handleListen = () =>
  console.log(`server listenting on port http://localhost:${PORT}`);
app.listen(PORT, handleListen);
