export const Users = (req, res) => res.send("Users");
export const User = (req, res) => res.send("User" + req.params.id);
export const Edit = (req, res) => res.send("edit");
