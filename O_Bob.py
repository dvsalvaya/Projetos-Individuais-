import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit as pt
import sys


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
 try:
    with sr.Microphone() as source:
        
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando =comando.lower()
        if "bob" in comando:
         comando = comando.replace('Bob','')
         
 except:
  print("Microfone não está ok")
  inicio()
 
 return comando

def comando_voz_usuario():
 comando = executa_comando()
 if "bob" in comando:
  if "horas" in comando:
    hora = datetime.datetime.now().strftime('%H:%M')
    maquina.say('Agora são' + hora)
    maquina.runAndWait()
    maquina.say('Mais alguma coisa?')
    maquina.runAndWait()
  elif "procure por" in comando:
     procurar = comando.replace('procure por','')
     wikipedia.set_lang("pt")
     resultado = wikipedia.summary(procurar, 2)
     print(resultado)
     maquina.say(resultado)
     maquina.runAndWait()
     maquina.say('Mais alguma coisa?')
     maquina.runAndWait()
  elif "toque" in comando:
     musica = comando.replace('toque', '')
     resultado = pt.playonyt(musica)
     maquina.say("Tocando música")
     maquina.runAndWait()
  elif "desligar" in comando:
   sys.exit()
  elif "mensagem" in comando:
   #Nome da pessoa e o número
   if '' in comando :
     phone_number = '+55'
     message = comando.replace('bob mensagem ','')
   elif '' in comando:
     phone_number = '+55'
     message = comando.replace('bob mensagem ','')  
   elif '' in comando:
     phone_number = '+55'
     message = comando.replace('bob mensagem ','')
   pt.sendwhatmsg_instantly(phone_number,message,7,True,2)
   maquina.say('Mais alguma coisa?')
   maquina.runAndWait()
    

  

def inicio():
 while True:
  comando_voz_usuario()
  

maquina.say('Eu sou o Bob, como posso ajudar?')
maquina.runAndWait()
inicio()
