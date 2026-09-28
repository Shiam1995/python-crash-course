alien_colors = ["red","yellow","green"]

alien_color = alien_colors[-1]

player_points = 0

if alien_color == "green":
    player_points = player_points + 5

print("Ship is " + alien_color + ".")
print("Player points is " + str(player_points) + ".")

print("\n")



alien_color = alien_colors[-2]


if (alien_color == "yellow" or alien_color == "red"):
    player_points = player_points + 10

print("Ship is " + alien_color + ".")
print("Player points is " + str(player_points) + ".")
print(player_points)