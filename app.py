from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("Form Submitted Successfully")
        print("Registration Data: ", request.form)
        return "Registration Successful"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
