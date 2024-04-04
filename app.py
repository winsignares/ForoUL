from flask import Flask, render_template,request,json,jsonify 
from config.db import app
@app.route('/',methods=['GET'])
def index():
    return "hola mundoo"

if __name__ =="__main__":
    app.run(debug=True, host  ='0.0.0.0')