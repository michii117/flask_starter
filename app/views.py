"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app import app
from flask import render_template, request, redirect, url_for, flash
import requests
import json
from werkzeug.utils import secure_filename



from app.forms import LoginForm
from app.forms import Search
from app.forms import MakeSubscription
from app.forms import Prospects

from app.models import AdProspects
from app.models import UserAccount


from datetime import datetime

api_key_header = 'Bearer ' + os.path.join(app.config['API_KEY'])
header = {'Authorization': api_key_header}
current = 'us'
today = datetime.today().strftime("%b %d, %Y")

###
# Routing for your application.
###  
def get_key(val):
    country = {'Ukraine':'ua', 'United Kingdom':'uk', 'United States':'us', 'Russia':'ru', 'Australia':'au', 'Belgium':'be', 'Brazil':'br', 'Canada':'ca', 'China':'cn', 'Cuba':'cu', 'France':'fr', 'Germany':'de', 'Hong Kong':'hk','India':'in', 'Mexico':'mx', 'Netherlaands':'nl','New Zealand':'nz','Nigeria':'ng', 'Singapore':'sg', 'South Africa':'za', 'South Korea':'kr','Thailand':'th','Turkey':'tr'}
    for key, value in country.items():
         if val == value:
             return key

def search(word, country):
    req = requests.get('https://newsapi.org/v2/everything?q='+ get_key(current) + " "+ word + '&language=en', headers= header)
    return req.json()['articles']


def searchByCountry():
    global current
    req = requests.get('https://newsapi.org/v2/top-headlines?country=' + current, headers= header)
    return req.json()['articles']



@app.route('/', methods=['POST','GET'])
def home():
    form = Search()
    advert = Prospects()
    country = {'Ukraine':'ua', 'United Kingdom':'uk', 'United States':'us', 'Russia':'ru', 'Australia':'au', 'Belgium':'be', 'Brazil':'br', 'Canada':'ca', 'China':'cn', 'Cuba':'cu', 'France':'fr', 'Germany':'de', 'Hong Kong':'hk','India':'in', 'Mexico':'mx', 'Netherlaands':'nl','New Zealand':'nz','Nigeria':'ng', 'Singapore':'sg', 'South Africa':'za', 'South Korea':'kr','Thailand':'th','Turkey':'tr'}


    if request.method == 'POST':
        if form.validate_on_submit():
            word = request.form['search']
            results = search(word,country)
            return render_template('home.html', articles = results, date= today, form=form, countries=country)
            
    results = searchByCountry()
    print(results)
    return render_template('home.html', articles = results, date= today, form=form, advert=advert, countries= country,active='News')




@app.route('/<searchTerm>', methods=['POST','GET'])
def term(searchTerm):
    form = Search()
    advert = Prospects()
    country = {'Ukraine':'ua', 'United Kingdom':'uk', 'United States':'us', 'Russia':'ru', 'Australia':'au', 'Belgium':'be', 'Brazil':'br', 'Canada':'ca', 'China':'cn', 'Cuba':'cu', 'France':'fr', 'Germany':'de', 'Hong Kong':'hk','India':'in', 'Mexico':'mx', 'Netherlaands':'nl','New Zealand':'nz','Nigeria':'ng', 'Singapore':'sg', 'South Africa':'za', 'South Korea':'kr','Thailand':'th','Turkey':'tr'}
     
    if request.method == 'POST':
        if form.validate_on_submit():
            word = request.form['search']
            results = search(word,country)
            return render_template('home.html', articles = results, date= today, form=form, countries=country)

    results = search(searchTerm,country)    
    return render_template('home.html', articles = results, date=today, form=form, advert=advert, countries=country, active=searchTerm)



@app.route('/advert', methods = ["POST"])
def advert():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    number = request.form['number']
    companytype = request.form['companytype']
    companyname = request.form['companyname']
    jobtitle = request.form['jobtitle']
    adverttitle = request.form['adverttitle']
    advertdescription = request.form['advertdescription']
    advertphoto = request.files['advertphoto']

    filename = secure_filename(advertphoto.filename)
    advertphoto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    ad = AdProspects(firstname, lastname, email, number, companytype, companyname, jobtitle, adverttitle, advertdescription, filename)
    db.session.add(ad)
    db.session.commit()

    return redirect(url_for('home'))




@app.route('/<count>', methods=['POST','GET'])
def country(count):
    global current 
    current = count
    form = Search()
    advert = Prospects()
    country = {'Ukraine':'ua', 'United Kingdom':'uk', 'United States':'us', 'Russia':'ru', 'Australia':'au', 'Belgium':'be', 'Brazil':'br', 'Canada':'ca', 'China':'cn', 'Cuba':'cu', 'France':'fr', 'Germany':'de', 'Hong Kong':'hk','India':'in', 'Mexico':'mx', 'Netherlaands':'nl','New Zealand':'nz','Nigeria':'ng', 'Singapore':'sg', 'South Africa':'za', 'South Korea':'kr','Thailand':'th','Turkey':'tr'}
    

    
    if request.method == 'POST':
        if form.validate_on_submit():
            word = request.form['search']
            results = search(word,country)
            return render_template('home.html', articles = results, date= today, form=form, countries=country)
    
    results = searchByCountry()    
    return render_template('home.html', articles = results, date= today, form=form, advert=advert, countries=country)





@app.route('/subscribe', methods = ['POST', 'GET'])
def subscribe():
    form = Search()
    subscribe = MakeSubscription()
    if request.method =='POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        
        user = UserAccount(fname,lname,email,password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        
        return redirect(url_for('home'))
        
            

    return render_template('signup.html', subscribe=subscribe)


@app.route('/login', methods= ['GET','POST'])
def login():

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = UserAccount.query.filter_by(email=email).first()

            if user is not None and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("home"))

    return render_template('login.html', form = form)

    
###
# The functions below should be applicable to all Flask apps.
###

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserAccount.query.get(int(id))


@app.route("/update", methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for("home"))



# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
