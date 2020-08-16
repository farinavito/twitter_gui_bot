from tkinter import *

import tweepy

# Initial parameters
root = Tk()
root.title("TWITTER BOT")
root.minsize(width=500, height=300)

def check_authorization():
    try:
        start_the_bot().get_authorization_url()
        successful_authorization_label = Label(root, text="Keys are alright", fg="green")
        successful_authorization_label.grid(column=0, row=10)
        return True
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
        unsuccessful_authorization_label = Label(root, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=10)


def retweet_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            tweet_want_to_retweet = retweet_entry.get()
            api.retweet(id=tweet_want_to_retweet)
            # Create a success label
            success_retweeted_tweet = Label(root, text="Retweeted", fg="green")
            success_retweeted_tweet.grid(column=1, row=8)
            retweet_entry.delete(0, "end")
        else:
            unsuccessful_authorization_label = Label(root, text="Keys aren't right", fg="red")
            unsuccessful_authorization_label.grid(column=1, row=8)

    except:
        unsuccess_retweeted_tweet = Label(root, text="Something went wrong!", fg="red")
        unsuccess_retweeted_tweet.grid(column=1, row=8)

def delete_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            tweet_id = tweet_delete_entry.get()
            api.destroy_status(id=tweet_id)
            # Create a success label
            success_destroy_tweet = Label(root, text="tweet deleted!", fg="green")
            success_destroy_tweet.grid(column=1, row=5)
            tweet_delete_entry.delete(0, "end")
        else:
            unsuccessful_authorization_label = Label(root, text="Keys are wrong", fg="red")
            unsuccessful_authorization_label.grid(column=1, row=5)

    except:
        unsuccess_destroy_tweet = Label(root, text="Something went wrong!", fg="red")
        unsuccess_destroy_tweet.grid(column=1, row=5)


def create_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            text_of_the_tweet = tweet_creation_text.get(0.0, END)
            api.update_status(text_of_the_tweet)
            # Create a success label
            success_tweet = Label(root, text="You have tweeted", fg="green")
            success_tweet.grid(column=1, row=2)
            tweet_creation_text.delete(0.0, END)
        else:
            unsuccess_tweet = Label(root, text="Keys are wrong", fg="red")
            unsuccess_tweet.grid(column=1, row=2)

    except:
        unsuccess_tweet = Label(root, text="Something went wrong", fg="red")
        unsuccess_tweet.grid(column=1, row=2)



def my_account():
    # check for keys
    keys_alright = check_authorization()
    if keys_alright is True:
        new_window = Toplevel()
        api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
        my_twitter = api.me()
        # account's name
        my_name_label = Label(new_window, text="Name:\n" + my_twitter.screen_name)
        my_name_label.grid(column=0, row=1, sticky=W)

        # account's description
        my_description_label = Label(new_window, text="Description:\n" + my_twitter.description)
        my_description_label.grid(column=0, row=2, sticky=W)

        # account's followers
        my_followers_count_label = Label(new_window, text="Followers:\n" + str(my_twitter.followers_count))
        my_followers_count_label.grid(column=0, row=3, sticky=W)

        # acount follows
        my_following_count_label = Label(new_window, text="Following:\n" + str(my_twitter.friends_count))
        my_following_count_label.grid(column=0, row=5, sticky=W)

        # account's location


        # account's creation date
        date = my_twitter.created_at.strftime("%d-%b-%Y")
        my_creation_date_label = Label(new_window, text="Creation date:\n" + date)
        my_creation_date_label.grid(column=0, row=6, sticky=W)

        # verified account
        my_verified_account_label = Label(new_window, text="Verified account:\n" + str(my_twitter.verified))
        my_verified_account_label.grid(column=0, row=7, sticky=W)

        # number of tweets the account liked
        my_verified_account_label = Label(new_window, text="Number of liked tweets:\n" + str(my_twitter.favourites_count))
        my_verified_account_label.grid(column=0, row=8, sticky=W)

        # number of tweets the account issued
        my_verified_account_label = Label(new_window, text="Number of issued tweets:\n" + str(my_twitter.statuses_count))
        my_verified_account_label.grid(column=0, row=9, sticky=W)

        # default profile image
        my_verified_account_label = Label(new_window,
                                          text="Using default profile image:\n" + str(my_twitter.default_profile_image))
        my_verified_account_label.grid(column=0, row=10, sticky=W)
    else:
        unsuccessful_authorization_label = Label(root, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=10)




def start_the_bot():
    cks = consumer_key_entry.get()
    cse = consumer_secret_entry.get()
    ake = api_key_entry.get()
    ase = api_secret_entry.get()

    auth = tweepy.OAuthHandler(cks, cse)
    auth.set_access_token(ake, ase)
    return auth


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
access_button = Button(root, text="Account's info", command=my_account)
access_button.grid(column=0, row=8)

# create a tweet
tweet_creation_label = Label(root, text="Create a tweet:")
tweet_creation_label.grid(column=1, row=0)
tweet_creation_text = Text(root, height=5, width=30)
tweet_creation_text.grid(column=1, row=1, padx=(10, 5))
tweet_creation_button = Button(root, text="Tweet", height=5, command=create_tweet)
tweet_creation_button.grid(column=2, row=1)

# delete a tweet
tweet_delete_label = Label(root, text="Delete this tweet:")
tweet_delete_label.grid(column=1, row=3)
tweet_delete_entry = Entry(root, width=40)
tweet_delete_entry.grid(column=1, row=4, padx=(10, 5))
tweet_delete_button = Button(root, text="Delete", command=delete_tweet)
tweet_delete_button.grid(column=2, row=4)

# retweet
retweet_label = Label(root, text="Retweet this tweet:")
retweet_label.grid(column=1, row=6)
retweet_entry = Entry(root, width=40)
retweet_entry.grid(column=1, row=7, padx=(10, 5))
retweet_button = Button(root, text="Retweet", command=retweet_tweet)
retweet_button.grid(column=2, row=7)

# starting the app
root.mainloop()

