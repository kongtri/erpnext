# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'course',
<<<<<<< HEAD
		'transactions': [
			{
				'label': _('Program and Course'),
				'items': ['Program', 'Course Enrollment', 'Course Schedule']
=======
		'non_standard_fieldnames': {
		},
		'transactions': [
			{
				'label': _('Course'),
				'items': ['Course Enrollment', 'Course Schedule']
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
			},
			{
				'label': _('Student'),
				'items': ['Student Group']
			},
			{
				'label': _('Assessment'),
<<<<<<< HEAD
				'items': ['Assessment Plan', 'Assessment Result']
=======
				'items': ['Assessment Plan']
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
			},
		]
	}