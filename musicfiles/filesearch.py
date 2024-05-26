import os
import fnmatch

def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # fnmatch to match the artist_name to the directory name
        # fnmatch can accept '*' wild card eg. Bo* will return all names starting with Bo
        # for artist in fnmatch.filter(directories, artist_name):

        # convert directory name to upper case such artist_name isn't
        # case sensitive
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):   # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "aErosmith")
song_list = find_songs(album_list)

for s in song_list:
    print(s)
# for a in album_list:
#     print(a)