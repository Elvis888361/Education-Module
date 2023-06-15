// Copyright (c) 2023, kevin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book', {
	refresh: function(frm) {
	},

	on_submit: function(frm) {
		frappe.call({
			method: 'cbigdl_education.services.rest.update_number_of_books',
			args: {
				'name': frm.doc.name
			},
			callback: function(r) {
				// The update_number_of_books function has finished executing
			},
	});
	}
});


frappe.ui.form.on("Book Items", {
	book_description: function(frm, cdt, cdn) {
		let Item = locals[cdt][cdn];
		let book_description = Item.book_description;
		frappe.call({
			method: 'cbigdl_education.services.rest.get_qty_from_library',
			args: {
				'book_description': book_description
			},
			callback: function(r) {
			  let qty= r.message
			  frappe.model.set_value(cdt, cdn, {
				'qty_in_store':qty
			});  
			},
		});
	},
	quantity: function(frm, cdt, cdn) {
		let Item = locals[cdt][cdn];
		let quantity = parseInt(Item.quantity);
		let qty_in_store = parseInt(Item.qty_in_store);
		let new_qty = quantity + qty_in_store;
		frappe.model.set_value(cdt, cdn, {
			'new_qty':new_qty
		});  
		update_qty_received(frm)
	  },
	items_remove: function(frm, cdt, cdn){
		update_qty_received(frm)
	}
  })


  function update_qty_received(frm) {
    let total= 0;
    for (let item of frm.doc.items) {
		total+= parseInt(item.quantity)
    }
    frm.set_value({
          'qty_received':total
        })  
}
