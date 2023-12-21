import customtkinter as tk
import base64
import requests

class getCred():
    def __init__(self):
        pass
    # Function to retrieve token from saved data located in file
    def pullUserLogin():
        # Attempts to open file saved from previous session
        try:
            authFile = open("login.txt", "r")
            currline = authFile.readline()
            currline = currline.strip()
            client_id = str(currline)
            currline = authFile.readline()
            currline = currline.strip()
            client_secret = str(currline)
            authFile.close()
        except IOError:
            return -1, -1
        return client_id, client_secret

    # Function to save user's client id and secret to a file for future use
    def saveUserLogin(client_id, client_secret):
        currFile = open("login.txt", "w")
        currFile.write(str(client_id) +"\n")
        currFile.write(str(client_secret) +"\n")
        currFile.close
        print("Info saved to login.txt")
        return
        
# Function to retrieve the access token from the spotify API
    def retrieveToken(client_id, client_secret):
        # Get access token using by using retrieved client_id and client_secret variables
        auth_url = "https://accounts.spotify.com/api/token"
        # using base64, encode the client_id and client_secret to a single string and pass to auth_headers
        auth_headers = {"Authorization": "Basic " + base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
        auth_data = {"grant_type": "client_credentials"}

        # Perform request from spotify for the access token after passing headers from processed user auth data
        response = requests.post(auth_url, headers=auth_headers, data=auth_data)
        # Assign json data to a single variable for use
        response_json = response.json()

        # Checks if the access token was retrieved successfully. If not throw error
        # Assign the access token to a variable for future api calls
        try:
            access_token = response_json['access_token']
            token_type = response_json['token_type']
            success = True
            print("Success!")
        except:
            return "Invalid Client ID or Secret"
            print("Invalid Client ID or Secret")
        return access_token, token_type

    # Function to get user id and token either from a file saved from a previous login, or from user input
    def getLoginInfo():
        validSelection = False
        # Ask user if they they wish to read from a saved file or input
        while validSelection == False:
            try:
                selection = int(input("Select option:\n"
                        "1: Retrieve token from file\n"
                        "2: Input Client Secret and ID\n"))
                # Pull user login from saved data file
                if selection == 1:
                    validSelection = True
                    client_id, client_secret = getCred.pullUserLogin()
                    if client_id == -1 or client_secret == -1:
                        print("No credentials are saved")
                        selection = 2
                # Get client ID and Secret from user input and ask if they would like to save to file
                if selection == 2:
                    validSelection = True
                    client_id = input("Enter Client ID: ")
                    client_secret = input("Enter Client Secret: ")
                    saveSelection = ""
                    # Ask user if they want to save the data for future use. Throws error if not 'y' or 'n'
                    while saveSelection != "y" and saveSelection != "n":
                        try:
                            saveSelection = input("Save Client ID and Secret for future use? (y/n): ")
                            if saveSelection != "y" and saveSelection != "n":
                                raise ValueError("Value not y or n")
                            elif saveSelection == "y":
                                getCred.saveUserLogin(client_id, client_secret)
                        except ValueError as error:
                            if str(error) == "Value not y or n":
                                print("Please enter 'y' or 'n'")
                # Throws error if user selection isn't 1 or 2 to get client secret and client id from file or input
                elif selection != 1 and selection != 2:
                    raise ValueError("Invalid selection. Please enter '1' or '2'")
            except ValueError as error:
                print(str(error))
        access_token, token_type = getCred.retrieveToken(client_id, client_secret)
        return