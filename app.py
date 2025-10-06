import tkinter as tk
import pymongo 

# kopplar upp sig mot min local host
client = pymongo.MongoClient("mongodb://localhost:27017")

# Skapar en ny databas som kommer heta PyChat
db = client["PyChat"] 

# Chatapplication skapar en ny collection 
messages_collection = db["messages"] 

root = tk.Tk()
root.title("PyThonChatApplication") 
root.geometry("300x300")

# Det vi vill skicka till databasen (input fält)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

def send_message():
    message = entry.get()
    if message.strip():
        messages_collection.insert_one({"text": message})
        entry.delete(0,tk.END)
        

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)


message_label = tk.Label(root, text="Messages: ", justify="left")
message_label.pack()

def fetch_messages():
    messages = messages_collection.find().sort("_id")
    message_label.config(text="Messages: \n" + "\n".join(f" - {m['text']}" for m in messages))
    root.after(2000, fetch_messages)


fetch_messages()
root.mainloop()


#Skicka till Github
#Steg1, tryck på source control ikonen till vänster
#Steg2, append changes
#Steg3, skriv en kommentar




