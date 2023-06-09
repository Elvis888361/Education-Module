# Copyright (c) 2023, cbigdl and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class StudentResult(Document):
	pass

@frappe.whitelist()
def get_student_result(doc):
	student_data = frappe.db.get_all(
		"Examination Marks Entry",
		fields=[
		'admission_number',
		'student_name',
		'subject',
		'marks',
		'grade',
		'form',
		'academic_terms'
	]
	)[0]
	print(f"\n\n\n{student_data}")
	return student_data