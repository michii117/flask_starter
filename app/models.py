from . import db
from werkzeug.security import generate_password_hash
import psycopg2


class UserAccount(db.Model):
    __tablename__ = 'subscribed'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password, method = 'pbkdf2:sha256')


    def is_unique(self, email):
        user = users.query.filter(users.email==email).first()
        if user != None: # the query has returned a user
            flash("Please use a different email.")
            return render_template("newAccount.html")

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_email(self):
        return self.email

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return self.email

    def get_email(email):
        db = psycopg2.connect(host="localhost",database="SDUL Database", user="demitri", password="sky")
        cur = db.cursor()
        cur.execute("select * from accounts where email = %s", (email,))
        item = cur.fetchall()
        
        if len(item) == 0:
            return 0 
        else:
            return item[0][3]





class Profile(db.Model):
    __tablename__ = 'userprofile'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer)
    preferences = db.Column(db.String)
    country = db.Column(db.String)
    outlets = db.Column(db.String)


class AdProspects(db.Model):
    __tablename__='advertisements'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String)
    number = db.Column(db.String)
    companyname = db.Column(db.String)
    jobtitle = db.Column(db.String)
    adverttitle = db.Column(db.String)
    advertdescription = db.Column(db.String)
    advertphoto = db.Column(db.String)

    def __init__(self, firstname, lastname, email, number,companytype, companyname, jobtitle, adverttitle, advertdescription, advertphoto):
        self.firstname = firstname
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.number = number
        self.companytype = companytype
        self.companyname = companyname
        self.jobtitle = jobtitle
        self.adverttitle = adverttitle
        self.advertdescription = advertdescription
        self.advertphoto = advertphoto
