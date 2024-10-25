#p2204779/main.py
import tkinter as tk
from menu import Menu  

def create_window():
    window = tk.Tk()
    window.title("Brick Breaker")
    window.configure(bg="black")
    window.geometry("600x600") 
    return window

if __name__ == "__main__":
    window = create_window()
    app = Menu(window)  
    window.mainloop()