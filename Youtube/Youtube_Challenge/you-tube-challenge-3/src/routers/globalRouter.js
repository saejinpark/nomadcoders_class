import express from "express";
import {
  Home,
  Trending,
  New,
  Join,
  Login
} from "../controllers/globalControllers";
const globalRouter = express.Router();

globalRouter.get("/", Home);
globalRouter.get("/trending", Trending);
globalRouter.get("/new", New);
globalRouter.get("/join", Join);
globalRouter.get("/login", Login);

export default globalRouter;
