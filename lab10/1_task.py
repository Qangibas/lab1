
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Atikipuki12")

cur = conn.cursor()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute(' INSERT INTO postgres.public.phone_book("personname", "phonenumber") VALUES( %s, %s); ' , (name, number))

def importFromCSV():
    with open("info.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personname, phonenumber = row
            cur.execute(' INSERT INTO postgres.public.phone_book("personname", "phonenumber") VALUES( %s, %s); ', (personname, phonenumber))


def update_contact(personname, phonenumber):
    cur.execute(' UPDATE postgres.public.phone_book SET "phonenumber" = %s WHERE "personname" = %s ', (phonenumber, personname))

def queryData():
    cur.execute(' SELECT * FROM postgres.public.phone_book ')
    data = cur.fetchall()
    path = r"C:\Users\home\Desktop\lab 2\lab1\lab10\file.txt"

    f = open(path, "w")
    for row in data:
        f.write("Name: " + str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")
    f.close()

def deleteData():
    print("Which name do ypu want to delete?\n")
    personname = input()
    cur.execute(f''' DELETE FROM postgres.public.phone_book WHERE "personname"='{personname}' ''')

def deleteAllData():
    cur.execute(' DELETE FROM postgres.public.phone_book ')

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload form csv file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Delete data from table by person name\n\
          6. Delete all data from table\n\
          7. Exit")
    x = int(input("Enter number 1-5\n"))
    if(x == 1):
        inputData()
    elif(x == 2):
        importFromCSV()
    elif(x == 3):
        print("Which number do you want to update? Enter name and new number: ")
        name = input()
        newNumber = input()
        update_contact(name, newNumber)
    elif(x == 4):
        queryData()
    elif(x == 5):
        deleteData()
    elif(x == 6):
        deleteAllData()
    elif(x == 7):
        done = True
    conn.commit()
    
cur.close()
conn.close()
# cur.execute(' DELETE FROM postgres.public.phone_book ')
