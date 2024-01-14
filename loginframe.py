import customtkinter
import getCred, homeframe

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, padx=10, pady=10)

        # Create the entry for the user's Client ID
        self.idLabel = customtkinter.CTkLabel(self, text="Client ID:")
        self.idLabel.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.idEntry = customtkinter.CTkEntry(self)
        self.idEntry.grid(row=0, column=1, padx=10, pady=10)

        # Create the entry for the user's Client Secret
        self.secretLabel = customtkinter.CTkLabel(self, text="Client Secret:")
        self.secretLabel.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.secretEntry = customtkinter.CTkEntry(self, show="*")
        self.secretEntry.grid(row=1, column=1, padx=10, pady=10)

        # Button to process the entered Client ID and Secret
        self.loginButton = customtkinter.CTkButton(self, text="Login", command=self.processCreds)
        self.loginButton.grid(row=3, column=0, columnspan=2, sticky="EW", padx=10, pady=10)

        return
    
    # Method to attempt to retrieve the user's auth token from spotify's API
    def processCreds(self):
        access_token = ""
        token_type = ""
        try:
            access_token, token_type = getCred.getCred.retrieveToken(
                self.idEntry.get(),
                self.secretEntry.get())
            mainframe = homeframe.homeFrame
            self.grid_forget()
            mainframe(self.master, access_token, token_type)

        except:
            print("Invalid Client ID or Secretsss")
        return
