from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column("id", Integer, primary_key=True, index=True)
    firstname = Column("firstname", String(30))
    lastname = Column("lastname", String(30))
    phone_number = Column("phone", String(20))
    email = Column("email", String(40))
    born_date = Column("born_date", Date)
