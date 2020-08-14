from tkinter import *
import tweepy

# Initial parameters
root = Tk()
# root.configure(bg='grey')
root.title("TWITTER BOT")
root.geometry("500x300")

initials = ["consumer_key_entry", "consumer_secret_entry", "api_key_entry", "api_secret_entry"]

def start_the_bot():
    cks = consumer_key_entry.get()
    cse = consumer_secret_entry.get()
    ake = api_key_entry.get()
    ase = api_secret_entry.get()

    try:
        auth = tweepy.OAuthHandler(cks, cse)
        auth.set_access_token(ake, ase)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        global api

        success_status_bot = Label(root, text="Your bot is connected", fg="green")
        success_status_bot.pack()

    except tweepy.TweepError as e:

        error_status_bot = Label(root, text=e, fg="red")
        error_status_bot.pack()


################### GETING THE ACCESS TO THE BOT ####################################################

# consumer key
consumer_key_label = Label(root, text="Enter consumer key:")
consumer_key_label.pack()
consumer_key_entry = Entry(root)
consumer_key_entry.pack()

# consumer secret
consumer_secret_label = Label(root, text="Enter consumer secret:")
consumer_secret_label.pack()
consumer_secret_entry = Entry(root)
consumer_secret_entry.pack()

# api key
api_key_label = Label(root, text="Enter api key:")
api_key_label.pack()
api_key_entry = Entry(root)
api_key_entry.pack()

# api secret
api_secret_label = Label(root, text="Enter api secret:")
api_secret_label.pack()
api_secret_entry = Entry(root)
api_secret_entry.pack()

# access button
access_button = Button(root, text="Start your bot", command=start_the_bot)
access_button.pack()

###########################################################################################################

# starting the app
root.mainloop()