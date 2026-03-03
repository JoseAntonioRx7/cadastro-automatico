#Automatizando o processo de abrir o navegador, acessar um site e preencher um formulário usando a biblioteca pyautogui.

import pyautogui
import time

#Abrindo o navegador
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#Entrando no site
link = 'https://demoqa.com/text-box'
pyautogui.write(link)
pyautogui.press('enter')

