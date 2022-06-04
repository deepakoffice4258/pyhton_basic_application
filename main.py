import mysql.connector
import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password="Deepak4258@",database="storeprocedure")



def openacc():
    id=input("emter the id")
    n=input("enter the name:")
    ac=input("enter the account number:")
    db=input("enter date of birth")
    em=input("enter the your email")
    ob=int(input("enter the opening balance: "))
    dt = datetime.datetime.now()
    opeingbalnce=int(input("enter hte opeing balnce"))
    data1=(id,n,ac,db,em,dt,ob)
    data2=(id,ac,ob)
    data3=(ac,id)
    sql1=('insert into ACCOUNT values(%s,%s,%s,%s,%s,%s,%s)')
    sql2=('insert into Bankaccount(%s,%s,%s)')
    sql3=('insert into accountstatment (%s,%s)')
    x=mydb.cursor()
    x.execute(sql1.data1)
    x.execute(sql2.data2)
    x.execute(sql3.data3)
    print("data is entered ")
    main()
def depoammount():
    amount=input("enter the ammount you ant to deposite")
    ac=input("enter the account number:")
    a="select balance from amount where bankaccountnumber=%S"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a.data)
    result=x.fetchone()
    t=result[0]+amount
    sql1=("update amount set balnce where ACCOUNT=%s")
    d=(t,ac)
    x.excute(sql,d)
    mydb.commit()
    main()
def withdraw():
    amount=input("enter the ammount you ant to withdraw: ")
    ac=input("enter the account number:")
    a="select balance from amount where bankaccountnumber=%S"
    data = (ac)
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()

    t = result[0] - amount
    if t>5000:
        print("withdraw susefully")
        sql1 = ("update amount set balnce where ACCOUNT=%s")
        d = (t,ac)
        mydb.commit()
    else:
        print("you have to mainted minimum balance")
    main()
def  balnceenq():
    ac=input("enter the number no: ")
    a='select *from amount where bankaccountid=%s '
    data=(a,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("balance for account :",ac,"is",result[-1])


def main():
    print("""
         1.OPEN NEW ACCOUNT
         2.DEPOSITE AMMOUNT
         3.WITHDRAW AMOUNT
         4.BALANCE ENQUIRY
         5.DISPLAYING COUSTOMER DETALIS
         6.CLOSE ACCOUNT
         """)
    choice=input("enter the task: ")
    if (choice=="1"):
        openacc()
    elif(choice=="2"):
        depoammount()
    elif(choice=="3"):
        withdraw()
    elif(choice=="4"):
        balnceenq()
    else:
        print("envalid choice")
        main()
main()
