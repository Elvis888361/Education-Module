# Copyright (c) 2023, cbigdl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExaminationMarksEntry(Document):
	pass

@frappe.whitelist()
def get_grade(cat_marks,exam_marks,grade_format):
	marks=int(cat_marks)+int(exam_marks)
	grade_fromat=frappe.db.get_all('Grade Format', {'parent':grade_format}, ['grade','max_scale','min_scale'])
	for scale in grade_fromat:
		if(scale['min_scale'] <=int(marks)<=scale['max_scale']):
			return scale['grade'],marks
        
