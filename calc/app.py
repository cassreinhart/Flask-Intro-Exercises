from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def show_sum():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a,b)
    return str(res)

@app.route('/sub')
def show_diff():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a,b)
    return str(res)

@app.route('/mult')
def show_product():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a,b)
    return str(res)

@app.route('/div')
def show_quotient():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a,b)
    return str(res)

operator = {
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div
}

@app.route('/math/<oper>')
def do_math(oper):
    """do math operation on a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = operator[oper](a,b)
    return str(res)
