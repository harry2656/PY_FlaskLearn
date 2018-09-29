from app import app
from flask import render_template, flash, redirect,url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	#return "Hello World!"
	user = {'username':'XUEZHIHSAN'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts = posts)
	#return render_template('index.html', user=user)

'''
@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',title='Sign in',form=form)
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         #flash()���������û���ʾ��Ϣ����Ч;��
        flash('Login requested for user={},remeber_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))#ֱ����ģ���Դ�ļ���Ӳ�������Ӵ��������������һ�������������֯���ӣ���ô�㽫���ò�������Ӧ�����������滻��Щ����
    return render_template('login.html',title='Sign In',form=form)