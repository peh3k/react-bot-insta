#!!!---IMPORTANTE---!!! Leia o READ.ME!

from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import PySimpleGUI as sg
import pyautogui

class PainelGrafico:
    
    def __init__(self):
        
        sg.theme('SystemDefault')
        
        layout = [
            [sg.Text('Usuário: ', font='Arial'), sg.InputText(size=(18, 50), justification='c', key='-USUARIO-', 
            default_text=" ")],
            [sg.Text('Senha:   ', font='Arial'), sg.InputText(size=(18, 50), key='-SENHA-', password_char='*', justification='c')], 
            [sg.Text('Link:       ', font='Arial'), sg.InputText(size=(18, 50), key='-MENSAGEM-', 
            default_text=" ", justification='c')],
            [sg.Button('Sair'), sg.Push(), sg.Button('Iniciar')]
        ]
        self.window = sg.Window('Robô Reação', layout)

    def iniciar(self):
        while True:  
            self.events, self.values = self.window.read()
            if self.events == 'Iniciar':
                BotInsta.iniciar_bot(self)
            elif self.events == 'Sair' or self.events == sg.WINDOW_CLOSED or self.events:
                break 
            elif BotInsta.fechar_paginas(self) == True:
                break
                
class BotInsta:

    def abrir_dicionario_html(self): #/Xpath's e Classes do HTML
        self.endereços_HTML = {
            'Login Usuario xpath': '//*[@id="loginForm"]/div/div[1]/div/label/input', 
            'Login Senha xpath': '//*[@id="loginForm"]/div/div[2]/div/label/input', 
            'Botao Entrar Login xpath': '//*[@id="loginForm"]/div/div[3]', 
            'Botao Fechar Popup 1 xpath': '//*[@id="mount_0_0_q5"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button', 
            'Botao Fechar Popup 1 class': 'cmbtv',
            'Botao Fechar Popup 2 class': '_a9--',
            'Botao Fechar Popup 2 xpath': '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2] ',
            'Botao clicar busca': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div',
            'Text area story': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[1]/div/textarea',
            'Botao inserir user': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input',
            'Botao story busca': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/ul/div[1]/div/a/div/div[1]/div/span/img',
            'Botao Enviar Mensagem class': '_acan', 
            'Botao Mensagem tag_name': 'textarea', 
            'Botao Enviar xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button', 
            'Botao Mensagem Nao Lida xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div', 
            'Botao Messenger Dm xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[1]/div/div[3]/div/div[2]/a', 
            'Botao Messenger Home xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a',
            'Botao Mensagem Nao Lida class': '_ab8n',
            'Botao enviar story': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[1]/div[2]/button',
            'Botao voltar story': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/button[1]/div',
            'Botao avancar story': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/button[2]/div',
            'Botao story perfil': '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/div/div/span/img'}
            
    def coletar_dados_usuario(self):
        self.user_client_insta = self.values['-USUARIO-']
        self.password_client_insta = self.values['-SENHA-']
        self.link_story = self.values['-MENSAGEM-']
        
        
    def abrir_pagina(self):
        self.pagina = webdriver.Chrome()
        self.pagina.get('https://www.instagram.com')
    
    def fazer_login(self):
        time.sleep(3)
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Login Usuario xpath']).send_keys(self.user_client_insta) 
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Login Senha xpath']).send_keys(self.password_client_insta)
        time.sleep(1) 
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Entrar Login xpath']).click() 

    def buscar_story(self):
            time.sleep(5)
            self.pagina.get(self.link_story)

    def voltar_story(self):
        time.sleep(1)
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao voltar story']).click()
        
    
    def avancar_story(self):
        time.sleep(1)
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao avancar story']).click()
        BotInsta.reagir_story(self)

    def reagir_story(self):
            time.sleep(7)
            self.pagina.find_element(By.XPATH, self.endereços_HTML['Text area story']).click()
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao enviar story']).click()
            BotInsta.voltar_story(self)
            BotInsta.avancar_story(self)
    
    def iniciar_bot(self):
        BotInsta.abrir_dicionario_html(self)
        BotInsta.coletar_dados_usuario(self)
        BotInsta.abrir_pagina(self)
        BotInsta.fazer_login(self)
        BotInsta.buscar_story(self)
        BotInsta.reagir_story(self)
        
#Inicia tudo

init = PainelGrafico()
init.iniciar()


         
