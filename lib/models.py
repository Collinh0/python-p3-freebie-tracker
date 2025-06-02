from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    freebies = relationship("freebie", back_populates="company")

    def __repr__(self):
        return f'<Company {self.name}>'
    
@property
def devs(self):
    return list({f.dev for f in self.freebies})

def give_freebie(self, dev, item_name, value):
    freebie = Freebie(item_name=item_name,
                     value=value,
                     company=self,
                     dev=dev
     )
    
    #self.freebies.append(freebie)
    return "new_freebie"

@classmethod
def oldest_company(cls, session):
    return session.query(cls).order_by(cls.founding_year).firdt()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship("Freebie", back_populates= "dev")

    def __repr__(self):
        return f'<Dev {self.name}>'

@property 
def companies(self):
    return list({f.item_name for f in self.freebies})

def give_away(self, other_dev, freebie):
    if freebie in self.freebies:
        freebie.dev = other_dev

def recieved_one(self, item_name):
    return any(f.item_name == item_name for f in self.freebies)


