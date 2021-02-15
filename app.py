from flask import Flask, jsonify, request, render_template

app= Flask(__name__)

stores= [
    {
        "name": "My Store",
        "items": [
            {
                "name": "My Item",
                "price": "15.99"
            }
        ]
    }
]

@app.route("/")
def home():
    return render_template('index.html')

# it means http://www.google.com/ ---/ after domain name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)

#GET store with name
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # If store name matches, return it
    # If none matches, return error message
    for store in stores:
        if store['name'] == name:
           return jsonify(store)
        return jsonify({'message': 'Store name not matches'})


# GET store
@app.route('/store')
def get_stores():
    return jsonify(stores)

#POST /store/<string:name>/item { name:, price:}

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
        return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
           return jsonify(store['items'])
        return jsonify({'message':'store not found'})

app.run(host='0.0.0.0',port=8000,debug=True)
