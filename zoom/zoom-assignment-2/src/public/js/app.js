const socket = io();

const welcome = document.getElementById("welcome");
const form = welcome.querySelector("form");
const room = document.getElementById("room");

room.hidden = true;

let roomName;

function addMessage(other, message) {
  const ul = room.querySelector("ul");
  const li = document.createElement("li");
  const span = document.createElement("span");
  if (other) {
    li.classList.add("other");
  }
  span.innerText = message;
  li.appendChild(span);
  ul.appendChild(li);
}
function handleMessageSubmit(event) {
  event.preventDefault();
  const input = room.querySelector("#msg input");
  const value = input.value;
  socket.emit("new_message", input.value, roomName, () => {
    addMessage(false, `You: ${value}`);
  });
  input.value = "";
}
function handleNicknameSubmit(event) {
  event.preventDefault();
  const msgForm = room.querySelector("#msg");
  const nameForm = room.querySelector("#name");
  msgForm.hidden = false;
  nameForm.hidden = true;
  const input = room.querySelector("#name input");
  socket.emit("nickname", input.value);
  input.value = "";
}
function showRoom() {
  room.hidden = false;
  welcome.hidden = true;
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName}`;
  const msgForm = room.querySelector("#msg");
  const nameForm = room.querySelector("#name");
  msgForm.hidden = true;
  nameForm.hidden = false;
  msgForm.addEventListener("submit", handleMessageSubmit);
  nameForm.addEventListener("submit", handleNicknameSubmit);
}

function handleRoomSubmit(event) {
  event.preventDefault();
  const input = form.querySelector("input");
  socket.emit("enter_room", input.value, showRoom);
  roomName = input.value;
  input.value = "";
}

form.addEventListener("submit", handleRoomSubmit);

socket.on("welcome", (newCount) => {
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName} (${newCount})`;
  addMessage(false, `someone arrived!`);
});
socket.on("bye", (left, newCount) => {
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName} (${newCount})`;
  addMessage(false, `${left} leftㅠㅠ`);
});

socket.on("new_message", (msg) => {
  addMessage(true, msg);
});
socket.on("room_change", (rooms) => {
  const roomList = welcome.querySelector("ul");
  roomList.innerHTML = "";
  rooms.forEach((room) => {
    const li = document.createElement("li");
    li.innerText = room;
    roomList.appendChild(li);
  });
});
