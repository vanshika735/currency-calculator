from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.exchangerate-api.com/v4/latest/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    response = requests.get(API_URL + from_currency)
    data = response.json()
    rate = data['rates'][to_currency]
    result = amount * rate

    return render_template('index.html', result=result, from_currency=from_currency, to_currency=to_currency, amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
