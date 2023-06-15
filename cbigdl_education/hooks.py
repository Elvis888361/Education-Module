from . import __version__ as app_version

app_name = "cbigdl_education"
app_title = "Cbigdl Education"
app_publisher = "cbigdl"
app_description = "Education Management System"
app_email = "gkdevs50@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cbigdl_education/css/cbigdl_education.css"
# app_include_js = "/assets/cbigdl_education/js/cbigdl_education.js"

# include js, css files in header of web template
# web_include_css = "/assets/cbigdl_education/css/cbigdl_education.css"
# web_include_js = "/assets/cbigdl_education/js/cbigdl_education.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cbigdl_education/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "cbigdl_education.utils.jinja_methods",
#	"filters": "cbigdl_education.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cbigdl_education.install.before_install"
# after_install = "cbigdl_education.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cbigdl_education.uninstall.before_uninstall"
# after_uninstall = "cbigdl_education.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cbigdl_education.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"cbigdl_education.tasks.all"
#	],
#	"daily": [
#		"cbigdl_education.tasks.daily"
#	],
#	"hourly": [
#		"cbigdl_education.tasks.hourly"
#	],
#	"weekly": [
#		"cbigdl_education.tasks.weekly"
#	],
#	"monthly": [
#		"cbigdl_education.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "cbigdl_education.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "cbigdl_education.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "cbigdl_education.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["cbigdl_education.utils.before_request"]
# after_request = ["cbigdl_education.utils.after_request"]

# Job Events
# ----------
# before_job = ["cbigdl_education.utils.before_job"]
# after_job = ["cbigdl_education.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"cbigdl_education.auth.validate"
# ]

fixtures = [
    "Client Script",
    "Custom Field",
    "Print Format",
    "Property Setter"
]
jinja = {
    "methods": [
    "cbigdl_education.cbigdl_education.doctype.student_result.student_result.get_student_result",
    "cbigdl_education.services.rest.get_book_details",
    "cbigdl_education.cbigdl_education.doctype.examination_marks_entry.examination_marks_entry.get_student_result",
    "cbigdl_education.cbigdl_education.doctype.student_individual_result.student_individual_result.get_student_name"
    ]
}
  

