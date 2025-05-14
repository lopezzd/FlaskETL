from enum import Enum
from peewee import *
from datetime import datetime
from peewee_enum_field import EnumField
from src.infra.database.database import db  # Importa o db corretamente

class PaymentMethod(Enum):
    CREDIT = 'Cartão de Credito'
    DEBIT = 'Cartão de Debito'
    PIX = 'Pix'
    DINHEIRO = 'Dinheiro'

class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)
    modified_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField(null=True)

    class Meta:
        database = db
        legacy_table_names = False

class User(BaseModel):
    name = CharField()
    email = CharField()
    password = TextField()
    telephone = BigIntegerField()
    country = CharField()
    city = CharField()

class ProductCategory(BaseModel):
    name = CharField()
    desc = TextField(null=True)

class ProductInventory(BaseModel):
    quantity = IntegerField()

class Product(BaseModel):
    name = CharField()
    desc = TextField(null=True)
    sku = CharField()
    category = ForeignKeyField(ProductCategory, backref='products')
    inventory = ForeignKeyField(ProductInventory, backref='products')
    price = DecimalField(max_digits=10, decimal_places=2)

class ShoppingSession(BaseModel):
    user = ForeignKeyField(User, backref='sessions')
    total = DecimalField(max_digits=10, decimal_places=2)

class OrderDetails(BaseModel):
    user = ForeignKeyField(User, backref='orders')
    total = DecimalField(max_digits=10, decimal_places=2)
    payment = EnumField(PaymentMethod, default=PaymentMethod.CREDIT)

class OrderItems(BaseModel):
    order = ForeignKeyField(OrderDetails, backref='items')
    product = ForeignKeyField(Product, backref='order_items')
    quantity = IntegerField()
