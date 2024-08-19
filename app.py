### Other imports ###
from string import ascii_letters, digits
from random import choices
import json

### Flask imports ###
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



### Database ###
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
db = SQLAlchemy(app)

# DB models #
class UrlShortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_link = db.Column(db.Text)
    shortened_link = db.Column(db.Text)

    def __repr__(self):
        return f"<UrlShortener {self.shortened_link}>"
    



### utility functions ###
def generate_random_str(length: int = 6) -> str:
    #simple do-while using python
    while True:
        '''  Code to be executed at least once '''
        #generating a new string 
        random_str = ''.join(choices(ascii_letters+digits, k=length))
        #checking if it already in the db
        obj = UrlShortener.query.filter_by(shortened_link=random_str).first()

        ''' Condition to continue or exit the loop '''
        if not obj:
            break
    #returning the new str
    return random_str




### Routing ###
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        #collecting input-url
        input_url =  request.form.get("input-url")

        # generating random str with limit of 6
        random_str = generate_random_str(length=6) #max 62

        ## save data in db ##
        obj = UrlShortener.query.filter_by(original_link=input_url).first()
        # if exist
        if obj:
            random_str = obj.shortened_link
        else:
            obj = UrlShortener(original_link=input_url, shortened_link=random_str)
            db.session.add(obj)
            db.session.commit()
        
        # creating context
        context = {"input_url":input_url, "output_url": random_str}

        return render_template("index.html", **context)
    else:
        return render_template("index.html")


@app.route("/<shortened_link>", methods=["GET"])
def link_redirect(shortened_link):
    # collecting data from db
    obj = UrlShortener.query.filter_by(shortened_link=shortened_link).first()
    
    if obj is None:
        return redirect("/")
    else:
        return redirect(obj.original_link)
    

@app.route("/reroll/", methods=["POST"])
def reroll():
    #collecting the requested short link
    old_short_link = request.get_json(force=True)["shortLink"]

    # generating new random str with limit of 6
    random_str = generate_random_str(length=6) #max 62

    # collecting obj of old_short_link
    obj = UrlShortener.query.filter_by(shortened_link = old_short_link).first()

    # updating it's shortened_link field
    obj.shortened_link = random_str
    db.session.commit()

    # creating the json structure in python
    json_dict = {
        "newShortLink":random_str
    }

    return json.dumps(json_dict)





### Activation ###
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
