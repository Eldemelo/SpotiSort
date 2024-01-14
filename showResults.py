import customtkinter

class showResults(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)
        button = customtkinter.CTkButton(self)
        button.grid()
        return