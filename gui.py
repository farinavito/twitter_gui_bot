from tkinter import *
import tweepy

# Initial parameters
root = Tk()

frame = Frame(root, padx=10, pady=10)
frame.grid(row=1)
frame1 = Frame(frame)
frame1.grid(column=0, row=1, padx=5, pady=5)
frame2 = Frame(frame)
frame2.grid(column=1, row=1, padx=5, pady=5)
frame3 = Frame(frame)
frame3.grid(column=2, row=1, padx=5, pady=5)
frame4 = Frame(frame)
frame4.grid(column=3, row=1, padx=5, pady=5)
root.title("TWITTER BOT")
root.size()


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
        successful_authorization_label = Label(frame1, text="Keys are alright", fg="green")
        successful_authorization_label.grid(column=0, row=8)
        return True
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
        unsuccessful_authorization_label = Label(frame1, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=8)


def my_account():
    # check for keys
    keys_alright = check_authorization()
    if keys_alright is True:

        api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
        my_twitter = api.me()
        account_in_new_window(my_twitter)

    else:
        unsuccessful_authorization_label = Label(frame1, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=8)


def number_of_retweets(get_api):
    try:
        number_of_retweets_issued = get_api.retweets_of_me
        return number_of_retweets_issued
    except AttributeError:
        no_retweets = 0
        return no_retweets

def number_of_tweets(get_api):
    number_of_tweets_and_retweets = get_api.statuses_count
    number_of_my_retweets_count = number_of_retweets(get_api)
    number_of_my_tweets_count = number_of_tweets_and_retweets - number_of_my_retweets_count
    return number_of_my_tweets_count



def account_in_new_window(get_api):
    new_window_my_account = create_new_window()
    # account's name
    my_name_label = Label(new_window_my_account, text="Name:\n" + get_api.screen_name)
    my_name_label.grid(column=0, row=1, sticky=W)

    # account's description
    my_description_label = Label(new_window_my_account, text="Description:\n" + get_api.description)
    my_description_label.grid(column=0, row=2, sticky=W)

    # account's followers
    my_followers_count_label = Label(new_window_my_account, text="Followers:\n" + str(get_api.followers_count))
    my_followers_count_label.grid(column=0, row=3, sticky=W)

    # acount follows
    my_following_count_label = Label(new_window_my_account, text="Following:\n" + str(get_api.friends_count))
    my_following_count_label.grid(column=0, row=4, sticky=W)

    # account's creation date
    date = get_api.created_at.strftime("%d-%b-%Y")
    my_creation_date_label = Label(new_window_my_account, text="Creation date:\n" + date)
    my_creation_date_label.grid(column=0, row=5, sticky=W)

    # verified account
    my_verified_account_label = Label(new_window_my_account, text="Verified account:\n" + str(get_api.verified))
    my_verified_account_label.grid(column=0, row=6, sticky=W)

    # number of tweets the account liked
    my_verified_account_label = Label(new_window_my_account,
                                      text="Number of liked tweets:\n" + str(get_api.favourites_count))
    my_verified_account_label.grid(column=0, row=7, sticky=W)

    # number of tweets the account issued
    my_verified_account_label = Label(new_window_my_account,
                                      text="Number of tweets:\n" + str(number_of_tweets(get_api)))
    my_verified_account_label.grid(column=0, row=8, sticky=W)

    #number of retweets
    my_number_retweets_label = Label(new_window_my_account,
                                      text="Number of retweets:\n" + str(number_of_retweets(get_api)))
    my_number_retweets_label.grid(column=0, row=9, sticky=W)

    # default profile image
    my_verified_account_label = Label(new_window_my_account,
                                      text="Using default profile image:\n" + str(get_api.default_profile_image))
    my_verified_account_label.grid(column=0, row=10, sticky=W)

def create_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            text_of_the_tweet = tweet_creation_text.get(0.0, END)
            api.update_status(text_of_the_tweet)

            # Create a success label
            success_tweet = Label(frame2, text="You have tweeted", fg="green")
            success_tweet.grid(column=1, row=2)
            tweet_creation_text.delete(0.0, END)
        else:
            unsuccess_tweet = Label(frame2, text="Keys are wrong", fg="red")
            unsuccess_tweet.grid(column=1, row=2)

    except:
        unsuccess_tweet = Label(frame2, text="Something went wrong", fg="red")
        unsuccess_tweet.grid(column=1, row=2)


def unretweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            unretweet_id = unretweet_entry.get()
            api.unretweet(id=unretweet_id)

            # create a success label
            success_unretweet = Label(frame2, text="Unretweeted", fg="green")
            success_unretweet.grid(column=1, row=11)
            unretweet_entry.delete(0, "end")

        else:
            unsuccessful_authorization_label = Label(frame2, text="Keys are wrong", fg="red")
            unsuccessful_authorization_label.grid(column=1, row=11)

    except:
        unsuccess_destroy_tweet = Label(frame2, text="Something went wrong!", fg="red")
        unsuccess_destroy_tweet.grid(column=1, row=11)


def delete_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            tweet_id = tweet_delete_entry.get()
            api.destroy_status(id=tweet_id)

            # Create a success label
            success_destroy_tweet = Label(frame2, text="tweet deleted!", fg="green")
            success_destroy_tweet.grid(column=1, row=5)
            tweet_delete_entry.delete(0, "end")
        else:
            unsuccessful_authorization_label = Label(frame2, text="Keys are wrong", fg="red")
            unsuccessful_authorization_label.grid(column=1, row=5)

    except:
        unsuccess_destroy_tweet = Label(frame2, text="Something went wrong!", fg="red")
        unsuccess_destroy_tweet.grid(column=1, row=5)


def retweet_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            tweet_want_to_retweet = retweet_entry.get()
            api.retweet(id=tweet_want_to_retweet)

            # Create a success label
            success_retweeted_tweet = Label(frame2, text="Retweeted", fg="green")
            success_retweeted_tweet.grid(column=1, row=8)
            retweet_entry.delete(0, "end")
        else:
            unsuccessful_authorization_label = Label(frame2, text="Keys aren't right", fg="red")
            unsuccessful_authorization_label.grid(column=1, row=8)

    except:
        unsuccess_retweeted_tweet = Label(frame2, text="Something went wrong!", fg="red")
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
            success_tweet_info_label = Label(frame4, text="Retrieved", fg="green")
            success_tweet_info_label.grid(column=4, row=2)
            tweet_info_entry.delete(0, "end")
        else:
            unsuccessful_tweet_info_label = Label(frame4, text="Keys aren't right", fg="red")
            unsuccessful_tweet_info_label.grid(column=4, row=2)
    except:
        unsuccess_tweet_info = Label(frame4, text="Something went wrong!", fg="red")
        unsuccess_tweet_info.grid(column=4, row=2)


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

    # liked by me
    tweet_info_liked_by_me = Label(tweet_info_window, text="Liked by me:\n" + str(get_api.favorited))
    tweet_info_liked_by_me.grid(column=0, row=12)

    # retweeted by me
    tweet_info_liked_by_me = Label(tweet_info_window, text="Retweeted by me:\n" + str(get_api.retweeted))
    tweet_info_liked_by_me.grid(column=0, row=13)

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

def account_info():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            get_tweet_account_entry = tweet_account_entry.get()
            account_info_user = api.get_user(screen_name=get_tweet_account_entry)

            # create a new window with info
            account_in_new_window(account_info_user)

            # create a success message
            success_tweet_info_label = Label(frame4, text="Retrieved", fg="green")
            success_tweet_info_label.grid(column=4, row=5)
            tweet_info_entry.delete(0, "end")
        else:
            unsuccessful_tweet_info_label = Label(frame4, text="Keys aren't right", fg="red")
            unsuccessful_tweet_info_label.grid(column=4, row=5)
    except:
        unsuccess_tweet_info = Label(frame4, text="Something went wrong!", fg="red")
        unsuccess_tweet_info.grid(column=4, row=5)


def like_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            liked_tweet = like_tweet_entry.get()
            api.create_favorite(id=liked_tweet)

            # create a success message
            liked_tweet_label = Label(frame2, text="Liked", fg="green")
            liked_tweet_label.grid(column=1, row=14)
            like_tweet_entry.delete(0, "end")
        else:
            unsuccessful_like_tweet_label = Label(frame2, text="Keys aren't right", fg="red")
            unsuccessful_like_tweet_label.grid(column=1, row=14)
    except:
        unsuccess_like_tweet = Label(frame2, text="Something went wrong!", fg="red")
        unsuccess_like_tweet.grid(column=1, row=14)


def unlike_tweet():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:
            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            unliked_tweet = unlike_tweet_entry.get()
            api.destroy_favorite(id=unliked_tweet)

            # create a success message
            unliked_tweet_label = Label(frame2, text="Unliked", fg="green")
            unliked_tweet_label.grid(column=1, row=17)
            unlike_tweet_entry.delete(0, "end")
        else:
            unsuccessful_unlike_tweet_label = Label(frame2, text="Keys aren't right", fg="red")
            unsuccessful_unlike_tweet_label.grid(column=1, row=17)
    except:
        unsuccess_like_tweet = Label(frame2, text="Something went wrong!", fg="red")
        unsuccess_like_tweet.grid(column=1, row=17)

def get_my_tweets_info():
    # check for keys
    keys_alright = check_authorization()
    if keys_alright is True:

        api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
        create_new_window_with_scrollbar(api)
    else:
        unsuccessful_authorization_label = Label(frame1, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=8)


def create_new_window_with_scrollbar(get_api):
    # create a new window
    new_window_all_my_tweets = create_new_window()
    # create a scrollbar
    scrollbar = Scrollbar(new_window_all_my_tweets)
    scrollbar.pack(side=RIGHT, fill=Y)
    # create a list in a scrollbar
    mylist = Listbox(new_window_all_my_tweets, width=40, yscrollcommand=scrollbar.set)
    for status in tweepy.Cursor(get_api.user_timeline).items():
        time_of_creation = status.created_at.strftime("%d-%b-%Y")
        mylist.insert(END, status.text + ", " + status.id_str + ", " + time_of_creation)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

def was_mentioned_info():
    keys_alright = check_authorization()
    if keys_alright is True:

        api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
        create_new_window_for_mentioned_info(api)
    else:
        unsuccessful_authorization_label = Label(frame1, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=0, row=8)

def create_new_window_for_mentioned_info(get_api):
    # create a new window
    new_window_all_my_tweets = create_new_window()
    # create a scrollbar
    scrollbar = Scrollbar(new_window_all_my_tweets)
    scrollbar.pack(side=RIGHT, fill=Y)
    # create a list in a scrollbar
    mylist = Listbox(new_window_all_my_tweets, width=40, yscrollcommand=scrollbar.set)
    for mention in tweepy.Cursor(get_api.mentions_timeline).items():
        time_of_creation = mention.created_at.strftime("%d-%b-%Y")
        mylist.insert(END, mention.text + ", " + mention.id_str + ", " + time_of_creation)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

def who_retweeted_this_tweet():
    keys_alright = check_authorization()
    if keys_alright is True:

        api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
        create_new_window_for_who_retweeted_this_tweet(api)

        success_retweet_label = Label(frame4, text="Retrieved", fg="green")
        success_retweet_label.grid(column=4, row=9)
        who_retweeted_this_tweet_entry.delete(0, "end")
    else:
        unsuccessful_authorization_label = Label(frame4, text="Keys aren't right", fg="red")
        unsuccessful_authorization_label.grid(column=4, row=9)


def create_new_window_for_who_retweeted_this_tweet(get_api):
    # create a new window
    new_window_all_ids = create_new_window()
    # create a scrollbar
    scrollbar = Scrollbar(new_window_all_ids)
    scrollbar.pack(side=RIGHT, fill=Y)
    #retrieve entered tweet's id
    tweets_id = who_retweeted_this_tweet_entry.get()
    # create a list in a scrollbar
    mylist = Listbox(new_window_all_ids, width=40, yscrollcommand=scrollbar.set)
    # get ids of people who retweted this
    retweeted_list = get_api.retweets(id=tweets_id)
    for retweet in retweeted_list:
        mylist.insert(END, retweet.user.screen_name)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)


def block_account():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:

            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            who_will_get_blocked = block_this_user_entry.get()
            api.create_block(screen_name=who_will_get_blocked)

            success_block_account_label = Label(frame3, text="Blocked!", fg="green")
            success_block_account_label.grid(column=3, row=2)
            block_this_user_entry.delete(0, "end")
        else:
            unsuccessful_block_label = Label(frame3, text="Keys aren't right", fg="red")
            unsuccessful_block_label.grid(column=3, row=2)
    except:
        unsuccess_block_tweet = Label(frame3, text="Something went wrong!", fg="red")
        unsuccess_block_tweet.grid(column=3, row=2)

def unblock_account():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:

            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            who_will_get_unblocked = unblock_this_user_entry.get()
            api.destroy_block(screen_name=who_will_get_unblocked)

            success_unblock_account_label = Label(frame3, text="Unblocked!", fg="green")
            success_unblock_account_label.grid(column=3, row=5)
            unblock_this_user_entry.delete(0, "end")
        else:
            unsuccessful_unblock_label = Label(frame3, text="Keys aren't right", fg="red")
            unsuccessful_unblock_label.grid(column=3, row=5)
    except:
        unsuccess_unblock_tweet = Label(frame3, text="Something went wrong!", fg="red")
        unsuccess_unblock_tweet.grid(column=3, row=5)

def mute_account():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:

            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            who_will_get_muted = mute_this_user_entry.get()
            api.create_mute(screen_name=who_will_get_muted)

            success_mute_account_label = Label(frame3, text="Muted!", fg="green")
            success_mute_account_label.grid(column=3, row=8)
            mute_this_user_entry.delete(0, "end")
        else:
            unsuccessful_mute_label = Label(frame3, text="Keys aren't right", fg="red")
            unsuccessful_mute_label.grid(column=3, row=8)
    except:
        unsuccess_mute_tweet = Label(frame3, text="Something went wrong!", fg="red")
        unsuccess_mute_tweet.grid(column=3, row=8)

def unmute_account():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:

            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            who_will_get_unmuted = unmute_this_user_entry.get()
            api.destroy_mute(screen_name=who_will_get_unmuted)

            success_unmute_account_label = Label(frame3, text="Unmuted!", fg="green")
            success_unmute_account_label.grid(column=3, row=11)
            unmute_this_user_entry.delete(0, "end")
        else:
            unsuccessful_unmute_label = Label(frame3, text="Keys aren't right", fg="red")
            unsuccessful_unmute_label.grid(column=3, row=11)
    except:
        unsuccess_unmute_tweet = Label(frame3, text="Something went wrong!", fg="red")
        unsuccess_unmute_tweet.grid(column=3, row=11)


def report_spam():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:

            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            report_account = report_spam_entry.get()
            api.report_spam(screen_name=report_account)

            success_report_spam_label = Label(frame3, text="Reported!", fg="green")
            success_report_spam_label.grid(column=3, row=14)
            report_spam_entry.delete(0, "end")
        else:
            unsuccessful_report_spam_label = Label(frame3, text="Keys aren't right", fg="red")
            unsuccessful_report_spam_label.grid(column=3, row=14)

    except:
        unsuccessful_report_spam_label = Label(frame3, text="Something went wrong!", fg="red")
        unsuccessful_report_spam_label.grid(column=3, row=14)

def comment_any_tweet_outthere():
    try:
        keys_alright = check_authorization()
        if keys_alright is True:

            api = tweepy.API(start_the_bot(), wait_on_rate_limit=True)
            tweet_id = comment_any_tweet_entry.get()
            comment_you_wrote = comment_any_tweet_text.get(0.0, END)
            name_of = api.get_status(id=tweet_id)
            api.update_status("@" + name_of.user.screen_name + " " + comment_you_wrote, tweet_id)


            success_wrote_comment_of_any_tweet_label = Label(frame4, text="Commented!", fg="green")
            success_wrote_comment_of_any_tweet_label.grid(column=4, row=16)
            comment_any_tweet_text.delete(0.0, END)
            comment_any_tweet_entry.delete(0, "end")
        else:
            unsuccess_wrote_comment_of_any_tweet_label = Label(frame4, text="Keys aren't right", fg="red")
            unsuccess_wrote_comment_of_any_tweet_label.grid(column=4, row=16)
    except:
        success_wrote_comment_of_any_tweet_label_something = Label(frame4, text="Something went wrong!", fg="red")
        success_wrote_comment_of_any_tweet_label_something.grid(column=4, row=16)





########## 1 COLUMN ###########

# consumer key
consumer_key_label = Label(frame1, text="Enter consumer key:")
consumer_key_label.grid(column=0, row=0)
consumer_key_entry = Entry(frame1)
consumer_key_entry.grid(column=0, row=1)

# consumer secret
consumer_secret_label = Label(frame1, text="Enter consumer secret:")
consumer_secret_label.grid(column=0, row=2)
consumer_secret_entry = Entry(frame1)
consumer_secret_entry.grid(column=0, row=3)

# api key
api_key_label = Label(frame1, text="Enter api key:")
api_key_label.grid(column=0, row=4)
api_key_entry = Entry(frame1)
api_key_entry.grid(column=0, row=5)

# api secret
api_secret_label = Label(frame1, text="Enter api secret:")
api_secret_label.grid(column=0, row=6)
api_secret_entry = Entry(frame1)
api_secret_entry.grid(column=0, row=7)

# access button
access_button = Button(frame1, text="Account's info", width=12, command=my_account)
access_button.grid(column=0, row=10)

# tweets issued by me
tweets_issued_by_me_button = Button(frame1, text="Get my tweets", width=12, command=get_my_tweets_info)
tweets_issued_by_me_button.grid(column=0, row=11, pady=(10, 5))

# tweets that mentioned me
tweets_mentioned_me_button = Button(frame1, text="Was mentioned", width=12, command=was_mentioned_info)
tweets_mentioned_me_button.grid(column=0, row=12, pady=5)


##### 2 COLUMN #######

# create a tweet
tweet_creation_label = Label(frame2, text="Create a tweet:")
tweet_creation_label.grid(column=1, row=0)
tweet_creation_text = Text(frame2, height=5, width=30)
tweet_creation_text.grid(column=1, row=1, padx=(10, 5))
tweet_creation_button = Button(frame2, text="Tweet", height=5, width=10, command=create_tweet)
tweet_creation_button.grid(column=2, row=1)

# delete a tweet
tweet_delete_label = Label(frame2, text="Delete this tweet:")
tweet_delete_label.grid(column=1, row=3)
tweet_delete_entry = Entry(frame2, width=40)
tweet_delete_entry.grid(column=1, row=4, padx=(10, 5))
tweet_delete_button = Button(frame2, text="Delete", width=10, command=delete_tweet)
tweet_delete_button.grid(column=2, row=4)

# retweet
retweet_label = Label(frame2, text="Retweet this tweet:")
retweet_label.grid(column=1, row=6)
retweet_entry = Entry(frame2, width=40)
retweet_entry.grid(column=1, row=7, padx=(10, 5))
retweet_button = Button(frame2, text="Retweet", width=10, command=retweet_tweet)
retweet_button.grid(column=2, row=7)

# unretweet
unretweet_label = Label(frame2, text="Unretweet this tweet:")
unretweet_label.grid(column=1, row=9)
unretweet_entry = Entry(frame2, width=40)
unretweet_entry.grid(column=1, row=10, padx=(10, 5))
unretweet__button = Button(frame2, text="Unretweet", width=10, command=unretweet)
unretweet__button.grid(column=2, row=10)

#like the tweet
like_tweet_label = Label(frame2, text="Like this tweet:")
like_tweet_label.grid(column=1, row=12)
like_tweet_entry = Entry(frame2, width=40)
like_tweet_entry.grid(column=1, row=13, padx=(10, 5))
like_tweet_button = Button(frame2, text="Like", width=10, command=like_tweet)
like_tweet_button.grid(column=2, row=13)

#unlike the tweet
unlike_tweet_label = Label(frame2, text="Unlike this tweet:")
unlike_tweet_label.grid(column=1, row=15)
unlike_tweet_entry = Entry(frame2, width=40)
unlike_tweet_entry.grid(column=1, row=16, padx=(10, 5))
unlike_tweet_button = Button(frame2, text="Unlike", width=10, command=unlike_tweet)
unlike_tweet_button.grid(column=2, row=16)


###### 3 COLUMN ########

# block someone
block_this_user_label = Label(frame3, text="Block this account:")
block_this_user_label.grid(column=3, row=0)
block_this_user_entry = Entry(frame3, width=40)
block_this_user_entry.grid(column=3, row=1, padx=(10, 5))
block_this_user_button = Button(frame3, text="Block", width=7, command=block_account)
block_this_user_button.grid(column=4, row=1)

#unblock someone
unblock_this_user_label = Label(frame3, text="Unblock this account:")
unblock_this_user_label.grid(column=3, row=3)
unblock_this_user_entry = Entry(frame3, width=40)
unblock_this_user_entry.grid(column=3, row=4, padx=(10, 5))
unblock_this_user_button = Button(frame3, text="Unblock", width=7, command=unblock_account)
unblock_this_user_button.grid(column=4, row=4)

#mute someone
mute_this_user_label = Label(frame3, text="Mute this account:")
mute_this_user_label.grid(column=3, row=6)
mute_this_user_entry = Entry(frame3, width=40)
mute_this_user_entry.grid(column=3, row=7, padx=(10, 5))
mute_this_user_button = Button(frame3, text="Mute", width=7, command=mute_account)
mute_this_user_button.grid(column=4, row=7)

# unmute someone
unmute_this_user_label = Label(frame3, text="Unmute this account:")
unmute_this_user_label.grid(column=3, row=9)
unmute_this_user_entry = Entry(frame3, width=40)
unmute_this_user_entry.grid(column=3, row=10, padx=(10, 5))
unmute_this_user_button = Button(frame3, text="Unmute", width=7, command=unmute_account)
unmute_this_user_button.grid(column=4, row=10)

# report spam
report_spam_label = Label(frame3, text="Report spam for this account:")
report_spam_label.grid(column=3, row=12)
report_spam_entry = Entry(frame3, width=40)
report_spam_entry.grid(column=3, row=13, padx=(10, 5))
report_spam_button = Button(frame3, text="Report", width=7, command=report_spam)
report_spam_button.grid(column=4, row=13)

####### 4 COLUMN #########

# tweet's info
tweet_info_label = Label(frame4, text="Retrieve this tweet's info:")
tweet_info_label.grid(column=4, row=0)
tweet_info_entry = Entry(frame4, width=40)
tweet_info_entry.grid(column=4, row=1, padx=(10, 5))
tweet_info_button = Button(frame4, text="Info", width=8, command=retrieve_info)
tweet_info_button.grid(column=5, row=1)

# account info
tweet_account_label = Label(frame4, text="Retrieve this account's info:")
tweet_account_label.grid(column=4, row=3)
tweet_account_entry = Entry(frame4, width=40)
tweet_account_entry.grid(column=4, row=4, padx=(10, 5))
tweet_account_button = Button(frame4, text="Info", width=8, command=account_info)
tweet_account_button.grid(column=5, row=4)

#who retweeted this tweet
who_retweeted_this_tweet_label = Label(frame4, text="Who retweeted this tweet:")
who_retweeted_this_tweet_label.grid(column=4, row=6)
who_retweeted_this_tweet_entry = Entry(frame4, width=40)
who_retweeted_this_tweet_entry.grid(column=4, row=7, padx=(10, 5))
who_retweeted_this_tweet_button = Button(frame4, text="Get", width=8, command=who_retweeted_this_tweet)
who_retweeted_this_tweet_button.grid(column=5, row=7)

# comment any tweet
comment_any_tweet = Label(frame4, text="Comment any tweet")
comment_any_tweet.grid(column=4, row=9)
comment_any_tweet_label = Label(frame4, text="Tweet ID:")
comment_any_tweet_label.grid(column=4, row=10)
comment_any_tweet_entry = Entry(frame4, width=40)
comment_any_tweet_entry.grid(column=4, row=11, padx=(10, 5))

comment_any_tweet_hashtag_label = Label(frame4, text="If tweet contains hashtag bellow(optional):")
comment_any_tweet_hashtag_label.grid(column=4, row=12)
comment_any_tweet_hashtag_entry = Entry(frame4, width=40)
comment_any_tweet_hashtag_entry.grid(column=4, row=13, padx=(10, 5))

comment_any_tweet_comment = Label(frame4, text="Your comment:")
comment_any_tweet_comment.grid(column=4, row=14)
comment_any_tweet_text = Text(frame4, height=5, width=30)
comment_any_tweet_text.grid(column=4, row=15)
comment_any_tweet_button = Button(frame4, text="Comment", width=8, command=comment_any_tweet_outthere)
comment_any_tweet_button.grid(column=5, row=15)



# comment tweet on my timeline with specific hashtag
# comment_tweet_on_mytimeline_hashtags = Label(frame3, text="Comment any tweet")
# comment_tweet_on_mytimeline_hashtags.grid(column=3, row=15)
# comment_tweet_on_mytimeline_hashtags_label = Label(frame3, text="Tweet ID:")
# comment_tweet_on_mytimeline_hashtags_label.grid(column=3, row=16)
# comment_tweet_on_mytimeline_hashtags_entry = Entry(frame3, width=40)
# comment_tweet_on_mytimeline_hashtags_entry.grid(column=3, row=17, padx=(10, 5))
# comment_tweet_on_mytimeline_hashtags_comment = Label(frame3, text="Your comment:")
# comment_tweet_on_mytimeline_hashtags_comment.grid(column=3, row=18)
# comment_tweet_on_mytimeline_hashtags_text = Text(frame3, height=5, width=30)
# comment_tweet_on_mytimeline_hashtags_text.grid(column=3, row=19)
# comment_tweet_on_mytimeline_hashtags_button = Button(frame3, text="Comment", command=comment_any_tweet_outthere)
# comment_tweet_on_mytimeline_hashtags_button.grid(column=4, row=19)




# starting the app
root.mainloop()