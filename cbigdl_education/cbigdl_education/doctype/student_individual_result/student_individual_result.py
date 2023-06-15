# Copyright (c) 2023, cbigdl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentIndividualResult(Document):
	pass
@frappe.whitelist()
def get_student_result(doc):
	student_data = frappe.db.sql("""
		SELECT
			t1.name,
			t1.academic_terms,
			t1.form,
			t1.subject,
			t2.admission_number,
			t2.grade,
			t2.cat_marks,
			t2.exam_marks,
			t2.total_marks,
			t3.admission_number,
			t3.student_name
		FROM
			`tabExamination Marks Entry` t1
		JOIN
			`tabStudent Marks` t2 ON t1.name = t2.parent
		JOIN
			`tabStudent Registration` t3 ON t2.admission_number = t3.name;
	""", as_dict=1
	)
	return student_data

@frappe.whitelist()
def get_student_name(doc):
	student_data = frappe.db.sql("""
		SELECT
			admission_number,
			student_name
		FROM
			`tabStudent Registration`
	""", as_dict=1
	)
	return student_data