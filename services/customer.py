import copy

from fastapi import HTTPException, Depends

from schema.product import Product, products
from schema.order import Order, OrderCreate

from schema.customer import Customer, CustomerCreate, customers

from logger import logger



class CustomerService:

    @staticmethod
    def check_username(username: str):
        for customer in customers:
            if customer.username == username:
                raise HTTPException(status_code=400, detail="username already exist")
        return username
   
    
customer_service = CustomerService()
