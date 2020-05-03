class LeaveRequest():
    def __init__(self, employee, hours, requested):
        self.employee_name = employee
        self.leave_type = "Leave Request"
        self.hours_available = hours
        self.hours_requested = requested

    def get_employee(self):
        return f"{self.employee_name[0]} {self.employee_name[1]}"

    def get_leave_type(self):
        return self.leave_type

    def get_requested_hours(self):  # returns number of pto hours requested
        return self.hours_requested

    def get_total_hours(self):  # returns total pto avail
        return self.hours_available

    def add_hours(self, acquired):
        self.hours_available += acquired
        return self.hours_available

    def deduct_hours(self, consumed_pto):
        self.hours_available -= consumed_pto
        return self.hours_available

    def print_header(self):
        print(f"""{'*'*75}\n{self.leave_type.upper()}\n{'*'*75}""")


class PaidTimeOff(LeaveRequest):
    def __init__(self, employee, hours, requested):
        super().__init__(employee, hours, requested)
        self.leave_type = "Paid Time Off"

    def approval(self):
        if self.hours_available >= self.hours_requested:
            return True
        else:
            return False


class UnpaidTimeOff(LeaveRequest):
    def __init__(self, employee, hours, requested):
        super().__init__(employee, hours, requested)
        self.leave_type = "Unpaid Time Off"

    def approval(self, approved):
        self.approved = approved
        if approved == "y":
            self.approved = True
            return self.approved
        elif approved == "n":
            self.approval = False
            return False
        else:
            return "Invalid option, please select [y] or [n]"


class SickDays(LeaveRequest):
    def __init__(self, employee, hours, requested):
        super().__init__(employee, hours, requested)
        self.leave_type = "Sick Day"
        self.doctor_note = False

    def approval(self, note):
        if self.hours_available >= self.hours_requested and self.doctor_note == True:
            return True
        elif self.hours_available >= self.hours_requested and self.doctor_note == False:
            return "Please provide Dr. note for approval."
        else:
            return False
        
class Bereavement(LeaveRequest):
    def __init__(self, employee, hours, requested):
        super().__init__(employee, hours, requested)
        self.leave_type = "Bereavement"

    def approval(self, approved):
        self.approved = approved
        if approved == "y":
            self.approved = True
            return self.approved
        elif approved == "n":
            self.approval = False
            return False
        else:
            return "Invalid option, please select [y] or [n]"