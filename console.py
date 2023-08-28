import pdb
from models.destination import Destination
from models.user import User

from repositories import user_repository
from repositories import destination_repository

# destination_repository.delete_all()
# user_repository.delete_all()

user1 = User("Samantha")
user_repository.save(user1)
user2 = User("Sam")
user_repository.save(user2)
user3 = User("Lauren")
user_repository.save(user3)
user4 = User("Rebecca")
user_repository.save(user4)
user5 = User("Stacey")
user_repository.save(user5)
user6 = User("Stephanie")
user_repository.save(user6)
user7 = User("John")
user_repository.save(user7)
user8 = User("Alison")
user_repository.save(user8)
user9 = User("Gordon")
user_repository.save(user9)
user10 = User("Steve")
user_repository.save(user10)


destination1 = Destination("Paris", "France", user1, True)
destination_repository.save(destination1)
destination2 = Destination("Dubai", "UAE", user1, True)
destination_repository.save(destination2)
destination3 = Destination("Phucket", "Thailand", user1, True)
destination_repository.save(destination3)
destination4 = Destination("Miami", "USA", user1, True)
destination_repository.save(destination4)
destination4 = Destination("Ibiza", "Spain", user4, False)
destination_repository.save(destination4)
destination5 = Destination("New York", "USA", user6, False)
destination_repository.save(destination5)

user_repository.select_all()



