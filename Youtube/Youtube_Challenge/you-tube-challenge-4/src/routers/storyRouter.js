import express from "express";
import {
  seeStory,
  editStory,
  deleteStory
} from "../controllers/storyControllers";

const storyRouter = express.Router();

storyRouter.get("/:id(\\d+)", seeStory);
storyRouter.get("/:id(\\d+)/editStory", editStory);
storyRouter.get("/:id(\\d+)/deleteStory", deleteStory);

export default storyRouter;
