import express from "express";
import http from "http";
import { WebSocketServer } from 'ws';
import path from 'path';

const app = express();
const __dirname = path.resolve();

app.set("view engine", "pug");
app.set("views", __dirname + "/src/views");
app.use("/public", express.static(__dirname + "/src/public"));
app.get("/", (_, res) => res.render("home"));
app.get("/*", (_, res) => res.redirect("/"));

const handleListen = () => console.log('Listening on http://localhost:3000');

const server = http.createServer(app);
const wss = new WebSocketServer({ server });

function onSocketclose() {
    console.log('Disconnect from the Brower')
}

const sockets = [];

wss.on("connection", (socket) => {
    sockets.push(socket)
    socket["nickname"] = "Anon";
    console.log("Connected to Browser");
    socket.on("close", () => onSocketclose)
    socket.on("message", (msg) => {
        const messageString = msg.toString('utf8');
        const message = JSON.parse(messageString);
        switch(message.type){
            case "new_message":
                sockets.forEach(aSocket => aSocket.send(`${socket.nickname}: ${message.payload}`));
            case "nickname":
                socket["nickname"] = message.payload;
        }
    });
});
server.listen(3000, handleListen);