import csv
import os
import random
from datetime import date, timedelta
import re
from difflib import SequenceMatcher
from datetime import date



from datetime import datetime
from urllib import request
import pymysql
from werkzeug.utils import secure_filename

import ar_master
import smtplib, ssl
from flask import Flask, render_template,  request, session

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "serverkey2018@gmail.com"
password ="extazee2021"

# ps = PorterStemmer()
app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
conn = pymysql.connect(user='root', password='', host='localhost', database='python_cuisine_recommendation')

mm = ar_master.master_flask_code()
################################################################### HOME

# ps = PorterStemmer()
app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

mm = ar_master.master_flask_code()
################################################################### HOME
@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['pass'] == 'admin':
            return render_template('admin_home.html',error=error)
        else:
            return render_template('admin.html', error=error)
@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')


@app.route("/admin_add_train_dataset")
def admin_train_data():
    return render_template('admin_add_train_dataset.html')


@app.route("/admin_train_data1", methods=['GET', 'POST'])
def admin_train_data1():
    if request.method == 'POST':
        file = request.files['file']

        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename('seasonal.csv')))
        return render_template('admin_add_train_dataset.html', msg="Success")
    else:
        return render_template('admin_add_train_dataset.html', msg="Failed")
######################################
@app.route("/user_login",methods = ['GET', 'POST'])
def user_login():
    msg=None
    if request.method == 'POST':
        n = request.form['username']
        g = request.form['password']
        n1=str(n)
        g1=str(g)
        cursor = conn.cursor()
        q=("SELECT * from user_details where name='" + n1 + "' and password='" + str(g) + "'")

        session['uname'] = n
        cursor.execute(q)
        data = cursor.fetchone()
        conn.commit()
        if data is None:
            msg='Username or Password is wrong'
        else:
            msg='Success'

            return render_template('user_home.html',sid=n)
    return render_template('user.html',error=msg)
@app.route("/user")
def userpage():
    return render_template('user.html')
@app.route("/user_home")
def user_home():
    return render_template('user_home.html')
@app.route("/user_register")
def user_register():
    return render_template('user_register.html')

@app.route("/user_register1",methods = ['GET', 'POST'])
def user_register1():
    if request.method == 'POST':
        name = request.form['applicant_name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        dob = request.form['dob']
        qualification = request.form['qualification']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT max(id) FROM   user_details")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid = 1
        else:
            maxid = maxid + 1
        cursor = conn.cursor()
        result = cursor.execute("insert into user_details values('" + str(
            maxid) + "','" + name + "','" + contact + "','" + email + "','" + address + "','" + dob + "','" + qualification + "','" + password + "','0','0')")
        conn.commit()
        cursor.close()
        if (result == 1):
            return render_template('user.html')
        else:
            return render_template('user_register.html')
@app.route("/user_search")
def user_search():
    return render_template('user_search.html')
@app.route("/user_search1",methods = ['GET', 'POST'])
def user_search1():
    result=0
    cursor1 = conn.cursor()
    cursor1.execute("delete from search_details")
    conn.commit()
    if request.method == 'POST':
        data = request.form['textfield']
        csv_file1=os.path.join("static/uploads/", ('seasonal.csv'))
        with open(csv_file1, mode='r', encoding="cp437") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                name = row['NAME']
                price = row['PRICE']
                CUSINE_CATEGORY = row['CUSINE_CATEGORY']
                Area = row['Area']
                REGION = row['REGION']
                CUSINETYPE = row['CUSINE TYPE']
                TIMING=row['TIMING']
                RATING_TYPE=row['RATING_TYPE']

                RATING=row['RATING']
                VOTES=row['VOTES']
                comfort_food=row['comfort_food']
                comfort_food_reasons=row['comfort_food_reasons']

                data=data.lower()
                comfort_food_reasons=comfort_food_reasons.lower()
                result=SequenceMatcher(None, data, comfort_food_reasons).ratio()
                if(result>=0.6):
                    result=result+1

                    cursor = conn.cursor()
                    cursor.execute("insert into search_details values('" + str(name) + "','" + str(price) + "','" + str(CUSINE_CATEGORY) + "','"+str(TIMING)+"','"+str(RATING_TYPE)+"','"+str(RATING)+"','"+str(VOTES)+"','"+str(comfort_food)+"','"+str(comfort_food_reasons)+"')")
                    conn.commit()

                cursor2 = conn.cursor()
                cursor2.execute("select * from search_details order by VOTES DESC")

                cursor = conn.cursor()
                cursor.execute("select * from search_details order by   RATING DESC")
            return render_template('user_search1.html', items=cursor.fetchall(), best=cursor2.fetchone())

    return render_template('user_search1.html')



@app.route("/user_search2/<price>/<rating>/<vote>/<food>",methods = ['GET', 'POST'])
def user_search2(price,rating,vote,food):
    return render_template('user_search2.html',price=price,rating=rating,votes=vote,food=food)
@app.route("/user_search3",methods = ['GET', 'POST'])
def user_search3():
    uname = session['uname']
    if request.method == 'POST':
        food = request.form['food']
        vote = request.form['vote']
        rating = request.form['rating']
        price = request.form['price']
        quantity = request.form['quantity']
        total = request.form['total']
        customer_name = request.form['customer_name']
        customer_address = request.form['customer_address']
        customer_contact = request.form['customer_contact']
        card_no = request.form['card_no']
        holder_name = request.form['holder_name']
        cvv = request.form['cvv']
        ex_date = request.form['ex_date']
        today = date.today()
        cdate = today.strftime("%d-%m-%Y")

        maxin=mm.find_max_id("booking_details")
        qq="insert into booking_details values('"+str(maxin)+"','"+str(uname)+"','"+str(food)+"','"+str(vote)+"','"+str(rating)+"','"+str(price)+"','"+str(quantity)+"','"+str(total)+"','"+str(customer_name)+"','"+str(customer_address)+"','"+str(customer_contact)+"','"+str(card_no)+"','"+str(holder_name)+"','"+str(cdate)+"','0','0')"
        result=mm.insert_query(qq)



        if (result == 1):
            return render_template('user_home.html')
        else:
            return render_template('user_search.html')

@app.route("/user_review",methods = ['GET', 'POST'])
def user_review():
    uname = session['uname']

    if request.method == 'POST':
        review = request.form['review']

        maxin=mm.find_max_id("review_details")
        from datetime import date

        today = date.today()

        qq="insert into review_details values('"+str(maxin)+"','"+str(uname)+"','"+str(review)+"','"+str(today)+"','0','0')"
        result=mm.insert_query(qq)
        if (result == 1):
            return render_template('user_review.html')
        else:
            return render_template('user_review.html')
    return render_template('user_review.html')
@app.route("/admin_booked_details")
def admin_booked_details():
    qry="select uname,food,price,quantity,total,customer_name,customer_address,customer_contact,cdate from booking_details"
    data=mm.select_direct_query(qry)
    return render_template('admin_booked_details.html',items=data)

@app.route("/admin_review")
def admin_review():
    qry="select id,uname,review,today from review_details"
    data=mm.select_direct_query(qry)
    return render_template('admin_review.html',items=data)

######################################
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
