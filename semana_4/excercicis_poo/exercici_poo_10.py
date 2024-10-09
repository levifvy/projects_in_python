'''Ejercicio 10
Define una clase llamada Song, que mostrará la letra de una canción. Su método __init__() debe tener dos argumentos: self y lyrics. lyrics es una lista. Dentro de tu clase crea un método llamado sing_me_a_song que imprima cada elemento de la letra en su propia línea. Define una variable:

happy_bday = Song(["Que Dios te bendiga,", "Que te acompañe el sol,", "¡Feliz cumpleaños a ti!"])

Llama al método sing_me_a_song sobre esta variable.'''


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Que Dios te bendiga,", "Que te acompañe el sol,", "¡Feliz cumpleaños a ti!"])
happy_bday.sing_me_a_song()
