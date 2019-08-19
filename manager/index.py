import mysql.connector
from secureconfig import SecureConfigParser

def dbformation():

    allspark_db=mysql.connector.connect(host="localhost",user="catalogue",password="JieTh8Th", database="Catalogue")
    
def getconfig():
    configpath='config.ini'
    key_env = 'SCP_INI_KEY'

    scfg = SecureConfigParser.from_env('SCP_INI_KEY')
    scfg.read(configpath)

    username = scfg.get('credentials', 'username')
    password = scfg.get('credentials', 'password')

    connection = GetSomeConnection(username, password)

    # IMPORTANT: supply encrypt=True to encrypt values.
    scfg.set('credentials', 'password', 'better_password', encrypt=True)

    fh=open('/path/to/new_scfp.ini', 'w')
    scfg.write(fh)
    fh.close()
    


