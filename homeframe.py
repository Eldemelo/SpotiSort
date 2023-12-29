import customtkinter
import analyzePlaylist, similarSongs

class homeFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_token, token_type):
        global mainFrame
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
        self.showMainFrame()

        # Navigation buttons
        mainFrame.analyzePlaylistNavButton = customtkinter.CTkButton(navFrame, text="Analyze Playlist", command=self.showAnalyzePlaylistFrame)
        mainFrame.analyzePlaylistNavButton.grid(row=2, column=0, padx=10, pady=10)
        self.similarSongNavButton = customtkinter.CTkButton(navFrame, text="Similar Songs", command=self.showSimilarSongsFrame)
        self.similarSongNavButton.grid(row=3, column=0, padx=10, pady=10)

        return
    
    def forgetFrames(self):
        mainFrame.grid_forget()
        analyzePlaylist.analyzePlaylist.hideAnalyzePlaylist()
        similarSongs.similarSongs.hideSimilarSongsFrame()

    def showMainFrame(self):
        global mainFrame
        mainFrame = customtkinter.CTkFrame(self)
        mainFrame.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky="NSEW")
        self.mainHeader = customtkinter.CTkLabel(mainFrame, text="Main")
        self.mainHeader.pack(fill='x', padx=10, pady=10)

    def showAnalyzePlaylistFrame(self):
        global analyzePlaylistFrame
        analyzePlaylistFrame = analyzePlaylist
        self.forgetFrames()
        analyzePlaylistFrame.analyzePlaylist(self)

    def showSimilarSongsFrame(self):
        global similarSongsFrame
        similarSongsFrame = similarSongs
        self.forgetFrames()
        similarSongsFrame.similarSongs(self)
