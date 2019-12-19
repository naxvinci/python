from flask import Flask, escape, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/opgg')
def opgg():
    userName = request.args.get('userName')
    url = f"http://www.op.gg/summoner/userName={userName}"

    req = requests.get(url).text
    data = BeautifulSoup(req, 'html.parser')

    data.select_one()
    data.select_one()
    return render_template('opgg.html', userName = userName, url = url)




if __name__== "__main__": 
    app.run(debug=True)
