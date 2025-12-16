from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html',title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'nontagorn maungkot'
  email = 'std.67122420214@ubru.ac.th'
  mobile = '063-850-8329'
  age = 21
  return render_template('about.html', title=title,
                                      name=name,
                                      email=email,
                                      mobile=mobile,
                                      age=age) 

@app.route('/favorite/foods')
def favorits_foods():
  title = 'Favorits Foods Page'
  foods = ['ก๋วยเตี๋ยว','ก๋วยจั๊บ','กะเพรา']
  return render_template('favorits_foods.html',
                          title = title,
                            foods = foods)

@app.route('/favorits/sports')
def favorits_sports():
  title = 'Favorits Sports Page'
  sports = ['บอล','บาส','วอลเลย์',]
  return render_template('favorits_sports.html',
                          title=title,
                          sports=sports)