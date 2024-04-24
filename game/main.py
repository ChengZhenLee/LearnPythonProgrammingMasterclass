from player import Player

tim = Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim.lives)

print(tim.get_name())
tim.set_lives(300)