# Created By Billie Muzzy
from sqlalchemy import create_engine, Column, Integer, String, func, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Leave.db', echo=False)
Base = declarative_base()


class Permission(Base):

    def __init__(self, name, description, role_id):
        """Initialization

        Arguments:
            name {string} -- Name of permission
            description {string} -- Description of permission
            role_id {int} -- id of role permission is associated with
        """

        self.name = name
        self.description = description
        self.role_id = role_id

    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    role_id = Column(Integer)

    def add_permission(self):
        """Add Permission
        """

         # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Check if name already exists
        permissions = session.query(func.count(Permission.name)).filter(Permission.name == self.name).all()
        for permission in permissions:
            count = (permission[0])
        # if exist return error                      
        if count > 0:      
            session.close()
            return "Permission already exists"
        # if does not exit add and return message
        else:
            session.add(self)
            session.commit()
            session.close()
            return "Permission added"
        
    
    def edit_permission_name(self,id, name):
        """Method to edit permission name

        Arguments:
            id {integer} -- ID of record to edit
            name {string} -- Name to edit

        Returns:
            [string] -- Returns confirmation message
        """        
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(Permission).filter(Permission.id == id).\
            update({Permission.name: name}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # return message
        return f"Permission id {id} was updated"
    
    def edit_permission_description(self, id, description):
        """Method to edit permission description

        Arguments:
            id {Integer} -- ID of record to edit
            description {String} -- Description to edit

        Returns:
            String -- Confirmation message
        """        
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(Permission).filter(Permission.id == id).\
            update({Permission.description: description}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # return message
        return f"Permission id {id} was updated"
    
    def edit_permission_role(self,id, role):
        """Method to edit permission role_id

        Arguments:
            id {Integer} -- ID of record to edit
            role {Integer} -- Role ID to edit

        Returns:
            String -- Confirmation Message
        """        
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(Permission).filter(Permission.id == id).\
            update({Permission.role_id: role}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # return message
        return f"Permission id {id} was updated"
    
    def delete_permission(self, id):
        """Method to delete permission

        Arguments:
            id {Integer} -- ID of record to delete

        Returns:
            String -- Confirmation Message
        """        
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # check if name already exists
        session.query(Permission).filter(Permission.id == id).delete()
        # commit and close
        session.commit()
        session.close()
        # return message
        return f"Permission id {id} has been deleted"
    
    def get_data(self):
        """Method to print Permissions table
        """        
        Session = sessionmaker(bind=engine)
        session = Session()
        for row in session.query(Permission).order_by(Permission.id):
            print(row.id, row.name, row.description, row.role_id)
        session.close()
    
    
        
    
    
