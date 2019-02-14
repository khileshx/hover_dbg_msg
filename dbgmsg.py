##=============Tkinter GUI on seperate thread for logging===========
import tkinter
from tkinter.scrolledtext import ScrolledText
import time
import threading


def main():
   app = LogWin()
  
   app.update("Sup\n")
   print("Main thread is still running about to sleep for 2 sec")
   time.sleep(2)
   app.update("i can now insert as much text i want")
   time.sleep(2)
   app.update("\nWorking as expected")
   
    

#class LogWindow:
#    win = None
#    st = None
#
#    def __init__(self):
#        win = self.win = tkinter.Tk()
#        st = self.st = ScrolledText(win)
#        st.pack()
#        win.call("wm", "attributes", ".", "-topmost", "1")
#        threading.Thread(target=win.mainloop).start()
#
#    def update(self, text):
#        self.st.insert("insert", text)
        

class LogWin(threading.Thread):

    st = None
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
        time.sleep(3)

    def callback(self):
        print("Callback function is executed")
        self.root.quit()

    def run(self):
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        
        self.st = ScrolledText(self.root)
        self.st.pack()
        self.root.call("wm", "attributes", ".", "-topmost", "1")
        self.root.mainloop()
        
    def update(self, text, end="\n"):
        self.st.insert("insert", text + end)


        
if __name__ == "__main__": main()



