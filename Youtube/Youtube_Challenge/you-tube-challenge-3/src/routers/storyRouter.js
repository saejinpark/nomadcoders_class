import express from "express";
import { Trending, Edit, Delete } from "../controllers/storyControllers";

const storyRouter = express.Router();

storyRouter.get("/:id(\\d+)", Trending);
storyRouter.get("/:id(\\d+)/edit", Edit);
storyRouter.get("/:id(\\d+)/delete", Delete);

export default storyRouter;
