
alien_colors = ["red","yellow","green"]

alien_color = alien_colors[-3]
player_points = 0


if (alien_color == "green"):
    player_points = player_points+ 5
elif (alien_color == "yellow"):
    player_points = player_points + 10
else :
    player_points = player_points + 15

print("You earned " + str(player_points) + ".")
print("The alien color is " + alien_color)