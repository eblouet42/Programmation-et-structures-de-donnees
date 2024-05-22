import wave
import numpy as np

wall="C:/Users/evanb/Downloads/the_wall.wav"
wall1sur2="C:/Users/evanb/Downloads/the_wall_but_ugh.wav"
wallderangeant="C:/Users/evanb/Downloads/the_wall_interpole.wav"
wallvitessevariable="C:/Users/evanb/Downloads/the_wall_vitesse_variable.wav"
wallexperimental="C:/Users/evanb/Downloads/the_wall_experimental_version.wav"

#============= functions

# Exercice 1
def analyse_son(chemin_fichier_wav):
    """Returns the parameters of a .wav file as well as the value of each frame"""
    son=wave.open(chemin_fichier_wav,"rb")
    params=son.getparams()
    frames=son.readframes(params[3]) 
    audio_data=np.frombuffer(frames, dtype=np.int16)
    return params,audio_data

# Exercice 2
def creer_musique(chemin_fichier_wav,databytes,n_channels,sampwidth,framerate,n_frames,comptype,compname):
    """Modifies a .wav file according to the paramaters"""
    lilali=wave.open(chemin_fichier_wav,"wb")
    lilali.setparams((n_channels,sampwidth,framerate,n_frames,comptype,compname))
    lilali.writeframes(databytes)
    return None

# Exercice 3
def unenotesur2(chemin_fichier_wav_initial,chemin_fichier_wav_final):
    """Modifies the second .wav file with the first .wav file
    with only one frame in two"""
    params,audio_data=analyse_son(chemin_fichier_wav_initial)
    n_channels,sampwidth,framerate,n_frames,comptype,compname=params
    output_data = audio_data.reshape(-1, n_channels)[::2].flatten()
    creer_musique(chemin_fichier_wav_final,output_data.tobytes(),n_channels,sampwidth,framerate,n_frames,comptype,compname)

# Exercice 4
def interpolation_son(chemin_fichier_wav_initial,chemin_fichier_wav_final):
    """Modifies the second .wav file with the first .wav file
    where new frames are created by a linear interpolation between each frames"""
    params,audio_data=analyse_son(chemin_fichier_wav_initial)
    n_channels,sampwidth,framerate,n_frames,comptype,compname=params
    audio_data = audio_data.reshape(-1, n_channels)
    interpolated_length =2*len(audio_data)-1
    interpolated_data=np.zeros((interpolated_length, n_channels),dtype=np.int16)
    interpolated_data[::2]=audio_data
    interpolated_data[1::2]=(audio_data[:-1]+audio_data[1:])//2
    output_data = interpolated_data.flatten()
    creer_musique(chemin_fichier_wav_final,output_data.tobytes(),n_channels,sampwidth,framerate,n_frames,comptype,compname)
def boucherie(chemin_fichier_wav_initial,chemin_fichier_wav_final):
    """Modifies the second .wav file with the first .wav file
    where half of the frames were replaced by a interpolated frame (linearly)"""
    chemin_intermediaire = "temp.wav"
    unenotesur2(chemin_fichier_wav_initial, chemin_intermediaire)
    interpolation_son(chemin_intermediaire, chemin_fichier_wav_final)
    
# Exercice 5
def alacadence(chemin_fichier_wav_initial,chemin_fichier_wav_final,f):
    """Modifies the second .wav file with the first .wav file,
    with a rythm multiplied by the real 'f' """
    params,audio_data=analyse_son(chemin_fichier_wav_initial)
    n_channels,sampwidth,framerate,n_frames,comptype,compname=params
    output_data = audio_data.reshape(-1,n_channels).flatten()
    creer_musique(chemin_fichier_wav_final,output_data.tobytes(),n_channels,sampwidth,int(framerate*f),n_frames,comptype,compname)

# Exercice 6
def ajouter_echo(chemin_fichier_wav_initial, chemin_fichier_wav_final, delay, attenuation):
    """Modifies the second .wav file with the first .wav file,
    which now has some echo lasting during 'delay' seconds,
    attenuated by a factor of 'attenuation' """
    params,audio_data=analyse_son(chemin_fichier_wav_initial)
    n_channels,sampwidth,framerate,n_frames,comptype,compname=params
    audio_data=audio_data.reshape(-1,n_channels)
    nb_echo=int(delay*framerate)
    echoecho=np.zeros((len(audio_data)+nb_echo,n_channels),dtype=np.int16)
    echoecho[:len(audio_data)] = audio_data
    for i in range(nb_echo, len(echoecho)):
        echoecho[i]+=(audio_data[i-nb_echo]*attenuation).astype(np.int16)
    creer_musique(chemin_fichier_wav_final, echoecho.flatten().tobytes(),n_channels,sampwidth,framerate,n_frames,comptype,compname)

#============= main

# Exercice 1
T=analyse_son("C:/Users/evanb/Downloads/the_wall.wav")
print(T[0])
print(T[1])

# Exercice 3
unenotesur2(wall,wall1sur2)

# Exercice 4
boucherie(wall,wallderangeant)

# Exercice 5
alacadence(wall,wallvitessevariable,2)

# Exercice 6
ajouter_echo(wall,wallexperimental,0.5,0.5)