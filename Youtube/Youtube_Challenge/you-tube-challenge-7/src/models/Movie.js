import mongoose from "mongoose";

const movieSchema = new mongoose.Schema({
  title: String,
  summary: String,
  year: Date,
  rating: Number,
  genres: [{ type: String }],
  meta: {
    views: Number,
    rating: Number
  }
});

const Movie = mongoose.model("Movie", movieSchema);
export default Movie;
