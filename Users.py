# Created By Billie Muzzy
from sqlalchemy import create_engine, Column, Integer, String, func, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Leave.db', echo=False)
Base = declarative_base()

class User(Base):
    
    
    def __init__(self,  email, password, role_id):
        """Initialization

        Arguments:
            role_id {int} -- id of role that user is assigned to 
            email {string} -- email address of user
            password {string} -- password of user
        """
        self.email = email
        self.password = password
        self.role_id = role_id
     
        
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer)
    
    def add_user(self):
        """Method to add a user to the users table

        Returns:
            string -- Confirmation Message
        """
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Check if name already exists
        emails = session.query(func.count(User.email)).filter(User.email == self.email).all()
        for email in emails:
            count = (email[0])
        # if exist return error                      
        if count > 0:      
            session.close()
            return "User already exists"
        # if does not exit add and return message
        else:
            session.add(self)
            session.commit()
            session.close()
            return "User added"
        
    def edit_user_email(self, id, email):
        """Method to edit user's email from the
        users table. 

        Arguments:
            id {int} -- ID of user record
            email {string} -- The email address
            of the user. 
        """
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(User).filter(User.id == id).\
            update({User.email: email}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # print message
        return f" The email address {email} was updated for user id {id}."
    
    def edit_user_password(self, id, password):
        """Method to edit a user's password

        Arguments:
            id {int} -- ID of user record
            password {string} -- password of user

        Returns:
            string -- confirmation message
        """        
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(User).filter(User.id == id).\
            update({User.password: password}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # print message
        return f" The password was updated for user id {id}."
   

    def edit_user_role(self, id, role_id):
        """[summary]

        Arguments:
            id {int} -- id of user to edit
            role_id {int} -- id of role to edit
        """        
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(User).filter(User.id == id).\
            update({User.role_id: role_id}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # return message
        return f" The role_id was updated for user id {id}."
    
    def delete_user(self, id):
        """Method to delete user from the users table

        Arguments:
            id {integer} -- The ID of the record to be deleted
        """ 
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # check if name already exists
        session.query(User).filter(User.id == id).delete()
        # commit and close
        session.commit()
        session.close()
        # return message 
        return f"User id {id} has been deleted"
                                                     
    
    def get_data(self):
        """Method to display table contents.
        Does not display password
        """        
        Session = sessionmaker(bind=engine)
        session = Session()
        for row in session.query(User).order_by(User.id):
            print(row.id, row.email, row.role_id)
        session.close()
            
        

