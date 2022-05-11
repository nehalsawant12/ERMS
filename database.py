import pymysql

from models import Employee

db = pymysql.connect(host='localhost',user='root',password='',database='article')

cursor = db.cursor()
print("Connected to Database")
# *emp --> Variable number of arguments  create('raj',147852)
# **emp --> keyword number of arguments  create(ename='raj',esalary=14852)

def create(*emp):
    query = "insert into emp1(ename,esal,eimage) values (%s,%s,%s);"
    cursor.execute(query,emp)
    print('Row inserted')
    db.commit()

def Delete(eid):
    query = "Delete from emp1 where eid = %s;"
    cursor.execute(query,(eid))
    db.commit()

def update(*emp):
    query = "Update emp1 set ename = %s ,esalary = %s, eimage = %s where eid = %s;"
    cursor.execute(query,emp)
    print("Row Updated",emp)
    db.commit()
    


def all():
    query = "select * from emp1;"
    cursor.execute(query)
    rows = cursor.fetchall()
    emplist=[]
    for row in rows:
        emp=Employee(eid=row[0],ename=row[1],esalary=row[2],eimage=row[3])
        emplist.append(emp)
    return emplist


def get(eid):
    query = "select * from emp1 where eid=%s;"
    cursor.execute(query,(eid))
    row = cursor.fetchone()
    emp=Employee(eid=row[0],ename=row[1],esalary=row[2],eimage=row[3])
    return emp
    

    




emplist = all()
print(emplist)





    
    
