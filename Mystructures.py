'''Local structures used in the program'''
import Myfunctions


class path:
    def __init__(self,folder_path:str='',file_name:str=''):
        self.path = {
            'folder_path' : folder_path,
            'file_name' :file_name,
            'full_path' : folder_path + "\\" + file_name,
        }
        

class internal_data:
    def __init__(self,this_path: path=path()):
        companys = path()
        self.internal_data = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            'companys' : companys.path,
            'selected_company' : '',
        }


class companys:
    def __init__(self,this_path: path=path()):
        self.companys = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            self.__class__.__name__: {}
        }


class clients:
    def __init__(self,this_path: path=path()):
        self.clients = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            'index_number' : 0,
            self.__class__.__name__ : {}
        }


class contacts:
    def __init__(self,this_path: path=path()):
        self.contacts = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            self.__class__.__name__ : {}
        }


class outgoing_invoices:
    def __init__(self,this_path: path=path()):
        self.outgoing_invoices = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            'index_number' : 0,
            self.__class__.__name__ : {}
        }


class jobs:
    def __init__(self,this_path: path=path(),
                 active_jobs_path:path=path(),
                 invoiced_jobs:path=path()):
        self.jobs = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            self.__class__.__name__ : {
                'active_jobs' : active_jobs_path.path,
                'invoiced_jobs' : invoiced_jobs.path,
            }
        }


class active_jobs:
    def __init__(self,this_path: path=path()):
        self.jobs = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            self.__class__.__name__ : {}
        }


class invoiced_jobs:
    def __init__(self,this_path: path=path()):
        self.jobs = {
            'created' : Myfunctions.todays_date(),
            'this_path' : this_path.path,
            self.__class__.__name__ : {}
        }


class company:
    def __init__(self,
            name:str,
            contact_name:str,
            adress:str,
            postcode_and_city:str,
            contry:str,
            phone_number:str,
            email:str,
            organization_number:str,
            bank_account:str,
            momsreg_number:str,                
            this_path:path=path(),
            logo_path:path=path(),
            clients_path:path=path(),
            outgoing_invoices_path:path=path(),
            duns_number: str = '',
            iban: str = '',
            swift: str = '',
    ):        
        self.company = {
            'created' : Myfunctions.todays_date(),
            'name' : name,
            'contact_name' : contact_name,
            'adress' : adress,
            'postcode_and_city' : postcode_and_city,
            'contry' : contry,
            'phone_number' : phone_number,
            'email' : email,
            'organization_number' : organization_number,
            'momsreg_number' : momsreg_number,
            'bank_account' : bank_account,
            'duns_number' : duns_number,
            'iban' : iban,
            'swift' : swift,
            'this_path' : this_path.path,
            'logo_path' : logo_path.path,
            'clients_path' :clients_path.path,
            'outgoing_invoices_path' : outgoing_invoices_path.path     
        }


class payment_condition:
    def __init__(self,text:str = '15 dagar',days:int = 15,only_bussines_days:bool = True):
        self.payment_conditon  = {
            'text' : text,
            'days' : days,
            'only_bussines_days' : only_bussines_days
        }


class client:
    def __init__(self,
            name:str,
            adress:str,
            postcode_and_city:str,
            contry:str,
            phone_number:str,
            email:str,
            organization_number:str,
            momsreg_number:str,
            bank_account:str,
            hourly_wage:int,
            overtime_percent:float,
            qualified_overtime_precent:float,
            this_path: path=path(),
            logo_path: path=path(),
            contacts_path: path=path(),
            jobs_path: path=path(),
            index_number : int=0,
            duns_number: str = '',
            iban: str = '',
            swift: str = ''
            ):
        self.client = {
            'created' : Myfunctions.todays_date(),
            'index_number':index_number,
            'name' : name,
            'adress' : adress,
            'postcode_and_city' : postcode_and_city,
            'contry':contry,
            'phone_number' : phone_number,
            'email' : email,
            'organization_number' : organization_number,
            'momsreg_number' : momsreg_number,
            'bank_account' : bank_account,
            'duns_number' : duns_number,
            'iban' : iban,
            'swift' : swift,
            'hourly_wage' : hourly_wage,
            'overtime_percent' : overtime_percent,
            'qualified_overtime_precent' : qualified_overtime_precent,
            'payment_condition' : {},
            'this_path' : this_path.path,
            'logo_path' : logo_path.path,
            'contacts_path' : contacts_path.path,
            'jobs_path' : jobs_path.path
        }


class contact:
    def __init__(self,
                 first_name:str,
                 last_name:str='',
                 this_path: path=path(),
                phone_one:str='',
                 email_one:str='',
                 email_two:str='',
                 adress_home:str='',
                 phone_two:str=''):
        self.contact = {
            'created' : Myfunctions.todays_date(),
            'first_name' : first_name,
            'last_name' : last_name,
            'phone_one' : phone_one,
            'phone_two' : phone_two,
            'email_one' : email_one,
            'email_two' : email_two,
            'adress_home' : adress_home,
            'this_path' : this_path.path
        }


class invoice:
    def __init__ (self,index_number:int=0):
        self.invoice = {
            'filename': '',
            'logo_path': '',
            'invoice':{
                'index_number': index_number,
                'date': '',
                'payment_condition': '',
                'last_payment_day': ''            
            },
            'bill':{
                'exclusive_taxes': '',
                'taxes': '',
                'total': ''
            },
            'customer':{
                'index_number': '',
                'name': '',
                'adress': '',
                'postcode_and_city': '',
                'contry':'',
                'contact': '', 
                'order_number': '',
                'job_name':''
            },
            'company' : {
                'name': '',
                'adress': '',
                'postcode_and_city': '',
                'contry':'',
                'contact':'',
                'iban':'',
                'phone_number':'',
                'email':'',
                'bank_account':'',
                'organization_number':'',
                'momsreg_number':'',
            },
            'workdays': []
        }


class jobb:
    def __init__(self,
                 name:str,
                 contact:contact,
                 ordernumber:str,
                 job_type:str,               
                 ongoing_or_fixed_price:str='ongoing',
                 budget:int=0,
                 hourly_wage:int=0,
                 overtime_percent:int=0,
                 qualified_overtime_precent:int=0,
                 invoice:invoice=invoice(),
                 this_path: path=path(),
                 invoice_path: path=path(),
                 order_path: path=path(),
                 booking_invoice_path: path=path()
                 ):
        self.job = {
            'created' : Myfunctions.todays_date(),
            'name' : name,
            'contact' : contact,
            'ordernumber' : ordernumber,
            'job_type' : job_type,
            'ongoing_or_fixed_price' : ongoing_or_fixed_price,         
            'budget' : budget,
            'hourly_wage' : hourly_wage,
            'overtime_percent' : overtime_percent,
            'qualified_overtime_precent' : qualified_overtime_precent,
            'calculated' : {'budget_used' : 0,
                            'budget_remaining' : 0,                            
                            'overtime_wage' : 0,
                            'qualified_overtime_wage' : 0,
                            'worked_normal_hours' : 0,
                            'worked_overtime_hours' : 0,
                            'worked_qualified_overtime_hours' : 0,
                            'normal_hours_total_cost' : 0,
                            'overtime_hours_total_cost' : 0,
                            'qualified_overtime_hours_total_cost' : 0,
                            'material' : 0,
                            },
            'workdays' : {},
            'material' : {},
            'invoice' : invoice.invoice,
            'outgoing_invoice_booked' : False,
            'paid_outgoing_invoice_booked' : False,
            'invoice_paid' : False,
            'this_path' : this_path.path,
            'invoice_path' : invoice_path.path,
            'order_path' : order_path.path,
            'booking_invoice_path': booking_invoice_path.path
        }   


class work_hours:
    def __init__(self,hours:int,comment:str):
        self.work_hours = {
            'hours' : hours,
            'comment' : comment
        }


class workday:
    '''If date is not given it will be saved as of todays date!'''
    def __init__(self,
                 normal_hours:work_hours,
                 overtime_hours:work_hours,
                 qualified_overtime_hours:work_hours,
                 date:str=Myfunctions.todays_date()):
        self.workday ={
            'date': date,
            'normal_hours' : normal_hours.work_hours,
            'overtime_hours' : overtime_hours.work_hours,
            'qualified_overtime_hours' : qualified_overtime_hours.work_hours
        }


class material:
    def __init__(self,
                 description:str,
                 cost:float,
                 count:int):
        self.material ={
            'description': description,
            'cost' : cost,
            'count' : count,
        }
        

class summerized_workday:
    def __init__(self,
                 comment:str,
                 count:float,
                 price_unit:float,
                 total_price:float,
                 unit:str="st"):
        self.summerized_workday = {
            'comment' : comment,
            'count' : count,
            'price_unit': price_unit,
            'total_price' : total_price,
            'unit' : unit
        }