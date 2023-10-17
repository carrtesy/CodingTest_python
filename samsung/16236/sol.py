from pywinauto.mouse import click
from time import sleep
import win32api

x, y = win32api.GetCursorPos()
while True:
   sleep(10)
   click(coords = (x, y))