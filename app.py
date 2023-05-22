from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize an empty list for the orders
orders = []

@app.route('/')
def visit():
    return render_template('index.html', orders=orders)

@app.route('/order', methods=['POST'])
def order():
    order = request.form.get('input')
    orders.append(order)
    return f"Order of {order} received!"

@app.route('/clear', methods=['POST'])
def clear():
    orders.clear()
    return "Orders cleared!"

if __name__ == '__main__':
    app.run(debug=True)