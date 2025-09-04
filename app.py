from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    print("Form Submitted Successfully")
    print("Registration Data: ", request.form)
    return "Registration Successful"

if __name__ == '__main__':
    app.run(debug=True)
