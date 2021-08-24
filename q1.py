import requests
import os 
import json

if os.path.isfile("mearki_data.json"):
    with open ("mearki_data.json","r")as k:
        data=json.load(k)

else:
    saral=('http://saral.navgurukul.org/api/courses')
    data_1=requests.get(saral)
    data=data_1.json()
    with open("mearki_data.json","w")as k:
        json.dump(data,k,indent=4)
serial_no=0
for i in data["availableCourses"]:
    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1
    print("")

# taking user input for course number

user_input=int(input("What Course Do You Want Plase Enter of Number of cousre:-"))
parent_name=data["availableCourses"][user_input-1]["id"]
parent_id=data["availableCourses"][user_input-1]["name"]
print(parent_id)

if os.path.isfile("parent/"+parent_name+str(parent_id)+data["availableCourses"][user_input-1]["name"]+".json"):
    with open("parent/"+parent_name+str(parent_id)+data["availableCourses"][user_input-1]["name"]+".json","r")as child_data:
        data_1=json.load(child_data)
else:
    parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercises"
    parent_url = requests.get(parent_api)
    data_1 = parent_url.json()
    # with open ("parent/"+parent_name + str(parent_id)+data["availableCourses"][user_input-1]["name"] +".json","w") as child_data:
    #     json.dump(data_1,child_data,indent=4)
    with open ("parentes.json","w") as child_data:
        json.dump(data_1,child_data,indent=4)

serial_no=1
serial_no1=1
topic_list=[]
#for printing the details of the specific courses:

for index1 in data_1["data"]:
    if len(index1["childExercises"])==0:
        print("   ",serial_no,".",index1["name"])
        topic_list.append(index1["name"])
        print("           ",serial_no1,".",index1["slug"])
        serial_no+=1
    else:
        serial_no2=1
        print("   ",serial_no,".",index1["name"])
        topic_list.append(index1["name"])
        for questions in index1["childExercises"]:
            print("         ",serial_no2,".",questions["name"])
            serial_no2+=1
        serial_no+=1
slug=int(input("Enter the topic number:"))
question_list=[]
slug_list=[]
print("     ",slug,".",topic_list[slug-1])

s_num=1
for index1 in data_1["data"][slug-1]["childExercises"]:
    print("           ",s_num,".",index1["name"])
    question_list.append(index1["name"])
    s_num+=1
que=int(input("Enter question number:")) 
w=requests.get("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercise/getBySlug?slug="+str(data_1["data"][slug-1]["childExercises"][que-1]["slug"]))
DATA=w.json()
with open("question.json","w") as a:
    json.dump(DATA,a,indent=4)
    print(DATA["content"])
    # break








