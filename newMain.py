import customtkinter
import loginframe, welcomeframe

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Assign information to the window
        self.title("SpotiSort")
        self.geometry("1280x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Open the welcome frame
        self.welcome_frame = welcomeframe.WelcomeFrame(self)

app = App()
app.mainloop()