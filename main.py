import pymongo
import pprint

print("Welcome")
loop = 'true'
while(loop == 'true'):
    username = str(input("Username Please : "))
    password = str(input("Password Please : "))
    from pymongo import MongoClient
    client = MongoClient()
    db = client.test_database
    post = db.post
    post = {"username" : "abc" , "password" : "123"}

    
    if(username == username and password == password):
        print ('Login Successfully as ' +username)
        loop = 'false'
        loop1 = 'true'
        while(loop1 == 'true'):
            command = input(username + "{} >>")
            if(command == "exit" or command == "Exit"):
                break
            else:
                print ("'" + command + "' is not command!")

    else:
        print ('Invalid Credentials !')
