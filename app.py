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
in this code it is telling that if we run it is giving 
C:\EXAM 1279>python app.py
Traceback (most recent call last):
  File "C:\EXAM 1279\app.py", line 1, in <module>
    from flask import Flask, request, render_template, url_for
ModuleNotFoundError: No module named 'flask'
