from flask import Flask
from flask import request

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<p>Hi,I am @w0x7ce </p><p1><a href="https://me.w0x7ce.eu">Blog</a></p1>'


############################################# Twitter Block Begin #############################################
import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = "AAAAAAAAAAAAAAAAAAAAADP8bQEAAAAA6LsaDyCf9ez11v66luvQta5%2BSR0%3DiYLU3bbDVfByuVG6pyJ1a0gRGC6TPyRDw2CNv9uHRoow3xmPkL"

def create_url(twitter_id):
    # Replace with user ID below
    user_id = twitter_id
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at","tweet.fields":"text","max_results":20}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

############################################# Twitter Block End #############################################

############################################# Twitter Get User Begin #######################################
def create_id_url(twitter_name):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=%s"%str(twitter_name)
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url

def connect_to_endpoint_id(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

############################################  Twitter Get User End ######################################

from markupsafe import escape

@app.route('/tweet/<username>')
def show_user_profile(username):
    url = create_url(username)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    #return json.dumps(json_response, indent=4, sort_keys=True)
    return json_response 

@app.route("/tweet")
def tweet():
    url = create_url(2244994945)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    #return json.dumps(json_response, indent=4, sort_keys=True)
    return json_response 

@app.route('/tweet/get_id_by_name/<twitter_name>')
def get_user_id_by_name(twitter_name):
    url_id = create_id_url(twitter_name)
    json_response = connect_to_endpoint_id(url_id)
#     print(json.dumps(json_response, indent=4, sort_keys=True))
    return json_response

@app.route('/download/<video_id>')
def download_u2b(video_id):
    video_url = "https://youtu.be/"+video_id
    os_exec = "you-get %s"%video_url
    aa = os.system(os_exec)
    return aa

import feedparser
import json
@app.route('/rss/rthk')
def get_rthk():
    NewsFeed = feedparser.parse("https://rthk.hk/rthk/news/rss/c_expressnews_greaterchina.xml")
#    return json.dumps(NewsFeed.entries,ensure_ascii=False).replace("[","").replace("]","")
    return NewsFeed

@app.route('/rss/hket')
def get_hket():
    NewsFeed_hket = feedparser.parse("https://www.hket.com/rss/finance")
    return NewsFeed_hket

@app.route('/rss/url/<url>')
def get_rss_url(url):
    url = "https://w0x7ce-rss.herokuapp.com/"+url
    NewsFeed_url =  feedparser.parse(url)
    return NewsFeed_url

@app.route('/hub')
def get_hub():
    return '<p>使用方式 url 后加路径即可 </p><p1><a href="https://docs.rsshub.app/">使用文档</a></p1>'


@app.route('/hub/',methods=['GET','POST'])
def get_gg_data():
    #gg_data=""
    #gg_data.append(request.args.get("url"))
    gg_url = "https://w0x7ce-rss.herokuapp.com/"+ request.args.get("url")
    try:
        kk = feedparser.parse(gg_url)
        return kk
    except:
        return gg_url

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
