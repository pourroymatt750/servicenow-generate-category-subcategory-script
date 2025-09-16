class InputString:
    def __init__(self, inputString):
        self.inputString = inputString

# Ex: addOptions(category, ['', 'Atlas']);
add_cat = InputString("""
		case '':
			addOptions(category, allCategories);
			break;

		case 'ACCESS':
			addOptions(category, ['', 'Atlas']);
			break;

		case 'BROKEN FUNCTIONALITY':
			addOptions(category, ['', 'Atlas']);
			break;

		case 'CONTENT':
			addOptions(category, ['', 'Atlas']);
			break;

		case 'CONTENT/PRODUCTS':
			addOptions(category, ['', 'Avalon Consumer Website', 'Cosmos Consumer Website', 'Globus Consumer Website', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA', 'Travel Advisor Portal (TAP) IN/UK']);
			break;

		case 'FORMS':
			addOptions(category, ['', 'Avalon Consumer Website', 'Cosmos Consumer Website', 'Globus Consumer Website', 'TD Portal', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA']);
			break;

		case 'LOGIN':
			addOptions(category, ['', 'Avalon Consumer Website', 'Cosmos Consumer Website', 'Globus Consumer Website']);
			break;

		case 'PAYMENTS':
			addOptions(category, ['', 'Avalon Consumer Website', 'Cosmos Consumer Website', 'Globus Consumer Website', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA', 'Travel Advisor Portal (TAP) IN/UK', 'Websites']);
			break;

		case 'RESERVATIONS (BOOKING)':
			addOptions(category, ['', 'Avalon Consumer Website', 'Cosmos Consumer Website', 'Globus Consumer Website', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA', 'Travel Advisor Portal (TAP) IN/UK']);
			break;

		case 'ACCOUNT CREATION REQUEST':
			addOptions(category, ['', 'CallMiner']);
			break;

		case 'ERROR':
			addOptions(category, ['', 'CallMiner']);
			break;

		case 'PASSWORD RESET ISSUE':
			addOptions(category, ['', 'CallMiner']);
			break;

		case 'LOGIN/LOGOUT':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA', 'Travel Advisor Portal (TAP) IN/UK']);
			break;

		case 'GFOB UNIVERSITY':
			addOptions(category, ['', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA']);
			break;

		case 'PROMOS':
			addOptions(category, ['', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA']);
			break;

		case 'THE SOURCE':
			addOptions(category, ['', 'Travel Advisor Portal (TAP) Asia/AU/CA/NZ/US/ZA']);
			break;

		case 'PRINT EXCURSION':
			addOptions(category, ['', 'Travel Advisor Portal (TAP) IN/UK']);
			break;

		case 'VIEW VACATION OVERVIEW':
			addOptions(category, ['', 'Travel Advisor Portal (TAP) IN/UK']);
			break;

		case 'OTHER':
			addOptions(category, ['', 'Bluecow', 'Dynamics', 'EU Ops', 'Enterprise', 'Hardware', 'M365', 'Network', 'Security', 'TD Portal', 'Telecom']);
			break;

		case 'DOCUMENTS':
			addOptions(category, ['', 'TD Portal']);
			break;

		case 'OPTIONALS':
			addOptions(category, ['', 'TD Portal']);
			break;

		case 'PAYROLL':
			addOptions(category, ['', 'TD Portal']);
			break;

		case 'TOUR REPORT':
			addOptions(category, ['', 'TD Portal']);
			break;

		case 'VOUCHERS':
			addOptions(category, ['', 'TD Portal']);
			break;

		case 'ORCA (EPORT CENTRAL)':
			addOptions(category, ['', 'Websites']);
			break;

		case 'CONTENT HUB':
			addOptions(category, ['', 'Websites']);
			break;

		case 'TRAVEL AGENT PORTAL (TAP)':
			addOptions(category, ['', 'Websites']);
			break;

		case 'CALL CENTRE':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'DYNAMICS CUSTOMER INSIGHT':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'DYNAMICS CUSTOMER SERVICE':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'DYNAMICS MARKETING':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'DYNAMICS SALES':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'OUTLOOK APP':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'SIEBEL':
			addOptions(category, ['', 'Dynamics']);
			break;

		case 'ACCOUNTING':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'AIR':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'BOOKING':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'COMMUNICATIONS':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'CONTRACT/INVENTORY':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'DATA MAINTENANCE':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'GROUPS':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'MEDIA REPOSITORY':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'OPERATING':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'OPS PORTAL':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'OPTIONAL EXCURSIONS':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'PLANNING':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'PRODUCT/INVENTORY DATA LOADING':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'PROMOTION':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'TOPS':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'TRAMS':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'TRANSFER ENGINE':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'UK REPORTING':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'WORK REQUESTS':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'WORKFLOW':
			addOptions(category, ['', 'Enterprise']);
			break;

		case 'CCS: SALES CONTROL':
			addOptions(category, ['', 'EU Ops']);
			break;

		case 'DYNAMICS NAVISION':
			addOptions(category, ['', 'EU Ops']);
			break;

		case 'SMS: SERVICES MANAGEMENT SYSTEM':
			addOptions(category, ['', 'EU Ops']);
			break;

		case 'CONFERENCE PHONE':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'DESKTOP':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'DOCKING STATION':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'HEADSET':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'KEYBOARD/MOUSE':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'LAPTOP':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'MALFUNCTION/FAILURE':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'MISSING/LOST/STOLEN':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'MONITOR':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'PRINTER COPIER':
			addOptions(category, ['', 'Hardware']);
			break;

		case 'AUTHENTICATOR':
			addOptions(category, ['', 'M365']);
			break;

		case 'EXCEL':
			addOptions(category, ['', 'M365']);
			break;

		case 'OUTLOOK EMAIL':
			addOptions(category, ['', 'M365']);
			break;

		case 'POWER AUTOMATE':
			addOptions(category, ['', 'M365']);
			break;

		case 'POWERBI':
			addOptions(category, ['', 'M365']);
			break;

		case 'POWERPOINT':
			addOptions(category, ['', 'M365']);
			break;

		case 'SHAREPOINT':
			addOptions(category, ['', 'M365']);
			break;

		case 'TEAMS':
			addOptions(category, ['', 'M365']);
			break;

		case 'WORD':
			addOptions(category, ['', 'M365']);
			break;

		case 'APPLIANCE':
			addOptions(category, ['', 'Network']);
			break;

		case 'CIRCUIT':
			addOptions(category, ['', 'Network']);
			break;

		case 'CITRIX':
			addOptions(category, ['', 'Network']);
			break;

		case 'CONNECTIVITY':
			addOptions(category, ['', 'Network']);
			break;

		case 'DHCP':
			addOptions(category, ['', 'Network']);
			break;

		case 'FIREWALL':
			addOptions(category, ['', 'Network']);
			break;

		case 'FTP':
			addOptions(category, ['', 'Network']);
			break;

		case 'INTERNET':
			addOptions(category, ['', 'Network']);
			break;

		case 'LAN':
			addOptions(category, ['', 'Network']);
			break;

		case 'LATENCY':
			addOptions(category, ['', 'Network']);
			break;

		case 'NETWORK DRIVERS':
			addOptions(category, ['', 'Network']);
			break;

		case 'NETWORK SPEED SLOW':
			addOptions(category, ['', 'Network']);
			break;

		case 'PASSWORD LOCKED - RESET':
			addOptions(category, ['', 'Network']);
			break;

		case 'VPN':
			addOptions(category, ['', 'Network']);
			break;

		case 'WIRED':
			addOptions(category, ['', 'Network']);
			break;

		case 'WIRELESS':
			addOptions(category, ['', 'Network']);
			break;

		case 'DATA LOSS/BREACH':
			addOptions(category, ['', 'Security']);
			break;

		case 'MALICIOUS SOFTWARE (VIRUS / MALWARE / RANSOMWARE)':
			addOptions(category, ['', 'Security']);
			break;

		case 'PHISHING':
			addOptions(category, ['', 'Security']);
			break;

		case 'PHYSICAL SECURITY':
			addOptions(category, ['', 'Security']);
			break;

		case 'POLICY VIOLATION':
			addOptions(category, ['', 'Security']);
			break;

		case 'SECURITY EVENT/MESSAGE':
			addOptions(category, ['', 'Security']);
			break;

		case 'SOCIAL ENGINEERING':
			addOptions(category, ['', 'Security']);
			break;

		case 'SPAM':
			addOptions(category, ['', 'Security']);
			break;

		case 'SUSPICIOUS ACTIVITY (EMAIL / SPAM / PHISH)':
			addOptions(category, ['', 'Security']);
			break;

		case 'THEFT (ASSETS/IP)':
			addOptions(category, ['', 'Security']);
			break;

		case 'USER ID / PW ISSUE / COMPROMISE':
			addOptions(category, ['', 'Security']);
			break;

		case 'VIRUS/MALWARE ALERT':
			addOptions(category, ['', 'Security']);
			break;

		case 'NUMBER ROUTING':
			addOptions(category, ['', 'Telecom']);
			break;

		case 'OUTAGE':
			addOptions(category, ['', 'Telecom']);
			break;

		case 'PHONE QUEUE':
			addOptions(category, ['', 'Telecom']);
			break;

		case 'RINGCENTRAL MAX':
			addOptions(category, ['', 'Telecom']);
			break;

		case 'VOICEMAIL':
			addOptions(category, ['', 'Telecom']);
			break;

		case 'EVENT':
			addOptions(category, ['', 'Event Notification']);
			break;

		case 'AIRHUB':
			addOptions(category, ['', 'Hubs']);
			break;

		case 'RESHUB':
			addOptions(category, ['', 'Hubs']);
			break;

		case 'SALESHUB':
			addOptions(category, ['', 'Hubs']);
			break;

		case 'API SUPPORT':
			addOptions(category, ['', 'Inquiry']);
			break;

		case 'AVALONGO APP (WEB PAGE ONLY)':
			addOptions(category, ['', 'MyAvalon']);
			break;

		case 'DOCKING LOCATION':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'EMERGENCY CONTACTS':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'GUEST ACKNOWLEDGEMENT':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MAKE A PAYMENT':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MY ACCOMMODATIONS':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MY DOCUMENTATION':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MY EXCURSIONS':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MY PROFILE':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MY VOUCHERS':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'MY WALLET':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'PASSENGER REGISTRATION':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'RESERVATION COMMUNICATIONS':
			addOptions(category, ['', 'MyAvalon', 'MyCosmos', 'MyGlobus']);
			break;

		case 'COSMOSGO APP (WEB PAGE ONLY)':
			addOptions(category, ['', 'MyCosmos']);
			break;

		case 'GLOBUSGO APP (WEB PAGE ONLY)':
			addOptions(category, ['', 'MyGlobus']);
			break;

		case 'EXCURSION PORTAL':
			addOptions(category, ['', 'Payments']);
			break;

		case 'MYSITES':
			addOptions(category, ['', 'Payments']);
			break;

		case 'NON-CREDIT CARD':
			addOptions(category, ['', 'Payments']);
			break;

		case 'ORCA':
			addOptions(category, ['', 'Payments']);
			break;

		case 'ORS':
			addOptions(category, ['', 'Payments']);
			break;

		case 'TAPS':
			addOptions(category, ['', 'Payments']);
			break;

		case 'TD PORTAL':
			addOptions(category, ['', 'Payments']);
			break;

		case 'CUSTOMER SURVEY':
			addOptions(category, ['', 'Surveys']);
			break;			
""")

# Ex: addOptions(subCat, ['', 'Access', 'Broken Functionality', 'Content']);
add_subcat = InputString("""
		case '':
			addOptions(subCat, allSubCategories);
			break;

		case 'ATLAS':
			addOptions(subCat, ['', 'Access', 'Broken Functionality', 'Content']);
			break;

		case 'AVALON CONSUMER WEBSITE':
			addOptions(subCat, ['', 'Content/Products', 'Forms', 'Login', 'Payments', 'Reservations (Booking)']);
			break;

		case 'COSMOS CONSUMER WEBSITE':
			addOptions(subCat, ['', 'Content/Products', 'Forms', 'Login', 'Payments', 'Reservations (Booking)']);
			break;

		case 'GLOBUS CONSUMER WEBSITE':
			addOptions(subCat, ['', 'Content/Products', 'Forms', 'Login', 'Payments', 'Reservations (Booking)']);
			break;

		case 'TRAVEL ADVISOR PORTAL (TAP) ASIA/AU/CA/NZ/US/ZA':
			addOptions(subCat, ['', 'Content/Products', 'Forms', 'GFOB University', 'Login/Logout', 'Payments', 'Promos', 'Reservations (Booking)', 'The Source']);
			break;

		case 'TRAVEL ADVISOR PORTAL (TAP) IN/UK':
			addOptions(subCat, ['', 'Content/Products', 'Login/Logout', 'Payments', 'Print Excursion', 'Reservations (Booking)', 'View Vacation Overview']);
			break;

		case 'TD PORTAL':
			addOptions(subCat, ['', 'Documents', 'Forms', 'Optionals', 'Other', 'Payroll', 'Tour Report', 'Vouchers']);
			break;

		case 'WEBSITES':
			addOptions(subCat, ['', 'Content Hub', 'Orca (Eport Central)', 'Payments']);
			break;

		case 'CALLMINER':
			addOptions(subCat, ['', 'Account Creation Request', 'Error', 'Password Reset Issue']);
			break;

		case 'MYAVALON':
			addOptions(subCat, ['', 'AvalonGo App (Web Page Only)', 'Docking Location', 'Emergency Contacts', 'Guest Acknowledgement', 'Login/Logout', 'Make a Payment', 'My Accommodations', 'My Documentation', 'My Excursions', 'My Profile', 'My Vouchers', 'My Wallet', 'Passenger Registration', 'Reservation Communications']);
			break;

		case 'MYCOSMOS':
			addOptions(subCat, ['', 'CosmosGo App (Web Page Only)', 'Docking Location', 'Emergency Contacts', 'Guest Acknowledgement', 'Login/Logout', 'Make a Payment', 'My Accommodations', 'My Documentation', 'My Excursions', 'My Profile', 'My Vouchers', 'My Wallet', 'Passenger Registration', 'Reservation Communications']);
			break;

		case 'MYGLOBUS':
			addOptions(subCat, ['', 'Docking Location', 'Emergency Contacts', 'GlobusGo App (Web Page Only)', 'Guest Acknowledgement', 'Login/Logout', 'Make a Payment', 'My Accommodations', 'My Documentation', 'My Excursions', 'My Profile', 'My Vouchers', 'My Wallet', 'Passenger Registration', 'Reservation Communications']);
			break;

		case 'BLUECOW':
			addOptions(subCat, ['', 'Other']);
			break;

		case 'DYNAMICS':
			addOptions(subCat, ['', 'Call Centre', 'Dynamics Customer Insight', 'Dynamics Customer Service', 'Dynamics Marketing', 'Dynamics Sales', 'Other', 'Outlook App', 'Siebel']);
			break;

		case 'EU OPS':
			addOptions(subCat, ['', 'CCS: Sales Control', 'Dynamics Navision', 'Other', 'SMS: Services Management System']);
			break;

		case 'ENTERPRISE':
			addOptions(subCat, ['', 'Accounting', 'Air', 'Booking', 'Communications', 'Contract/Inventory', 'Data Maintenance', 'Groups', 'Media Repository', 'Operating', 'Ops Portal', 'Optional Excursions', 'Other', 'Planning', 'Product/Inventory Data Loading', 'Promotion', 'TOPS', 'TRAMS', 'Transfer Engine', 'UK Reporting', 'Work Requests', 'Workflow']);
			break;

		case 'HARDWARE':
			addOptions(subCat, ['', 'Conference Phone', 'Desktop', 'Docking Station', 'Headset', 'Keyboard/Mouse', 'Laptop', 'Malfunction/failure', 'Missing/lost/stolen', 'Monitor', 'Other', 'Printer Copier']);
			break;

		case 'M365':
			addOptions(subCat, ['', 'Authenticator', 'Excel', 'Other', 'Outlook Email', 'Power Automate', 'PowerBI', 'PowerPoint', 'SharePoint', 'Teams', 'Word']);
			break;

		case 'NETWORK':
			addOptions(subCat, ['', 'Appliance', 'Circuit', 'Citrix', 'Connectivity', 'DHCP', 'FTP', 'Firewall', 'Internet', 'LAN', 'Latency', 'Network Drivers', 'Network Speed Slow', 'Other', 'Password Locked - Reset', 'VPN', 'Wired', 'Wireless']);
			break;

		case 'SECURITY':
			addOptions(subCat, ['', 'Data Loss/Breach', 'Malicious Software (Virus / Malware / Ransomware)', 'Other', 'Phishing', 'Physical Security', 'Policy Violation', 'Security Event/Message', 'Social Engineering', 'Spam', 'Suspicious Activity (email / spam / phish)', 'Theft (Assets/IP)', 'User ID / PW Issue / Compromise', 'Virus/Malware Alert']);
			break;

		case 'TELECOM':
			addOptions(subCat, ['', 'Number Routing', 'Other', 'Outage', 'Phone Queue', 'RingCentral MAX', 'Voicemail']);
			break;

		case 'EVENT NOTIFICATION':
			addOptions(subCat, ['', 'Event']);
			break;

		case 'HUBS':
			addOptions(subCat, ['', 'AirHub', 'ResHub', 'SalesHub']);
			break;

		case 'INQUIRY':
			addOptions(subCat, ['', 'API Support']);
			break;

		case 'PAYMENTS':
			addOptions(subCat, ['', 'Excursion Portal', 'MySites', 'Non-Credit Card', 'ORCA', 'ORS', 'TAPs', 'TD Portal']);
			break;

		case 'SURVEYS':
			addOptions(subCat, ['', 'Customer Survey']);
			break;
""")

