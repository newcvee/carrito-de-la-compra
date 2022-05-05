from flask import Flask, jsonify
from flask_cors import CORS
from src.main import main, split_in_lines, split_array_from_pipe, list_to_dict, list_to_dict_with_new_key, split_in_lines

app = Flask("shopping-cart")
CORS(app)


@app.route("/shopping-cart", methods=["GET"])
def shopping_list():
    result = main()
    return jsonify(result)
