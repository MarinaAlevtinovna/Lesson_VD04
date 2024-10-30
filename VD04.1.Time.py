from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return f'Текущее время в Москве: {moscow_time.strftime('%Y-%m-%d %H:%M:%S')}'

if __name__=='__main__':
    app.run(port=5001)