from flask import Flask,render_template , request
import numpy as np
import joblib

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route("/submit",methods=['POST','GET'])   
def predict():
    if request.method=='POST':
        eop=float(request.form['EOP'])
        reg=joblib.load('regression_model.joblib')
        data=np.array([eop]).reshap(1,-1)
        result=reg.predict(data)
        result= str (result)
    return result
def ab():
    return render_template('aboutus.html')

if __name__== '__main__':
    app.run(debug=True)

