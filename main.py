import mysql.connector
import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password="Deepak4258@",database="storeprocedure")



def openacc():
    user_id=input("emter the id")
    name=input("enter the name:")
    accnumber=input("enter the account number:")
    user_dob=input("enter date of birth")
    user_email=input("enter the your email")
    datetime = datetime.datetime.now()
    opeingbalnce=int(input("enter hte opeing balnce"))
    data1=(user_id,name,accnumber,user_dob,user_email,datetime,opeingbalnce)
    data2=(user_id,accnumber,opeingbalnce)
    data3=(accnumber,user_id)
    sql1=("insert into ACCOUNT values(%s,%s,%s,%s,%s,%s,%s)")
    sql2=("insert into Bankaccount(%s,%s,%s)")
    sql3=("insert into accountstatment (%s,%s)")
    x=mydb.cursor()
    x.execute(sql1.data1)
    x.execute(sql2.data2)
    x.execute(sql3.data3)
    print("data is entered ")
    main()
def depoammount():
    amount=input("enter the ammount you ant to deposite")
    accnumber=input("enter the account number:")
    a="select balance from amount where bankaccountnumber=%S"
    data=(accnumber)
    x=mydb.cursor()
    x.execute(a.data)
    result=x.fetchone()
    t=result[0]+amount
    sql1=("update amount set balnce where ACCOUNT=%s")
    d=(t.accnumber)
    mydb.commit()
    main()
def   withdraw():
    amount=input("enter the ammount you ant to withdraw")
    accnumber=input("enter the account number:")
    a="select balance from amount where bankaccountnumber=%S"
    data = (accnumber)
    x = mydb.cursor()
    x.execute(a.data)
    result = x.fetchone()

    t = result[0] - amount
    if t>5000:
        print("withdraw susefully")
        sql1 = ("update amount set balnce where ACCOUNT=%s")
        d = (t.accnumber)
        mydb.commit()
    else:
        print("you have to mainted minimum balance")
    main()
def  balnceenq():
    accnumber=input("enter the number no: ")
    a='select *from amount where bankaccountid=%s '
    data=(ac,)
    x=mydb.cursor()
    x.execute(a.data)
    result=x.fetchone()
    print("balance for account :",accnumber,"is",result[-1])

















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
