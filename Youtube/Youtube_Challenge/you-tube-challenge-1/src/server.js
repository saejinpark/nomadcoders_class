import express from "express";
const app = express();
const PORT = 4000;
const handleHome = (req, res) => {
  res.send("<h1>Home</h1>");
};
const handleAbout = (req, res) => {
  res.send("<h1>About</h1>");
};
const handleContact = (req, res) => {
  res.send("<h1>Contact</h1>");
};
const handleLogin = (req, res) => {
  res.send("<h1>Login</h1>");
};
app.get("/", handleHome);
app.get("/about", handleAbout);
app.get("/contact", handleContact);
app.get("/login", handleLogin);

const handleListen = () =>
  console.log(`server listenting on port http://localhost:${PORT}`);
app.listen(PORT, handleListen);
