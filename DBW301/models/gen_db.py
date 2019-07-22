from .customer import Customer
from .mail_order_customer import MailOrderCustomer
from .walk_in_customer import WalkInCustomer
from .order import Order
from .ordered_item import OrderedItem
from .items import Items
from .stored_items import StoredItem
from .stores import Stores
from .headquarter import Headquarter
from . import db
from random import randrange, randint
 

class GenDB(object):
    def random_date(self):
        year = randint(2010,2019)
        month = randint(1,12)
        date = randint(1,28)
        return "%s-%s-%s"%(str(year),str(month),str(date))

    def gen_customer_table(self):
        for x in range(10000):
            x+=1
            customer_name='Cusomer %s'%(str(x))
            city_home_id = randrange(10)
            customer = Customer(customer_id=x,customer_name=customer_name,city_home_id=city_home_id,first_order_date=self.random_date())
            db.session.add(customer)
        db.session.commit()

    def gen_walk_in_customer_table(self):
        for x in range(5000):
            x+=1
            tourism_guide = "Tourism Guide %s"%(str(x))
            walk_in_customer = WalkInCustomer(customer_id=x,tourism_guide=tourism_guide,time_order=self.random_date())
            db.session.add(walk_in_customer)
        db.session.commit()

    def gen_mail_order_customer_table(self):
        for x in range(5000):
            x+=5001
            post_address = "Post address %s"%(str(x))
            mail_order_customer = MailOrderCustomer(customer_id=x,post_address=post_address,time_order=self.random_date())
            db.session.add(mail_order_customer)
        db.session.commit()

    def gen_headquater_table(self):
        for x in range(10000):
            x+=1
            city_name = 'City name %s'%(str(x))
            headquarter_addr = 'Headquater address %s'%(str(x))
            state = 'State %s'%(str(x))
            headquarter = Headquarter(city_id=x,city_name=city_name,headquarter_addr=headquarter_addr,state=state,start_time=self.random_date())
            db.session.add(headquarter)
        db.session.commit()

GenDB().gen_customer_table()
GenDB().gen_walk_in_customer_table()
GenDB().gen_mail_order_customer_table()
GenDB().gen_headquater_table()