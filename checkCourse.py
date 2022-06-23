import requests
import sqlite3
import Database as datab
import recommendCourse as rc
import json
def displaycourse():
  d=rc.classer("CseCourses","nothing")
  