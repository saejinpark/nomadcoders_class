import express from "express";
import { Users, User, Edit } from "../controllers/userControllers";

const userRouter = express.Router();

userRouter.get("/", Users);
userRouter.get("/:id(\\d+)", User);
userRouter.get("/edit-profile", Edit);

export default userRouter;
