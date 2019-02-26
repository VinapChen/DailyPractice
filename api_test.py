# -*- coding: utf-8 -*-
# filename: main.py
import web
import json
from flask import Response, Flask
from flask import send_file
import os
from django.http import HttpResponse
from flask import jsonify



app = Flask(__name__)


# urls = (
#     '/dataReturn','ReturnDataTest',
# )
#
#
# class ReturnDataTest:
#     def GET(self):
#         data = {
#             "data":123,
#         }
#         resp = jsonify(data)
#         resp.headers['Access-Control-Allow-Origin'] = '*'
#         return resp
#
#


@app.route('/dataReturn', methods=['GET'])
def index():
    data = [
        {'name': 'a', 'pv': 32, 'uv': 12},
        {'name': 'b', 'pv': 34.2, 'uv': 34.5},
        {'name': 'c', 'pv': 24, 'uv': 55},
        {'name': 'd', 'pv': 14, 'uv': 24},
        {'name': 'e', 'pv': 54, 'uv': 34},
        {'name': 'f', 'pv': 23.4, 'uv': 33.4},
    ]
    resp = jsonify(data)
    # 跨域设置
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    # app = web.application(urls, globals())
    app.run()