import requests
import sqlite3
import Database as datab
import json
def classer(dbfile1):
  conn1=sqlite3.connect("Courses.db")
  cur1=conn1.cursor()
  conn2=sqlite3.connect("") # not yet made database
  cur2=conn2.cursor()
  l=[]
  l2=[]
  cur1.execute("SELECT * FROM "+dbfile1)
  # list1OfTuple = cur1.fetchall() #Course.db
  # cur2.execute("SELECT * FROM "+dbfile2)
  # list2OfTuple = cur2.fetchall() #preferCourse/MandatoryCourse
  dict=datab.insert_allCSEcourses("AllCSEUndergraduate")
  return dict
def getmyclasses(topics,difficulty,mandatoryornot):
  def comparator1(listA,listB):
    listA>listB
  d=classer("CseCourses","nothing")
  # d=d.sort(comparator1()))
  #
  #first round of checking-by virtue of topic
  listofdels=[]
  for m in d.keys():
    if(topics in m):
      pass
    else:
      listofdels.append(m)
  for n in d.keys():
    if(d[n][0]<=difficulty):
      pass
    else:
      listofdels.append(n)
  for x in d.keys():
    if(d[x][2]==mandatoryornot):
      pass
    else:
      listofdels.append(x)
  lagain=[]
  listofdels2=list(set(listofdels))
  for b in listofdels2:
    if(b not in lagain):
      d.pop(b)
      lagain.append(b)
  return d
