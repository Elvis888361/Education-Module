# Copyright (c) 2023, cbigdl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExaminationMarksEntry(Document):
	pass

@frappe.whitelist()
def get_grade(cat_marks,exam_marks,grade_format):
	cat=(float(cat_marks)/100)*30
	marks=cat+float(exam_marks)
	grade_fromat=frappe.db.get_all('Grade Format', {'parent':grade_format}, ['grade','max_scale','min_scale'])
	for scale in grade_fromat:
		if(scale['min_scale'] <=int(marks)<=scale['max_scale']):
			return scale['grade'],marks
        
@frappe.whitelist()
def create_student_data(academic_term,form):
	academic_term_exists = frappe.db.exists("Student Result", {"academic_term": academic_term})
	if academic_term_exists:
		form_exists = frappe.db.exists("Student Result", {"form": form})
		if form_exists:
			print(f"\n\n\n{True}")
		else:
			insert_student_result=frappe.get_doc({
				"doctype":"Student Result",
				"academic_term":academic_term,
				"form":form
			})
			insert_student_result.insert(ignore_permissions=True)
			frappe.db.commit()
	else:
		insert_student_result=frappe.get_doc({
			"doctype":"Student Result",
			"academic_term":academic_term,
			"form":form
		})
		insert_student_result.insert(ignore_permissions=True)
		frappe.db.commit()
@frappe.whitelist()
def get_name(academic_term,form):
	student_data = frappe.db.sql(f"""
		SELECT
			name
		FROM
			`tabStudent Result`
		WHERE
			academic_term='{academic_term}'
		AND
			form='{form}'
	""", as_dict=1
	)
	if student_data:
		return student_data
	else:
		print("\n\n\nNo student data found.")
	
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
			t2.total_marks
		FROM
			`tabExamination Marks Entry` t1
		JOIN
			`tabStudent Marks` t2
		ON
			t1.name = t2.parent;
	""", as_dict=1
	)
	return student_data
