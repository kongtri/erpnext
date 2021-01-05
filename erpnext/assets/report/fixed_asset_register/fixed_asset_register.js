// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Fixed Asset Register"] = {
	"filters": [
		{
			fieldname:"company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company"),
			reqd: 1
		},
		{
			fieldname:"status",
			label: __("Status"),
			fieldtype: "Select",
			options: "In Location\nDisposed",
			default: 'In Location',
			reqd: 1
		},
		{
<<<<<<< HEAD
			"fieldname":"filter_based_on",
			"label": __("Period Based On"),
			"fieldtype": "Select",
			"options": ["Fiscal Year", "Date Range"],
			"default": ["Fiscal Year"],
			"reqd": 1
		},
		{
			"fieldname":"from_date",
			"label": __("Start Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.nowdate(), -12),
			"depends_on": "eval: doc.filter_based_on == 'Date Range'",
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("End Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.nowdate(),
			"depends_on": "eval: doc.filter_based_on == 'Date Range'",
			"reqd": 1
		},
		{
			"fieldname":"from_fiscal_year",
			"label": __("Start Year"),
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"default": frappe.defaults.get_user_default("fiscal_year"),
			"depends_on": "eval: doc.filter_based_on == 'Fiscal Year'",
			"reqd": 1
		},
		{
			"fieldname":"to_fiscal_year",
			"label": __("End Year"),
			"fieldtype": "Link",
			"options": "Fiscal Year",
			"default": frappe.defaults.get_user_default("fiscal_year"),
			"depends_on": "eval: doc.filter_based_on == 'Fiscal Year'",
			"reqd": 1
		},
		{
			"fieldname":"date_based_on",
			"label": __("Date Based On"),
			"fieldtype": "Select",
			"options": ["Purchase Date", "Available For Use Date"],
			"default": "Purchase Date",
			"reqd": 1
		},
		{
			fieldname:"asset_category",
			label: __("Asset Category"),
			fieldtype: "Link",
			options: "Asset Category"
		},
		{	
=======
			fieldname:"purchase_date",
			label: __("Purchase Date"),
			fieldtype: "Date"
		},
		{
			fieldname:"available_for_use_date",
			label: __("Available For Use Date"),
			fieldtype: "Date"
		},
		{
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
			fieldname:"finance_book",
			label: __("Finance Book"),
			fieldtype: "Link",
			options: "Finance Book"
		},
		{
<<<<<<< HEAD
			fieldname:"cost_center",
			label: __("Cost Center"),
			fieldtype: "Link",
			options: "Cost Center"
		},
		{
			fieldname:"group_by",
			label: __("Group By"),
			fieldtype: "Select",
			options: ["--Select a group--", "Asset Category", "Location"],
			default: "--Select a group--",
			reqd: 1
=======
			fieldname:"asset_category",
			label: __("Asset Category"),
			fieldtype: "Link",
			options: "Asset Category"
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
		},
		{
			fieldname:"is_existing_asset",
			label: __("Is Existing Asset"),
			fieldtype: "Check"
		},
	]
};
