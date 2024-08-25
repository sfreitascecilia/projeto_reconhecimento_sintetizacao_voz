import speech_recognition as sr
import pyttsx3
import sys
import datetime

# Inicializar o reconhecedor de fala e o mecanismo de síntese de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Função para responder ao comando de voz
def respond_to_command(command):
    # Respostas básicas baseadas no comando
    now = datetime.datetime.now()
    if 'ajuda' in command:
        response = "Olá! Como posso ajudá-lo?"
    elif 'como está' in command:
        response = ("Eu sou apenas um assistente, mas estou funcionando bem. "
                    "Obrigado por perguntar!")
    elif 'hora' in command:
        response = f"A hora atual é {now.strftime('%H:%M:%S')}."
    elif 'data' in command:
        response = f"Hoje é {now.strftime('%d de %B de %Y')}."
    elif 'nome' in command:
        response = "Eu sou um assistente de voz, mas você pode me chamar de Alex!"
    elif 'clima' in command:
        response = "Desculpe, não posso acessar informações sobre o clima no momento."
    elif 'encerrar' in command:
        response = "Tenha um ótimo dia!"
        # Falar a resposta
        engine.say(response)
        engine.runAndWait()
        # Encerrar o programa
        sys.exit()
    else:
        response = "Desculpe, não entendi o comando."

    # Falar a resposta
    engine.say(response)
    engine.runAndWait()


# Função principal para capturar e processar o áudio
def ativar_assistente():
    with sr.Microphone() as source:
        print("Ajustando o ruído de fundo. Por favor, aguarde...")
        recognizer.adjust_for_ambient_noise(source)
        print("Pronto para ouvir...")

        while True:
            try:
                # Captura o áudio do microfone
                audio = recognizer.listen(source)
                print("Reconhecendo...")

                # Usa o reconhecimento de fala do Google para transcrever o áudio
                command = recognizer.recognize_google(audio, language="pt-BR")
                print(f"Você disse: {command}")

                # Transcreve o comando para um arquivo de texto
                with open("transcricoes.txt", "a") as file:
                    file.write(command + "\n")

                # Responde ao comando
                respond_to_command(command)

            except sr.UnknownValueError:
                print("Não consegui entender o áudio.")
            except sr.RequestError:
                print("Não consegui conectar ao serviço de reconhecimento de fala.")
            except KeyboardInterrupt:
                print("Interrompido pelo usuário.")
                break


# Chamada direta da função main
ativar_assistente()
