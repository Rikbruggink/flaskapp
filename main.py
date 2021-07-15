from flask import Flask, request, Response, render_template, session

app = Flask(__name__)
app.secret_key = 'supersecret!'

session = {}
@app.route('/webhook', methods=['POST'])
def respond():
    session['json'] = request.json['data']
    return Response(status=200)


@app.route("/")
def template_test():
    return render_template('template.html', my_string=session.get('json', 'frontpage_square'))

if __name__ == '__main__':
    app.run()


## curl -H "Content-Type: application/json" -X POST -d '{"data": "frontpage_square_red"}' localhost:5000/webhook