from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://', echo=True)

session_maker = sessionmaker(engine)
