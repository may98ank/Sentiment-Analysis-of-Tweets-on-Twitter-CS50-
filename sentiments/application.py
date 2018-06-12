from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    tweetAnalyzer = Analyzer( "positive-words.txt","negative-words.txt")
    positive, negative, neutral = 0.0, 0.0, 0.0
    pos, neg, neu = 0, 0, 0
    for tweet in tweets:
        score = tweetAnalyzer.analyze(tweet)
        if score > 0:
            pos += 1
        elif score < 0:
            neg += 1
        else:
            neu += 1
    positive = (pos/len(tweets))*100
    negative = (neg/len(tweets))*100
    neutral = (neu/len(tweets))*100
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
