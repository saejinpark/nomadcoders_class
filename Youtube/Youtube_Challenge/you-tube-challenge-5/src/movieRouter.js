import express from "express";
import { home, filter, movieDetail } from "./movieController";

const movieRouter = express.Router("/");

movieRouter.get("/", home);
movieRouter.get("/filter", filter);
movieRouter.get("/(\\d+)", movieDetail);

export default movieRouter;
