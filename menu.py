#/p2204779/menu
import tkinter as tk

class Menu:
    def __init__(self, window):
        self.window = window
        self.is_fullscreen = False
        self.setup_interface()
        self.sizeNormal
        self.start_countdown(10)

    def start_countdown(self, count):

        if count > 0:
            self.title_label.config(text=f"Please choose the size you want ({count} seconds)")
            self.window.after(1000, self.start_countdown, count - 1)  # Call again after 1 second
        else:
            self.title_label.config(text="Time's up! Starting the game...")
            self.window.after(2000, self.start_game)  


    def start_game(self):
        """Starts the game by calling the game module."""
        self.window.destroy()  # Close the menu window
        import game  # Import the game module
        game.run_game(self.selected_dimensions)
    def setup_interface(self):
        self.title_label = tk.Label(self.window, 
                                    text="Please choose the size you want",
                                    font=("",25))
        self.title_label.place(x=0,y=75)

        self.sizeNormal = tk.Button(self.window,
                                    text="Normal",
                                    font=("",20),
                                    height=2, width=20,
                                    fg='white',bg='black',
                                  command=self.size_Normal)
        self.sizeBig = tk.Button (self.window,
                                  text="Big",
                                  font=("",20),
                                  height=2, width=20,
                                  fg='white',bg='black',
                                  command=self.size_Big)
        
        self.sizeFullScreen = tk.Button(self.window,
                                        text="Full Screen",
                                        font=("",20),
                                        height=2, width=20,
                                        fg='white',bg='black',
                                        command=self.size_FullScreen)
        
        self.title_label.pack(side='top',fill='x',expand=False)
        #set position
        self.sizeNormal.place(relx=0.25,rely=0.2)
        self.sizeBig.place(relx=0.25,rely=0.4)
        self.sizeFullScreen.place(relx=0.25,rely=0.6)
        
    def size_Normal(self):
        self.is_fullscreen=False
        self.window.attributes('-fullscreen', self.is_fullscreen)
        self.window.geometry("600x600")  
        self.title_label.config(font=("",25))
        #set size
        self.sizeNormal.config(font=("",20),
                               height=2, width=20,)
        self.sizeBig.config(font=("",20),
                               height=2, width=20,)
        self.sizeFullScreen.config(font=("",20),
                               height=2, width=20,)
        self.sizeNormal.place(relx=0.25,rely=0.2)
        self.sizeBig.place(relx=0.25,rely=0.4)
        self.sizeFullScreen.place(relx=0.25,rely=0.6)
        self.selected_dimensions = (600, 600)

        
        
    def size_Big(self):
        self.is_fullscreen=False
        self.window.attributes('-fullscreen', self.is_fullscreen)
        self.window.geometry("1000x1000")  # Set the window size to big
        self.title_label.config(font=("",40))
        #set size
        self.sizeNormal.config(font=("",30),
                               height=3, width=20,)
        self.sizeBig.config(font=("",30),
                               height=3, width=20,)
        self.sizeFullScreen.config(font=("",30),
                               height=3, width=20,)    
                               
        #set position
        self.sizeNormal.place(relx=0.3,rely=0.2)
        self.sizeBig.place(relx=0.3,rely=0.4)
        self.sizeFullScreen.place(relx=0.3,rely=0.6)
        self.selected_dimensions = (1000, 1000)
    def size_FullScreen(self):
        self.is_fullscreen = not self.is_fullscreen  # Toggle the state
        self.window.attributes('-fullscreen', self.is_fullscreen)  # Set full screen
        self.title_label.config(font=("",40))
        self.sizeNormal.config(font=("",40),
                               height=3, width=20,)
        self.sizeBig.config(font=("",40),
                               height=3, width=20,)
        self.sizeFullScreen.config(font=("",40),
                               height=3, width=20,) 
        self.sizeNormal.place(relx=0.35,rely=0.2)
        self.sizeBig.place(relx=0.35,rely=0.4)
        self.sizeFullScreen.place(relx=0.35,rely=0.6)
        self.selected_dimensions = (self.window.winfo_screenwidth(), self.window.winfo_screenheight())
