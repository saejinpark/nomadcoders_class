






const Clock = () => {
    const clock = document.getElementById("clock");
    const date = clock.querySelector("h1");
    const Time = clock.querySelector("h2");
    const meridiem = Time.querySelector("span:nth-child(1)");
    const time = Time.querySelector("span:nth-child(2)");
    const DetailedTime = clock.querySelector("h3");
    const now = new Date;
    const hour = now.getHours();
    const minute = now.getMinutes();
    const second = now.getSeconds();
    let millisecond = now.getMilliseconds();
    if(millisecond < 100)millisecond = "0" + millisecond;
    if(millisecond < 10)millisecond = "0" + millisecond;
    if(millisecond < 1)millisecond = "0" + millisecond;
    date.innerText = `${now.getFullYear()}년 ${now.getMonth() + 1}월 ${now.getDate()}일 ${["일", "월", "화", "수", "목", "금", "토"][now.getDay()]}요일`;
    meridiem.innerText = `${hour > 12 ? "pm":"am"}`;
    time.innerText = `${hour > 12 ? (hour-12 < 10 ? "0" + (hour-12):(hour-12)):(hour < 10 ? "0" + hour:hour)}:${minute < 10 ? "0"+minute:minute}`
    DetailedTime.innerText = `${hour < 10 ? "0" + hour:hour}:${minute < 10 ? "0"+minute:minute}:${second < 10 ? "0"+second:second}:${millisecond}`;
}
setInterval(Clock, 1);