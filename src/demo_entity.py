from marshmallow_dataclass import dataclass as mm_dataclass
from dataclasses_json import dataclass_json, Undefined
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.serializer import loads, dumps
from sqlalchemy.sql import func
from base_factory import Base
import json

@dataclass_json
@mm_dataclass
class DemoEntity(Base):
    __tablename__ = 'DemoEntity'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
