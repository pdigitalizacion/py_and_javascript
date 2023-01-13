# from flask import Flask, render_template, request, redirect, session
# import json
#
# app = Flask(__name__)
#
#
# @app.route('/refresh/', methods=['GET'])
# def refresh(userInfo):
#     userInfo = json.load(userInfo)
#     userInfo = json.load(userInfo)
#     print()
#     print('USER INFO RECEIVED')
#     print('__________________')
#     print(f"User name: {userInfo['name']}")
#     print(f"User type: {userInfo['type']}")
#     print()
#     return 'Info'
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

##########################
# from flask import Flask, render_template, jsonify
#
# app = Flask(__name__)
#
#
# @app.route('/refresh-tool', methods=['GET'])
# def refresh():
#     # alert1 = one()
#     return jsonify()
#
#
# # var json = alert1
# print("var json ='{}'".format(jsonify))
#
# # alert1=alert1
#
# def one():
#     while True:
#         i = input()
#         x = 1
#         if i == x:
#             alert1 = x
#         else:
#             alert1 = 'error'
#         return alert1
#
#
# @app.route('/')
# def time_refresh():
#     return render_template('index.html')

# @app.route('/')
# def index():
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(use_reloader=True)


############## test 3################

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    value: request.json['array'][0]
    result = "result"
    return jsonify({"key": [0, 1, 2, 3, 4, 5]})


if __name__ == '__main__':
    app.run(debug=True)
