# Import class files in order to be able to use their contents.
import media
import fresh_tomatoes


# Create multiple instances of the class Movie.
# Declare instance variables that hold
# the values passed as arguments for the init function.

underworld = media.Movie("Underworld",
                         ("Action thriller about a war "
                          "between vampires and werewolves"),
                         ("https://upload.wikimedia.org/wikipedia/en/c/cc/"
                          "Underworld_%282003_film%29_poster.jpg"),
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

lord_of_rings = media.Movie("The Lord of the Rings",
                            ("Fantasy adventure film based on "
                             "the first volume of J.R.R. Tolkien's "
                             "The Lord of the Rings"),
                            ("https://upload.wikimedia.org/wikipedia/en/9/9d/"
                             "The_Lord_of_the_Rings_"
                             "The_Fellowship_of_the_Ring_"
                             "%282001%29_theatrical_poster.jpg"),
                            "https://www.youtube.com/watch?v=z_WZxJpHzEE")

tomb_raider = media.Movie("Tomb Raider",
                          ("Adventure film based on "
                           "Tomb Raider video games series"),
                          ("https://upload.wikimedia.org/wikipedia/en/"
                           "9/98/Lara_Croft_film.jpg"),
                          "https://www.youtube.com/watch?v=G4bhBabn-wU")

knockaround_guys = media.Movie("Knockaround Guys",
                               ("Drama film about the son of a mob boss "
                                "used as little more than an errand boy"),
                               ("https://upload.wikimedia.org/wikipedia/en/"
                                "6/61/Knockaround_guys_poster.jpg"),
                               "https://www.youtube.com/watch?v=dvyeucAN6Q8")

pitch_black = media.Movie("Pitch Black",
                          ("Science fiction action horror film, "
                           "predatory alien creatures begin attacking "
                           "the survivors of a crashed spaceship "
                           "landen on desert planet"),
                          ("https://upload.wikimedia.org/wikipedia/en/"
                           "2/26/Pitch_Black_poster.JPG"),
                          "https://www.youtube.com/watch?v=fIeSV4i7bxQ")

jurassic_park = media.Movie("Jurassic Park",
                            ("Scienc-fiction adventure film, "
                             "billionaire philanthropist and "
                             "a small team of genetic scientists "
                             "have created a wildlife park "
                             "of cloned dinosaurs "),
                            ("https://upload.wikimedia.org/wikipedia/en/"
                             "e/e7/Jurassic_Park_poster.jpg"),
                            "https://www.youtube.com/watch?v=QWBKEmWWL38")


# List of movies which will be passed as argument
# for the function open_movies_page
movies = [underworld,
          lord_of_rings,
          tomb_raider,
          knockaround_guys,
          pitch_black,
          jurassic_park]
fresh_tomatoes.open_movies_page(movies)
