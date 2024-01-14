import customtkinter
import analyzePlaylist, similarSongs

class homeFrame(customtkinter.CTkFrame):
    login_token, token_type = "",""
    def __init__(self, master, login_token, token_type):
        self.login_token = login_token
        self.token_type = token_type
        super().__init__(master)
        print(login_token, token_type)

        # Assign weight of each column to 1
        colCount = 5
        for i in range(colCount):
            self.grid_columnconfigure(i, weight=1)
        self.grid(row=0, column=0, padx=10, pady=10, sticky='NSWE')

        # Create a grid within a grid for the navigation area
        self.grid_columnconfigure(0, weight=0)
        navFrame = customtkinter.CTkFrame(self)
        navFrame.grid(row=0, column=0, padx=10, pady=10, sticky="NSWE")
        self.navHeader = customtkinter.CTkLabel(navFrame, text="Navigate")
        self.navHeader.grid(padx=20, pady=10)

        # Create grid for the main area
        self.instantiateFrames()

        # Navigation buttons
        self.analyzePlaylistNavButton = customtkinter.CTkButton(navFrame, text="Analyze Playlist", command=self.showAnalyzePlaylistFrame)
        self.analyzePlaylistNavButton.grid(row=2, column=0, padx=10, pady=10)
        self.similarSongNavButton = customtkinter.CTkButton(navFrame, text="Similar Songs", command=self.showSimilarSongsFrame)
        self.similarSongNavButton.grid(row=3, column=0, padx=10, pady=10)
        return
    
    # Function to hide all frames
    def hideFrames(self):
        analyzePlaylistFrame.grid_forget()
        showSimilarSongsFrame.grid_forget()

    # Function to instantiate all frames for use
    def instantiateFrames(self):
        global analyzePlaylistFrame, showSimilarSongsFrame
        analyzePlaylistFrame = analyzePlaylist.analyzePlaylist(self, self.login_token, self.token_type)
        showSimilarSongsFrame = similarSongs.similarSongs(self)

    # Functions to show different frames
    def showAnalyzePlaylistFrame(self):
        self.hideFrames()
        analyzePlaylistFrame.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky='NSWE')
        
    def showSimilarSongsFrame(self):
        self.hideFrames()
        showSimilarSongsFrame.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky='NSWE')
