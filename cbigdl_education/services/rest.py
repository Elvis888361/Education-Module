import frappe

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
    