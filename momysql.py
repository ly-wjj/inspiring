import MySQLdb
import conf

class MoMysql():
    def __init__(self):
        self.host = conf.getConfig("database","dbhost")
        self.port = conf.getConfig("database","dbport")
        self.database = conf.getConfig("database","dbname")
        self.user = conf.getConfig("database","dbuser")
        self.passwd = conf.getConfig("database","dbpassword")
        self.charser = conf.getConfig("database","dbcharset")
        #self.conn = MySQLdb.connect(self.host,self.database,self.user,self.passwd,self.charser)
        #self.cursor = self.conn.cursor()

    def moinsert(self):
        db = MySQLdb.connect(host=str(self.host),port=int(self.port),db=self.database,
                             user=self.user,passwd=self.passwd,charset=self.charser)
        cursor = db.cursor()
        sql = "insert into groups(groupname) values(\"dbuser\")"
        try:
            cursor.execute(sql)
            print "1234"
        except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        except:
            print "INSERT FAILED!"
        # Rollback in case there is any error
            db.rollback()

        # close mysql connection
	    db.close()

    def moselect(self):
        db = MySQLdb.connect(host=str(self.host), port=int(self.port), db=self.database,
                             user=self.user, passwd=self.passwd, charset=self.charser)
        cursor = db.cursor()
        sql = "select * from groups"
        try:
            # execute sql
            cursor.execute(sql)
            # get all records
            dbresults = cursor.fetchall()
            print "successed"
        except:
            print "Error: unable to fecth data"

        # close the connection of database
        db.close()
        return dbresults;

momysql = MoMysql()
res = momysql.moselect()
print res
