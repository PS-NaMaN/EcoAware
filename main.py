from flask import Flask, render_template, request

app = Flask(__name__)

'''@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num3'])
        num2 = float(request.form['num4'])
        result = num1 + num2
        return render_template('result.html', result=result)
'''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/regislink.html')
def dashboard():
    return render_template('regislink.html')


if __name__ == '__main__':
    app.run(debug=True,port=8008)
