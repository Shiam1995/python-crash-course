alien_colors = ["red","yellow","green"]

alien_color = alien_colors[-1]

player_points = 0

print(alien_color)
if alien_color == "green":
    player_points = player_points + 5
elif alien_color == "blue":
    player_points = player_points + 100

print(player_points)


print("\nAlien shot")

alien_color = alien_colors[-2]

print(alien_color)