// Copyright (c) 2023, cbigdl and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Class Group List"] = {
	filters: [
		
		{
		  fieldname: "class_group",
		  label: __("Class Group"),
		  fieldtype: "Link",
		  options: "Class Group",
		  width: 100,
		  reqd: 1,
		  default: "Form 1"
		},
		{
		  fieldname: "class",
		  label: __("Class"),
		  fieldtype: "Link",
		  options: "Class",
		  width: 100,
		  reqd: 0,
		},
		{
		  fieldname: "admission_number",
		  label: __("Admission Number"),
		  fieldtype: "Link",
		  options: "Student Registration",
		  width: 100,
		  reqd: 0,
		}
	  ],
};
