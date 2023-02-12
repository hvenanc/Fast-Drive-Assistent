from capAudio import reconhecer_fala
import pyttsx3 as vc
import time
import requests
import PySimpleGUI as sg

sg.theme('LightGrey1')


layout = [
    [sg.Text('Fast Drive Assistent', pad = (0,0))],
    [sg.Button('Converse com July', pad = (0,20), size = (15,2), button_color = 'green')],
    [sg.Button('Desligar Sistema', pad = (0,0),size = (15,2), button_color = 'red')]
]

window = sg.Window('Carro Inteligente',layout,element_justification='c',size = (750,200))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Desligar Sistema':
        window.close()
        break
        

    if event == 'Converse com July':

        url = 'http://192.168.120.124'
        msg = ''
        index = 0
        frases = {
            '13': 'Seu carro está prontinho para acelerar!',
            '10': 'Nossa Recife está sempre quente, acabei de ligar o Ar-Condicionado',
            '11': 'Prontinho faróis ligados',
            '12': 'Sistema desligado com sucesso obrigado por utilizar o Fast Drive Assistent'
        }
            

        voice = vc.init()
        voice.say('Olá sou a July, sua assistente. Qual é o destino de hoje?')
        voice.runAndWait()

        while True:

            x = reconhecer_fala()
            time.sleep(3)

            if 'desligar' in x:
                notificacao = 'Sistema Desligado'
                index = '12'
                msg = frases.get(index)
                voice.say(msg)
                requests.post(url, data=index)
                voice.runAndWait()
                window.close()
                break

            elif 'condicionado' in x:
                notificacao = 'Ar-Condicionado Ligado'
                index = '10'
                msg = frases.get(index)

            elif 'faróis' in x:
                notificacao = 'Faróis Acessos!'
                index = '11'
                msg = frases.get(index)

            elif 'carro' in x:
                notificacao = 'Veiculo Ligado'
                index = '13'
                msg = frases.get(index)
                
                
            
            requests.post(url, data=index)
            print(msg)
            voice.say(msg)
            voice.runAndWait()
            sg.SystemTray.notify('Fast Drive Assistent', notificacao)
