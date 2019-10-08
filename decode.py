# -*- coding: utf-8 -*-
from tools import Crypter
from Tkinter import Tk

c=Crypter()

res=c.decode('WDMSJFqSEWApVDABOF8SPA==')
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(res)
r.destroy()
print res