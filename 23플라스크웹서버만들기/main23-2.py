# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return "hello"

# @app.route('<int:i>')
# def dynamic_route(i):
#     return f"{i} page ok"
    
# @app.route('/2')
# def test2page():
#     return "2page ok"


# def main():
#     app.run(debug=True, port=80)

# if __name__ =="__main__":
#     main()


from flask import Flask

app = Flask(__name__)

def dynamic_route(i):
    return f"{i} page ok"

for i in range(0, 10):
    app.add_url_rule(f'/{i}', endpoint=str(i), view_func=lambda i=i: dynamic_route(i))

@app.route('/')
def hello():
    return "hello"

def main():
    app.run(debug=True, port=80)

if __name__ == "__main__":
    main()
