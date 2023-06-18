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

@frappe.whitelist(allow_guest=True)
def create_student_result(admission_number,form,marks,grade):
    student_exists=frappe.db.sql(f"""SELECT COUNT(admission_number) FROM Student Result WHERE admission_number={admission_number} AND form={form}""")
    if student_exists is None or student_exists == 0:
        
        insert_student_result=frappe.get_doc({
        "doctype":"Student Result",
        "admission_number":admission_number,
        "Marks":marks,
        "total_grade":grade
        })
        insert_student_result.insert(ignore_permissions=True)
        frappe.db.commit()
    else:
        print(student_exists)

#get which class the book belong from library
@frappe.whitelist()
def get_class(book_description):
    class_group= frappe.db.get_value('Library', {"name": book_description}, "class")
    return class_group

#update the status of book in the book record to issued
@frappe.whitelist()
def update_book_status_to_issued(book_number, admission_number):
    frappe.db.set_value('Book Record', book_number, 'status', 'Issued')
    frappe.db.set_value('Book Record', book_number, 'issued_to', admission_number)


# Update the status of the book in the book record to available
@frappe.whitelist()
def update_book_status_to_available(book_number,admission_number):
    frappe.db.set_value('Book Record', book_number, 'status', 'Available')
    frappe.db.set_value('Book Record', book_number, 'received_from',admission_number)

#update who is issued book in book record form student book record
@frappe.whitelist()
def get_admission_issued_book(book_number):
    admission_issued_book = frappe.db.get_value("Book Record", {"name": book_number}, 'issued_to')
    return admission_issued_book


#update number of books in library from student book record
@frappe.whitelist()
def update_number_of_books_in_library(book_description):
    qty_from_library = frappe.db.get_value('Library', {'name': book_description}, 'quantity')
    new_qty_in_library = int(qty_from_library) + 1
    frappe.db.set_value('Library', {'name': book_description}, 'quantity',new_qty_in_library)


@frappe.whitelist()
def get_student_name(student_admission):
    student_name = frappe.db.get_value('Student Registration', {'name': student_admission}, 'student_name')
    return student_name
#update number of books in library from student book record when issued direct from library
@frappe.whitelist()
def update_number_of_books(book_description):
    qty_from_library = frappe.db.get_value('Library', {'name': book_description}, 'quantity')
    new_qty_in_library = int(qty_from_library) - 1
    frappe.db.set_value('Library', {'name': book_description}, 'quantity',new_qty_in_library)

@frappe.whitelist()
def get_staff_name(cleared_by):
    staff_name = frappe.db.get_value('Employee', {'name': cleared_by}, 'first_name')
    return staff_name



@frappe.whitelist()
def get_book_details(doc):
    sql_book_details= f"""
	SELECT 
      book_description,
      class_group,
      book_number,
      issued_to,
      status
	FROM
	  `tabBook Record`
    """
    book_details = frappe.db.sql(sql_book_details, as_dict=True)
    return book_details

