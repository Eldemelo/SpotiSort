import customtkinter

class similarSongs(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky='NSWE')

    def hideSimilarSongsFrame(self):
        self.grid_forget()

    