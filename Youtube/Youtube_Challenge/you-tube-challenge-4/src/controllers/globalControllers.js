export const home = (req, res) => res.render("home", { pageTitle: "Home" });
export const tranding = (req, res) =>
  res.render("trending", { pageTitle: "Trending" });
export const newStories = (req, res) =>
  res.render("newStories", { pageTitle: "NewStories" });
export const join = (req, res) => res.render("join", { pageTitle: "Join" });
export const login = (req, res) => res.render("login", { pageTitle: "Login" });
