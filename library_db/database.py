
from sqlalchemy.orm import sessionmaker
from .models import init_db

engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()