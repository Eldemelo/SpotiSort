import customtkinter

class homeFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_token, token_type):
        super().__init__(master)
        print(login_token, token_type)
        self.grid(row=0, column=0, padx=10, pady=10, sticky='NSWE')

        self.navHeader = customtkinter.CTkLabel(self, text="Navigate")
        self.navHeader.grid(row=0, column=0, padx=10, pady=10)

        self.mainHeader = customtkinter.CTkLabel(self, text="")
        self.mainHeader.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        
        return