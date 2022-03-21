import tkinter

class ScaleExample:
    def __init__(self, frame):
        self.frame = frame
    
    def DrawScale(self):
        scale = tkinter.Scale(self.frame, orient="horizontal", showvalue=True, from_=100, to=0, command=lambda value: self.CallScale(value))
        scale.grid(row=0, column=0)

    def CallScale(self, value):
        print(value)

def main():
    main_window = tkinter.Tk()      
    main_window.title('scaleExample')
    main_window.geometry('200x200+0+0') # windows size : width, heigth, x, y
    main_window.resizable(False, False) # window scale enable : Updown, LeftRight
    scaleExample = ScaleExample(main_window)
    scaleExample.DrawScale()
    main_window.mainloop()

if __name__ == '__main__':
    main() 