from flask import Blueprint,request,flash,render_template,session
from controller.registerUrl import user
from sever.userSever import *

@user.route('/login_form',methods=['get'])
def login_form():
    return render_template('account/login.html')

@user.route('/login',methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)

    if not all([username,password]):
        message = '参数不完整'
        model = {"message":message}
        return render_template('login.html',model)

    elif getUserByNameAndPass(username,password) == None:
        message = '用户名或密码错误'
        model = {"message":message}
        return render_template('login.html',model = model)

    else:
        user = getUserByNameAndPass(username,password).to_json()
        session['user'] = user
        print(session)
        return render_template('index.html')

@user.route('/register_form',methods=['get'])
def register_form():
    return render_template('account/register.html')

@user.route('/register',methods=['post'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    repeatpassword = request.form.get('repeatpassword')
    print("password",password.strip(),"reap",repeatpassword.strip())

    if not all([username,password,repeatpassword]):
        message = '参数不完整'
        model = {"message":message}
        return render_template('account/register.html',model = model)
    elif getUserByUsername(username)!=None:
        message = '用户名已存在'
        model = {"message":message}
        return render_template('account/register.html',model = model)
    elif password == repeatpassword:
        insertUser(username, password)
        return render_template('account/login.html')
    else:
        message = '两次输入密码不一致'
        model = {"message":message}
        return render_template('account/register.html',model = model)

@user.route('/logout',methods=['get'])
def logout():
    session['user']=None
    return render_template('monitor/main.html')



@user.route('/index.html',methods = ['get'])
def template():
    return render_template('index.html')

@user.route('/index-green.html',methods = ['get'])
def template0():
    return render_template('index-green.html')

@user.route('/index-light.html',methods = ['get'])
def template1():
    return render_template('index-light.html')

@user.route('/index-orange.html',methods = ['get'])
def template2():
    return render_template('index-orange.html')

@user.route('/index1.html',methods = ['get'])
def template3():
    return render_template('index1.html')

@user.route('/index-orange.html',methods = ['get'])
def template4():
    return render_template('index-orange.html')

@user.route('/index-purple.html',methods = ['get'])
def template5():
    return render_template('index-purple.html')

@user.route('/index-red.html',methods = ['get'])
def template6():
    return render_template('index-red.html')

@user.route('/alert.html',methods = ['get'])
def template7():
    return render_template('alert.html')

@user.route('/buttons.html',methods = ['get'])
def template8():
    return render_template('buttons.html')

@user.route('/calendar-basic.html',methods = ['get'])
def template9():
    return render_template('calendar-basic.html')

@user.route('/calendar-external-events.html',methods = ['get'])
def template10():
    return render_template('calendar-external-events.html')

@user.route('/calendar-list.html',methods = ['get'])
def template11():
    return render_template('calendar-list.html')

@user.route('/cards.html',methods = ['get'])
def template12():
    return render_template('cards.html')

@user.route('/icon-font-awesome.html',methods = ['get'])
def template13():
    return render_template('icon-font-awesome.html')

@user.route('/icon-simple-line.html',methods = ['get'])
def template14():
    return render_template('icon-simple-line.html')

@user.route('/inbox.html',methods = ['get'])
def template15():
    return render_template('inbox.html')

@user.route('/inbox-compose.html',methods = ['get'])
def template16():
    return render_template('inbox-compose.html')

@user.route('/inbox-details.html',methods = ['get'])
def template17():
    return render_template('inbox-details.html')

@user.route('/portlet-advanced.html',methods = ['get'])
def template18():
    return render_template('portlet-advanced.html')

@user.route('/portlet-base.html',methods = ['get'])
def template19():
    return render_template('portlet-base.html')

@user.route('/table-basic.html',methods = ['get'])
def template20():
    return render_template('table-basic.html')

@user.route('/widgets-base.html',methods = ['get'])
def template21():
    return render_template('widgets-base.html')

@user.route('/widgets-chart.html',methods = ['get'])
def template22():
    return render_template('widgets-chart.html')

@user.route('/profile.html',methods = ['get'])
def template23():
    return render_template('profile.html')

@user.route('/invoice.html',methods = ['get'])
def template24():
    return render_template('invoice.html')

@user.route('/flot-chart.html',methods = ['get'])
def template25():
    return render_template('flot-chart.html')





