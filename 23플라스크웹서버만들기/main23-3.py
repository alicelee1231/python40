from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/simple')
def simple():
    return render_template("simple.html")

def main():
    app.run(debug=True,port=80)

if __name__ =="__main__":    
    main()
