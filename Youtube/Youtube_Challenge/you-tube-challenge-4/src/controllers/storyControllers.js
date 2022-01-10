export const seeStory = (req, res) =>
  res.render("seeStory", { pageTitle: "SeeStory" });
export const editStory = (req, res) =>
  res.render("editStory", { pageTitle: "EditStory" });
export const deleteStory = (req, res) =>
  res.render("deleteStory", { pageTitle: "DeleteStory" });
