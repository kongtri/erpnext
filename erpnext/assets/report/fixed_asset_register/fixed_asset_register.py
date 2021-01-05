# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
<<<<<<< HEAD
from frappe.utils import cstr, today, flt, add_years, formatdate, getdate
from erpnext.accounts.report.financial_statements import get_period_list, get_fiscal_year_data, validate_fiscal_year
=======
from frappe.utils import cstr, today, flt
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	chart = prepare_chart_data(data, filters) if filters.get("group_by") not in ("Asset Category", "Location") else {}

<<<<<<< HEAD
	return columns, data, None, chart
=======
def get_columns(filters):
	return [
		{
			"label": _("Asset Id"),
			"fieldtype": "Link",
			"fieldname": "asset_id",
			"options": "Asset",
			"width": 100
		},
		{
			"label": _("Asset Name"),
			"fieldtype": "Data",
			"fieldname": "asset_name",
			"width": 140
		},
		{
			"label": _("Asset Category"),
			"fieldtype": "Link",
			"fieldname": "asset_category",
			"options": "Asset Category",
			"width": 100
		},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": 90
		},
		{
			"label": _("Purchase Date"),
			"fieldtype": "Date",
			"fieldname": "purchase_date",
			"width": 90
		},
		{
			"label": _("Available For Use Date"),
			"fieldtype": "Date",
			"fieldname": "available_for_use_date",
			"width": 90
		},
		{
			"label": _("Gross Purchase Amount"),
			"fieldname": "gross_purchase_amount",
			"options": "Currency",
			"width": 90
		},
		{
			"label": _("Asset Value"),
			"fieldname": "asset_value",
			"options": "Currency",
			"width": 90
		},
		{
			"label": _("Opening Accumulated Depreciation"),
			"fieldname": "opening_accumulated_depreciation",
			"options": "Currency",
			"width": 90
		},
		{
			"label": _("Depreciated Amount"),
			"fieldname": "depreciated_amount",
			"options": "Currency",
			"width": 90
		},
		{
			"label": _("Cost Center"),
			"fieldtype": "Link",
			"fieldname": "cost_center",
			"options": "Cost Center",
			"width": 100
		},
		{
			"label": _("Department"),
			"fieldtype": "Link",
			"fieldname": "department",
			"options": "Department",
			"width": 100
		},
		{
			"label": _("Vendor Name"),
			"fieldtype": "Data",
			"fieldname": "vendor_name",
			"width": 100
		},
		{
			"label": _("Location"),
			"fieldtype": "Link",
			"fieldname": "location",
			"options": "Location",
			"width": 100
		},
	]
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

def get_conditions(filters):
	conditions = { 'docstatus': 1 }
	status = filters.status
<<<<<<< HEAD
	date_field = frappe.scrub(filters.date_based_on or "Purchase Date")

	if filters.get('company'):
		conditions["company"] = filters.company
	if filters.filter_based_on == "Date Range":
		conditions[date_field] = ["between", [filters.from_date, filters.to_date]]
	if filters.filter_based_on == "Fiscal Year":
		fiscal_year = get_fiscal_year_data(filters.from_fiscal_year, filters.to_fiscal_year)
		validate_fiscal_year(fiscal_year, filters.from_fiscal_year, filters.to_fiscal_year)
		filters.year_start_date = getdate(fiscal_year.year_start_date)
		filters.year_end_date = getdate(fiscal_year.year_end_date)

		conditions[date_field] = ["between", [filters.year_start_date, filters.year_end_date]]
=======
	date = filters.date

	if filters.get('company'):
		conditions["company"] = filters.company
	if filters.get('purchase_date'):
		conditions["purchase_date"] = ('<=', filters.get('purchase_date'))
	if filters.get('available_for_use_date'):
		conditions["available_for_use_date"] = ('<=', filters.get('available_for_use_date'))
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
	if filters.get('is_existing_asset'):
		conditions["is_existing_asset"] = filters.get('is_existing_asset')
	if filters.get('asset_category'):
		conditions["asset_category"] = filters.get('asset_category')
<<<<<<< HEAD
	if filters.get('cost_center'):
		conditions["cost_center"] = filters.get('cost_center')
=======
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

	# In Store assets are those that are not sold or scrapped
	operand = 'not in'
	if status not in 'In Location':
		operand = 'in'

	conditions['status'] = (operand, ['Sold', 'Scrapped'])

	return conditions

def get_data(filters):

	data = []

	conditions = get_conditions(filters)
	depreciation_amount_map = get_finance_book_value_map(filters)
	pr_supplier_map = get_purchase_receipt_supplier_map()
	pi_supplier_map = get_purchase_invoice_supplier_map()

	group_by = frappe.scrub(filters.get("group_by"))

	if group_by == "asset_category":
		fields = ["asset_category", "gross_purchase_amount", "opening_accumulated_depreciation"]
		assets_record = frappe.db.get_all("Asset", filters=conditions, fields=fields, group_by=group_by)

	elif group_by == "location":
		fields = ["location", "gross_purchase_amount", "opening_accumulated_depreciation"]
		assets_record = frappe.db.get_all("Asset", filters=conditions, fields=fields, group_by=group_by)

	else:
		fields = ["name as asset_id", "asset_name", "status", "department", "cost_center", "purchase_receipt",
			"asset_category", "purchase_date", "gross_purchase_amount", "location",
<<<<<<< HEAD
			"available_for_use_date", "purchase_invoice", "opening_accumulated_depreciation"]
		assets_record = frappe.db.get_all("Asset", filters=conditions, fields=fields)
=======
			"available_for_use_date", "status", "purchase_invoice", "opening_accumulated_depreciation"])
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

	for asset in assets_record:
		asset_value = asset.gross_purchase_amount - flt(asset.opening_accumulated_depreciation) \
			- flt(depreciation_amount_map.get(asset.name))
		row = {
			"asset_id": asset.asset_id,
			"asset_name": asset.asset_name,
			"status": asset.status,
			"department": asset.department,
			"cost_center": asset.cost_center,
			"vendor_name": pr_supplier_map.get(asset.purchase_receipt) or pi_supplier_map.get(asset.purchase_invoice),
			"gross_purchase_amount": asset.gross_purchase_amount,
			"opening_accumulated_depreciation": asset.opening_accumulated_depreciation,
			"depreciated_amount": depreciation_amount_map.get(asset.asset_id) or 0.0,
			"available_for_use_date": asset.available_for_use_date,
			"location": asset.location,
			"asset_category": asset.asset_category,
			"purchase_date": asset.purchase_date,
			"asset_value": asset_value
		}
		data.append(row)

	return data

<<<<<<< HEAD
def prepare_chart_data(data, filters):
	labels_values_map = {}
	date_field = frappe.scrub(filters.date_based_on)

	period_list = get_period_list(filters.from_fiscal_year, filters.to_fiscal_year, 
		filters.from_date, filters.to_date, filters.filter_based_on, "Monthly", company=filters.company)

	for d in period_list:
		labels_values_map.setdefault(d.get('label'), frappe._dict({'asset_value': 0, 'depreciated_amount': 0}))

	for d in data:
		date = d.get(date_field)
		belongs_to_month = formatdate(date, "MMM YYYY")

		labels_values_map[belongs_to_month].asset_value += d.get("asset_value")
		labels_values_map[belongs_to_month].depreciated_amount += d.get("depreciated_amount")

	return {
		"data" : {
			"labels": labels_values_map.keys(),
			"datasets": [
				{ 'name': _('Asset Value'), 'values': [d.get("asset_value") for d in labels_values_map.values()] },
				{ 'name': _('Depreciatied Amount'), 'values': [d.get("depreciated_amount") for d in labels_values_map.values()] }
			]
		},
		"type": "bar",
		"barOptions": {
			"stacked": 1
		},
	}

def get_finance_book_value_map(filters):
	date = filters.to_date if filters.filter_based_on == "Date Range" else filters.year_end_date
=======
def get_finance_book_value_map(filters):
	date = filters.get('purchase_date') or filters.get('available_for_use_date') or today()
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

	return frappe._dict(frappe.db.sql(''' Select
		parent, SUM(depreciation_amount)
		FROM `tabDepreciation Schedule`
		WHERE
			parentfield='schedules'
			AND schedule_date<=%s
			AND journal_entry IS NOT NULL
			AND ifnull(finance_book, '')=%s
		GROUP BY parent''', (date, cstr(filters.finance_book or ''))))

def get_purchase_receipt_supplier_map():
	return frappe._dict(frappe.db.sql(''' Select
		pr.name, pr.supplier
		FROM `tabPurchase Receipt` pr, `tabPurchase Receipt Item` pri
		WHERE
			pri.parent = pr.name
			AND pri.is_fixed_asset=1
			AND pr.docstatus=1
			AND pr.is_return=0'''))

def get_purchase_invoice_supplier_map():
	return frappe._dict(frappe.db.sql(''' Select
		pi.name, pi.supplier
		FROM `tabPurchase Invoice` pi, `tabPurchase Invoice Item` pii
		WHERE
			pii.parent = pi.name
			AND pii.is_fixed_asset=1
			AND pi.docstatus=1
			AND pi.is_return=0'''))

def get_columns(filters):
	if filters.get("group_by") in ["Asset Category", "Location"]:
		return [
			{
				"label": _("{}").format(filters.get("group_by")),
				"fieldtype": "Link",
				"fieldname": frappe.scrub(filters.get("group_by")),
				"options": filters.get("group_by"),
				"width": 120
			},
			{
				"label": _("Gross Purchase Amount"),
				"fieldname": "gross_purchase_amount",
				"fieldtype": "Currency",
				"options": "company:currency",
				"width": 100
			},
			{
				"label": _("Opening Accumulated Depreciation"),
				"fieldname": "opening_accumulated_depreciation",
				"fieldtype": "Currency",
				"options": "company:currency",
				"width": 90
			},
			{
				"label": _("Depreciated Amount"),
				"fieldname": "depreciated_amount",
				"fieldtype": "Currency",
				"options": "company:currency",
				"width": 100
			},
			{
				"label": _("Asset Value"),
				"fieldname": "asset_value",
				"fieldtype": "Currency",
				"options": "company:currency",
				"width": 100
			}
		]

	return [
		{
			"label": _("Asset Id"),
			"fieldtype": "Link",
			"fieldname": "asset_id",
			"options": "Asset",
			"width": 60
		},
		{
			"label": _("Asset Name"),
			"fieldtype": "Data",
			"fieldname": "asset_name",
			"width": 140
		},
		{
			"label": _("Asset Category"),
			"fieldtype": "Link",
			"fieldname": "asset_category",
			"options": "Asset Category",
			"width": 100
		},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": 80
		},
		{
			"label": _("Purchase Date"),
			"fieldtype": "Date",
			"fieldname": "purchase_date",
			"width": 90
		},
		{
			"label": _("Available For Use Date"),
			"fieldtype": "Date",
			"fieldname": "available_for_use_date",
			"width": 90
		},
		{
			"label": _("Gross Purchase Amount"),
			"fieldname": "gross_purchase_amount",
			"fieldtype": "Currency",
			"options": "company:currency",
			"width": 100
		},
		{
			"label": _("Asset Value"),
			"fieldname": "asset_value",
			"fieldtype": "Currency",
			"options": "company:currency",
			"width": 100
		},
		{
			"label": _("Opening Accumulated Depreciation"),
			"fieldname": "opening_accumulated_depreciation",
			"fieldtype": "Currency",
			"options": "company:currency",
			"width": 90
		},
		{
			"label": _("Depreciated Amount"),
			"fieldname": "depreciated_amount",
			"fieldtype": "Currency",
			"options": "company:currency",
			"width": 100
		},
		{
			"label": _("Cost Center"),
			"fieldtype": "Link",
			"fieldname": "cost_center",
			"options": "Cost Center",
			"width": 100
		},
		{
			"label": _("Department"),
			"fieldtype": "Link",
			"fieldname": "department",
			"options": "Department",
			"width": 100
		},
		{
			"label": _("Vendor Name"),
			"fieldtype": "Data",
			"fieldname": "vendor_name",
			"width": 100
		},
		{
			"label": _("Location"),
			"fieldtype": "Link",
			"fieldname": "location",
			"options": "Location",
			"width": 100
		},
	]