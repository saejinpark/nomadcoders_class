import {
  getMovieById,
  getMovies,
  getMovieByMinimumRating,
  getMovieByMinimumYear
} from "./db";

export const home = (req, res) => {
  const movies = getMovies();
  res.render("home", {
    movies: movies
  });
};
export const filter = (req, res) => {
  var movies = getMovies();
  if (req.query.year > 2012) movies = getMovieByMinimumYear(req.query.year);
  if (req.query.rating != "")
    movies = getMovieByMinimumRating(req.query.rating);
  res.render("filterMovie", { movies: movies });
};
export const movieDetail = (req, res) => {
  console.log(getMovieById(req.url.replace("/", "")));
  res.render("movieDetail", {
    movie: getMovieById(req.url.replace("/", ""))
  });
};
