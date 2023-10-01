import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

##### Passo 1 : Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# Entrar no link 
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)


##### Passo 2 : Fazer login

# Preencher os campos
pyautogui.click(x=603, y=447)
pyautogui.write('test@gmail.com')

pyautogui.click(x=601, y=573)
pyautogui.write('sua senha aqui')

# Botão Login
pyautogui.press('tab')
pyautogui.press('enter')


##### Passo 3 : Importar a base de dados de produtos

tabela = pandas.read_csv('produtos.csv')
print(tabela)


##### Passo 4 : Cadastrar 1 produto

for linha in tabela.index:
    pyautogui.click(x=592, y=296)

    # Preencher os campos
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press('tab')

    # Enviar
    pyautogui.press('enter')

    pyautogui.scroll(50000)


# Passo 5 : Repetir o cadastro para todos os produtos
