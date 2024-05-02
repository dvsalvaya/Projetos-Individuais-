import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
from tkinter import *

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
 try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando =comando.lower()
        if "Bob" in comando:
         comando = comando.replace('Bob','')
         maquina.say(comando)
         maquina.runAndWait()
 except:
  print("Microfone não está ok")

 return comando

def comando_voz_usuario():
 comando = executa_comando()
 if "horas" in comando:
    hora = datetime.datetime.now().strftime('%H:%M')
    maquina.say('Agora são' + hora)
    maquina.runAndWait()
 elif "procure por" in comando:
     procurar = comando.replace('procure por','')
     wikipedia.set_lang("pt")
     resultado = wikipedia.summary(procurar, 2)
     print(resultado)
     maquina.say(resultado)
     maquina.runAndWait()
 elif "toque" in comando:
     musica = comando.replace('toque', '')
     resultado = pywhatkit.playonyt(musica)
     maquina.say("Tocando música")
     maquina.runAndWait()

  



comando_voz_usuario

bob = Tk()
bob.geometry('400x300')
bob.title('Eu sou o Bob')


lbl = Label(bob, text='Fala ai, estou te...')
lbl.grid(column=0, row=0, padx=20 , pady=70)


b=Button(bob, text='Aperte para falar' , command= comando_voz_usuario )
b.grid(column=0, row=1)

bob.mainloop()