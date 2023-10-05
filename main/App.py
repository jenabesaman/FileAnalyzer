import os
from flask import Flask, request, jsonify, Response
import Predicting
import Language

app = Flask(__name__)
app.debug = True


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'message': 'Invalid Input Url'})


@app.errorhandler(400)
def invalid_route(e):
    return jsonify({'errorCode': 400, 'message': 'Bad Request,input json text is not correct'})


@app.errorhandler(500)
def invalid_route(e):
    return jsonify({'errorCode': 500, 'message': 'Internal Server Error'})


@app.route("/ping")
def ping():
    return "This is a api test only"


@app.route("/predict", methods=["post"])
def predicting():
    try:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        data = request.get_json(force=True)
        # if 'file_path' not in data:
        #     return jsonify({'error': 'file_path is missing in the JSON data'}), 400
        base64_string = data["base64_string"]
        result = Predicting.predicting(base64_string=base64_string)
        return jsonify({'result': result})
    except:
        return "cant predict"


@app.route("/translate", methods=["post"])
def translating():
    try:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        data = request.get_json(force=True)
        lang = data["language"]
        data_list = list(data.items())
        selected_items = data_list[1:]
        selected_items = dict(selected_items)
        my_dict = {}
        for key, value in selected_items.items():
            translated = Language.translate_text(input_text=value, lang=lang)
            my_dict[key] = translated
            last_key=key[-1]
            
            # for key1, value1 in reversed(my_dict.items()):
            #     reversed_dict[key1] = value1
        return my_dict
    except:
        return "cant translate"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
