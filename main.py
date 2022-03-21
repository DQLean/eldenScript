'''
  __Name = '艾尔登法环快速传送脚本'
  __Author = 'Rabbit'
  Released under the MIT License.
  本脚本只用于坏档快速脱出传送，貌似当前代码也只能做到这些...
'''

from tkinter import *
from pynput.keyboard import Listener, Key, Controller
import time

class App:
  def __init__(self):
      self.GUI()

  def GUI(self):
    root = Tk()
    root.title('EldenScript')
    root.geometry('400x290')

    lab2 = Label(root, text='Open Map TimeOut', font=("微软雅黑", 9), fg="gray")
    lab2.place(relx=0.05, y=10, relwidth=0.4, height=30)
    self.mapinput = Entry(root, font=("微软雅黑", 10))
    self.mapinput.place(relx=0.05, y=40, relwidth=0.4, height=30)
    self.mapinput.insert(0, 0.05)

    lab2 = Label(root, text='Key Press TimeOut', font=("微软雅黑", 9), fg="gray")
    lab2.place(relx=0.55, y=10, relwidth=0.4, height=30)
    self.keyinput = Entry(root, font=("微软雅黑", 10))
    self.keyinput.place(relx=0.55, y=40, relwidth=0.4, height=30)
    self.keyinput.insert(0, 0.05)

    label3 = Label(root, text='---------- Help ----------', font=("微软雅黑", 8), fg="gray")
    label3.place(relx=0.05, y=90, relwidth=0.9, height=20)
    state = Text(root, font=("微软雅黑", 10))
    state.place(relx=0.05, y=110, relwidth=0.9, height=120)
    state.insert(0.1, '上方左边是打开地图后延时，右边是按键延时，单位为秒，如果默认延时无法正常工作，可以将其设置高一点。设置完毕后按Start开始监听，在游戏中按F5开始脚本')

    # 开始按钮
    self.btn_start = Button(root, text='START', font=("微软雅黑", 12), fg="white", bg="gray", command=self.start)
    self.btn_start.place(relx=0.3, y=240, relwidth=0.4, height=30)

    root.mainloop()

  def start(self):
    try:
      # 将文本框读到的字符串转化为浮点数
      self.maptime = float(self.mapinput.get())
      self.keytime = float(self.keyinput.get())

      #监听键盘
      self.listener = Listener(on_press=self.on_press,on_release=self.on_release)
      self.listener.start()
    except Exception as ep:
      print(ep)

  #按下键盘
  def on_press(self, key):
    print("按下{}".format(key))
    if key == Key.f5:
      self.keyScript()
      
  #松开键盘
  def on_release(self, key):
    print("松开{}".format(key))
    if key == Key.esc:
      #esc键退出监听
      return False

  # 执行脚本
  def keyScript(self):

    keyboard = Controller()

    keyboard.press('g')
    time.sleep(self.maptime)
    keyboard.press('f')
    time.sleep(self.keytime)
    keyboard.press('e')
    time.sleep(self.keytime)
    keyboard.release('e')
    time.sleep(self.keytime)
    keyboard.press('e')
    time.sleep(self.keytime)
    keyboard.release('f')
    keyboard.release('g')
    keyboard.release('e')


if __name__ == '__main__':
  App()