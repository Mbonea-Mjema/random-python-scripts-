from vlc import Instance
import os

#playlist1 = [r'C:\Users\SAMSUNG\Downloads\Music\01.mp3',r'C:\Users\SAMSUNG\Downloads\Music\Selfie.mp3']


favourite = list()
path = "/home/pi/Music/"
Constant_path="/home/pi/Music"
for i in os.listdir(Constant_path):
    item  = path + i
    favourite.append(item)

other = list()
path2 = '/home/pi/other/'
for i in os.listdir("/home/pi/other"):
    item  = path2 + i
    other.append(item)



class music:
    
    def music(self,choice):
        player = Instance()
        mediaListPlayer = player.media_list_player_new()
        mediaList = player.media_list_new()
        if choice == "favourite":
            for song in favourite:
                mediaList.add_media(player.media_new(song))

            mlp = mediaListPlayer.set_media_list(mediaList)
        elif choice == "other":
            for song in other:
                mediaList.add_media(player.media_new(song))

                mediaListPlayer.set_media_list(mediaList)

        return mediaListPlayer

#ins = music.music("favourite")
#ins.play()

