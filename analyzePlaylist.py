import customtkinter
import requests
import showResults

class analyzePlaylist(customtkinter.CTkFrame):
    def __init__(self, master, login_token, token_type):
        self.login_token, self.token_type = login_token, token_type
        super().__init__(master)

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)
        
        self.analyzePlaylistHeader = customtkinter.CTkLabel(self, text="Analyze Playlist")
        self.analyzePlaylistHeader.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky='WE')

        self.urlEntry = customtkinter.CTkEntry(self)
        self.urlEntry.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky='WE')

        self.analyzePlaylistButton = customtkinter.CTkButton(self, text="Analyze", command=self.getPlaylistID)
        self.analyzePlaylistButton.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky='')
        self.resultsFrame = showResults.showResults(self)
        return

    # Function to get all the songs from the playlist entered by the user
    def getPlaylistID(self):
        currUrl = self.urlEntry.get()
        try:
            splitUrl = currUrl.split('/')
            if splitUrl[3] != "playlist": # Only allow urls of playlist type
                raise ValueError("Not a playlist")
            id = splitUrl[4]
            id = id.split('?')
            id = id[0]
            print("Success! Playlist ID:", id)
            self.getPlaylistSongs(id)
        except:
            print("Invalid URL")
    
    def getPlaylistSongs(self, playlistID):
        try:
            retrievalURL = "https://api.spotify.com/v1/playlists/" + playlistID
            token_headers = {"Authorization": "Bearer " + self.login_token}

            response = requests.get(retrievalURL, headers=token_headers)
            self.response_json = response.json()
            self.showResultsFrame()
        except:
            print("Error!")

    def showResultsFrame(self):
        self.resultsFrame.grid(row=3, column=0, columnspan=7, padx=10, pady=10, sticky='NSWE')

    def getResponse(self):
        return self.response_json