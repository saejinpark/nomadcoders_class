
const login = () => {
  const info = localStorage.getItem("info");
  const title = document.querySelector("#title");
  const loginForm = document.querySelector("#loginForm");
  const logout = document.querySelector("#logout");
  if (info) {
    title.innerText = info + "'s To Do List!!";
    title.hidden = false;
    loginForm.hidden = true;
    logout.hidden = false;
  } else {
    title.hidden = true;
    loginForm.hidden = false;
    logout.hidden = true;
  }
};
const logout = () => {
  const logout = document.querySelector("#logout");
  logout.addEventListener("click", () => {
    const title = document.querySelector("#title");
    localStorage.removeItem("info");
    title.innerText = "";
    login();
  });
};
const moment = () => {
    const daylist = ['일', '월', '화', '수', '목', '금', '토']
    const dateArticle = document.querySelector("#date")
    const now = new Date;
    const year = now.getFullYear()
    const month = now.getMonth();
    const date = now.getDate();
    const day = now.getDay();
    const h1 = dateArticle.querySelector("h1");
    h1.innerText = `${year}년 ${month}월 ${date}일 ${daylist[day]}요일`;
    const h2 = dateArticle.querySelectorAll("h2");
    const hour = now.getHours();
    const minute = now.getMinutes();
    const second = now.getSeconds();
    let millisecond = now.getMilliseconds();
    const clock01 = h2[0]
    const clock02 = h2[1]
    const clock01span = h2[0].querySelectorAll("span")
    clock01span[0].innerText = hour > 12 ? "Pm":"Am";
    clock01span[1].innerText = hour > 12 ? hour-12:hour;
    clock01span[2].innerText = minute;
    clock01span[3].innerText = second;
    const clock02span = h2[1].querySelectorAll("span")
    clock02span[0].innerText = hour > 10 ? hour:"0" + hour;
    clock02span[1].innerText = minute > 10 ? minute:"0" + minute;
    clock02span[2].innerText = second > 10 ? second:"0" + second;
    if(millisecond < 10)millisecond = "00" + millisecond;
    else if(millisecond < 100)millisecond = "0" + millisecond;
    clock02span[3].innerText = millisecond;
}
const clock = () => {
    setInterval(moment ,1)
}
const app = () => {
    const loginForm = document.querySelector("#loginForm");
    loginForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const form = event.target;
        const input = form.querySelector("input");
        const value = input.value;
        localStorage.setItem("info", value);
        input.value = "";
        login();
    });
    login();
    logout();
    clock();
}