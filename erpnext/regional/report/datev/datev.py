# coding: utf-8
"""
Provide a report and downloadable CSV according to the German DATEV format.

- Query report showing only the columns that contain data, formatted nicely for
  dispay to the user.
- CSV download functionality `download_datev_csv` that provides a CSV file with
  all required columns. Used to import the data into the DATEV Software.
"""
from __future__ import unicode_literals

import json
<<<<<<< HEAD
=======
import six
from six import string_types
from csv import QUOTE_NONNUMERIC

>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70
import frappe
from six import string_types

from frappe import _
from erpnext.accounts.utils import get_fiscal_year
<<<<<<< HEAD
from erpnext.regional.germany.utils.datev.datev_csv import zip_and_download, get_datev_csv
from erpnext.regional.germany.utils.datev.datev_constants import Transactions, DebtorsCreditors, AccountNames

COLUMNS = [
	{
		"label": "Umsatz (ohne Soll/Haben-Kz)",
		"fieldname": "Umsatz (ohne Soll/Haben-Kz)",
		"fieldtype": "Currency",
		"width": 100
	},
	{
		"label": "Soll/Haben-Kennzeichen",
		"fieldname": "Soll/Haben-Kennzeichen",
		"fieldtype": "Data",
		"width": 100
	},
	{
		"label": "Konto",
		"fieldname": "Konto",
		"fieldtype": "Data",
		"width": 100
	},
	{
		"label": "Gegenkonto (ohne BU-Schlüssel)",
		"fieldname": "Gegenkonto (ohne BU-Schlüssel)",
		"fieldtype": "Data",
		"width": 100
	},
	{
		"label": "Belegdatum",
		"fieldname": "Belegdatum",
		"fieldtype": "Date",
		"width": 100
	},
	{
		"label": "Belegfeld 1",
		"fieldname": "Belegfeld 1",
		"fieldtype": "Data",
		"width": 150
	},
	{
		"label": "Buchungstext",
		"fieldname": "Buchungstext",
		"fieldtype": "Text",
		"width": 300
	},
	{
		"label": "Beleginfo - Art 1",
		"fieldname": "Beleginfo - Art 1",
		"fieldtype": "Link",
		"options": "DocType",
		"width": 100
	},
	{
		"label": "Beleginfo - Inhalt 1",
		"fieldname": "Beleginfo - Inhalt 1",
		"fieldtype": "Dynamic Link",
		"options": "Beleginfo - Art 1",
		"width": 150
	},
	{
		"label": "Beleginfo - Art 2",
		"fieldname": "Beleginfo - Art 2",
		"fieldtype": "Link",
		"options": "DocType",
		"width": 100
	},
	{
		"label": "Beleginfo - Inhalt 2",
		"fieldname": "Beleginfo - Inhalt 2",
		"fieldtype": "Dynamic Link",
		"options": "Beleginfo - Art 2",
		"width": 150
	}
]
=======
import pandas as pd
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70


def execute(filters=None):
	"""Entry point for frappe."""
	data = []
	if filters and validate(filters):
		data = get_transactions(filters, as_dict=0)

	return COLUMNS, data


def validate(filters):
	"""Make sure all mandatory filters and settings are present."""
	company = filters.get('company')
	if not company:
		frappe.throw(_('<b>Company</b> is a mandatory filter.'))

	from_date = filters.get('from_date')
	if not from_date:
		frappe.throw(_('<b>From Date</b> is a mandatory filter.'))

	to_date = filters.get('to_date')
	if not to_date:
		frappe.throw(_('<b>To Date</b> is a mandatory filter.'))

	validate_fiscal_year(from_date, to_date, company)
<<<<<<< HEAD

	if not frappe.db.exists('DATEV Settings', filters.get('company')):
		frappe.log_error(_('Please create {} for Company {}.').format(
			'<a href="desk#List/DATEV%20Settings/List">{}</a>'.format(_('DATEV Settings')),
			frappe.bold(filters.get('company'))
		))
		return False
=======

	try:
		frappe.get_doc('DATEV Settings', filters.get('company'))
	except frappe.DoesNotExistError:
		frappe.throw(_('Please create <b>DATEV Settings</b> for Company <b>{}</b>.').format(filters.get('company')))


def validate_fiscal_year(from_date, to_date, company):
	from_fiscal_year = get_fiscal_year(date=from_date, company=company)
	to_fiscal_year = get_fiscal_year(date=to_date, company=company)
	if from_fiscal_year != to_fiscal_year:
		frappe.throw(_('Dates {} and {} are not in the same fiscal year.').format(from_date, to_date))


def get_columns():
	"""Return the list of columns that will be shown in query report."""
	columns = [
		{
			"label": "Umsatz (ohne Soll/Haben-Kz)",
			"fieldname": "Umsatz (ohne Soll/Haben-Kz)",
			"fieldtype": "Currency",
		},
		{
			"label": "Soll/Haben-Kennzeichen",
			"fieldname": "Soll/Haben-Kennzeichen",
			"fieldtype": "Data",
		},
		{
			"label": "Konto",
			"fieldname": "Konto",
			"fieldtype": "Data",
		},
		{
			"label": "Gegenkonto (ohne BU-Schlüssel)",
			"fieldname": "Gegenkonto (ohne BU-Schlüssel)",
			"fieldtype": "Data",
		},
		{
			"label": "Belegdatum",
			"fieldname": "Belegdatum",
			"fieldtype": "Date",
		},
		{
			"label": "Belegfeld 1",
			"fieldname": "Belegfeld 1",
			"fieldtype": "Data",
		},
		{
			"label": "Buchungstext",
			"fieldname": "Buchungstext",
			"fieldtype": "Text",
		},
		{
			"label": "Beleginfo - Art 1",
			"fieldname": "Beleginfo - Art 1",
			"fieldtype": "Link",
			"options": "DocType"
		},
		{
			"label": "Beleginfo - Inhalt 1",
			"fieldname": "Beleginfo - Inhalt 1",
			"fieldtype": "Dynamic Link",
			"options": "Beleginfo - Art 1"
		},
		{
			"label": "Beleginfo - Art 2",
			"fieldname": "Beleginfo - Art 2",
			"fieldtype": "Link",
			"options": "DocType"
		},
		{
			"label": "Beleginfo - Inhalt 2",
			"fieldname": "Beleginfo - Inhalt 2",
			"fieldtype": "Dynamic Link",
			"options": "Beleginfo - Art 2"
		}
	]
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

	return True


def validate_fiscal_year(from_date, to_date, company):
	from_fiscal_year = get_fiscal_year(date=from_date, company=company)
	to_fiscal_year = get_fiscal_year(date=to_date, company=company)
	if from_fiscal_year != to_fiscal_year:
		frappe.throw(_('Dates {} and {} are not in the same fiscal year.').format(from_date, to_date))


def get_transactions(filters, as_dict=1):
	"""
	Get a list of accounting entries.

	Select GL Entries joined with Account and Party Account in order to get the
	account numbers. Returns a list of accounting entries.

	Arguments:
	filters -- dict of filters to be passed to the sql query
	as_dict -- return as list of dicts [0,1]
	"""
	filter_by_voucher = 'AND gl.voucher_type = %(voucher_type)s' if filters.get('voucher_type') else ''
	gl_entries = frappe.db.sql("""
		SELECT

			/* either debit or credit amount; always positive */
			case gl.debit when 0 then gl.credit else gl.debit end as 'Umsatz (ohne Soll/Haben-Kz)',

			/* 'H' when credit, 'S' when debit */
			case gl.debit when 0 then 'H' else 'S' end as 'Soll/Haben-Kennzeichen',

			/* account number or, if empty, party account number */
			coalesce(acc.account_number, acc_pa.account_number) as 'Konto',

			/* against number or, if empty, party against number */
			coalesce(acc_against.account_number, acc_against_pa.account_number) as 'Gegenkonto (ohne BU-Schlüssel)',
			
			gl.posting_date as 'Belegdatum',
			gl.voucher_no as 'Belegfeld 1',
			LEFT(gl.remarks, 60) as 'Buchungstext',
			gl.voucher_type as 'Beleginfo - Art 1',
			gl.voucher_no as 'Beleginfo - Inhalt 1',
			gl.against_voucher_type as 'Beleginfo - Art 2',
			gl.against_voucher as 'Beleginfo - Inhalt 2'

		FROM `tabGL Entry` gl

			/* Statistisches Konto (Debitoren/Kreditoren) */
			left join `tabParty Account` pa
			on gl.against = pa.parent
			and gl.company = pa.company

			/* Kontonummer */
			left join `tabAccount` acc 
			on gl.account = acc.name

			/* Gegenkonto-Nummer */
			left join `tabAccount` acc_against 
			on gl.against = acc_against.name

			/* Statistische Kontonummer */
			left join `tabAccount` acc_pa
			on pa.account = acc_pa.name

			/* Statistische Gegenkonto-Nummer */
			left join `tabAccount` acc_against_pa 
			on pa.account = acc_against_pa.name

		WHERE gl.company = %(company)s 
		AND DATE(gl.posting_date) >= %(from_date)s
		AND DATE(gl.posting_date) <= %(to_date)s
		{}
		ORDER BY 'Belegdatum', gl.voucher_no""".format(filter_by_voucher), filters, as_dict=as_dict)

	return gl_entries


def get_customers(filters):
	"""
	Get a list of Customers.

	Arguments:
	filters -- dict of filters to be passed to the sql query
	"""
	return frappe.db.sql("""
		SELECT

			acc.account_number as 'Konto',
			CASE cus.customer_type WHEN 'Company' THEN cus.customer_name ELSE null END as 'Name (Adressatentyp Unternehmen)',
			CASE cus.customer_type WHEN 'Individual' THEN con.last_name ELSE null END as 'Name (Adressatentyp natürl. Person)',
			CASE cus.customer_type WHEN 'Individual' THEN con.first_name ELSE null END as 'Vorname (Adressatentyp natürl. Person)',
			CASE cus.customer_type WHEN 'Individual' THEN '1' WHEN 'Company' THEN '2' ELSE '0' end as 'Adressatentyp',
			adr.address_line1 as 'Straße',
			adr.pincode as 'Postleitzahl',
			adr.city as 'Ort',
			UPPER(country.code) as 'Land',
			adr.address_line2 as 'Adresszusatz',
			con.email_id as 'E-Mail',
			coalesce(con.mobile_no, con.phone) as 'Telefon',
			cus.website as 'Internet',
			cus.tax_id as 'Steuernummer'

		FROM `tabParty Account` par

			left join `tabAccount` acc
			on acc.name = par.account

			left join `tabCustomer` cus
			on cus.name = par.parent

			left join `tabAddress` adr
			on adr.name = cus.customer_primary_address

			left join `tabCountry` country
			on country.name = adr.country

			left join `tabContact` con
			on con.name = cus.customer_primary_contact

		WHERE par.company = %(company)s
		AND par.parenttype = 'Customer'""", filters, as_dict=1)


def get_suppliers(filters):
	"""
	Get a list of Suppliers.

	Arguments:
	filters -- dict of filters to be passed to the sql query
	"""
<<<<<<< HEAD
	return frappe.db.sql("""
		SELECT

			acc.account_number as 'Konto',
			CASE sup.supplier_type WHEN 'Company' THEN sup.supplier_name ELSE null END as 'Name (Adressatentyp Unternehmen)',
			CASE sup.supplier_type WHEN 'Individual' THEN con.last_name ELSE null END as 'Name (Adressatentyp natürl. Person)',
			CASE sup.supplier_type WHEN 'Individual' THEN con.first_name ELSE null END as 'Vorname (Adressatentyp natürl. Person)',
			CASE sup.supplier_type WHEN 'Individual' THEN '1' WHEN 'Company' THEN '2' ELSE '0' end as 'Adressatentyp',
			adr.address_line1 as 'Straße',
			adr.pincode as 'Postleitzahl',
			adr.city as 'Ort',
			UPPER(country.code) as 'Land',
			adr.address_line2 as 'Adresszusatz',
			con.email_id as 'E-Mail',
			coalesce(con.mobile_no, con.phone) as 'Telefon',
			sup.website as 'Internet',
			sup.tax_id as 'Steuernummer',
			case sup.on_hold when 1 then sup.release_date else null end as 'Zahlungssperre bis'

		FROM `tabParty Account` par

			left join `tabAccount` acc
			on acc.name = par.account

			left join `tabSupplier` sup
			on sup.name = par.parent

			left join `tabDynamic Link` dyn_adr
			on dyn_adr.link_name = sup.name
			and dyn_adr.link_doctype = 'Supplier'
			and dyn_adr.parenttype = 'Address'
			
			left join `tabAddress` adr
			on adr.name = dyn_adr.parent
			and adr.is_primary_address = '1'

			left join `tabCountry` country
			on country.name = adr.country

			left join `tabDynamic Link` dyn_con
			on dyn_con.link_name = sup.name
			and dyn_con.link_doctype = 'Supplier'
			and dyn_con.parenttype = 'Contact'

			left join `tabContact` con
			on con.name = dyn_con.parent
			and con.is_primary_contact = '1'

		WHERE par.company = %(company)s
		AND par.parenttype = 'Supplier'""", filters, as_dict=1)


def get_account_names(filters):
	return frappe.db.sql("""
		SELECT

			account_number as 'Konto',
			LEFT(account_name, 40) as 'Kontenbeschriftung',
			'de-DE' as 'Sprach-ID'

		FROM `tabAccount`
		WHERE company = %(company)s
		AND is_group = 0
		AND account_number != ''
	""", filters, as_dict=1)

=======
	coa = frappe.get_value("Company", filters.get("company"), "chart_of_accounts")
	coa_used = "04" if "SKR04" in coa else ("03" if "SKR03" in coa else "")

	header = [
		# A = DATEV-Format-KZ
		#   DTVF = created by DATEV software,
		#   EXTF = created by other software
		'"EXTF"',
		# B = version of the DATEV format
		#   141 = 1.41, 
		#   510 = 5.10,
		#   720 = 7.20
		"700",
		# C = Data category
		#   21 = Transaction batch (Buchungsstapel),
		#   67 = Buchungstextkonstanten,
		#   16 = Debitors/Creditors,
		#   20 = Account names (Kontenbeschriftungen)
		"21",
		# D = Format name
		#   Buchungsstapel,
		#   Buchungstextkonstanten,
		#   Debitoren/Kreditoren,
		#   Kontenbeschriftungen
		"Buchungsstapel",
		# E = Format version (regarding format name)
		"9",
		# F = Generated on
		datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '000',
		# G = Imported on -- stays empty
		"",
		# H = Herkunfts-Kennzeichen (Origin)
		# Any two letters
		'"EN"',
		# I = Exported by
		'"%s"' % frappe.session.user,
		# J = Imported by -- stays empty
		"",
		# K = Tax consultant number (Beraternummer)
		frappe.get_value("DATEV Settings", filters.get("company"), "consultant_number") or "",
		# L = Tax client number (Mandantennummer)
		frappe.get_value("DATEV Settings", filters.get("company"), "client_number") or "",
		# M = Start of the fiscal year (Wirtschaftsjahresbeginn)
		frappe.utils.formatdate(filters.get("fiscal_year_start"), "yyyyMMdd"),
		# N = Length of account numbers (Sachkontenlänge)
		str(filters.get('account_number_length', 4)),
		# O = Transaction batch start date (YYYYMMDD)
		frappe.utils.formatdate(filters.get('from_date'), "yyyyMMdd"),
		# P = Transaction batch end date (YYYYMMDD)
		frappe.utils.formatdate(filters.get('to_date'), "yyyyMMdd"),
		# Q = Description (for example, "January - February 2019 Transactions")
		"Buchungsstapel",
		# R = Diktatkürzel
		"",
		# S = Buchungstyp
		#   1 = Transaction batch (Buchungsstapel),
		#   2 = Annual financial statement (Jahresabschluss)
		"1",
		# T = Rechnungslegungszweck
		"0", # vom Rechnungslegungszweck unabhängig
		# U = Festschreibung
		"0", # keine Festschreibung
		# V = Kontoführungs-Währungskennzeichen des Geldkontos
		frappe.get_value("Company", filters.get("company"), "default_currency"),
		# reserviert
		'',
		# Derivatskennzeichen
		'',
		# reserviert
		'',
		# reserviert
		'',
		# SKR
		'"%s"' % coa_used,
		# Branchen-Lösungs-ID
		'',
		# reserviert
		'',
		# reserviert
		'',
		# Anwendungsinformation (Verarbeitungskennzeichen der abgebenden Anwendung)
		''
	]
	columns = [
		# All possible columns must tbe listed here, because DATEV requires them to
		# be present in the CSV.
		# ---
		# Umsatz
		"Umsatz (ohne Soll/Haben-Kz)",
		"Soll/Haben-Kennzeichen",
		"WKZ Umsatz",
		"Kurs",
		"Basis-Umsatz",
		"WKZ Basis-Umsatz",
		# Konto/Gegenkonto
		"Konto",
		"Gegenkonto (ohne BU-Schlüssel)",
		"BU-Schlüssel",
		# Datum
		"Belegdatum",
		# Rechnungs- / Belegnummer
		"Belegfeld 1",
		# z.B. Fälligkeitsdatum Format: TTMMJJ
		"Belegfeld 2",
		# Skonto-Betrag / -Abzug (Der Wert 0 ist unzulässig)
		"Skonto",
		# Beschreibung des Buchungssatzes
		"Buchungstext",
		# Mahn- / Zahl-Sperre (1 = Postensperre)
		"Postensperre",
		"Diverse Adressnummer",
		"Geschäftspartnerbank",
		"Sachverhalt",
		# Keine Mahnzinsen
		"Zinssperre",
		# Link auf den Buchungsbeleg (Programmkürzel + GUID)
		"Beleglink",
		# Beleginfo
		"Beleginfo - Art 1",
		"Beleginfo - Inhalt 1",
		"Beleginfo - Art 2",
		"Beleginfo - Inhalt 2",
		"Beleginfo - Art 3",
		"Beleginfo - Inhalt 3",
		"Beleginfo - Art 4",
		"Beleginfo - Inhalt 4",
		"Beleginfo - Art 5",
		"Beleginfo - Inhalt 5",
		"Beleginfo - Art 6",
		"Beleginfo - Inhalt 6",
		"Beleginfo - Art 7",
		"Beleginfo - Inhalt 7",
		"Beleginfo - Art 8",
		"Beleginfo - Inhalt 8",
		# Zuordnung des Geschäftsvorfalls für die Kostenrechnung
		"KOST1 - Kostenstelle",
		"KOST2 - Kostenstelle",
		"KOST-Menge",
		# USt-ID-Nummer (Beispiel: DE133546770)
		"EU-Mitgliedstaat u. USt-IdNr.",
		# Der im EU-Bestimmungsland gültige Steuersatz
		"EU-Steuersatz",
		# I = Ist-Versteuerung,
		# K = keine Umsatzsteuerrechnung
		# P = Pauschalierung (z. B. für Land- und Forstwirtschaft),
		# S = Soll-Versteuerung
		"Abw. Versteuerungsart",
		# Sachverhalte gem. § 13b Abs. 1 Satz 1 Nrn. 1.-5. UStG
		"Sachverhalt L+L",
		# Steuersatz / Funktion zum L+L-Sachverhalt (Beispiel: Wert 190 für 19%)
		"Funktionsergänzung L+L",
		# Bei Verwendung des BU-Schlüssels 49 für „andere Steuersätze“ muss der
		# steuerliche Sachverhalt mitgegeben werden
		"BU 49 Hauptfunktionstyp",
		"BU 49 Hauptfunktionsnummer",
		"BU 49 Funktionsergänzung",
		# Zusatzinformationen, besitzen den Charakter eines Notizzettels und können
		# frei erfasst werden.
		"Zusatzinformation - Art 1",
		"Zusatzinformation - Inhalt 1",
		"Zusatzinformation - Art 2",
		"Zusatzinformation - Inhalt 2",
		"Zusatzinformation - Art 3",
		"Zusatzinformation - Inhalt 3",
		"Zusatzinformation - Art 4",
		"Zusatzinformation - Inhalt 4",
		"Zusatzinformation - Art 5",
		"Zusatzinformation - Inhalt 5",
		"Zusatzinformation - Art 6",
		"Zusatzinformation - Inhalt 6",
		"Zusatzinformation - Art 7",
		"Zusatzinformation - Inhalt 7",
		"Zusatzinformation - Art 8",
		"Zusatzinformation - Inhalt 8",
		"Zusatzinformation - Art 9",
		"Zusatzinformation - Inhalt 9",
		"Zusatzinformation - Art 10",
		"Zusatzinformation - Inhalt 10",
		"Zusatzinformation - Art 11",
		"Zusatzinformation - Inhalt 11",
		"Zusatzinformation - Art 12",
		"Zusatzinformation - Inhalt 12",
		"Zusatzinformation - Art 13",
		"Zusatzinformation - Inhalt 13",
		"Zusatzinformation - Art 14",
		"Zusatzinformation - Inhalt 14",
		"Zusatzinformation - Art 15",
		"Zusatzinformation - Inhalt 15",
		"Zusatzinformation - Art 16",
		"Zusatzinformation - Inhalt 16",
		"Zusatzinformation - Art 17",
		"Zusatzinformation - Inhalt 17",
		"Zusatzinformation - Art 18",
		"Zusatzinformation - Inhalt 18",
		"Zusatzinformation - Art 19",
		"Zusatzinformation - Inhalt 19",
		"Zusatzinformation - Art 20",
		"Zusatzinformation - Inhalt 20",
		# Wirkt sich nur bei Sachverhalt mit SKR 14 Land- und Forstwirtschaft aus,
		# für andere SKR werden die Felder beim Import / Export überlesen bzw.
		# leer exportiert.
		"Stück",
		"Gewicht",
		# 1 = Lastschrift
		# 2 = Mahnung
		# 3 = Zahlung
		"Zahlweise",
		"Forderungsart",
		# JJJJ
		"Veranlagungsjahr",
		# TTMMJJJJ
		"Zugeordnete Fälligkeit",
		# 1 = Einkauf von Waren
		# 2 = Erwerb von Roh-Hilfs- und Betriebsstoffen
		"Skontotyp",
		# Allgemeine Bezeichnung, des Auftrags / Projekts.
		"Auftragsnummer",
		# AA = Angeforderte Anzahlung / Abschlagsrechnung
		# AG = Erhaltene Anzahlung (Geldeingang)
		# AV = Erhaltene Anzahlung (Verbindlichkeit)
		# SR = Schlussrechnung
		# SU = Schlussrechnung (Umbuchung)
		# SG = Schlussrechnung (Geldeingang)
		# SO = Sonstige
		"Buchungstyp",
		"USt-Schlüssel (Anzahlungen)",
		"EU-Mitgliedstaat (Anzahlungen)",
		"Sachverhalt L+L (Anzahlungen)",
		"EU-Steuersatz (Anzahlungen)",
		"Erlöskonto (Anzahlungen)",
		# Wird beim Import durch SV (Stapelverarbeitung) ersetzt.
		"Herkunft-Kz",
		# Wird von DATEV verwendet.
		"Leerfeld",
		# Format TTMMJJJJ
		"KOST-Datum",
		# Vom Zahlungsempfänger individuell vergebenes Kennzeichen eines Mandats
		# (z.B. Rechnungs- oder Kundennummer).
		"SEPA-Mandatsreferenz",
		# 1 = Skontosperre
		# 0 = Keine Skontosperre
		"Skontosperre",
		# Gesellschafter und Sonderbilanzsachverhalt
		"Gesellschaftername",
		# Amtliche Nummer aus der Feststellungserklärung
		"Beteiligtennummer",
		"Identifikationsnummer",
		"Zeichnernummer",
		# Format TTMMJJJJ
		"Postensperre bis",
		# Gesellschafter und Sonderbilanzsachverhalt
		"Bezeichnung SoBil-Sachverhalt",
		"Kennzeichen SoBil-Buchung",
		# 0 = keine Festschreibung
		# 1 = Festschreibung
		"Festschreibung",
		# Format TTMMJJJJ
		"Leistungsdatum",
		# Format TTMMJJJJ
		"Datum Zuord. Steuerperiode",
		# OPOS-Informationen, Format TTMMJJJJ
		"Fälligkeit",
		# G oder 1 = Generalumkehr
		# 0 = keine Generalumkehr
		"Generalumkehr (GU)",
		# Steuersatz für Steuerschlüssel
		"Steuersatz",
		# Beispiel: DE für Deutschland
		"Land"
	]

	empty_df = pd.DataFrame(columns=columns)
	data_df = pd.DataFrame.from_records(data)

	result = empty_df.append(data_df)
	result['Belegdatum'] = pd.to_datetime(result['Belegdatum'])

	header = ';'.join(header).encode('latin_1')
	data = result.to_csv(
		# Reason for str(';'): https://github.com/pandas-dev/pandas/issues/6035
		sep=str(';'),
		# European decimal seperator
		decimal=',',
		# Windows "ANSI" encoding
		encoding='latin_1',
		# format date as DDMM
		date_format='%d%m',
		# Windows line terminator
		line_terminator='\r\n',
		# Do not number rows
		index=False,
		# Use all columns defined above
		columns=columns,
		# Quote most fields, even currency values with "," separator
		quoting=QUOTE_NONNUMERIC
	)

	if not six.PY2:
		data = data.encode('latin_1')

	return header + b'\r\n' + data
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

@frappe.whitelist()
def download_datev_csv(filters):
	"""
	Provide accounting entries for download in DATEV format.

	Validate the filters, get the data, produce the CSV file and provide it for
	download. Can be called like this:

	GET /api/method/erpnext.regional.report.datev.datev.download_datev_csv

	Arguments / Params:
	filters -- dict of filters to be passed to the sql query
	"""
	if isinstance(filters, string_types):
		filters = json.loads(filters)

	validate(filters)
<<<<<<< HEAD
	company = filters.get('company')

	fiscal_year = get_fiscal_year(date=filters.get('from_date'), company=company)
	filters['fiscal_year_start'] = fiscal_year[1]
=======

	filters['account_number_length'] = frappe.get_value('DATEV Settings', filters.get('company'), 'account_number_length')

	fiscal_year = get_fiscal_year(date=filters.get('from_date'), company=filters.get('company'))
	filters['fiscal_year_start'] = fiscal_year[1]

	data = get_gl_entries(filters, as_dict=1)
>>>>>>> 03933f846114cd3cb5da8676693a75b277ae8f70

	# set chart of accounts used
	coa = frappe.get_value('Company', company, 'chart_of_accounts')
	filters['skr'] = '04' if 'SKR04' in coa else ('03' if 'SKR03' in coa else '')

	filters['account_number_length'] = frappe.get_value('DATEV Settings', company, 'account_number_length')

	transactions = get_transactions(filters)
	account_names = get_account_names(filters)
	customers = get_customers(filters)
	suppliers = get_suppliers(filters)

	zip_name = '{} DATEV.zip'.format(frappe.utils.datetime.date.today())
	zip_and_download(zip_name, [
		{
			'file_name': 'EXTF_Buchungsstapel.csv',
			'csv_data': get_datev_csv(transactions, filters, csv_class=Transactions)
		},
		{
			'file_name': 'EXTF_Kontenbeschriftungen.csv',
			'csv_data': get_datev_csv(account_names, filters, csv_class=AccountNames)
		},
		{
			'file_name': 'EXTF_Kunden.csv',
			'csv_data': get_datev_csv(customers, filters, csv_class=DebtorsCreditors)
		},
		{
			'file_name': 'EXTF_Lieferanten.csv',
			'csv_data': get_datev_csv(suppliers, filters, csv_class=DebtorsCreditors)
		},
	])
