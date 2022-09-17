from flask import Flask,render_template,url_for,request,redirect;
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("login.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

@app.route("/success/<name>")
def success(name):
    return "Welcome " + name


if __name__ == '__main__':
    app.run(debug=True)