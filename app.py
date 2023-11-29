from flask import Flask,render_template,request,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", s="0")
@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method=="POST":
        res=request.files['file']
        res.save("static/"+res.filename)
        return render_template("result.html",s=res.filename)
    if __name__ == '__main__':
        app.run(debug=True,port=8001,host="localhost")