from flask import Flask, render_template
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

### Routing ###
@app.route("/")
def home():
    return render_template("index.html")

### Activation ###
if __name__ == "__main__":
    app.run()
