import media
import my_web

logan = media.Movie("Logan","Story of my fav, Wolverine","http://oncenerd.com/wp-content/uploads/2016/10/logan.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

#print(toy_story.storyline)

logan = media.Movie("Logan","Story of my fav, Wolverine","http://oncenerd.com/wp-content/uploads/2016/10/logan.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

thor = media.Movie("Thor Ragnarok","Story of my fav, Wolverine","http://cdn.movieweb.com/img.news.tops/NEOe3FBKEIX3SQ_2_b.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

captain = media.Movie("Captain Marvel","Story of my fav, Wolverine","https://i.redd.it/omdyjp5kvlgx.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

gardians= media.Movie("Gardians of the galaxy Vol 2","Story of my fav, Wolverine","http://t3.gstatic.com/images?q=tbn:ANd9GcQWA3pKqv8oaHq4cP6YK3QKpgPbMjoHIzytUlThEF3P8ZAvyeZv",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

logan = media.Movie("Logan","Story of my fav, Wolverine","http://oncenerd.com/wp-content/uploads/2016/10/logan.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")
#logan.show_trailer()
#logan.show_poster()
movies = [logan, logan, thor, captain, gardians, logan]

#my_web.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)

