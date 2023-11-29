class autoFill:
    global client_id, client_secret
    def __init__():
        return

    def getFromFile():
        print("testing")
        # Attempts to open file saved from previous session
        try:
            authFile = open("login.txt", "r")
            currline = authFile.readline()
            currline = currline.strip()
            client_id = currline
            currline = authFile.readline()
            currline = currline.strip()
            client_secret = currline
            authFile.close()
        except IOError:
            return -1, -1
        print("success")
        return client_id, client_secret
    
    def getClientId():
        return client_id
    
    def getClientSecret():
        return client_secret
