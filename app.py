import jwt
import datetime
import hashlib

import requests as requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests
=======
from pymongo import MongoClient
import certifi
>>>>>>> 845bc90a8f4bd5289a1844873d3b5c1d5b6e6e07

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

ca = certifi.where()

client = MongoClient('mongodb+srv://dlgksqor:sparta@cluster0.jueqc.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.animal

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:sparta@cluster0.we7bi.mongodb.net/cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)


@app.route('/hospital', methods=["POST"])
def information_post():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://www.google.com/localservices/prolist?g2lbs=AL1YbfU2_G6oRy7bHObp5Xqp13bAnvJsRsvZOWdGghzny7VniZ6jfVjHIJCdCZLDu0y0FRWOblja&hl=ko-KR&gl=kr&ssta=1&q=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&oq=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&scp=ChRnY2lkOmFuaW1hbF9ob3NwaXRhbBJJEhIJjbZ-5eR5fDURwrX21pgfDAEaEgmbuhHL61VkNRFL24i6AJskkSIJ6rK96riw64-EKhQNppL9FRW6-ExLHRaG1BYl_p41TBoM64-Z66y867OR7JuQIhXqsr3quLDrj4Trj5nrrLzrs5Hsm5AqDOuPmeusvOuzkeybkA%3D%3D&slp=MgBSAggC&src=2&origin=https%3A%2F%2Fwww.google.com&sa=X&ved=2ahUKEwia6fGHmfL4AhUhqFYBHR-OB6wQjGp6BAgCEEY&lci=0',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    hospitals = soup.select(
        '#yDmH0d > c-wiz > div > div:nth-child(3) > div > div > div.XJInM > div.YhtaGd.aQOEkf > div.jq95K > c-wiz > div > div > div.Jtakfe > c-wiz > div > div')
    for hospital in hospitals:
        a1 = hospital.select_one('div.deyx8d > div > div > div.YtX3Td > div.rgnuSb.xYjf2e')
        if (a1 != None):
            name = a1.text

            b1 = hospital.select_one(
                'div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(1) > span')
            if (b1 != None):
                opening_hours = b1.text
            else:
                opening_hours = ""

            c1_1 = hospital.select_one('div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(1)')
            c1_2 = hospital.select_one('div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(2)')
            if (c1_1 != None):
                tel_1 = c1_1.text
            else:
                tel_1 = ""

            if (c1_2 != None):
                tel_2 = c1_2.text
            else:
                tel_2 = ""

            if '-' not in tel_1:
                tel_1 = None
                if (tel_1 == None):
                    tel_1 = ""
            if '-' not in tel_2:
                tel_2 = None
                if (tel_2 == None):
                    tel_2 = ""

            phone = tel_1 + tel_2

            if (phone == ""):
                phone = "???????????? ????????????"

            d1_1 = hospital.select_one(
                'div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(2) > span')
            d1_2 = hospital.select_one(
                'div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(3) > span')

            if (d1_1 != None):
                add1 = d1_1.text
            else:
                add1 = ""

            if (d1_2 != None):
                add2 = d1_2.text
            else:
                add2 = ""

            address = add1 + add2

            if (address == ""):
                address = "???????????? ????????????"

            e1 = hospital.select_one('div.deyx8d > div > div > div.z6yOqb.i1baHb > img')
            if (e1 != None):
                photo = e1['src']
            else:
                photo = 'https://previews.123rf.com/images/siamimages/siamimages1504/siamimages150401064/39173277-%EC%82%AC%EC%A7%84-%EC%97%86%EC%9D%8C-%EC%95%84%EC%9D%B4%EC%BD%98-%EC%97%86%EC%9D%8C.jpg'

            doc = {
                'photo': photo,
                'name': name,
                'phone': phone,
                'address': address,
                'opening_hours': opening_hours
            }

            return jsonify({'msg1': '????????? ??????'})





@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        return render_template('index.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="????????? ????????? ?????????????????????."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="????????? ????????? ???????????? ????????????."))


<<<<<<< HEAD

@app.route("/hospital", methods=["GET"])
def information_get():
    hospital_list = list(db.project.find({}, {'_id': False}))
    return jsonify({'hospital': hospital_list})


@app.route('/detail')
def detail():
    return render_template("detail.html")

=======
@app.route('/hospital', methods=["GET"])
def post_information():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://www.google.com/localservices/prolist?g2lbs=AL1YbfU2_G6oRy7bHObp5Xqp13bAnvJsRsvZOWdGghzny7VniZ6jfVjHIJCdCZLDu0y0FRWOblja&hl=ko-KR&gl=kr&ssta=1&q=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&oq=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&scp=ChRnY2lkOmFuaW1hbF9ob3NwaXRhbBJJEhIJjbZ-5eR5fDURwrX21pgfDAEaEgmbuhHL61VkNRFL24i6AJskkSIJ6rK96riw64-EKhQNppL9FRW6-ExLHRaG1BYl_p41TBoM64-Z66y867OR7JuQIhXqsr3quLDrj4Trj5nrrLzrs5Hsm5AqDOuPmeusvOuzkeybkA%3D%3D&slp=MgBSAggC&src=2&origin=https%3A%2F%2Fwww.google.com&sa=X&ved=2ahUKEwia6fGHmfL4AhUhqFYBHR-OB6wQjGp6BAgCEEY&lci=0',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    hospitals = soup.select(
        '#yDmH0d > c-wiz > div > div:nth-child(3) > div > div > div.XJInM > div.YhtaGd.aQOEkf > div.jq95K > c-wiz > div > div > div.Jtakfe > c-wiz > div > div')
    dict_list=[]
    for hospital in hospitals:
        a1 = hospital.select_one('div.deyx8d > div > div > div.YtX3Td > div.rgnuSb.xYjf2e')
        if (a1 != None):
            name = a1.text

            b1 = hospital.select_one(
                'div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(1) > span')
            if (b1 != None):
                opening_hours = b1.text
            else:
                opening_hours = ""

            c1_1 = hospital.select_one('div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(1)')
            c1_2 = hospital.select_one('div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(2)')
            if (c1_1 != None):
                tel_1 = c1_1.text
            else:
                tel_1 = ""

            if (c1_2 != None):
                tel_2 = c1_2.text
            else:
                tel_2 = ""

            if '-' not in tel_1:
                tel_1 = None
                if (tel_1 == None):
                    tel_1 = ""
            if '-' not in tel_2:
                tel_2 = None
                if (tel_2 == None):
                    tel_2 = ""

            phone = tel_1 + tel_2

            if (phone == ""):
                phone = "???????????? ????????????"

            d1_1 = hospital.select_one(
                'div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(2) > span')
            d1_2 = hospital.select_one(
                'div.deyx8d > div > div > div.YtX3Td > div:nth-child(3) > span:nth-child(3) > span')

            if (d1_1 != None):
                add1 = d1_1.text
            else:
                add1 = ""

            if (d1_2 != None):
                add2 = d1_2.text
            else:
                add2 = ""

            address = add1+add2

            if (address == ""):
                address = "???????????? ????????????"

            e1 = hospital.select_one('div.deyx8d > div > div > div.z6yOqb.i1baHb > img')
            if (e1 != None):
                photo = e1['src']
            else:
                photo = 'https://previews.123rf.com/images/siamimages/siamimages1504/siamimages150401064/39173277-%EC%82%AC%EC%A7%84-%EC%97%86%EC%9D%8C-%EC%95%84%EC%9D%B4%EC%BD%98-%EC%97%86%EC%9D%8C.jpg'

            doc = {
                'photo': photo,
                'name': name,
                'phone': phone,
                'address': address,
                'opening_hours': opening_hours
            }

            dict_list.append(doc)

    return jsonify({'dict':dict_list})


@app.route("/db.tees", methods=["GET"])
def information_get():
    hospital_list = list(db.project.find({}, {'_id': False}))
    return jsonify({'hospital': hospital_list})
>>>>>>> 845bc90a8f4bd5289a1844873d3b5c1d5b6e6e07


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/user/<username>')
def user(username):
    # ??? ???????????? ???????????? ?????? ????????? ??? ?????? ??????
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        status = (username == payload["id"])  # ??? ??????????????? True, ?????? ?????? ????????? ???????????? False

        user_info = db.users.find_one({"username": username}, {"_id": False})
        return render_template('user.html', user_info=user_info, status=status)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # ?????????
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # ????????? 24?????? ??????
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})  # decode('utf-8')
    # ?????? ?????????
    else:
        return jsonify({'result': 'fail', 'msg': '?????????/??????????????? ???????????? ????????????.'})


# ????????????
@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,  # ?????????
        "password": password_hash,  # ????????????
        "profile_name": username_receive,  # ????????? ?????? ???????????? ?????????
        "profile_pic": "",  # ????????? ?????? ?????? ??????
        "profile_pic_real": "profile_pics/profile_placeholder.png",  # ????????? ?????? ?????? ?????????
        "profile_info": ""  # ????????? ??? ??????
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


# ????????????
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/posting', methods=['POST'])
def posting():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # ???????????????
        return jsonify({"result": "success", 'msg': '????????? ??????'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route("/get_posts", methods=['GET'])
def get_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # ????????? ?????? ????????????
        return jsonify({"result": "success", "msg": "???????????? ??????????????????."})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/update_like', methods=['POST'])
def update_like():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # ????????? ??? ??????
        return jsonify({"result": "success", 'msg': 'updated'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)