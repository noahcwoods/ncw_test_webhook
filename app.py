from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
webhook_data = {}


@app.route('/webhook', methods=['POST'])
def respond():
    # Get the json data
    global webhook_data
    webhook_data = request.json

    # Add data to a file
    export_data = pd.DataFrame.from_dict(webhook_data)
    export_data.to_csv('export.csv')

    # return to acknowledge receipt of data
    return '', 200


@app.route('/')
def index():
    global webhook_data
    return "Hello World!"


if __name__ == '__main__':
    app.run()
