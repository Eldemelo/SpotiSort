import customtkinter

class homeFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_token, token_type):
        super().__init__(master)
        print(login_token, token_type)

        # Assign weight of each column to 1
        colCount = 5
        for i in range(colCount):
            self.grid_columnconfigure(i, weight=1)
        self.grid(row=0, column=0, padx=10, pady=10, sticky='NSWE')

        # Create a grid within a grid for the navigation area
        navFrame = customtkinter.CTkFrame(self)
        navFrame.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="NSWE")
        self.navHeader = customtkinter.CTkLabel(navFrame, text="Navigate")
        self.navHeader.place(relx=0.5, rely=0.1, anchor='center')

        # Create grid for the main area
        mainFrame = customtkinter.CTkFrame(self)
        mainFrame.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky="NSEW")
        self.mainHeader = customtkinter.CTkLabel(mainFrame, text="Main")
        self.mainHeader.pack(fill='x', padx=10, pady=10)
        
        return