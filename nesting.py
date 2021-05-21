albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
song_index = 1
while True:
    print("Please choose your album?(invalid input will exit)")
    for number in range(len(albums)):
        print(f"{number+1}: {albums[number][0]} ")
    album_index = int(input())-1
    if not 0 <= album_index < len(albums):
        break
    chosen_album = albums[album_index]
    for number,song in chosen_album[3]:
        print(f"{number}: {song}")
    song_index = int(input())-1
    if not 0 <= song_index < len(chosen_album[3]):
        break
    chosen_song = albums[album_index][3][song_index][1]
    print(f"'{chosen_song}' song is playing now")
    print("="*50)

