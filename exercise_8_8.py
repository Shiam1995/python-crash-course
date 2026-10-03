def make_album(artist_name = '',  album_name = '' ):
    return [artist_name, album_name]



artist_name_full = " "
artist_album_name = " "

while True:

    print("Give me names")
    print("press q to quit")

    artist_name_full = input("Name")
    if artist_name_full == "q":
        break

    artist_album_name = input("Album")
    if artist_name_full == "q":
        break

    print(make_album(artist_name_full, artist_album_name))
    print("\n next \n")


