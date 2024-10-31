from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', caption= 'Детская студия Лучик')

@app.route('/наши цены/')
def blog():
    context = {
        'caption': 'Наши цены',
        'link': 'Подать заявку',
    }
    return render_template('price.html', **context)

@app.route('/контакты/')
def contacts():
    return render_template('about.html', caption='Контакты')

if __name__=='__main__':
    app.run(port=5006)