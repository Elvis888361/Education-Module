// Copyright (c) 2023, kevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library', {
	refresh: function(frm) {
		frm.set_query("item_code", function() {
			return {
			  "filters": {
				"item_group": "Book",
			  }
			};
		  });
	},

	item_code: function(frm){
		let qty = '0'
		frm.set_value("quantity", qty)
	}
});
