from flask import render_template,request, redirect, url_for
from home import app
from home.models import User
from home import db
from flask_login import login_user,logout_user,current_user

@app.route('/role', methods=['GET', 'POST'])
def role():
    user=User.query.all()
    return render_template("roles.html",user=user)

@app.route('/users', methods=['GET', 'POST'])
def users():
    user=User.query.all()
    return render_template("users.html",user=user)

@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("role"))
    error_msg=''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user=User.query.filter_by(email=email).first()
        if user == None:
            error_msg="Login Unsuccesful ! Email incorrect or not registered"
        else:
            if email==user.email and password==user.password:
                login_user(user)
                return redirect(url_for("role"))
            else:
                error_msg="Login Unsuccesful ! Password wrong"
    return render_template("login.html",title='Login Page',error_msg=error_msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("role"))
    error_msg=''
    msg = ''
    if request.method == 'POST' and 'name' in request.form:
        # Create variables for easy access
        name = request.form['name']
        email = request.form['email']
        country=request.form['country']
        nationality=request.form['nationality']
        phone=request.form['phone']
        role=request.form['role']
        password = request.form['password']
        user=User.query.filter_by(email=email).first()

        #Server side validation
        done=False
        while not done:
            if not name[0].isalpha():
                error_msg="UserName should start with an alphabet"+"\n"
                done=True
            elif len(phone)!=10:
                error_msg="Enter valid phone number"
                done=True
            elif len(password)<5:
                error_msg="Password length should be greater than 5"
                done=True
            elif not password[0].isupper():
                error_msg="First letter of password should be capital"
                done=True
            elif User.query.filter_by(phone=phone).first() !=None :
                error_msg='Account is already registered with this number'
                done=True
            elif user==None and done == False:
                user=User(name=name,email=email,country=country,nationality=nationality,phone=phone,role=role,password=password)
                db.session.add(user)
                db.session.commit()
                msg = 'You have successfully registered as '+name+'!'
                error_msg=''
                done=True
            elif user!=None:
                error_msg="This email is already registered"
                done=True
    return render_template("register.html",title='Register Page',error_msg=error_msg,msg=msg)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for("login"))