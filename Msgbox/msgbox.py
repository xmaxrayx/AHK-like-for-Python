from tkinter import messagebox
import platform
import os
import re

if platform.system() == "Windows":
    from ctypes import windll




def Msgbox(text = "Press ok to continue" , title =  os.path.basename(__file__) , option= None ):
    
    def search_L(haystack , *needleBundle , startSearch = "" , EndSearch = "" , mode = 0 ,debug = False  ):
        if mode == 1:
            startSearch = "(?-i)"
        for needle in needleBundle:
            x = re.search(needle , startSearch + haystack + EndSearch)
            if debug == True:
                Msgbox("Haystack:   ["+ needle + "]\nNeedle:    [" + str(startSearch + haystack + EndSearch) + "]\nResult :     [" + str(x) + "]")
            if bool(x) == True:
                return True
        
    
    #Path(__file__).stem
    if platform.system() == "Windows":
        windll.shcore.SetProcessDpiAwareness(1)
    
    if option == None:
        return messagebox.showinfo(title ,text)
    elif search_L(option, "yn" , "ny" , mode=1 ) :
        return messagebox.askyesno(title ,text)       
    elif search_L(option, "ok" , mode=1 ) :
        return messagebox.showinfo(title ,text)
    elif search_L(option, "?" , mode=1 ) :
        return messagebox.askquestion(title ,text)
    elif search_L(option, "rc" ,"cr" , mode=1 ):
        return messagebox.askretrycancel(title ,text)
