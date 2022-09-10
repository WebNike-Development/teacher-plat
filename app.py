from flask import Flask, request, render_template, session, redirect, url_for, json
from flask_mysqldb import MySQL
import random , string
import smtplib
from werkzeug.security import generate_password_hash , check_password_hash
from functions import mail_sender, sms_sender
# from db import teacher_address_mode, teacher_certificate_get_mode, teacher_certificate_post_mode, teacher_delete_mode, teacher_description_mode, teacher_detail_mode, teacher_edit_exp_get, teacher_edit_exp_post, teacher_edit_get_post, teacher_edit_post_mode, teacher_exp_get, teacher_exp_post, teacher_phone_mode, teacher_phone_verify_mode, teacher_subject_mode, teacher_teaching_detail_mode, teacher_type_mode, teacher_verification_mode
from db import *
from student_db import *
import datetime
from authlib.integrations.flask_client import OAuth
import stripe
from config import app , mysql
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# app = Flask(__name__)

# mysql = MySQL(app)

# =================================== Google Auth Credentials =====================================
oauth = OAuth(app)
google = oauth.register(
	name = 'google',
	client_id= '302030832901-ifiaimlm7ae4jgk9hfvghe4fu6bs90rm.apps.googleusercontent.com',
	client_secret = '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',
	access_token_url = 'https://accounts.google.com/o/oauth2/token',
	access_token_params = None,
	authorize_url = 'https://accounts.google.com/o/oauth2/auth',
	authorize_params = None,
	api_base_url = 'https://www.googleapis.com/oauth2/v1/',
	client_kwargs = {'scope': 'openid profile email'},
	# client_kwargs = {'scope':  
    #  'https://www.googleapis.com/auth/user.phonenumbers.read'},
	jwks_uri = "https://www.googleapis.com/oauth2/v3/certs",

)


# app.config['MYSQL_USER'] = os.getenv('USER')
# app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
# app.config['MYSQL_HOST'] = os.getenv('HOST')
# app.config['MYSQL_PORT']= int(os.getenv('PORT'))
# app.config['MYSQL_DB'] = os.getenv('DATABASE')
# app.config['MYSQL_CURSORCLASS'] = os.getenv('DB_TYPE')
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51LckOJIO68NMTnSru0MfSzVDjEZWx2cBnAnLUcvEnACTjDSFflFMCuTO1vCZ6ElbCHtRU8bluS5hBiT8TlsXl9fe003rqJiCGO'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51LckOJIO68NMTnSrP1MTqrvSd8EmZm55rhYuzWkgSZGqkIzPAvfVbbTIwAFmNWMtrct1AWfojqSNeYtNZSGbpXQE00goa5JGH3'
stripe.api_key = 'sk_test_51LckOJIO68NMTnSrP1MTqrvSd8EmZm55rhYuzWkgSZGqkIzPAvfVbbTIwAFmNWMtrct1AWfojqSNeYtNZSGbpXQE00goa5JGH3'


# =================================== Landing Page =====================================
@app.route('/', methods=["GET","POST"])
def home_view():

	return render_template('home.html')



# =================================== Registration =====================================
@app.route('/registration', methods=['GET', 'POST'])
def register_view():
	if request.method == 'POST':
		user_name = request.form['user_name']
		email = request.form['email']
		password = request.form['password']
		user_role = request.form['user_role']
		cursor = mysql.connection.cursor()
		my_query = """SELECT * FROM login WHERE email=%s"""
		data = (email,)
		cursor.execute(my_query, data)
		row = cursor.fetchall()
		if row:
			return render_template('register.html', msg="trigger function") 
		else:
			pass_hash = generate_password_hash(password)
			random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
			my_query = """INSERT INTO login (user_name, email, password, user_role, verify_code) VALUES (%s,%s,%s,%s,%s)"""
			data = (user_name,email, pass_hash, user_role,random_str,)
			cursor.execute(my_query, data)
			mysql.connection.commit()
			
			mail_sender(email, random_str, 'email_verification')
			
			my_query = """SELECT id_pk, user_name, email FROM login WHERE email=%s"""
			data = (email,)
			cursor.execute(my_query,data)
			row = cursor.fetchall()

			session["id"] = row[0]['id_pk']
			session["user_name"] = row[0]['user_name']
			session["email"] = row[0]['email']
			session["link"] = random_str

			return redirect(url_for("email_verification_view"))
			# return render_template('verify_email')
	else:
		return render_template('register.html')



# =================================== Resend Email =====================================
@app.route('/resend_email', methods=['GET','POST'])
def resend_email_view():
	if request.method == 'POST':
		email = request.form['email']
		mail_sender(email, session['link'])
		
		cursor = mysql.connection.cursor()
		my_query = """UPDATE login SET email=%s WHERE id_pk=%s"""
		data = (email,session["id"],)
		cursor.execute(my_query, data)
		mysql.connection.commit()
		return redirect(url_for('email_verification_view'))
	else:
		return render_template('verify_email.html')



# ================================ Email verification and link =====================================
@app.route('/email_verification', methods=['GET'])
def email_verification_view():
	print(request.args)
	req_string = request.args.get('q')
	if req_string:
		cursor = mysql.connection.cursor()
		my_query = """SELECT verify_code FROM login WHERE id_pk=%s"""
		data = (session["id"],)
		cursor.execute(my_query,data)
		row = cursor.fetchall()
		if req_string == row[0]['verify_code']:
			my_query = """UPDATE login SET verified = 1 WHERE id_pk=%s"""
			data = (session["id"],)
			cursor.execute(my_query, data)
			mysql.connection.commit()
			return render_template('email_verified.html')

	else:
		return render_template('verify_email.html')



# ======================================== Login =====================================
@app.route('/login', methods=['GET', 'POST'])
def login_view():
	if request.method == "POST":
		email =  request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor()
		my_query = """ SELECT id_pk, user_name, email, user_role, password FROM login WHERE email=%s """
		data = (email,)
		cursor.execute(my_query, data)
		row = cursor.fetchall()
		if row:
			pass_check = check_password_hash(row[0]['password'], password)
			if pass_check:
				session["id"]= row[0]['id_pk']
				session["user_name"]= row[0]['user_name']
				session["email"]= row[0]['email']
				session["user_role"] = row[0]['user_role']
				# my_query = """ SELECT teacher_category, speciality, dob, location, phone_no, gender FROM personal_info WHERE user_id_fk=%s """
				# data = (session["id"],)
				# cursor.execute(my_query, data)
				# row2 = cursor.fetchall()
				if session["user_role"] == 'Teacher':
					return redirect(url_for('teacher_type_view'))
				elif session["user_role"] == 'Student':
					return redirect(url_for('student_role_view'))

				# ============    logics to complete profile   ====================
				# if row2[0]['teacher_category'] == " ":
				# 	return redirect(url_for('teacher_type_view'))
				# elif row2[0]['speciality'] == " ":
				# 	return render_template('home.html', msg ="please complete your profile from speciality")
				# elif row2[0]['location'] == " ":
				# 	return render_template('home.html', msg ="please complete your profile from location")
				# elif row2[0]['phone_no'] == " ":
				# 	return render_template('home.html', msg ="please complete your profile from phone no")
				# elif row2[0]['subject'] == " ":
				# 	return render_template('home.html', msg ="please complete your profile from sbject")
				# else :
				# 	return redirect('home_view')
			else:
				return render_template('login.html', msg="trigger function")
		else:
			return render_template('login.html', msg="trigger function")
		
	else:
		return render_template('login.html')



# ======================================== Logout =====================================
@app.route('/logout')
def logout_view():
	del session["id"]
	del session["user_name"]
	del session["email"]
	del session["user_role"]

	return redirect(url_for("home_view"))



# =================================== Confirmation Email =====================================
@app.route('/confirmation-email', methods=['GET', 'POST'])
def confirmation_email_view():
	if request.method == 'POST':
		random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
		email = request.form['email']
		cursor =  mysql.connection.cursor()
		my_query = """UPDATE login SET verify_code=%s WHERE email=%s"""
		data = (random_str, email,)
		cursor.execute(my_query,data)
		mysql.connection.commit()
		mail_sender(email, random_str, 'password_verify_mail')
		session["email"] = email
		return render_template('confirmation_email.html')
	else:
		return render_template('confirmation_email.html')



# =================================== Set Password =====================================
@app.route('/password_verify_mail', methods=['GET'])
def password_verify_view():
	cursor =  mysql.connection.cursor()
	req_string = request.args.get('q')
	session["code"] = req_string
	my_query = """SELECT verify_code FROM login WHERE email=%s"""
	data = (session["email"],)
	cursor.execute(my_query,data)
	row = cursor.fetchall()
	if req_string == row[0]['verify_code']:
		# my_query = """UPDATE login SET password=%s WHERE verify_code=%s"""
		# data = (session["email"],)
		# cursor.execute(my_query,data)
		return redirect(url_for('successfully_reset_view'))
	else:
		return render_template('confirmation_email.html')



# ===================== successfully reset/ passwrod Reset Confirmation  ==========================
@app.route('/successfully_reset', methods=['POST', 'GET'])
def successfully_reset_view():
	if request.method == 'POST':
		password = request.form['password']
		pass_hash = generate_password_hash(password)
		cursor = mysql.connection.cursor()
		my_query = """UPDATE login SET password=%s WHERE verify_code=%s"""
		data = (pass_hash, session["code"])
		cursor.execute(my_query, data)
		mysql.connection.commit()
		return render_template('password_set_confirmation.html')

	else:
		return render_template('set_password.html')



# =================================== Google Login ===============================
@app.route('/google_login')
def google_login_view():
	google = oauth.create_client('google')
	redirect_url = url_for('authorize', _external=True)
	return google.authorize_redirect(redirect_url)

@app.route('/authorize')
def authorize():
	google = oauth.create_client('google')
	token = google.authorize_access_token()
	user_info = google.get('userinfo', token=token)
	info = user_info.json()
	# cursor = mysql.connection.cursor()
	# my_query = """INSERT INTO table (user_name, email, password, user_role, verify_code) VALUES (%s,%s,%s,%s,%s)"""
	# data = (info['name'], info['email'], 'NIL', 'user_role', 1,)
	# cursor.execute(my_query, data)
	# mysql.connection.commit()
	# print("userinfo ==============", info)
	# print("email ++++++++++++", info['email'])
	return redirect(url_for("home_view"))



# =================================== Teacher type view ===============================
@app.route('/teacher_type', methods=['GET','POST'])
def teacher_type_view():

	if request.method == 'POST':
		teacher_type= request.form['degreeTypeId']
		if teacher_type:
			ful_name = request.form['fullname']
			comp_name = request.form['companyname']
			role_title = request.form['role/job']
			display_name = request.form['dis_name']
			teacher_type_mode(session["id"], teacher_type,ful_name,comp_name,role_title,display_name)

			return redirect(url_for('teacher_detail_view'))
		else:
			return render_template('teacher1.html', msg = "Trigger function")
	else:
		return render_template('teacher1.html')


# =================================== Teacher details view ===============================
@app.route('/teacher_detail', methods=['GET','POST'])
def teacher_detail_view():
	if request.method == 'POST':
		speciality = request.form['speciality']
		gender = request.form['gender']
		dob = request.form['dob']
		if speciality and gender and dob:

			teacher_detail_mode(speciality, gender, dob, session["id"])
			return redirect(url_for('teacher_address_view'))
		else:
			return render_template('teacher2.html', msg="trigger function")
	else:
		return render_template('teacher2.html')



# =================================== Teacher address view ===============================
@app.route('/teacher_address', methods=['GET', 'POST'])
def teacher_address_view():
	if request.method == 'POST':
		location = request.form['location']
		zip = request.form['zip']
		if location:

			teacher_address_mode(location, zip, session["id"])
			return redirect(url_for('teacher_phone_view'))
		else:
			return render_template('teacher3.html', msg = "trigger function")
	else:
		return render_template('teacher3.html')



# =================================== Techer phone ===============================
@app.route('/teacher_phone', methods=['GET', 'POST'])
def teacher_phone_view():
	if request.method == 'POST':
		c_code = request.form['c-code']
		phone = request.form['phone']
		if c_code and phone:
			cc_code = c_code.split(" ")
			contact_no = cc_code[0] + phone
			session['contact_no'] = contact_no
			teacher_phone_mode(contact_no, session["id"])
			otp= random.randint(100000,999999)
			sms_sender(otp)
			session['otp'] = otp
			return redirect(url_for('teacher_phone_verify_view'))
		else:
			return render_template('teacher4.html', msg = "trigger message")
	else:
		return render_template('teacher4.html')


# =============================== Teacher phone verify ====================
@app.route('/teacher_phone_verify', methods=['GET','POST'])
def teacher_phone_verify_view():
	if request.method == 'POST':
		my_otp = request.form['password-register']
		my_otp = int(my_otp)
		if my_otp == session['otp']:

			teacher_phone_verify_mode(session["id"])
			return render_template('teacher_phone_code4.html', mxg="trigger1")
			
	else:
		return render_template('teacher_phone_code4.html')		




#=================================== Teacher Subject ========================
@app.route('/teacher_subject', methods=['GET', 'POST'])
def teacher_subject_view():
	if request.method == 'POST':
		subject = request.form['subjects']
		level = request.form['level']
		high_level = request.form['highlevel']
		teacher_subject_mode(session["id"], subject, level, high_level)
		return redirect(url_for('teacher_certification_view'))
	else:
		return render_template('teacher5.html')


# =============================== Teacher Certification Delete ========================
@app.route('/teacher_delete_records/<string:id>')
def teacher_delete_view(id):
	para =  request.args.get('type')
	if para == '"table1"':
		table_name = 'user_education_info'
		temp_name ='teacher_certification_view'
		col_name = 'education_id'
	elif para == '"table2"':
		table_name = 'user_experience_info'
		temp_name = 'teacher_experience_view'
		col_name = 'experience_id'
	
	
	teacher_delete_mode(id, table_name, col_name)
	return redirect(url_for(temp_name))


# # =============================== Teacher Certification Edit ========================
@app.route('/teacher_edit/<id>', methods=['GET', 'POST'])
def teacher_edit_view(id):
	session['myid'] = id
	if request.method == 'POST':
		inst_name = request.form['Institution']
		deg_type = request.form['degreeTypeId']
		deg_name = request.form['degree_name']
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		association = request.form['association']
		speciality = request.form['speciality']
		score = request.form['score']

		teacher_edit_post_mode(inst_name,deg_type,deg_name,start_date,end_date,association,speciality,score,id)
		return redirect(url_for('teacher_certification_view'))
	else:
		mydata = teacher_edit_get_post(id) 
		return render_template('teacher6.html', mydata=mydata, edit='yes')



#======================================= Techer Certification =============================
@app.route('/teacher_certification', methods=['GET', 'POST'])
def teacher_certification_view():
	if request.method == 'POST':
		inst_name = request.form['Institution']
		deg_type = request.form['degreeTypeId']
		deg_name = request.form['degree_name']
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		association = request.form['association']
		speciality = request.form['speciality']
		score = request.form['score']

		teacher_certificate_post_mode(session["id"],inst_name,deg_type,deg_name,start_date,end_date,association,speciality,score)

	mydata=teacher_certificate_get_mode(session["id"])
	return render_template('teacher6.html', mydata=mydata)


# ============================== Teacher Experience update ===================
@app.route('/teacher_edit_experince/<id>', methods=['GET', 'POST'])
def teacher_edit_experience_view(id):
	session['myide'] = id
	if request.method == 'POST':
		org_name = request.form['org_name']
		designation = request.form['designation']
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		association = request.form['association']
		job_decs = request.form['job_decs']

		teacher_edit_exp_post(org_name, designation, start_date, end_date, association, job_decs,id)
		return redirect(url_for('teacher_experience_view'))

	else:
		mydata=teacher_edit_exp_get(id)
		return render_template('teacher7.html', mydata=mydata, edit='yes')
		



# =============================== Teacher Experience ===========================	
@app.route('/teacher_experience', methods=['GET', 'POST'])
def teacher_experience_view():
	if request.method == 'POST':
		org_name = request.form['org_name']
		designation = request.form['designation']
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		association = request.form['association']
		job_decs = request.form['job_decs']

		teacher_exp_post(session["id"],org_name, designation, start_date, end_date, association, job_decs)


	mydata= teacher_exp_get(session["id"])
	return render_template('teacher7.html', mydata=mydata)



# =============================== Teacher Teaching Details ==========================
@app.route('/teacher_teaching_details', methods=['GET', 'POST'])
def teacher_teaching_details_view():
	if request.method == 'POST':
		pay_dur = request.form['pay_dur']
		min_fee = request.form['min_fee']
		max_fee = request.form['max_fee']
		fee_detail = request.form['fee_detail']
		year_exp = request.form['year_exp']
		# tech_exp = request.form['tech_exp']
		radio_1 = request.form['radio-1']
		distance = request.form['distance']
		online_teaching = request.form['online_teaching']
		digital_pen = request.form['digital_pen']
		assignment = request.form['assignment']
		jpo = request.form['jpo']
		association = request.form['association']

		teacher_teaching_detail_mode(session['id'],pay_dur, min_fee, max_fee, fee_detail, year_exp, radio_1, distance, online_teaching, digital_pen, assignment, jpo, association)
		return redirect(url_for('teacher_description_view'))
	else:
		return render_template('teacher8.html')



# ================================= Teacher Description ======================= 
@app.route('/teacher_description', methods=['GET', 'POST'])
def teacher_description_view():
	if request.method == 'POST':
		desc = request.form['text']

		teacher_description_mode(desc, session["id"])
		return redirect(url_for('teacher_verification_view'))
	else:
		return render_template('teacher9.html')



# ============================== Teacher Id Verify ============================
@app.route('/teacher_id_verify', methods=['GET', 'POST'])
def teacher_verification_view():

	if request.method == 'POST':
		myfile = request.files['ufile']
		path = f'static/files/{session["id"]}'
		if not os.path.exists(path):
			os.makedirs(path)
		
		myfile.filename = 'verify_doc.pdf'
		doc_type = request.form['doc_type']
		myfile.save(os.path.join(f'static/files/{session["id"]}', myfile.filename))

		teacher_verification_mode(session["id"],myfile.filename,doc_type)
		return redirect(url_for('home_view'))
	
	return render_template('teacher10.html')


#=============================== Student role ===========================
@app.route('/student_role', methods=['GET', 'POST'])
def student_role_view():
	if request.method == "POST":
		role = request.form['role']
		if role != "Company/Mediator":

			student_role_std_mode(session["id"], role)
			return redirect(url_for('student2_view'))
		else:
			fullname = request.form['fullname']
			company_name = request.form['company_name']
			display_name = request.form['display_name']

			student_role_comp_mode(session["id"], company_name, fullname, display_name)
			return redirect(url_for('student2_view'))
	else:
		return render_template('student1.html')



#============================ Student 2 ========================
@app.route('/student2', methods=['GET', 'POST'])
def student2_view():
		return render_template('student2.html')



#================================ Student request tutor ======================
@app.route('/student_req_tutor', methods=['GET', 'POST'])
def student_req_tutor_view():
	if request.method == "POST":
		location = request.form['location']
		c_code = request.form['c-code']
		phone = request.form['phone']
		session['phone'] = phone
		detail_req = request.form['detail_req']
		radio = request.form['radio']
		# distance = request.form['distance']
		budget = request.form['budget']
		pay_type = request.form['pay_type']
		cc_code = c_code.split(" ")
		contact_no = cc_code[0] + phone
		session['contact_no'] = contact_no

		student_req_tutor_mode(location, contact_no, detail_req, radio, budget, pay_type, session["id"])
		return redirect(url_for('phone_code_send'))
	else:
		return render_template('student3.html')

@app.route('/phone_code_send', methods=['GET'])
def phone_code_send():
	otp= random.randint(100000,999999)
	sms_sender(otp)
	session['otp'] = otp
	return redirect(url_for('student_verify_code_view'))


# ================================ Student verify phone =====================
@app.route('/student_verify_code', methods=['GET', 'POST'])
def student_verify_code_view():
	if request.method == "POST":
		# print(request.form)
		my_otp = request.form['password-register']
		my_otp = int(my_otp)
		if my_otp == session['otp']:

			student_verify_mode(session["id"])
			return render_template('student_phone_code4.html', mxg="trigger1")
			
	else:
		return render_template('student_phone_code4.html')


@app.route('/student_phone_verified', methods=['GET', 'POST'])
def student_phone_veified():
	if request.method == "POST":
		return redirect(url_for('student_subject_teacher_view'))# change it afterward if need
	else:
		return redirect(url_for('student_subject_teacher_view'))# change to verify4 after confirmation



#=================================== student subject teacher ==================
@app.route('/student_subject_teacher', methods=['GET', 'POST'])
def student_subject_teacher_view():
	if request.method == "POST":
		subject = request.form['subjects']
		level = request.form['level']
		high_level = request.form['highlevel']

		student_subject_mode(subject, level, high_level, session["id"])
		return redirect(url_for('student_last_data_view'))
	else:
		return render_template('student5.html')


@app.route('/student_last_data', methods=['GET', 'POST'])
def student_last_data_view():
	if request.method == 'POST':
		gender = request.form['genderPreference']
		no_tutor = request.form['noOfRequiredTutors']
		association  = request.form['association']
		lang = request.form['languages']
		myfile = request.files['ufile']
		path = f'static/files/{session["id"]}'
		if not os.path.exists(path):
			os.makedirs(path)
		
		myfile.save(os.path.join(f'static/files/{session["id"]}', myfile.filename))

		student_last_data_mode(f'static/files/{session["id"]}/{myfile.filename}', myfile.filename, lang, gender, no_tutor, association, session["id"])
		return redirect(url_for('teacher_req_view'))
	else:

		lang = student_last_data_get_mode()
		return render_template('student_last_data.html', lang = lang)


# ========================= student request view ===================
@app.route('/teacher_req_view', methods=['GET','POST'])
def teacher_req_view():

	mydata=teacher_req_mode(session["id"])
	return render_template('student6.html', data=mydata)


#=========================== Student Last review =====================
@app.route('/student_last_review', methods=['GET'])
def student_last_review_view():

	row = student_last_mode(session["id"])
	lang = row[0]['lang']
	my_lang = lang.split(",")
	b = []
	for i in my_lang:
		b.append(int(i))
	lang_data = tuple(b)

	row2 = student_last1_mode(lang_data)
	time = str(datetime.datetime.now() - row[0]['date_time'])[0][0]
	print(time)
	return render_template('student7.html', mydata=row , time=time, lang_data=row2)



# =========================================== Stripe Payment =============================
@app.route('/create-checkout-session',methods=['GET'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price':'price_1Ld7IEIO68NMTnSrOSUlny5F', # dynamically change when we build frontend of checkout
                    'quantity':1
                }
            ],
            mode='payment',
            success_url="http://127.0.0.1:5000/thanks",
            cancel_url="http://127.0.0.1:5000/"
        )
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url,code=303)


@app.route('/webhook', methods=['POST'])
def webhook():
	event = None
	payload = request.get_data()
	sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
	endpoint_secret = "whsec_140962aabc5be00a0307af69dc45a00031a71e5eb6d928d551a60865339d751e"

	try:
		event = stripe.Webhook.construct_event(
			payload, sig_header, endpoint_secret
		)
	except ValueError as e:
		# Invalid payload
		raise e
	except stripe.error.SignatureVerificationError as e:
		# Invalid signature
		raise e

	# Handle the event
	if event['type'] == 'payment_intent.succeeded':
		payment_intent = event['data']['object']
		# print(payment_intent)
		# print(payment_intent['charges']['data'][0]['billing_details']['address']['country'])
	# ... handle other event types
	else:
		print('Unhandled event type {}'.format(event['type']))
	
	return {}


# ===================================== Remove later ============================
@app.route('/thanks')
def thanks_view():
	return render_template('thanks.html')


# ================================= stripe and Db product Curd =====================
@app.route('/v1/products', methods=['POST'])
def stripe_product():
	if request.method == 'POST':
		product=stripe.Product.create(name="Gold Special17" ,description="abcd product" ,default_price_data={"currency":"usd" ,"unit_amount":5000*100})
		name = product['name']
		description = product['description']
		product_id = product['id']
		default_price = product['default_price']
		active = str(product['active'])
		cursor = mysql.connection.cursor()
		my_query = """INSERT INTO product_detail (product_name, product_description, active, product_price, product_id) VALUES (%s,%s,%s,%s,%s)"""
		data = (name,description,active,default_price,product_id,)
		cursor.execute(my_query, data)
		mysql.connection.commit()
	return f'{name, product_id}'

@app.route('/v1/products/<id>', methods=['GET', 'POST', 'DELETE'])
def stripe_product_curd(id):

	if request.method == 'DELETE':
		#put logic here to delete from db set active = false
		cursor = mysql.connection.cursor()
		my_query = """UPDATE product_detail SET active = 'False' WHERE product_id=%s"""
		data = (id,)
		cursor.execute(my_query, data)
		mysql.connection.commit()

	# if request.method == 'POST':
		# stripe.Product.modify(id, name="qwerty",) it is to update on db
		# here comes logic of update into db
	return ""






# teacher profile
# @app.route('/teacher-profile')
# def teacher_profile_view():
# 	return render_template('teacher_profile.html')



if __name__ == "__main__":
	app.run(port=5000, debug=True)