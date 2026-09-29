favourite_places = {"shiam": "park", "maihs":'city', "hsiam": "pool"}

favourite_places['chuttoo'] = 'moon   '
for key, value in favourite_places.items():
    print(key.title() + " favourite place is " + value.title())