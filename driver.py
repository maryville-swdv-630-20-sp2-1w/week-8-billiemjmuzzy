from Roles import *
from Users import *
from Permissions import *
from Notifications import * 
from LeaveRequest import *

def main():
    
    def role():
        # Created by Billie Muzzy
        
        # create instance of Role class
        new_role = Role('Lead', 'Initial Approval')
        # add role
        print(new_role.add_role())
        # edit role description
        print(new_role.edit_role_description(1, 'Super User'))
        # edit role name
        print(new_role.edit_role_name(1, 'Manager'))
        # delete role
        print(new_role.delete_role(4))
        # print table contents
        new_role.get_data()
        
    def user():
        # Created by Billie Muzzy
         
        # create instace of Users class
        new_user = User('fake@fake.com', 'H#LL0K!TTY', 3)
        # add user
        print(new_user.add_user())
        # edit user email
        print(new_user.edit_user_email(2, 'gizmo@muzznation.com'))
        # edit user password
        print(new_user.edit_user_password(1, 'H3ll0Puppy'))
        # edit user role id
        print(new_user.edit_user_role(2,1))
        # delete user
        print(new_user.delete_user(3))
        # print table contents
        new_user.get_data()
        
    def permission():
        # Created by Billie Muzzy
         
        # create instance of Permissions class
        new_permission = Permission('View', 'Read Only', 4)
        # add permission
        print(new_permission.add_permission())
        # edit permission name
        print(new_permission.edit_permission_name(1, 'Super User'))
        # edit permission description
        print(new_permission.edit_permission_description(1,'Read, Write, Edit, Delete'))
        # edit permission role
        print(new_permission.edit_permission_role(4,3))
        # delete permission
        print(new_permission.delete_permission(4))
        # print table contents
        new_permission.get_data()
        
    def notifications():
        # Created by Billie Muzzy
         
        # events
        pub = NotificationPublisher(['Leave Request', 'Leave Request Updated'])
        
        # subscribers
        atlas = NotificationSubscriber('Atlas', 'manager')
        gizmo = NotificationSubscriber('Gizmo', 'supervisor')
        billie = NotificationSubscriber('Billie', 'employee')
        
    
        # events registered for 
        pub.register("Leave Request", atlas)
        pub.register("Leave Request", gizmo)
        pub.register("Leave Request Updated", billie)

        # messages dispatched
        print("First Request:")
        pub.dispatch("Leave Request", "PTO Request")
        pub.dispatch("Leave Request Updated", "PTO Request")
        print()
        
        # unregister from event
        pub.unregister('Leave Request', gizmo)
        
        # messages dispatched 
        print("Second Request")
        pub.dispatch("Leave Request", "WFH Request")
        pub.dispatch("Leave Request Updated", "WFH Request")
    
    def leave():
        # Created by Ben Muzzy
        def leave_request():
            lr = LeaveRequest(["Ben", "Muzzy"], 50, 0)
            lr.print_header()
            # Should be Ben Muzzy
            print(f"Employee Name: {lr.get_employee()}")
            # Should be 12
            print(f"Leave Requested:  {lr.get_requested_hours()}")
            # Should be 10
            print(f"Total PTO Avail: {lr.get_total_hours()}\n")

        def paid_time_off():
                pto = PaidTimeOff(["Mike", "Muzzy"], 0, 10)
                pto.print_header()
                # Should be Mike Muzzy
                print(f"Employee Name: {pto.get_employee()}")
                # Should be 10
                print(f"PTO Requested:  {pto.get_requested_hours()}")
                # Should be 0
                print(f"Total PTO Avail: {pto.get_total_hours()}")
                # Should be False
                print(f"PTO Approved: {pto.approval()}")
                pto.add_hours(10)
                # Should be 10
                print(f"Updated PTO Avail: {pto.get_total_hours()}")
                # Should be True
                print(f"PTO Approved: {pto.approval()}\n")

        def unpaid_time_off():
            uto = UnpaidTimeOff(["Karline", "Muzzy"], 0, 10)
            uto.print_header()
            # Should be Karline Muzzy
            print(f"Employee Name: {uto.get_employee()}")
            print(f"Unpaid Time Off Requested: {uto.get_requested_hours()}")
            # Should be True
            print(f"Unpaid Time Off Approved: {uto.approval('y')}\n")

        def sick_days():
            sd = SickDays(["Atlas", "Muzzy"], 10, 8)
            sd.print_header()
            # Should be Atlas Muzzy
            print(f"Employee Name: {sd.get_employee()}")
            # Should be 8
            print(f"Sick Day Hours Request: {sd.get_requested_hours()}")
            # Should be 10
            print(f"Total PTO Avail: {sd.get_total_hours()}")
            print(f"Unpaid Time Off Approved: {sd.approval(False)}\n")
            
        def bereavement():
            b = Bereavement(["John", "Doe"], 5, 16)
            b.print_header()
            # Should be John Doe
            print(f"Employee Name: {b.get_employee()}")
            # Should be 16
            print(f"Bereavement Hours Request: {b.get_requested_hours()}")
            # Should be True
            print(f"Bereavement Approved: {b.approval('y')}\n")
        

        leave_request()
        paid_time_off()
        unpaid_time_off()
        sick_days()
        bereavement()   
       
    role() 
    user()
    permission()
    notifications()
    leave()
        
main()