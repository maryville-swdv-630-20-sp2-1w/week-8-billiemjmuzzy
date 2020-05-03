from sqlalchemy import create_engine, Column, Integer, String, func, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Leave.db', echo=False)
Base = declarative_base()


class Role(Base):

    def __init__(self, name, description):
        """Initialization

        Arguments:
            name {string} -- name of role
            description {string} -- description of role
        """
        self.name = name
        self.description = description

    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def add_role(self):
        """Method to add a role to the roles table

        Returns:
            string -- Confirmation Message
        """
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Check if name already exists
        names = session.query(func.count(Role.name)).filter(
            Role.name == self.name).all()
        for name in names:
            count = (name[0])
        # if exist return error
        if count > 0:
            session.close()
            return "Role already exists"
        # if does not exit add and return message
        else:
            session.add(self)
            session.commit()
            session.close()
            return "Role added"

    def edit_role_description(self, id, update):
        """Method to edit the role description in the roles table

        Arguments:
            id {int} -- Unique id for the role
            update {string} -- the new role description

        Returns:   
            string: Confirmation the role updated
        """

        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # filter
        session.query(Role).filter(Role.id == id).\
            update({Role.description: update}, synchronize_session='fetch')
        # commit and close
        session.commit()
        session.close()
        # return message
        return f"Role id {id} was updated"

    def edit_role_name(self, id, update):
        """Method to edit role name in the roles table

        Arguments:
            id {int} -- id of role
            update {string} -- the new role name
        """
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(Role).filter(Role.id == id).\
            update({Role.name: update}, synchronize_session='fetch')
        session.commit()
        session.close()
        return f"Role id {id} was updated"

    def delete_role(self, id):
        """Method to delete the role from the roles table

        Arguments:
            id {[int]} -- id of record to delete
        """
        # create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # check if name already exists
        session.query(Role).filter(Role.id == id).delete()
        # commit and close
        session.commit()
        session.close()
        # return message
        return f"Role id {id} has been deleted"

    def get_data(self):
        """Method to return data
        """
        Session = sessionmaker(bind=engine)
        session = Session()
        for row in session.query(Role).order_by(Role.id):
            print(row.id, row.name, row.description)
        session.close()
