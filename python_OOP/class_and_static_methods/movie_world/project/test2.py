from battle.project import Customer
from battle.project import DVD
from battle.project import MovieWorld

movie_world = MovieWorld("Test")
d = DVD("A", 1, 1254, "February", 10)
c = Customer("Pesho", 20, 4)
movie_world.add_customer(c)
movie_world.add_dvd(d)
movie_world.rent_dvd(4, 1)
result = movie_world.return_dvd(4, 1)
print(result)
print(c.rented_dvds)
print(d.is_rented)