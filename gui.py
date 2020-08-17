from tkinter import *
import tweepy

# Initial parameters
root = Tk()
root.title("TWITTER BOT")
root.minsize(width=500, height=300)


def start_the_bot():
    cks = consumer_key_entry.get()
    cse = consumer_secret_entry.get()
    ake = api_key_entry.get()
    ase = api_secret_entry.get()

    auth = tweepy.OAuthHandler(cks, cse)
    auth.set_access_token(ake, ase)
    return auth

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


def my_account():
    # check for keys
    keys_alright = check_authorization()
    if keys_alright is True:
        new_window_my_account = create_new_window()
        api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
        my_twitter = api.me()

        # account's name
        my_name_label = Label(new_window_my_account, text="Name:\n" + my_twitter.screen_name)
        my_name_label.grid(column=0, row=1, sticky=W)

        # account's description
        my_description_label = Label(new_window_my_account, text="Description:\n" + my_twitter.description)
        my_description_label.grid(column=0, row=2, sticky=W)

        # account's followers
        my_followers_count_label = Label(new_window_my_account, text="Followers:\n" + str(my_twitter.followers_count))
        my_followers_count_label.grid(column=0, row=3, sticky=W)

        # acount follows
        my_following_count_label = Label(new_window_my_account, text="Following:\n" + str(my_twitter.friends_count))
        my_following_count_label.grid(column=0, row=4, sticky=W)

        # account's creation date
        date = my_twitter.created_at.strftime("%d-%b-%Y")
        my_creation_date_label = Label(new_window_my_account, text="Creation date:\n" + date)
        my_creation_date_label.grid(column=0, row=5, sticky=W)

        # verified account
        my_verified_account_label = Label(new_window_my_account, text="Verified account:\n" + str(my_twitter.verified))
        my_verified_account_label.grid(column=0, row=6, sticky=W)

        # number of tweets the account liked
        my_verified_account_label = Label(new_window_my_account,
                                          text="Number of liked tweets:\n" + str(my_twitter.favourites_count))
        my_verified_account_label.grid(column=0, row=7, sticky=W)

        # number of tweets the account issued
        my_verified_account_label = Label(new_window_my_account,
                                          text="Number of issued tweets:\n" + str(my_twitter.statuses_count))
        my_verified_account_label.grid(column=0, row=8, sticky=W)

        # default profile image
        my_verified_account_label = Label(new_window_my_account,
                                          text="Using default profile image:\n" + str(my_twitter.default_profile_image))
        my_verified_account_label.grid(column=0, row=9, sticky=W)
    else:
        unsuccessful_authorization_label = Label(root, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=10)


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


def unretweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            unretweet_id = unretweet_entry.get()
            api.unretweet(id=unretweet_id)

            # create a success label
            success_unretweet = Label(root, text="Unretweeted", fg="green")
            success_unretweet.grid(column=1, row=11)
            unretweet_entry.delete(0, "end")

        else:
            unsuccessful_authorization_label = Label(root, text="Keys are wrong", fg="red")
            unsuccessful_authorization_label.grid(column=1, row=11)

    except:
        unsuccess_destroy_tweet = Label(root, text="Something went wrong!", fg="red")
        unsuccess_destroy_tweet.grid(column=1, row=11)


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


def retrieve_info():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            get_tweet_info_entry = tweet_info_entry.get()
            tweet_info = api.get_status(id=get_tweet_info_entry)

            # create a new window with info
            show_tweet_info(tweet_info)

            # create a success message
            success_tweet_info_label = Label(root, text="Retrieved", fg="green")
            success_tweet_info_label.grid(column=3, row=2)
            tweet_info_entry.delete(0, "end")
        else:
            unsuccessful_tweet_info_label = Label(root, text="Keys aren't right", fg="red")
            unsuccessful_tweet_info_label.grid(column=3, row=2)
    except:
        unsuccess_tweet_info = Label(root, text="Something went wrong!", fg="red")
        unsuccess_tweet_info.grid(column=3, row=2)


def show_tweet_info(get_api):
    tweet_info_window = create_new_window()
    # tweet's id
    tweet_info_id = Label(tweet_info_window, text="Tweet's id:\n" + str(get_api.id_str))
    tweet_info_id.grid(column=0, row=0)

    # tweet's date creation
    tweet_info_date = get_api.created_at.strftime("%d-%b-%Y")
    my_creation_date_label = Label(tweet_info_window, text="Creation date:\n" + tweet_info_date)
    my_creation_date_label.grid(column=0, row=1)

    # Tweet's text
    tweet_info_text_label = Label(tweet_info_window, text="Text:\n" + get_api.text)
    tweet_info_text_label.grid(column=0, row=2)

    # tweet's source
    tweet_info_source = Label(tweet_info_window, text="Tweet's source:\n" + get_api.source)
    tweet_info_source.grid(column=0, row=3)

    # is tweet truncated
    tweet_info_truncated = Label(tweet_info_window, text=" Is tweet truncated:\n" + str(get_api.truncated))
    tweet_info_truncated.grid(column=0, row=4)

    # is this quoted tweet
    tweet_info_quoted = Label(tweet_info_window, text="Is this a quoted tweet:\n" + str(get_api.is_quote_status))
    tweet_info_quoted.grid(column=0, row=5)

    # number of times this tweet has been retweeted
    tweet_info_retweeted_count = Label(tweet_info_window, text="Retweeted by:\n" + str(get_api.retweet_count))
    tweet_info_retweeted_count.grid(column=0, row=6)

    # number of times this tweet has been liked
    tweet_info_liked_count = Label(tweet_info_window, text="Liked by:\n" + str(get_api.favorite_count))
    tweet_info_liked_count.grid(column=0, row=7)

    try:
        # retriveing tweet's entities
        entities_ = get_api.entities
        # retriveing user mentions from a tweet
        get_user_mentions_from_tweet(entities_, tweet_info_window)
        # retriveing hashtags from a tweet
        get_hashtags_from_tweet(entities_, tweet_info_window)

        status_id = get_api.in_reply_to_status_id_st
        screen_name = get_api.in_reply_to_screen_name

        # to which tweet is replying
        tweet_info_replying_id = Label(tweet_info_window,
                                       text="This is a reply to tweet:\n" + status_id)
        tweet_info_replying_id.grid(column=0, row=8)
        # to which screen name is this tweet replying
        tweet_info_replying_screen_name = Label(tweet_info_window,
                                                text="This a reply to:\n" + screen_name)
        tweet_info_replying_screen_name.grid(column=0, row=9)

    except AttributeError:
        # if searched tweet wasn't a reply
        unsuccess_tweet_info_replying_id = Label(tweet_info_window, text="This tweet wasn't a reply")
        unsuccess_tweet_info_replying_id.grid(column=0, row=8)


def get_user_mentions_from_tweet(entities_, tweet_info_window):
    try:
        user_mentions_all = entities_.user_mentions
        success_tweet_info_user_mentions = Label(tweet_info_window,
                                            text="User mentions:\n" + user_mentions_all)
        success_tweet_info_user_mentions.grid(column=0, row=11)
        return success_tweet_info_user_mentions

    except AttributeError:
        unsuccess_tweet_info_user_mentions = Label(tweet_info_window, text="No one has been mentioned")
        unsuccess_tweet_info_user_mentions.grid(column=0, row=11)
        return unsuccess_tweet_info_user_mentions

def get_hashtags_from_tweet(entities_, tweet_info_window):
    try:
        hashtags_all = entities_.hashtags
        success_tweet_info_hashtags = Label(tweet_info_window,
                                            text="Hashtags:\n" + hashtags_all)
        success_tweet_info_hashtags.grid(column=0, row=10)
        return success_tweet_info_hashtags

    except AttributeError:
        unsuccess_tweet_info_hashtags = Label(tweet_info_window, text="This tweet has no hashtags")
        unsuccess_tweet_info_hashtags.grid(column=0, row=9)
        return unsuccess_tweet_info_hashtags

def create_new_window():
    window = Toplevel()
    window.minsize(width=250, height=300)
    return window

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

# unretweet
unretweet_label = Label(root, text="Unretweet this tweet:")
unretweet_label.grid(column=1, row=9)
unretweet_entry = Entry(root, width=40)
unretweet_entry.grid(column=1, row=10, padx=(10, 5))
unretweet__button = Button(root, text="Unretweet", command=unretweet)
unretweet__button.grid(column=2, row=10)

# tweet's info
tweet_info_label = Label(root, text="Retrieve this tweet's info:")
tweet_info_label.grid(column=3, row=0)
tweet_info_entry = Entry(root, width=40)
tweet_info_entry.grid(column=3, row=1, padx=(10, 5))
tweet_info_button = Button(root, text="Info", command=retrieve_info)
tweet_info_button.grid(column=4, row=1)

# starting the app
root.mainloop()

