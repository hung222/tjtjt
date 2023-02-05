from flask import Flask ,render_template ,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'giác hơi 100 hủ'
@app.route('/trangthu2.html/<name>')
def trangthu2():
      return render_template('trangthu2.html', name=name)
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
