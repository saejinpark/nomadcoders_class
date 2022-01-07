export const Trending = (req, res) => res.send("Trending" + req.params.id);
export const Edit = (req, res) => res.send("Edit" + req.params.id);
export const Delete = (req, res) => res.send("Delete" + req.params.id);
