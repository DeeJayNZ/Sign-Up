
#ver 1.5 adding checkin page to test data
from bottle import run, route, view, get, post, request
from itertools import count

class Ticket: #a class is an object that holds information / data
    #_signifies a private variable. not to be used outside of this class
    _ids = count(0)
    
    def __init__(self, name, email, date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in
    

tickets = [
    Ticket("superman", "superman@superman.com", "15.12.1987", False),
    Ticket("batman", "batman@batman.com", "23.07.1989", False),
    Ticket("hulk", "hulk@brucebanner.com", "26.06.2003", False),
    Ticket("robin", "robin@somepoororphan.com", "25.09.2000", False)
    ]




#pages
#index page
@route("/")
@view("index")
def index(): #this function attatches decorators above
    pass



@route("/check-in")
@view("check-in")
def check_in(): #this function attatches decorators above
    data = dict (ticket_list = tickets)
    return data

@route('/check-in-success/<ticket_id>')
@view('check-in-success')
def check_in_success(ticket_id):
    ticket_id = int(ticket_id)
    found_ticket = None
    for ticket in tickets:
        if ticket.id == ticket_id:
            found_ticket = ticket
    data = dict(ticket = found_ticket)
    found_ticket.check_in= True
    return data
            







run(host="0.0.0.0", port = 8080, reloader=True, debug=True)