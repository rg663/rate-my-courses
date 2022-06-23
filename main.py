import bottle
import requests
import UBITConfirm as u
import Database as datab
import recommendCourse as rc
import rateMyCourse as rrmc
import sqlite3
import csv
import json
#Check UBitName

datab.insert_allCSEcourses("AllCSEUndergraduate.csv",{})
conn = sqlite3.connect("Course.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS " + datab.coursesRating_table + " (courses, overall rating, difficulty rating, workLoad rating)")
cur.execute("SELECT * FROM " + datab.coursesRating_table)
listOfTuple = cur.fetchmany(51)
data_dict = datab.insertDataToDictionary(listOfTuple)
# To access empty list just do: list = data_dict[Name of class code][4]
# empty = data_dict["CSE 101"][4]
# print(empty)
# print(data_dict)

###############################################################################
NameToCODE = datab.CodeToName()
# print(NameToCODE)

name = NameToCODE["CSE 220"]
print(name)
dictOFProf  = datab.insert_allProfessors("Professor.csv") # code:Prof
# print(dictOFProf)

def validRating(rating):

  if (int(rating['numericalvalue']) <= 10) and (int(rating['numericalvalue']) >= 1):
    return True
  else:
    return False

  
@bottle.route("/")
def html_open():
  return bottle.static_file("/index.html",root=".")

@bottle.route("/style.css")
def css_open():
  return bottle.static_file("/style.css",root=".")

@bottle.route('/<js_file>.js')
def javascript_file(js_file):
  code_js = bottle.static_file(js_file+".js", root=".")
  return code_js  

@bottle.route('/script.js')
def scriptgetter():
  code_js = bottle.static_file("/script.js", root=".")
  return code_js  
@bottle.route('/faviconn.png')
def favvy():
  return bottle.static_file("/faviconn.png",root=".")
@bottle.route('/bg.png')
def favvyy():
  return bottle.static_file("/bg.png",root=".")


@bottle.post("/putreview")
def importingData():
  json_blob = bottle.request.body.read().decode()
  dict_userRating = json.loads(json_blob)
  print(dict_userRating)
  rating=dict_userRating
  ubit=rating["ubit"]
  dropval=rating["csecode"]
  if(u.finder(ubit)==1):
    if validRating(rating) == True:
      numericrating = rating['numericalvalue']
      statement_rating = rating['statement']
      # for m in data_dict.keys():
      #   if(m==dropval):
      data_dict[dropval][4].append(statement_rating)
      data_dict[dropval][0] = int(numericrating) 
      
      
      return json.dumps(data_dict)

    else:
      return json.dumps({"":"","":"","":"","":"","":"","":""})
    
    # To access empty list just do: data_dict[Name of class code][4]
  else:
    return json.dumps({"":"","":"","":"","":"","":"","":""})



@bottle.route("/gimmetheDATA")
def getmyclass():
  json_blob = bottle.request.body.read().decode()
  dict_userRating = json.loads(json_blob)
  x=topics,difficulty,mandatoryornot
  d=data_dict
  # d=d.sort(comparator1()))
  #
  #first round of checking-by virtue of topic
  listofdels=[]
  for m in d.keys():
    if(topics in m):
      pass
    else:
      listofdels.append(m)
  return json.dumps(d)

#Code:[overallRating,difficultyRating,workLoadRating,MandatoryOrNot]
# To access empty list just do: list = data_dict[Name of class code][4]
    
# d=datab.CodeToName() 
# print(d)
# with open("txtxt.txt","w") as f:
#   for m in d.keys():
#     f.write('<option value="'+str(m)+'">'+str(m)+'</option>'+'\n')

#Code:[overallRating,difficultyRating,workLoadRating,MandatoryOrNot]

bottle.run(host="0.0.0.0",port="0808")

# datab.insert_allCSEcourses("AllCSEUndergraduate.csv")

