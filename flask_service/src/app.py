from flask import Flask, jsonify, request

products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]

app = Flask(__name__)


# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(products)


# curl -v http://localhost:5000/product/1
@app.route('/product/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 0:
        return f'Product with id {id} not found', 404
    return jsonify(product_list[0])


# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}' -v http://localhost:5000/product
@app.route('/product', methods=['POST'])
def post_product():
    # Retrieve the product from the request body
    request_product = request.json

    # Generate an ID for the post
    new_id = max([product['id'] for product in products]) + 1

    # Create a new product
    new_product = {
        'id': new_id,
        'name': request_product['name']
    }

    # Append the new product to our product list
    products.append(new_product)

    # Return the new product back to the client
    return jsonify(new_product), 201


# curl --header "Content-Type: application/json" --request PUT --data '{"name": "Updated Product 2"}' -v http://localhost:5000/product/2
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    # Get the request payload
    updated_product = request.json

    # Find the product with the specified ID
    for product in products:
        if product['id'] == id:
            # Update the product name
            product['name'] = updated_product['name']
            return jsonify(product), 200

    return f'Product with id {id} not found', 404

# curl --request DELETE -v http://localhost:5000/product/2
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    # Find the product with the specified ID
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 1:
        products.remove(product_list[0])
        return f'Product with id {id} deleted', 200

    return f'Product with id {id} not found', 404

# curl --header "Content-Type: application/json" --request POST --data '{"factor_1": 4, "factor_2": 7}' -v http://localhost:5000/mult
@app.route('/mult', methods=['GET', 'PUT', 'POST'])
def multiply_two():
    if request.method == 'GET':
        return '''This endpoint allows to multiply numbers.\n
                    Use POST method to send two numbers   \n 
                    factor_1 and factor_2  \n
                    of type int or float.  \n
                    format request body as JSON. \n
                    Response will include info about  \n
                    their product.  \n
        '''

    elif request.method == 'PUT':
        try:
            factor_1_str = request.args.get('factor_1')
            factor_2_str = request.args.get('factor_2')
        except:
            return jsonify({"Error 412": "something is wrong"}), 412

        try:
            factor_1 = float(factor_1_str)
        except:
            return jsonify({"Error 412": "factor_1 is not a number"}), 412

        try:
            factor_2 = float(factor_2_str)
        except:
            return jsonify({"Error 412": "factor_2 is not a number"}), 412

        try:
            product = factor_1 * factor_2
            ok_response = ('Product of {} and {} is {}'.format(factor_1, factor_2, product))
            return jsonify({"Success": ok_response}), 200
        except:
            return jsonify({"Error 412": "something is wrong 2"}), 412


    elif request.method == 'POST':
        # show the post with the given id, the id is an integer
        # return 'Post %d' % post_id
        # body = request.get_json()
        req_data = request.get_json()

        try:
            factor_1 = float(req_data.get('factor_1'))
        except:
            return jsonify({"Error 412": "factor_1 is not a number"}), 412

        try:
            factor_2 = float(req_data.get('factor_2'))
        except:
            return jsonify({"Error 412": "factor_2 is not a number"}), 412

        try:
            product = factor_1 * factor_2
            # ok_response = f"Product of {factor_1} and {factor_2} is {product}"
            # ok_response = ('Product of {} and {} is {}'.format(factor_1,factor_2,product))
            ok_response = product
            return jsonify({"Success": ok_response}), 200

        except:
            return jsonify({"Error 412": "can not multiply"}), 412

        # return jsonify({"Success": ok_response}), 200
        return ok_response



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
