// Copyright (c) 2023, cbigdl and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Clearance Record', {
	// refresh: function(frm) {

	// }

	student_admission: function(frm){
		frappe.call({
			method: 'cbigdl_education.services.rest.get_student_name',
			args: {
				'student_admission': frm.doc.student_admission
			},
			callback: function(r) {
				let student_name = r.message
				frm.set_value('student_name', student_name)
			},
	});
	},


	cleared_by: function(frm){
		frappe.call({
			method: 'cbigdl_education.services.rest.get_staff_name',
			args: {
				'cleared_by': frm.doc.cleared_by
			},
			callback: function(r) {
				let staff_name = r.message
				frm.set_value('staff_name', staff_name)
			},
	});
	}

});
