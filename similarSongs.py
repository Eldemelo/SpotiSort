import customtkinter

class similarSongs(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

    def hideSimilarSongsFrame(self):
        self.grid_forget()

    