import express from "express";
import {
  home,
  tranding,
  newStories,
  join,
  login
} from "../controllers/globalControllers";
const globalRouter = express.Router();

globalRouter.get("/", home);
globalRouter.get("/trending", tranding);
globalRouter.get("/newStories", newStories);
globalRouter.get("/join", join);
globalRouter.get("/login", login);

export default globalRouter;
