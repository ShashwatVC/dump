import json

credentials ="""[
    google{
        "app":"google",
        "usnm":"payload",
        "pwd":"1234"
    }
    

]"""

#with open('dat.json') as f:
data = json.loads(credentials)
app = input("Application Name :")

if app in data:
    print("%s is found in JSON data" %app)
    print("The value of", app,"is", data[app])
else:
    # Print the message if the value does not exist
    print("%s is not found in JSON data" %app)

#for cred in data['credentials']:
#    print(cred[app],cred['usnm'])