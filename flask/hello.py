from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/fstring')
def fstring():
    name = "박나은"
    return f"제 이름은 {name} 입니다."


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    name = "박나은"
    return render_template('hi.html', html_name = name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num**3
    return render_template('num3.html', cube_num = cube_num, num = num)

@app.route('/dinner')
def dinner():
    menu = ['삼각김밥', '컵라면', '스테이크', '마라탕', '훠궈']
    dinner = random.choice(menu)
    menu_img = {'삼각김밥': '//item.ssgcdn.com/96/16/97/item/1000024971696_i1_1200.jpg', 
                '컵라면' : 'http://image.auction.co.kr/itemimage/11/21/cd/1121cdc7b6.jpg', 
                '스테이크' : 'http://recipe1.ezmember.co.kr/cache/recipe/2017/07/09/6741acc7f6bf0f7d04245851fb365c311.jpg', 
                '마라탕' : 'https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/4BYf/image/_pc0k6Jz3BHHLVwylaQYEPZdQd0.jfif', 
                '훠궈' : 'https://mp-seoul-image-production-s3.mangoplate.com/1250135_1547430500643161.jpg?fit=around|738:738&crop=738:738;*,*&output-format=jpg&output-quality=80'}
    img_url = menu_img[dinner]


    return render_template('dinner.html', dinner = dinner, img_url = img_url)

@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', movies = movies)









if __name__== "__main__": 
    app.run(debug=True)
