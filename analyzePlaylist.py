import customtkinter

class analyzePlaylist(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky='NSWE')

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)
        
        self.analyzePlaylistHeader = customtkinter.CTkLabel(self, text="Analyze Playlist")
        self.analyzePlaylistHeader.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky='WE')

        self.urlEntry = customtkinter.CTkEntry(self)
        self.urlEntry.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky='WE')

        self.analyzePlaylistButton = customtkinter.CTkButton(self, text="Analyze", command=self.getPlaylistSongs)
        self.analyzePlaylistButton.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky='')
        return
    
    def hideAnalyzePlaylist(self):
        self.grid_forget()

    # Function to get all the songs from the playlist entered by the user
    def getPlaylistSongs(self):
        currUrl = self.urlEntry.get()
        try:
            splitUrl = currUrl.split('/')
            id = splitUrl[4]
            id = id.split('?')
            id = id[0]
            print("Success! Playlist ID:", id)
        except:
            print("Invalid URL")