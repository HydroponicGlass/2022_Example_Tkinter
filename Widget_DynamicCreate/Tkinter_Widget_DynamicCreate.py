import tkinter

class DynamicWidget:
    def __init__(self, mainFrame):
        self.entries = []
        self.labels = []
        self.buttons = []
    
        self.frame_input = tkinter.Frame(mainFrame)
        self.frame_result = tkinter.Frame(mainFrame)
        self.frame_input.grid(row=0, column=0)
        self.frame_result.grid(row=1, column=0)

        lbl_input = tkinter.Label(self.frame_input, text="num", padx=10)
        entry_input = tkinter.Entry(self.frame_input, width=10)
        btn_input = tkinter.Button(self.frame_input, width=10, text="make", command=lambda:DynamicWidget.MakeDynamicWidget(self, entry_input.get()))
        lbl_input.grid(row=0, column=0)
        entry_input.grid(row=0, column=1)
        btn_input.grid(row=0, column=2)

    def MakeDynamicWidget(self, num):
        num = int(num)
        for i in range(num): 
            self.labels.append(tkinter.Label(self.frame_result, text=i, padx=10))
            self.labels[i].grid(row=i, column=0)
            self.entries.append(tkinter.Entry(self.frame_result, width=10))
            self.entries[i].grid(row=i, column=1)
            self.buttons.append(tkinter.Button(self.frame_result, width=10, text="button", command=lambda i=i: DynamicWidget.Buttonselect(self, i)))
            self.buttons[i].grid(row=i, column=2)

    def Buttonselect(self, idx):
        self.entries[idx].delete(0, 'end')
        self.entries[idx].insert(0, idx)

def main():
    main_window = tkinter.Tk()   
    main_window.title('test')
    main_window.geometry('200x200+0+0') # windows size : width, heigth, x, y
    main_window.resizable(False, False) # window scale enable : Updown, LeftRight
    dynamicWidget = DynamicWidget(main_window)
    main_window.mainloop()

if __name__ == '__main__':
    main()


'''
entries = []
labels = []
buttons = []

def MakeDynamicWidget(num):
    num = int(num)
    for i in range(num): 
        labels.append(tkinter.Label(frame_result, text=i, padx=10))
        labels[i].grid(row=i, column=0)
        entries.append(tkinter.Entry(frame_result, width=10))
        entries[i].grid(row=i, column=1)
        buttons.append(tkinter.Button(frame_result, width=10, text="button", command=lambda i=i: Buttonselect(i)))
        buttons[i].grid(row=i, column=2)

def Buttonselect(idx):
    entries[idx].delete(0, 'end')
    entries[idx].insert(0, idx)

main_window = tkinter.Tk()   
main_window.title('test')
main_window.geometry('200x200+0+0') # windows size : width, heigth, x, y
main_window.resizable(False, False) # window scale enable : Updown, LeftRight
frame_input = tkinter.Frame(main_window)
frame_result = tkinter.Frame(main_window)
frame_input.grid(row=0, column=0)
frame_result.grid(row=1, column=0)
lbl_input = tkinter.Label(frame_input, text="num", padx=10)
entry_input = tkinter.Entry(frame_input, width=10)
btn_input = tkinter.Button(frame_input, width=10, text="make", command=lambda:MakeDynamicWidget(entry_input.get()))
lbl_input.grid(row=0, column=0)
entry_input.grid(row=0, column=1)
btn_input.grid(row=0, column=2)
main_window.mainloop()

'''