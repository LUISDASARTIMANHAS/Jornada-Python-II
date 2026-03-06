# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import meu_utils

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# pausa padrão para cada comando do pyautogui
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
credenciais = {"user": "admin@ifes.edu.br", "password": "admin"}


# abrir o navegador (chrome)
# usando o executar para abrir porque não precisa interagir com a barra de pesquisa do windows, o comando já abre o navegador
pyautogui.hotkey("win", "r")
pyautogui.write("chrome.exe --guest")
pyautogui.press("enter")
# esperar o navegador abrir
time.sleep(2)

# entrar no link
pyautogui.write(link)
pyautogui.press("enter")
# esperar o site carregar
time.sleep(4)

# selecionar o primeiro campo 
pyautogui.press("tab")
for key in credenciais:
    # apertar tab pra selecionar o proximo automaticamente
    meu_utils.escrever_e_tab(credenciais[key])
# apertar botão de enviar
pyautogui.press("enter")
# esperar o site carregar
time.sleep(4)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")    
print(tabela)

# Passo 4: Cadastrar um produto
for i in tabela.index:
    linha = tabela.iloc[i]
    # Point(x=501, y=258)
    # clica no primeiro campo 
    pyautogui.click(501,258)
    # para cada campo na linha repetir o inserir
    meu_utils.preencher_campos(linha)
    # apertar o botão de enviar
    pyautogui.press("enter")
    # voltar a tela para cima 
    pyautogui.scroll(5000)
