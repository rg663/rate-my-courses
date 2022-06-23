import sqlite3
import bottle
import UBITConfirm as ubit
def submit_rating(rating):
  ubit=rating["ubit"]
  # if(True):
  #   numericrating = rating['numericvalue']
  #   statement_rating = rating['statement']
  #   numericrating = rating.get('numericvalue','')
  #   # Create the SQL statement we need
  #   sql_quote = '"'
  #   conn = sqlite3.connect("Courses.db")
  #   cur = conn.cursor()
    # # id_sql = sql_quote + song_id + sql_quote
    # rating_sql = str(rating_num)
    # review_sql = sql_quote + review + sql_quote
    # cur.execute("UPDATE "+ "Courses.db"+"SET overallrating = "+numericrating+" WHERE "+ dropval)

  #Print added for debugging:
  # print("->"+sql_string)
  # sql_string = 'INSERT INTO ' + ratings_table + ' VALUES '+\
  #              '('+id_sql+','+rating_sql+','+review_sql+')'
  # cur.execute(sql_string)
  # conn.commit()
