from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname':  'leave_policy',
		'transactions': [
			{
<<<<<<< HEAD
=======
				'label': _('Employees'),
				'items': ['Employee', 'Employee Grade']
			},
			{
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
				'label': _('Leaves'),
				'items': ['Leave Allocation']
			},
		]
	}	
