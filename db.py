from flask_mysqldb import MySQL
from config import app , mysql
import datetime


def teacher_type_mode(id, teacher_type,ful_name,comp_name,role_title,display_name):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO personal_info (user_id_fk, teacher_category, full_name, company_name, role_title, display_name) VALUES (%s,%s,%s,%s,%s,%s)"""
    data = (id, teacher_type,ful_name,comp_name,role_title,display_name,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_detail_mode(speciality, gender, dob, id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE personal_info SET speciality=%s, gender=%s, dob=%s WHERE user_id_fk=%s"""
    data = (speciality, gender, dob, id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_address_mode(location, zip, id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE personal_info SET location=%s, postal_code=%s WHERE user_id_fk=%s"""
    data = (location, zip, id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_phone_mode(contact_no, id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE personal_info SET phone_no=%s WHERE user_id_fk=%s"""
    data = (contact_no, id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_phone_verify_mode(id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE personal_info SET ph_no_verify = 1 WHERE user_id_fk=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_subject_mode(id, subject, level, high_level):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO user_subj_teach (user_id_fk, subj_teach_name, from_level, to_level) VALUES (%s,%s,%s,%s)"""
    data = (id, subject, level, high_level,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_delete_mode(id,table_name,col_name):
    cursor = mysql.connection.cursor()
    my_query = f"""DELETE FROM {table_name} WHERE {col_name}=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_edit_post_mode(inst_name,deg_type,deg_name,start_date,end_date,association,speciality,score,id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE user_education_info SET institue_name=%s, degree_type=%s, degree_name=%s, start_date=%s, passing_year=%s, association=%s, specialization=%s, score=%s WHERE education_id=%s"""
    data = (inst_name,deg_type,deg_name,start_date,end_date,association,speciality,score,id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_edit_get_post(id):
    cursor = mysql.connection.cursor()
    my_query = """SELECT education_id, score, association, institue_name, degree_name, start_date, passing_year, specialization, degree_type FROM user_education_info WHERE education_id=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    row = cursor.fetchall()
    return row

def teacher_certificate_post_mode(id,inst_name,deg_type,deg_name,start_date,end_date,association,speciality,score):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO user_education_info (user_id_fk, institue_name, degree_type, degree_name, start_date, passing_year, association, specialization, score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    data = (id,inst_name,deg_type,deg_name,start_date,end_date,association,speciality,score,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_certificate_get_mode(id):
    cursor = mysql.connection.cursor()
    my_query = """SELECT education_id, degree_name, institue_name, start_date, passing_year, degree_type FROM user_education_info WHERE user_id_fk=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    row = cursor.fetchall()
    return row

def teacher_edit_exp_post(org_name, designation, start_date, end_date, association, job_decs,id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE user_experience_info SET company_name=%s, job_title=%s, join_date=%s, left_date=%s, association=%s, job_description=%s WHERE experience_id=%s"""
    data = (org_name, designation, start_date, end_date, association, job_decs,id)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_edit_exp_get(id):
    cursor = mysql.connection.cursor()
    my_query = """SELECT * FROM user_experience_info WHERE experience_id=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    row = cursor.fetchall()
    return row

def teacher_exp_post(id,org_name, designation, start_date, end_date, association, job_decs):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO user_experience_info (user_id_fk, company_name, job_title, join_date, left_date, association, job_description) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    data = (id,org_name, designation, start_date, end_date, association, job_decs,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_exp_get(id):
    cursor = mysql.connection.cursor()
    my_query = """SELECT experience_id, company_name, join_date, left_date, job_title FROM user_experience_info WHERE user_id_fk=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    row = cursor.fetchall()
    return row

def teacher_teaching_detail_mode(id,pay_dur, min_fee, max_fee, fee_detail, year_exp, radio_1, distance, online_teaching, digital_pen, assignment, jpo, association):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO teaching_details (user_id_fk, teach_i_charge, minimum_fee, maximum_fee, fee_details, year_exper, travel, far_travel, online_teaching, digitalpen, Homwork_assign, current_teacher, association) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    data = (id,pay_dur, min_fee, max_fee, fee_detail, year_exp, radio_1, distance, online_teaching, digital_pen, assignment, jpo, association,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def teacher_description_mode(desc, id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE teaching_details SET profile_description=%s WHERE user_id_fk=%s"""
    data = (desc, id,)
    cursor.execute(my_query, data)

def teacher_verification_mode(id, filename, doc_type):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO user_file (file_path, file_name, datetime, file_type, user_id_fk, document_type) VALUES (%s,%s,%s,%s,%s,%s)"""
    data = (f'static/files/{id}/{filename}', filename, datetime.datetime.now(), '.pdf', id, doc_type,)
    cursor.execute(my_query, data)
    mysql.connection.commit()