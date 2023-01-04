import csv
import sqlite3
 
 
try:
 
    with open('badges.csv', 'r') as fin:
        dr = csv.DictReader(fin)
        badges = [(i['badge_name'], i['id'],i['reference_id'], i['reference_id'], i['badge_group_id'],i['enabled'], i['points'],i['highest_points'],i['created_at'],i['updated_at'],i['deleted_at'] ) for i in dr]
        print(badges)
 
    sqliteConnection = sqlite3.connect('crowdstaffing.db')
    cursor = sqliteConnection.cursor()
 
    cursor.execute('create table badges(badge_name VARCHAR, reference_type VARCHAR,reference_id VARCHAR, badge_group_id int ,enabled bool,points float,highest_points float,created_at,updated_at,deleted_at );')
 
    cursor.executemany(
        "insert into badge (badge_name, reference_id,reference_id,badge_group_id,enabled,'points,highest_points,created_at,updated_at,deleted_at ) VALUES (?, ?);", badges)
 
    cursor.execute('select * from student;')
 
    result = cursor.fetchall()
    print(result)
 
    sqliteConnection.commit()
    cursor.close()
 
except sqlite3.Error as error:
    print('Error occurred - ', error)
 
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
        
        
        
        
        
        
        
        
        
