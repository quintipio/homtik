import pychromecast
import os

# démarrer un serveur http manuellement : python3 -m http.server

# finir par 32 pour la chambre, finir par 90 pour le salon
ADRESSE_IP_CHROMECAST = "192.168.1."

# changer en fonction du pc
ADRESSE_IP_PC = "192.168.1.92"

# nom du film à mettre (le film doit être dans le mê)
FICHIER_FILM = ""

FICHIER_CONVERTI  = "film.mp4"

HEURE_REPRISE = 0

MINUTE_REPRISE = 0


def convert_movie_to_mp4():
    if FICHIER_FILM.lower().endswith(".avi"):
        os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = FICHIER_FILM, output = FICHIER_CONVERTI))
    if FICHIER_FILM.lower().endswith(".mkv"):
        os.popen("ffmpeg -i {input} -codec copy -strict -2 {output}.mp4".format(input = FICHIER_FILM, output = FICHIER_CONVERTI))


def play_movie_to_chromecast():
    chromecast = pychromecast.Chromecast(ADRESSE_IP_CHROMECAST)
    chromecast.wait()
    print(chromecast.device)
    print(chromecast.status)
    time = (HEURE_REPRISE * 3600) + (MINUTE_REPRISE * 60)
    controller = chromecast.media_controller
    controller.play_media('http://{}:8000/{}'.format(ADRESSE_IP_PC, FICHIER_CONVERTI), title=FICHIER_FILM, content_type='video/mp4', current_time=time, autoplay=True)
    controller.block_until_active()
    print(controller.status)
    controller.play()


if __name__ == "__main__":
    convert_movie_to_mp4()
    play_movie_to_chromecast()
