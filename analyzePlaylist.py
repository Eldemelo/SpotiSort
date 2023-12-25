import customtkinter
import homeframe

class analyzePlaylist(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        print('test')
        analyzePlaylistFrame = customtkinter.CTkFrame(self)
        analyzePlaylistFrame.grid(row=0, column=2, columnspan=6, padx=10, pady=10, sticky='NSWE')
        analyzePlaylistURLEntry = customtkinter.CTkEntry(homeframe.analyzePlaylistFrame)
        analyzePlaylistURLEntry.grid(row = 0, column=0)
        analyzePlaylistFrame = customtkinter.CTkFrame(self)
        analyzePlaylistFrame.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky='NSWE')
        analyzePlaylistURLEntry = customtkinter.CTkEntry(analyzePlaylistFrame)
        analyzePlaylistURLEntry.grid(row = 0, colum=0)

        return self

    def getPlaylistSongs(songURL):
        pass