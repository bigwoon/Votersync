from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's
# voter_sync_app.db file.
engine = create_engine('sqlite:///voter_sync_app.db')

# Create a base class for our classes definitions.
Base = declarative_base()

# Define a Voter class which will be used to create the voters table.
class Voter(Base):
    __tablename__ = 'voters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    street_number = Column(String)
    email = Column(String)
    race = Column(String)

# Create all tables in the engine.
Base.metadata.create_all(engine)

# Create a configured "Session" class.
Session = sessionmaker(bind=engine)

# Create a Session.
session = Session()

# Example of adding a new voter to the database.
new_voter = Voter(name='John Doe', age=30, address='123 Main St', street_number='123', email='john.doe@example.com', race='Caucasian')
session.add(new_voter)
session.commit()

# Query the database.
for voter in session.query(Voter).all():
    print(voter.name, voter.age, voter.address, voter.street_number, voter.email, voter.race)