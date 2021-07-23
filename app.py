from flask import Flask, request, jsonify

app = Flask(__name__)

datas = [
    {
        'id':1,
        'contact':'94828485022',
        'name': 'Aryan',
        'done': False
    },
    {
        'id':2,
        'contact': '9488472894',
        'name': 'Rahul',
        'done': False
    },
]

@app.route("/add-data", methods=["POST"])

def add_data():
    if not request.json:
        return jsonify(
            {
            "status": 'error',
            "message": "Please provide the data"
            },
            400
        )

    data = {
        'id': datas[-1]['id']+1,
        'contact': request.json['contact'],
        'name': request.json.get('name', ""),
        'done': False
    }

    datas.append(data)
    return jsonify(
        {
            "status": 'Success',
            "message": "Data Added Successfully"
        }
    )

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": datas
    })

if __name__ == "__main__":
    app.run(debug=True)