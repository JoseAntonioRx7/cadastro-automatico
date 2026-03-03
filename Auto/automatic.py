#Automatizando o processo de abrir o navegador, acessar um site e preencher um formulário usando a biblioteca pyautogui.

import pyautogui
import time

#Abrindo o navegador
pyautogui.PAUSE = 1 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#Entrando no site
link = 'https://demoqa.com/text-box'
pyautogui.write(link)
pyautogui.press('enter')

#Aguardando o site carregar
time.sleep(3)


#Preenchendo o formulário
pyautogui.click(x=931, y=359) #Clicando no campo de Full Name
pyautogui.write('Jose Antonio Ramos') #Escrevendo o nome
pyautogui.press('tab') #Clicando no campo de Email
pyautogui.write('joseantonio@gmail.com') #Escrevendo o email
pyautogui.press('tab') #Clicando no campo de Current Address
pyautogui.write('Rua da Blockchain, n° 123') #Escrevendo o endereço
pyautogui.press('tab') #Clicando no campo de Permanent Address
pyautogui.write('Desenvolvi isso aqui para automatizar o preenchimento de formularios, ou oque voce quiser!') #Escrevendo
pyautogui.press('tab') #Clicando no botão de Submit
pyautogui.press('enter') #Clicando no botão de Submit

#Aguardando o resultado aparecer
time.sleep(3) #Aguardando o resultado aparecer
print('Formulário preenchido e enviado com sucesso!')









