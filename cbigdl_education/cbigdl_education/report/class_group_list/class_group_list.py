# Copyright (c) 2023, cbigdl and contributors
# For license information, please see license.txt


import frappe
from frappe import _

def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
    conditions = ""

    if filters.get('class_group'):
        conditions += f" AND sr.student_group = '{filters.get('class_group')}'"
        
    if filters.get('class'):
        conditions += f" AND sr.class = '{filters.get('class')}'"
        
    if filters.get('admission_number'):
        conditions += f" AND sr.name = '{filters.get('admission_number')}'"
        
    if filters.get('student_name'):
        conditions += f" AND sr.student_name = '{filters.get('student_name')}'"

    SQL1 = f"""
        SELECT
            sr.name,
            sr.student_name,
            sr.gender,
            sr.age,
            sr.class,
            sr.student_group
        FROM 
            `tabStudent Registration` AS sr
        WHERE
            1 =1 {conditions}
        ORDER BY 
            name ASC
    """

    data = frappe.db.sql(SQL1)

    return data



def get_columns():
	return [
		"Admission Number:Link/Student Registration:150",
		"Student Name:Link/Student Registration:350",
		"Gender:Data:100",
		"Age:Data:70",
		"Class:Data:150",
        "Student Group:0"
	]

