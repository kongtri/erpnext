# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'assessment_plan',
<<<<<<< HEAD
=======
		'non_standard_fieldnames': {
		},
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
		'transactions': [
			{
				'label': _('Assessment'),
				'items': ['Assessment Result']
			}
<<<<<<< HEAD
		],
		'reports': [
			{
				'label': _('Report'),
				'items': ['Assessment Plan Status']
			}
=======
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
		]
	}