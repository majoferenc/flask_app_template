from dataclasses import dataclass
from dataclasses_json import dataclass_json
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func
from base_factory import Base
import json

@dataclass_json
@dataclass
class DemoEntity(Base):
    __tablename__ = 'DemoEntity'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return "<DemoEntity Value(id='%s', firstname='%s', lastname='%s' created_at='%s')>" % (
            self.id, self.firstname, self.lastname, self.created_at)


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)