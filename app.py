from typing import List
from flask import Flask, jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Olivia',
        'Contact': u'9364862938',
        'done': False
    },
    {
        'id': 2,
        'Name': u'Arolin',
        'Contact': u'8253741638',
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    contact = {
        'id': List[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    } 
    List.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added succesfully!"
    }) 

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)