import pyautogui
import pandas as pd 
import time

pyautogui.PAUSE = 0.5

#Acessando a planilha de produtos
pyautogui.press("Win")
pyautogui.write("D:\Projetos python\PowerUp\produtos.csv")
pyautogui.press("enter")
time.sleep(2)

pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Acessando sistema de cadastro
pyautogui.click(x=604, y=60)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=570, y=399)
pyautogui.write("caique_rocha@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senha1234567890")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Cadastrando produto
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index: 
    print(linha)
    
    pyautogui.click(x=647, y=274)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(-5000)
    time.sleep(0.5)
    pyautogui.scroll(5000)


