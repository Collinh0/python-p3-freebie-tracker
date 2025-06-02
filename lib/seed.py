#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

company1 = Company(name="META", founding_year=2013)
company2 = Company(name="Safaricom", founding_year=2003)
company3 = Company(name="AWS", founding_year=2014)