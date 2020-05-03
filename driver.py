from Roles import *
from Users import *
from Permissions import *
from Notifications import * 
from LeaveRequest import *

def main():
    
    def role():
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
        # create instance of the LeaveRequest class
        
        
   
        
       
       
    # role() 
    # user()
    # permission()
    # notifications()
    leave()
    
   
    

    
        
main()