// Copyright (c) 2023, kevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Record', {
	refresh: function(frm) {
		frm.set_df_property('class', 'hidden', 1)
	},

	refresh: function(frm){
		// frm.set_query("admission_number", function() {
		// 	return {
		// 		"filters": {
		// 		"class_group":frm.doc.class_group
		// 		}
		// 	};
		// 	});
	}
});
