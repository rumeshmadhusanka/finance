import json
from threading import Thread

from flask import Flask, jsonify
from flask import Response

from modules.company import Company
from modules.config import Config as Conf
from modules.daily_task import DailyTask

app = Flask(__name__)
app.config.from_object(Conf)


@app.route('/daily_price/<company_code>/<start_date>/<end_date>', methods=['GET'])
def daily_price(company_code, start_date, end_date):
    try:
        company = Company(company_code)
        return jsonify(company.get_daily_data(start_date, end_date))
    except ConnectionError as e:
        return Response({"message": "Error " + str(e)}, status=502, mimetype='application/json')


@app.route('/company_info/<company_code>/', methods=['GET'])
def info(company_code):
    try:
        company = Company(company_code)
        inf = company.get_company_info()
        ret = jsonify(inf)
        return ret
    except Exception as e:
        return Response({"message": "Error " + str(e)}, status=502, mimetype='application/json')


@app.route('/recommendations/<company_code>/<start_date>/<end_date>', methods=['GET'])
def recommend(company_code, start_date, end_date):
    try:
        company = Company(company_code)
        inf = company.get_recommendations(start_date, end_date)
        ret = json.dumps(inf, indent=4, sort_keys=True, default=str)
        return ret
    except Exception as e:
        print(e)
        return Response({"message": "Error " + str(e)}, status=502, mimetype='application/json')


@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Default Route"})


def back():
    daily_update = DailyTask()
    daily_update.start()
    daily_update.task()


t = Thread(target=back)
t.start()

if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=True)
