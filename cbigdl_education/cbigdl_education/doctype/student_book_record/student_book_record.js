// Copyright (c) 2023, cbigdl and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Book Record', {
	refresh: function(frm) {
		frm.set_query("book_number", function() {
			return {
			  "filters": {
				"status": "Available",
				"class_group":frm.doc.class_group
			
			  }
			};
		  });

		frm.set_query("admission_number", function() {
			return {
			  "filters": {
				"student_group":frm.doc.class_group
			
			  }
			};
		  });  
	},
	book_number: function(frm){
		console.log(frm.doc.class_group);
	},
	is_returned: function(frm){
		if(frm.doc.is_returned){
		frm.set_df_property('admission_number', 'read_only', 1)
		frm.set_query("book_number", function() {
			return {
				"filters": {
				"status": "Issued",
				"class_group":frm.doc.class_group
				}
			};
			});
		}else{
		frm.set_df_property('admission_number', 'read_only', 0)
		frm.set_query("book_number", function() {
			return {
				"filters": {
				"status": "Available",
				"class_group":frm.doc.class_group
				}
			};
			});
		}
	},

	before_save: function(frm){
		let date = frappe.datetime.get_today()
		frm.set_value("year", date);
	},

	book_description: function(frm){
		frappe.call({
			method: 'cbigdl_education.services.rest.get_class',
			args: {
				'book_description': frm.doc.book_description
			},
			callback: function(r) {
				let class_group = r.message
				frm.set_value('class_group', class_group)
			},
	});
	},


	class_group: function(frm){
		frm.set_query("class", function() {
			return {
			  "filters": {
				"parent": frm.doc.class_group,
			  }
			};
		  });
	},


	book_number: function(frm){
		if(frm.doc.is_returned){
			frappe.call({
				method: 'cbigdl_education.services.rest.get_admission_issued_book',
				args: {
					'book_number': frm.doc.book_number,
				},
				callback: function(r) {
					let admission_number = r.message
					frm.set_value('admission_number', admission_number)
				},
			});
		}
	},


	on_submit: function(frm){

		if(frm.doc.issue){
			frappe.call({
				method: 'cbigdl_education.services.rest.update_book_status_to_issued',
				args: {
					'book_number': frm.doc.book_number,
					'admission_number': frm.doc.admission_number
				},
				callback: function(r) {
				},
			});
			frappe.call({
				method: 'cbigdl_education.services.rest.update_number_of_books',
				args: {
					'book_description': frm.doc.book_description,
				},
				callback: function(r) {
				},
			});
		}
		if(frm.doc.is_returned){
			frappe.call({
				method: 'cbigdl_education.services.rest.update_book_status_to_available',
				args: {
					'book_number': frm.doc.book_number,
					'admission_number': frm.doc.admission_number
				},
				callback: function(r) {
				},
			});
			frappe.call({
				method: 'cbigdl_education.services.rest.update_number_of_books_in_library',
				args: {
					'book_description': frm.doc.book_description,
				},
				callback: function(r) {
				},
			});
		}else{
			frappe.call({
				method: 'cbigdl_education.services.rest.update_book_status_to_issued',
				args: {
					'book_number': frm.doc.book_number,
					'admission_number': frm.doc.admission_number
				},
				callback: function(r) {
				},
			});
		}
	
	}
});
