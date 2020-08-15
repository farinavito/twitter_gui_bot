from tkinter import *
import tweepy

# Initial parameters
root = Tk()
root.title("TWITTER BOT")
root.minsize(width=500, height=300)

def retweet_tweet():
    try:
        tweet_want_to_retweet = retweet_entry.get()
        retweet = start_the_bot()
        retweet.retweet(id=tweet_want_to_retweet)

        success_retweeted_tweet = Label(root, text="Retweeted", fg="green")
        success_retweeted_tweet.grid(column=1, row=8)
        retweet_entry.delete(0, "end")

    except:
        unsuccess_retweeted_tweet = Label(root, text="Something went wrong!", fg="red")
        unsuccess_retweeted_tweet.grid(column=1, row=8)

def delete_tweet():
    try:
        tweet_id = tweet_delete_entry.get()
        destroy_tweet = start_the_bot()
        destroy_tweet.destroy_status(id=tweet_id)

        success_destroy_tweet = Label(root, text="tweet deleted!", fg="green")
        success_destroy_tweet.grid(column=1, row=5)
        tweet_delete_entry.delete(0, "end")

    except:
        unsuccess_destroy_tweet = Label(root, text="Something went wrong!", fg="red")
        unsuccess_destroy_tweet.grid(column=1, row=5)


def create_tweet():
    try:
        text_of_the_tweet = tweet_creation_text.get(0.0, END)
        create_tweet = start_the_bot()
        create_tweet.update_status(text_of_the_tweet)

        success_tweet = Label(root, text="You have tweeted", fg="green")
        success_tweet.grid(column=1, row=2)
        tweet_creation_text.delete(0.0, END)

    except:
        unsuccess_tweet = Label(root, text="Something went wrong", fg="red")
        unsuccess_tweet.grid(column=1, row=2)



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

    auth = tweepy.OAuthHandler(cks, cse)
    auth.set_access_token(ake, ase)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


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
access_button = Button(root, text="Start the bot", command=start_the_bot)
access_button.grid(column=0, row=8)



#Create a tweet
tweet_creation_label = Label(root, text="Create a tweet:")
tweet_creation_label.grid(column=1, row=0)
tweet_creation_text = Text(root, height=5, width=30)
tweet_creation_text.grid(column=1, row=1, padx=(10, 5))
tweet_creation_button = Button(root, text="Tweet", height=5, command=create_tweet)
tweet_creation_button.grid(column=2, row=1)


#Delete a tweet
tweet_delete_label = Label(root, text="Delete this tweet:")
tweet_delete_label.grid(column=1, row=3)
tweet_delete_entry = Entry(root, width=40)
tweet_delete_entry.grid(column=1, row=4, padx=(10, 5))
tweet_delete_button = Button(root, text="Delete", command=delete_tweet)
tweet_delete_button.grid(column=2, row=4)

#Retweet
retweet_label = Label(root, text="Retweet this tweet:")
retweet_label.grid(column=1, row=6)
retweet_entry = Entry(root, width=40)
retweet_entry.grid(column=1, row=7, padx=(10, 5))
retweet_button = Button(root, text="Retweet", command=retweet_tweet)
retweet_button.grid(column=2, row=7)





# starting the app
root.mainloop()

