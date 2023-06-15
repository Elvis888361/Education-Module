// Copyright (c) 2023, cbigdl and contributors
// For license information, please see license.txt

frappe.ui.form.on('Examination Marks Entry', {
	
	academic_terms: function(frm) {
		frappe.call({
			method: 'cbigdl_education.cbigdl_education.doctype.examination_marks_entry.examination_marks_entry.get_name',
			args: {
				'academic_term':frm.doc.academic_terms,
	 			'form':frm.doc.form
			},
			callback: function(r) {
				let data=r.message
				frm.add_custom_button(__('Print Result'), function(){
					frappe.set_route('student-result/'+data, 'Student Result', data)
				}, __("Action"));
			}
		});
		
	},
	after_save:function(frm){
		frappe.call({
			method: 'cbigdl_education.cbigdl_education.doctype.examination_marks_entry.examination_marks_entry.create_student_data',
			args: {
				'academic_term':frm.doc.academic_terms,
	 			'form':frm.doc.form
			},
			callback: function(r) {

			}
		});
	}
});
