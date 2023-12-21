import customtkinter
import loginframe, getCred, homeframe

class WelcomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, padx=10, pady=10)

        self.enterCredsButton = customtkinter.CTkButton(self, text="Enter Credentials", command=self.openLoginFrame)
        self.enterCredsButton.grid(row=0, column=0, padx=10, pady=10)

        self.fromFileButton = customtkinter.CTkButton(self, text="Login from file", command=self.retrieveFromFile)
        self.fromFileButton.grid(row=1, column=0, padx=10, pady=10)
    
    def openLoginFrame(self):
        loginFrame = loginframe.LoginFrame
        self.grid_forget()
        loginFrame(self.master)
    
    def retrieveFromFile(self):
        client_id, client_secret = getCred.getCred.pullUserLogin()
        if client_id == -1:
            print("File not found!")
            self.openLoginFrame()
        else:
            access_token, token_type = getCred.getCred.retrieveToken(client_id, client_secret)
            mainframe = homeframe.homeFrame
            self.grid_forget()
            mainframe(self.master, access_token, token_type)