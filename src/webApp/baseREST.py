from flask import render_template, request, jsonify



def restConfigure(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/hello/<name>')
    def hello_name(name):
        return 'Hello %s!' % name

    @app.route('/api',methods = ['POST', 'GET'])
    def rest():
            if request.method == 'POST':
                obj = {
                    'name': request.form['name'],
                    'contact': request.form['contact'],
                    'email': request.form['email']
                }
                return jsonify(obj)
            else:
                return  jsonify({"name":request.args.get('name')})
