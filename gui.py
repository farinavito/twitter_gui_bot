from tkinter import *
import tweepy

# Initial parameters
root = Tk()
root.title("TWITTER BOT")
root.minsize(width=500, height=300)

def my_account():
    # return api
    me = start_the_bot()
    my_twitter = me.me()

    # twitter's name
    my_name_label = Label(root, text="Name:\n" + my_twitter.screen_name)
    my_name_label.grid(column=0, row=12, sticky=W)

    # twitter's description
    my_description_label = Label(root, text="Description:\n" + my_twitter.description)
    my_description_label.grid(column=0, row=13, sticky=W)

    # twitter's followers
    my_followers_count_label = Label(root, text="Followers:\n" + str(my_twitter.followers_count))
    my_followers_count_label.grid(column=0, row=14, sticky=W)


def start_the_bot():
    cks = consumer_key_entry.get()
    cse = consumer_secret_entry.get()
    ake = api_key_entry.get()
    ase = api_secret_entry.get()

    try:
        auth = tweepy.OAuthHandler(cks, cse)
        auth.set_access_token(ake, ase)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        success_status_bot = Label(root, text="Your bot is connected", fg="green")
        success_status_bot.grid(column=0, row=9, sticky=W)

        return api


    except tweepy.TweepError as e:
        error_status_bot = Label(root, text=e, fg="red")
        error_status_bot.grid(column=0, row=9)





################### GETING THE ACCESS TO THE BOT ####################################################

# consumer key
consumer_key_label = Label(root, text="Enter consumer key:")
consumer_key_label.grid(column=0, row=0)
consumer_key_entry = Entry(root)
consumer_key_entry.grid(column=0, row=1)

# consumer secret
consumer_secret_label = Label(root, text="Enter consumer secret:")
consumer_secret_label.grid(column=0, row=2)
consumer_secret_entry = Entry(root)
consumer_secret_entry.grid(column=0, row=3)

# api key
api_key_label = Label(root, text="Enter api key:")
api_key_label.grid(column=0, row=4)
api_key_entry = Entry(root)
api_key_entry.grid(column=0, row=5)

# api secret
api_secret_label = Label(root, text="Enter api secret:")
api_secret_label.grid(column=0, row=6)
api_secret_entry = Entry(root)
api_secret_entry.grid(column=0, row=7)

# access button
access_button = Button(root, text="Start your bot", command=my_account)
access_button.grid(column=0, row=8)

###########################################################################################################

# starting the app
# window = Window()
# window.mainloop()
root.mainloop()

