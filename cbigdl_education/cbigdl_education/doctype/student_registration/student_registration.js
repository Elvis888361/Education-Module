// Copyright (c) 2023, cbigdl and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Registration', {
    student_group: function(frm) {
        cur_frm.fields_dict['class'].get_query = function(doc) {
            return {
                filters: {
                    "parent": frm.doc.student_group,
                }
            }
        }
    }
});