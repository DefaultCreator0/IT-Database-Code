
import mysql.connector
import csv


def main():

    # a = QueryEmpList("select * from employeeinfo")

    # b = QueryDeviceList("select * from deviceinfo")

    # c = QueryTicketList("select * from ticket")

    # #a[1][0] : Touple of Name
    # #a[1][0][0] String of Name for employeeinfo
    # ToCSV(a,a[1][1][0])
    # #b[1][0] : Touple of Name
    # #b[1][0][0] String of Name for deviceinfo
    # ToCSV(b,b[1][0][0])
    # #c[1][0] : Touple of Name
    # #c[1][0][0] String of Name for deviceinfo
    # ToCSV(c,c[1][2][0])

    functions = {
        "getEmpInfoPackage":getEmpInfoPackage,
        "GeneralQuery" : GeneralQuery
    }


#Querying the employeeinfo table in the database and storing in the "employeeinfo.csv" file
def QueryEmpList(query):
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    #Query that Is requested
    temp = ["EmployeeID","ManagerID","Job Position","Name"]
    name = []
    QueryList = []
    QueryList.append(temp)
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute(query)
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x)
    #Returning a touple
    cursor.execute("Select table_name from information_schema.tables where table_schema = 'company'")
    for x in cursor:
        name.append(x)

    TotalData =[QueryList,name]

    return TotalData
#Querying the deivceinfo table in the database and storing in the "deviceinfo.csv" file
def QueryDeviceList(query):
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    #Query that Is requested
    temp = ["SN Number","M Number","Year of Manufacture","Brand","Model","Device User"]
    name = []
    QueryList = []
    QueryList.append(temp)
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute(query)
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x)
    #Returning a touple
    cursor.execute("Select table_name from information_schema.tables where table_schema = 'company'")
    for x in cursor:
        name.append(x)

    TotalData =[QueryList,name]

    return TotalData
#Querying the Ticket table in the database and storing in the "ticket.csv" file
def QueryTicketList(query):
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    #Query that Is requested
    temp = ["Ticket ID","Contents","Requester","Priority","Assigned To","Nature","Department"]
    name = []
    QueryList = []
    QueryList.append(temp)
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute(query)
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x)
    #Returning a touple
    cursor.execute("Select table_name from information_schema.tables where table_schema = 'company'")
    for x in cursor:
        name.append(x)

    TotalData =[QueryList,name]

    return TotalData

#Writing data into a CSV file from List
def ToCSV(data,name):
    
    name = name+".csv"
    with open(name, "w" ,newline='') as file:
        writer = csv.writer(file)

        writer.writerows(data[0])

#Pulling data from CSV into Python
def FromCSV():

    Empdata = []
    Devicedata = []
    Ticketdata = []

    #Opening and storing CSV data into Lists that are going to be parsed later
    try:
        with open("New Employees.csv",mode ='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                Empdata.append(lines)
        
        with open("New Device.csv",mode ='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                Devicedata.append(lines)
            
        with open("New Tickets.csv",mode ='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                Ticketdata.append(lines)
    except:
        print("No file found")
    
    IntoDatabase(Empdata,"Emp")
    IntoDatabase(Devicedata,"Dev")
    IntoDatabase(Ticketdata,"Tik")
    #Erasing Existing data in CSV file and leaving only Template Data 
    with open("New Employees.csv","w") as file:
        writer =csv.writer(file)
        writer.writerow(["EmployeeID","ManagerID","JobPosition","Name"])
        pass
    with open("New Device.csv","w") as file:
        writer =csv.writer(file)
        writer.writerow(["SN","MN","YearOfManufacture","Brand","Model","DeviceUserID"])
        pass
    with open("New Tickets.csv","w") as file:
        writer =csv.writer(file)
        writer.writerow(["TicketID","Contents","Requester","Priority","AssignedTo","Nature","Department"])
        pass
#Inserting New Data Into Database
def IntoDatabase(data,which):
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    
    #Inserting New Employee Data into Database
    if(which == "Emp"):
        try:
            for x in range(1,len(data)):
                cursor = db.cursor()
                temp ="insert into employeeinfo values("+data[x][0]+","+data[x][1]+",'"+data[x][2]+"','"+data[x][3]+"')"
                cursor.execute(temp)
        except:
            print("No new Employee")
    #Inserting New Device Data into Database
    if(which == "Dev"):
        try:
            for x in range(1,len(data)):
                cursor = db.cursor()
                temp ="insert into deviceinfo values('"+data[x][0]+"','"+data[x][1]+"','"+data[x][2]+"','"+data[x][3]+"','"+data[x][4]+"','"+data[x][5]+"')"
                print(temp)
                cursor.execute(temp)
        except:
            print("No new Device")
    #Inserting New Ticket Data into Database
    if(which == "Tik"):
        try:
            for x in range(1,len(data)):
                cursor = db.cursor()
                temp ="insert into ticket values("+data[x][0]+",'"+data[x][1]+"',"+data[x][2]+",'"+data[x][3]+"',"+data[x][4]+",'"+data[x][5]+"','"+data[x][3]+"')"
                cursor.execute(temp)
        except:
            print("No new Ticket")
    db.commit()


def getExistingEmpIDs():
    '''Returns a list of all Employee IDs that are in use'''
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    QueryList = []
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute("select * from employeeinfo")
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x[0])
    return QueryList

def getEmpFromID(ID):
    '''Returns Employee Data based on the ID provided'''
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    Query = []
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute("select * from employeeinfo where EmployeeID ="+str(ID))
    for x in cursor:
        Query.append(x)
    
    return Query

def getDevFromEmp(ID):
    '''Returns the Devices that are in use by the provided Employee'''
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    Query = []
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute("select * from deviceinfo where DeviceUser ="+str(ID))
    for x in cursor:
        Query.append(x)
    
    return Query



def NewEmpWritUp(EmpID = 0,ManID = 0,Pos ="",Name = ""):

    Emp = [EmpID,ManID,Pos,Name]
    EmpWriteToDatabase(Emp) 
def EmpWriteToDatabase(data):
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    try:
        cursor = db.cursor()
        temp ="insert into employeeinfo values("+str(data[0])+","+str(data[1])+",'"+data[2]+"','"+data[3]+"')"
        cursor.execute(temp)
        db.commit()
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:
            print("This entry is already in the database")
        elif e.errno == 1452:
            print("Invalid Employee ID")

def NewDevWriteUp(SN = "",MN = "",Year = 0,Brand = "",Model = "",User = 0):

    Dev = [SN,MN,Year,Brand,Model,User]
    DevWriteToDatabase(Dev)
def DevWriteToDatabase(data):
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    try:
        cursor = db.cursor()
        temp ="insert into deviceinfo values('"+data[0]+"','"+data[1]+"','"+str(data[2])+"','"+str(data[3])+"','"+str(data[4])+"','"+str(data[5])+"')"
        cursor.execute(temp)
        db.commit()
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:
            print("This entry is already in the database")
        elif e.errno == 1452:
            print("Invalid Employee ID")    

def NewTicketWriteUp(ID = 0,Contents = "",Requester = 0,Priority = "",AssignedTo = 0,Nature = "",Dept = ""):
    
    Tik =[ID,Contents,Requester,Priority,AssignedTo,Nature,Dept]
    TikWriteToDatabase(Tik)
def TikWriteToDatabase(data):
    
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    try:
        cursor = db.cursor()
        temp ="insert into ticket values("+str(data[0])+",'"+str(data[1])+"',"+str(data[2])+",'"+str(data[3])+"',"+str(data[4])+",'"+str(data[5])+"','"+str(data[3])+"')"
        cursor.execute(temp)
        db.commit()
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:
            print("This entry is already in the database")
        elif e.errno == 1452:
            print("Invalid Employee ID")
            
def getAllEmpName():
    '''Returns a list of all Employee names that are in the database'''
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    QueryList = []
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute("select * from employeeinfo")
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x[3])
    return QueryList

def getAllEmpPos():
    '''Returns a list of all Employee names that are in the database'''
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    QueryList = []
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute("select * from employeeinfo")
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x[2])
    return QueryList

def GeneralQuery(query):
    '''Returns a list of all Employee names that are in the database'''
    #Connects to Database
    db = mysql.connector.connect(user='root', password="Turbo50%", # required
    port=3306,
    host="127.0.0.1", # required
    database='company',
    auth_plugin='caching_sha2_password' # required
    )
    QueryList = []
    #Fetching the Query
    cursor = db.cursor()
    cursor.execute(query)
    #Placing the Query into a List
    for x in cursor:
        QueryList.append(x[2])
    return QueryList

def getEmpInfoPackage():
    data = []

    data.append(getExistingEmpIDs())
    data.append(getAllEmpName())
    data.append(getAllEmpPos())

    return data


main()
# FromCSV()
# NewEmpWritUp(75,15,"Manager","Roosevelt")
# NewDevWriteUp("2134123","1236fsds",2005,"HP","Envy",75)
# NewTicketWriteUp(1221,"Laptop charger is broken",75,"Important",15,"Repair","IT")
# print(getEmpInfoPackage()[0])
# print(getEmpInfoPackage()[1])
# print(getEmpInfoPackage()[2])

