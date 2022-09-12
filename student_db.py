from flask_mysqldb import MySQL
import datetime
from config import app , mysql



def student_role_std_mode(id, role):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO student_table (user_id_fk, std_type) VALUES (%s,%s)"""
    data = (id, role,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def student_role_comp_mode(id, company_name, fullname, display_name):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO student_company (std_user_id, std_company_name, std_company_fullname, std_compnay_disname) VALUES (%s,%s,%s,%s)"""
    data = (id, company_name, fullname, display_name)
    cursor.execute(my_query, data)
    mysql.connection.commit()
    my_query = """UPDATE student_table SET std_company = 1 WHERE user_id_fk=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def student_req_tutor_mode(location, contact_no, detail_req, radio, budget, pay_type, id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE student_table SET std_location=%s, std_phone_no=%s, std_req=%s, std_mode=%s, std_budget=%s, std_charge_for=%s WHERE user_id_fk=%s"""
    data = (location, contact_no, detail_req, radio, budget, pay_type, id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def student_verify_mode(id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE student_table SET ph_no_verify = 1 WHERE user_id_fk=%s"""
    data = (id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def student_subject_mode(subject, level, high_level, id):
    cursor = mysql.connection.cursor()
    my_query = """INSERT INTO subj_learn (subject_name, subj_level, help_want, std_id_fk) VALUES (%s,%s,%s,%s)"""
    data = (subject, level, high_level, id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def student_last_data_mode(filepath,myfile, lang, gender, no_tutor, association, id):
    cursor = mysql.connection.cursor()
    my_query = """UPDATE subj_learn SET file_path=%s, file_name=%s, date_time=%s, file_type=%s, lang=%s, gender=%s, tutor=%s, association=%s WHERE std_id_fk=%s"""
    data = (filepath, myfile, datetime.datetime.now(), '.pdf', lang, gender, no_tutor, association, id,)
    cursor.execute(my_query, data)
    mysql.connection.commit()

def student_last_data_get_mode():
    cursor = mysql.connection.cursor()
    my_query = """select id, language_name from languages"""
    cursor.execute(my_query)
    row = cursor.fetchall()
    return row

def teacher_req_mode(id):
    cursor = mysql.connection.cursor()
    my_query="""select std.std_location,std.std_mode, std.std_req,subj.subject_name, subj.subj_level, subj.help_want 
        from student_table std INNER JOIN subj_learn subj
        ON std.user_id_fk=subj.std_id_fk where std.user_id_fk=%s"""
    data =(id,)
    cursor.execute(my_query, data)
    row = cursor.fetchall()
    return row

def student_last_mode(id):
    cursor = mysql.connection.cursor()
    my_query="""select std.std_location,std.std_mode, std.std_phone_no,std.std_type,
        std.std_req,subj.subject_name, subj.lang, subj.subj_level, subj.association, subj.gender, subj.date_time, subj.help_want, login.user_name
    from student_table std INNER JOIN subj_learn subj
    ON std.user_id_fk=subj.std_id_fk INNER JOIN login ON std.user_id_fk=login.id_pk where login.id_pk=%s"""
    data =(id,)
    cursor.execute(my_query, data)
    row = cursor.fetchall()
    return row

def student_last1_mode(lang_data):
    cursor = mysql.connection.cursor()
    my_query1 = """SELECT language_name FROM languages WHERE id IN %s"""
    cursor.execute(my_query1, (lang_data,))
    row2 = cursor.fetchall()
    return row2


def student_tutor_mode():
    cursor = mysql.connection.cursor()
    my_query = """SELECT user_name, profile_description, year_exper, maximum_fee, 
    job_title, teach_i_charge,location FROM login INNER JOIN teaching_details ON login.id_pk = teaching_details.user_id_fk INNER JOIN user_experience_info ON user_experience_info.user_id_fk = login.id_pk INNER JOIN personal_info ON personal_info.user_id_fk= login.id_pk"""
    cursor.execute(my_query)
    row = cursor.fetchall()
    return row


def filter_by_loc_mode():
    cursor = mysql.connection.cursor()
    my_query = f"""SELECT user_name, teach_i_charge, profile_description, 
    year_exper, maximum_fee, job_title, location 
    FROM login INNER JOIN teaching_details ON login.id_pk = teaching_details.user_id_fk 
    INNER JOIN user_experience_info ON user_experience_info.user_id_fk = login.id_pk 
    INNER JOIN personal_info ON personal_info.user_id_fk= login.id_pk"""
    cursor.execute(my_query)
    row = cursor.fetchall()
    print(row)
    return(row)