from flask import Flask, render_template, request
import csv

app = Flask(__name__)
PER_PAGE = 20

def load_listings():
    with open("data/listings.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.route("/")
def index():
    page = 1
    listings = load_listings()
    start = (page - 1) * PER_PAGE
    end = page * PER_PAGE
    visible = listings[start:end]
    has_more = len(listings) > end
    return render_template("index.html", listings=visible, has_more=has_more)

@app.route("/listings")
def listings_ajax():
    page = int(request.args.get("page", 2))
    listings = load_listings()
    start = (page - 1) * PER_PAGE
    end = page * PER_PAGE
    visible = listings[start:end]
    return render_template("partials/listing_cards.html", listings=visible)

if __name__ == "__main__":
    app.run(debug=True)