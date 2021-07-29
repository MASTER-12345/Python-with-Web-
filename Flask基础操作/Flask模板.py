from flask import Flask,render_template,flash,request,make_response,jsonify,redirect
import pymysql
import sqlite3
import random
import csv
app=Flask(__name__)
app.secret_key = 'secret string'

@app.route('/',methods=['POST','GET'])
def index():


    if request.method == 'POST':
       
        zhi = request.form.get('zhi')
        print(zhi)
        if zhi=='asked':
            shuru = request.form.get('shuru')
            print(shuru)

            asker="成功！"
            return jsonify({'word':asker})

    return render_template('up_photo.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
