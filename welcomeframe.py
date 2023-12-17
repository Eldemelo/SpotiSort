import customtkinter
import loginframe

class WelcomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, padx=10, pady=10)

        self.enterCredsButton = customtkinter.CTkButton(self, text="Enter Credentials", command=self.openLoginFrame)
        self.enterCredsButton.grid(row=0, column=0, padx=10, pady=10)

        self.fromFileButton = customtkinter.CTkButton(self, text="Login from file")
        self.fromFileButton.grid(row=1, column=0, padx=10, pady=10)

        return
    
    def openLoginFrame(self):
        loginFrame = loginframe.LoginFrame
        self.grid_forget()
        loginFrame(self.master)
        return