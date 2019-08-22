import mysql.connector

class tenant(object):
    def __init__(self,id,name,generic_mail,user):
        self.id=id
        self.name=name
        self.generic_mail=generic_mail
        self.owner=user

class user(object):
    def __init__(self,id,username,password,firstname,lastname,phone,mail,role,idp_managed):
        self.id=id
        self.username=username
        self.password=password
        self.firstname=firstname
        self.lastname=lastname
        self.phone=phone
        self.mail=mail
        self.role=role
        self.idp_managed=idp

class group(object):
    def __init__(self,id,name,user):
        self.id=id
        self.name=name
        self.owner=user

class role(object):
    def __init__(self,id,name):
        self.id=id
        self.name=name

class permission(object):
    def __init__(self,id,permission):
        self.id=id
        self.name=name

class region(object):
    def __init__(self,id,name,idp_service):
        self.id=id
        self.name=name
        self.idp_service=idp_service

class idp_service(object):
    def __init__(self,id,host,port,service_credentials):
        self.id=id
        self.host=host
        self.port=port
        self.service_credentials=service_credentials

class service_credentials(object):
    def __init__(self,id,login,password):
        self.id=id
        self.login=login
        self.password=password

class forge_service(object):
    def __init__(self,id,name,host,port,service_credentials)
        self.id=id
        self.name=name
        self.host=host
        self.port=port
        self.service_credentials=service_credentials
