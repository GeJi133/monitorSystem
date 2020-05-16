# config=utf-8
from .DBUtil import db

class User(db.Model):
    username = db.Column(db.String(200), unique=True,primary_key = True)
    password = db.Column(db.String(50), unique=True)
    dorId = db.Column(db.String(20),unique = True)
    phonenumber = db.Column(db.String(20),unique = True)
    iffeet = db.Column(db.Integer(),unique=False)
    ifwater = db.Column(db.Integer(),unique=False)


    __tablename__ = 'user'

    def __init__(self, username=None, password=None, dorId = None, phonenumber = None,iffeet =None,ifwater=None):
        self.password = password
        self.username = username
        self.dorId = dorId
        self.phonenumber = phonenumber
        self.ifwater=ifwater
        self.iffeet=iffeet

    def __repr__(self):
        return '<User %r>' % (self.username)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item



class SignOn(db.Model):

    username = db.Column(db.String(200), unique=True,primary_key = True)
    password = db.Column(db.String(50), unique=True)


    __tablename__ = 'signon'

    def __init__(self, username=None, password=None):
        self.password = password
        self.username = username

    def __repr__(self):
        return '<User %r>' % (self.username)

class Water(db.Model):

    username = db.Column(db.String(255), unique=True,primary_key = True)
    ontime = db.Column(db.Time(6), unique=False)
    offtime = db.Column(db.Time(6),unique = False)

    __tablename__ = 'water'

    def __init__(self, username=None, ontime=None, offtime = None):
        self.username = username
        self.ontime = ontime
        self.offtime = offtime

    def __repr__(self):
        return '<User %r>' % (self.username)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

class WaterLog(db.Model):
    id=db.Column(db.Integer(),unique=True,autoincrement=True,primary_key=True)
    username = db.Column(db.String(255), unique=True,autoincrement=True)
    time = db.Column(db.DateTime(6), unique=False)
    operation = db.Column(db.String(255),unique = False)

    __tablename__ = 'water_log'

    def __init__(self, username=None, time=None, operation = None):
        self.username = username
        self.time = time
        self.operation = operation

    def __repr__(self):
        return '<Water %r,%r>' % (self.username,self.operation)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item


class Feet(db.Model):

    username = db.Column(db.String(255), unique=True, primary_key=True)
    time = db.Column(db.Time(6), unique=False)
    amount = db.Column(db.String(255), unique=False)
    petname = db.Column(db.String(255),unique=False)
    category = db.Column(db.String(255),unique=False)

    __tablename__ = 'feet'

    def __init__(self, username=None, time=None, amount=None,petname = None,category = None):
        self.username = username
        self.time = time
        self.amount = amount
        self.petname = petname
        self.category = category
    def __repr__(self):
        return '<Feets %r,%r,%r>' % (self.username,self.amount,self.petname)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item
class FeetLog(db.Model):
    id=db.Column(db.Integer(),unique=True,autoincrement=True,primary_key=True)
    username = db.Column(db.String(255), unique=True)
    time = db.Column(db.DateTime(6), unique=False)
    amount = db.Column(db.String(255), unique=False)
    petname = db.Column(db.String(255),unique=False)
    category = db.Column(db.String(255),unique=False)

    __tablename__ = 'feet_log'

    def __init__(self, username=None, time=None, amount=None,petname = None,category = None):
        self.username = username
        self.time = time
        self.amount = amount
        self.petname = petname
        self.category = category

    def __repr__(self):
        return '<FeetLogs %r,%r,%r>' % (self.username,self.amount,self.petname)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item
class Alert(db.Model):
    id=db.Column(db.Integer(),unique=True,autoincrement=True,primary_key=True)
    type = db.Column(db.String(40))
    time = db.Column(db.DateTime(6))
    message = db.Column(db.String(40))
    username = db.Column(db.String(40))

    __tablename__ = 'alert'

    def __init__(self, type=None, username=None,time=None, message=None):
        self.type=type
        self.message=message
        self.time = time
        self.username=username


    def __repr__(self):
        return '<FeetLogs %r,%r,%r>' % (self.username,self.message,self.time)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item



