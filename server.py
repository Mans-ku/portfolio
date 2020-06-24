from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)


def write_data(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a' ,newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer =  csv.writer(database2, delimiter=',',
                            quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,subject,message])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
        
            return redirect('/thank.html')
        except:
            return 'Did not ave to database'
    else:
        return 'error'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# # @app.route('/favicon.ico')
# # def
