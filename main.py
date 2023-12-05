# A software designed to hook into the Spotify API for data collection, song suggestion and other various uses
import customtkinter as tk
import getCred, autoFill

# Open welcome window and give user prompts for login
def welcomePage():
    label = tk.CTkLabel(master=welcome, text="Enter credentials or use saved login?")
    label.place(relx=0.5, rely=0.4, anchor="center")
    welcome.pack(padx=5, pady=10, fill="both", expand=True)
    button = tk.CTkButton(master=welcome, text="Enter Credentials", command=loginPage)
    button.place(relx=0.5, rely=0.5, anchor="center")
    button = tk.CTkButton(master=welcome, text="Auto-Login", command=autofillCreds)
    button.place(relx=0.5, rely=0.55, anchor="center")

# function to retrieve client id and secret from a saved previous login
def autofillCreds():
    getTokenFile = autoFill.autoFill
    client_id, client_secret = getTokenFile.getFromFile()
    print("success", client_id, client_secret)
    return client_id, client_secret

# Opens login window for user to enter credentials
def loginPage():
    global welcome
    getUserToken = getCred.getCred
    welcome.pack_forget()
    login.pack(padx=3, pady=5, fill="both", expand=True)
    
    idLabel = tk.CTkLabel(master=login, text="Enter Client ID")
    idLabel.place(relx=0.5, rely=0.35, anchor="center")
    idEntry = tk.CTkEntry(master=login, show="*****")
    idEntry.place(relx=0.5, rely=0.4, anchor="center")
    secretLabel = tk.CTkLabel(master=login, text="Enter Client Secret")
    secretLabel.place(relx=0.5, rely=0.45, anchor="center")
    secretEntry = tk.CTkEntry(master=login, show="*****")
    secretEntry.place(relx=0.5, rely=0.5, anchor="center")

    return

# Function to declare the pages being used during application use
def declarePages():
    global welcome, login
    welcome = tk.CTkFrame(master=app)
    login = tk.CTkFrame(master=app)

# Main function to perform calls to other functions
def main(): 
    global app, welcome, login

    # Create the application
    app = tk.CTk()
    app.geometry("1280x720")
    app.title("SpotiSort")
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("green")

    # Run function to declare all pages
    declarePages()

    # Call welcome page for main window
    welcomePage()

    # Begin runtime for the application window
    app.mainloop()
    return

main()


'''
frame = tk.CTkFrame(master=app)
frame.pack(pady=4, padx=12, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text="User OAuth System", font=("Sans", 24))
label.pack(pady=12, padx=10)

entry1 = tk.CTkEntry(master=frame, placeholder_text="User ID")
entry1.pack(pady=12, padx=10)

entry2 = tk.CTkEntry(master=frame, placeholder_text="User Token", show="*")
entry2.pack(pady=12, padx=10)

button = tk.CTkButton(master=frame, text="Login", command=credentials)
button.pack(pady=12, padx=10)

checkbox = tk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

'''