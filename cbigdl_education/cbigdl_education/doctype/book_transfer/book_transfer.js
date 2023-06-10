// Copyright (c) 2023, kevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Transfer', {

	refresh: function(frm) {
		frm.set_query("teacher_number", function() {
			return {
			  "filters": {
				"designation": "Teacher",
			  }
			};
		  });
	},

	book_description: function(frm){
		frappe.call({
			method: 'cbigdl_education.services.rest.get_qty_from_library',
			args: {
				'book_description': frm.doc.book_description
			},
			callback: function(r) {
				let qty= r.message
			  frm.set_value({
				'qty_in_library':qty
			});  
			},
		});
	},

	teacher_number: function(frm){
		frappe.call({
			method: 'cbigdl_education.services.rest.get_teacher_name',
			args: {
				'teacher_number': frm.doc.teacher_number
			},
			callback: function(r) {
				let full_name= r.message
			  frm.set_value({
				'full_name':full_name
			});  
			},
		});
	},

	qty_to_issue: function(frm){
		if(frm.doc.is_returned){
			console.log("hello");
		}else{
			let qty_to_issue = frm.doc.qty_to_issue
			let qty_in_library = frm.doc.qty_in_library
			if(qty_to_issue > qty_in_library){
				frappe.throw("Quantity to transfer cannot be more than quantity in library");
		}
		}
	},

	validate: function(frm){
		if(frm.doc.is_returned){
			console.log("hello");
		}else{
			let qty_to_issue = frm.doc.qty_to_issue
			let qty_in_library = frm.doc.qty_in_library
			if(qty_to_issue > qty_in_library){
				frappe.throw("Quantity to transfer cannot be more than quantity in library");
			}
		}
	},

	on_submit:function(frm){
		if(frm.doc.is_returned){
			frappe.call({
				method: 'cbigdl_education.services.rest.update_new_qty_in_library',
				args: {
					'book_description': frm.doc.book_description,
					'qty_to_issue': frm.doc.qty_to_issue,
					'qty_in_library': frm.doc.qty_in_library,
				},
				callback: function(r) {
				
				},
			});

		}else{
		frappe.call({
			method: 'cbigdl_education.services.rest.update_qty_in_library',
			args: {
				'book_description': frm.doc.book_description,
				'qty_to_issue': frm.doc.qty_to_issue,
				'qty_in_library': frm.doc.qty_in_library,
			},
			callback: function(r) {
			
			},
		});
		}
	}
});
