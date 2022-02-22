from sqlalchemy import Column, TIMESTAMP, String, ForeignKey, Sequence, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import func
import os

engine = create_engine(os.getenv('SQL_ENGINE'))
Base = declarative_base()

Session = sessionmaker(bind=engine)

class ProductModel(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    create_date = Column(TIMESTAMP, server_default=func.now())
    first_image_url = Column(Integer)
    title_fa = Column(String(300))
    title_en = Column(String(300))

    def __repr__(self):
       return "<ProductModel(title='%s')>" % (self.title)
    

class ProductDetailsModel(Base):
    __tablename__ = 'product_details'
    id = Column(Integer, Sequence('product_details_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    create_date = Column(TIMESTAMP, server_default=func.now())
    quality_rate = Column(Integer)
    # Purchase value relative to price
    pbv_rate = Column(Integer)
    innovation_rate = Column(Integer)
    features_rate = Column(Integer)
    useable_rate = Column(Integer)
    Design_rate = Column(Integer)
    price = Column(Integer)
    price_with_discount= Column(Integer)

    def __repr__(self):
       return "<ProductDetailsModel(product_id='%s')>" % (self.product_id)


Base.metadata.create_all(engine)