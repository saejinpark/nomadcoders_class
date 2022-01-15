import express from "express";
import { home, movieDetail } from "./movieController";

const movieRouter = express.Router();

movieRouter.get("/", home);
movieRouter.get("/:id", movieDetail);
// create the '/' route
// create the /:id route
// create the /add route (GET + POST)

export default movieRouter;
