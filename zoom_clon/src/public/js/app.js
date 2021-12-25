const messageList = document.querySelector("ul");
const nickForm = document.querySelector("#nick");
const messageForm = document.querySelector("#message");
const socket = new WebSocket(`ws://${window.location.host}`)

function makeMessage(type, payload) {
    const msg = {type, payload};
    return JSON.stringify(msg);
}

function handleOpen() {
    console.log("Connected to Server");
}

function handleMessage(message) {
    const li = document.createElement("li")
    li.innerText = message.data;
    messageList.append(li)
}

function handleClose() {
    console.log("DisConnected from Server")
}

socket.addEventListener("open", handleOpen)

socket.addEventListener("message", handleMessage)

socket.addEventListener("close", handleClose);

function handleSubmit(event) {
    event.preventDefault();
    const input = messageForm.querySelector("input");
    socket.send(makeMessage("new_message", input.value));
    input.value = "";
}

messageForm.addEventListener("submit", handleSubmit)

function handleNickSubmit(event) {
    event.preventDefault();
    const input = nickForm.querySelector("input");
    socket.send(makeMessage("nickname", input.value))
    input.value = "";
}

nickForm.addEventListener("submit", handleNickSubmit)