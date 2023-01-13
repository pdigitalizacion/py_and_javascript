# from flask import Flask, request, jsonify, render_template
#
# app1 = Flask(__name__)
#
# Data ={
#     "alert1": "alert1"
# }
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def JsonResponse(param):
    pass


def HttpResponse(param):
    pass


def vista_sumar(request):
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        c = refresh(a, b)
        return JsonResponse({request: c})
    else:
        return HttpResponse("Peticion no valida")


@app.route('/refresh-tool', methods=['GET'])
def refresh(a, b):
    popup = {"popup": "popup"}
    # order = run_scanner()
    return jsonify(a, b)


#
# def sumar(a, b):
#     return a + b


@app.route('/')
def time_refresh():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
