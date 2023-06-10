import frappe

@frappe.whitelist()
def update_number_of_books(name):
    # Retrieve book information from the 'Book Items' table
    book_information = frappe.get_all(
        'Book Items',
        filters={'parent': name},
        fields=[
            'book_description',
            'quantity',
            ]
    )

    for book_inform in book_information:
        item_code = book_inform.get('book_description')
        quantity = book_inform.get('quantity')

        # Retrieve library information from the 'Library' table
        library_information = frappe.get_all(
            'Library',
            filters={
                'name':item_code,
            },
            fields=[
                'name',
                'quantity']
        )
        for library_info in library_information:
            library_name = library_info.get('name')
            actual_qty = library_info.get('quantity')

            # Add the quantity from 'Book Items' to the 'actual_qty' in 'Library'
            new_actual_qty = int(actual_qty) + int(quantity)

            # Update the 'quantity' in 'Library' with the new value
            frappe.db.set_value(
                'Library',
                library_name,
                'quantity',
                new_actual_qty
            )


@frappe.whitelist()
def get_qty_from_library(book_description):
    qty_from_library = frappe.db.get_value('Library', {'name': book_description}, 'quantity')
    return qty_from_library

@frappe.whitelist()
def get_teacher_name(teacher_number):
    teacher_name = frappe.db.get_value('Employee', {"name": teacher_number}, 'employee_name')
    return teacher_name


@frappe.whitelist()
def update_qty_in_library(book_description,qty_to_issue, qty_in_library):
    new_qty_in_library = int(qty_in_library) - int(qty_to_issue)
    frappe.db.set_value('Library', {'name': book_description}, 'quantity',new_qty_in_library)


@frappe.whitelist()
def update_new_qty_in_library(book_description,qty_to_issue, qty_in_library):
    new_qty_in_library = int(qty_in_library) + int(qty_to_issue)
    frappe.db.set_value('Library', {'name': book_description}, 'quantity',new_qty_in_library)


