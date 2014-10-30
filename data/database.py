from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set echo to True to write queries to console when they are executed.
engine = create_engine('sqlite://///tmp/testdb.sqlite', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

