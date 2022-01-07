import express from "express";
import morgan from "morgan";
import globalRouter from "./routers/globalRouter";
import storyRouter from "./routers/storyRouter";
import userRouter from "./routers/userRouter";

const PORT = 4000;

const app = express();
const loger = morgan("dev");

app.use(loger);

app.use("/", globalRouter);
app.use("/users", userRouter);
app.use("/stories", storyRouter);

const handleListen = () =>
  console.log(`server listenting on port http://localhost:${PORT}`);
app.listen(PORT, handleListen);
