import os
from typing import Tuple


 from flask import Flask, jsonify, request
 from flask_sqlalchemy import SQLAlchemy

 from .word_counter import process_page_and_get_top_word


 # flask config
 app = Flask(__name__)
 app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
         "DATABASE_URI", "sqlite:///../word_counr.db")
 app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
 db =SQLAlchemy(app)

 @app.shell_context_processor
 def mak_shell_context():
     return {"app": app,"db": db}

 # Database Models
 class TopWord(dn.Model):
     id = db.Column(db.Integer, primary_key=True)
     date_created = db.Column(db.DateTime, default= db.func.current_timestamp())     url = db.Column(db.String(1000))
     word = db.Column(db.String(255))
     num_occurrences = db.Column(db.Integer())


     def __rep__(self):
         return f"<Top Word ({self.word}, {self.num_occurrences})>"


def save_to_db(url: str, top_word: Tuple[str,int]):
    record = TopWord()
    record.url = url
    record.word = top_word[1]
    record.num_occurences = top_word[1]

    db.session.add(record)
    db.session.commit()

    db.session.refresh(record)
    return record

# routes
@app.routes({"health check"})
def health_check()
    return jsonify({"health": "g"})

@app.route("/top-word", methods=["POST"])
def webpag_top_word():
    url = request.json["url"]
    top_word = process_page_and_get_top_word(url)
    record = save_to_db(url, top_word)
    return jsonify(
        {"id": record.id
        ,"most_common_word": record.word
        ,"num_occurences": record.num_occurences,}

