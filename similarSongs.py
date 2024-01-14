import customtkinter

class similarSongs(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)