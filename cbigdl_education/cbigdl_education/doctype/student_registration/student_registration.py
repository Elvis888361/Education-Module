# Copyright (c) 2023, cbigdl and contributors
# For license information, please see license.txt

import frappe
import dateutil
from frappe import _
from frappe.utils import getdate, today
from frappe.model.document import Document

class StudentRegistration(Document):
	def validate(self):
		self.set_title()
		self.validate_dates()
		self.calculate_age()

	def set_title(self):
		self.student_name = " ".join(
			filter(None, [self.first_name, self.middle_name, self.last_name])
		)

	def validate_dates(self):
		for sibling in self.siblings:
			if sibling.date_of_birth and getdate(sibling.date_of_birth) > getdate():
				frappe.throw(
					_("Row {0}:Sibling Date of Birth cannot be greater than today.").format(
						sibling.idx
					)
				)

		if self.date_of_birth and getdate(self.date_of_birth) >= getdate():
			frappe.throw(_("Date of Birth cannot be greater than today."))

		if self.date_of_birth and getdate(self.date_of_birth) >= getdate(self.joining_date):
			frappe.throw(_("Date of Birth cannot be greater than Joining Date."))

		if (
			self.joining_date
			and self.date_of_leaving
			and getdate(self.joining_date) > getdate(self.date_of_leaving)
		):
			frappe.throw(_("Joining Date can not be greater than Leaving Date"))


	def calculate_age(self):
		if not self.date_of_birth:
			return
		date_of_birth = getdate(self.date_of_birth)
		age = dateutil.relativedelta.relativedelta(getdate(), date_of_birth)
		self.age = f'{age.years} Years'

	
	def after_insert(self):
		customers = frappe.db.get_all(
			"Customer",
			fields=["admission_number"],
			or_filters={"admission_number": self.admission_number},
		)
		if customers and customers[0]:
			frappe.throw(
				_(
					"Customer exists with Admission Number {}<br>Please check Admission Number."
				).format(frappe.bold(customers[0].admission_number)),
				frappe.DuplicateEntryError,
			)

		customer = frappe.get_doc(
			{
				"doctype": "Customer",
				"customer_name": self.student_name,
				"admission_number": self.admission_number,
				"gender": self.gender,
				"customer_type": "Individual",
				"customer_group": "Individual",
				"territory": "Kenya",
			}
		)
		customer.insert()