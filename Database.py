import sqlite3
import csv

database_filename = "Course.db"
coursesRating_table = "CseCourses"
course_table = "preferCourses/MandatoryCourses"
sql_quote = '"'
# for dict in list:
  
  

##############################################################################################################################################################
conn = sqlite3.connect(database_filename)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS " + "CseCourses" + " (courses, overall, difficulty rating, workLoad rating, MandatoryOrNot)")

##############################################################################################################################################################
def insert_allProfessors(csvFile):

  dict = {}
  list2 = []
  with open (csvFile,"r") as file:
    csvReader = csv.reader(file)
    next(csvReader)

    for line in csvReader: 
      
      AllCoursesCode = line[0].strip()
      if len(line) >1 :
        for index in range(1,len(line)):
          
          list2.append(line[index].strip())
    
        dict[AllCoursesCode] = list2

      else: 

        dict[AllCoursesCode] = list2
      
      list2 = []
  return dict
 ############################################################################################################################################################## 

def insert_allCSEcourses(csvFile,dict):

  with open(csvFile,"r") as file:
    csvReader = csv.reader(file)
    next(csvReader)
    
    for line in csvReader:

      
      AllCoursesCode = line[0]
      overall_ratings = "0"
      difficulty_ratings = "0"
      workload_ratings = "0"
      mandatoryOrNot = line[5].strip()
      # Create the SQL statement we need
      AllCSE_sql = sql_quote + AllCoursesCode + sql_quote
      overallRatings_sql = sql_quote + overall_ratings + sql_quote
      difficultyRatings_sql = sql_quote + difficulty_ratings + sql_quote
      workloadRatings_sql = sql_quote + workload_ratings + sql_quote
      mandatoryOrNot_sql = sql_quote + mandatoryOrNot+ sql_quote
                
      sql_string = 'INSERT INTO ' + coursesRating_table + ' VALUES '+'('+AllCSE_sql+','+overallRatings_sql+','+difficultyRatings_sql+','+workloadRatings_sql+','+mandatoryOrNot_sql+')'
      # Print added for debugging:
      # print("->"+sql_string)
      cur.execute(sql_string)
      conn.commit()
##############################################################################################################################################################
def CodeToName():

  dict = {}
  with open("AllCSEUndergraduate.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for line in csv_reader:
      
      dict[line[0]] = line[1]
  
    return dict

############################################################################################################################################################## 
cur.execute("SELECT * FROM " + coursesRating_table)
listOfTuple = cur.fetchmany(51)

def insertDataToDictionary(listTuple):

  dict= {}

  for tuple in listTuple:

    code = tuple[0]
    overallRating = int(tuple[1])
    difficultyRating = int(tuple[2])
    workLoadRating = int(tuple[3])
    MandatoryOrNot = tuple[4]

    list = [overallRating,difficultyRating,workLoadRating,MandatoryOrNot,[]]

    dict[code] = list
  
  return dict
  
  

# UPDATE table_name.
# SET variable = 'changed field', variable = 'another changed field'
# WHERE firstline_name = 1;