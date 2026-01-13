from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('form.html')

@app.route('/submit-form', methods =['POST'])
def submit_form():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    return f'{firstname, lastname}'

if __name__ =='__main__':
    app.run(debug=True)