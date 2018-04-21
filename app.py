from flask import Flask, jsonify, request, render_template

app= Flask(__name__)

stores = [
    {
        'name': 'My wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'Price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }

    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_items_in_store(name):
    new_item = request.get_json()
    for store in stores:
        if(store['name'] == name):
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})



app.run(port=3000)
