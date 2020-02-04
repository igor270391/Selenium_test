import mysql.connector as mysql

db_connector = mysql.connect(
    host='localhost',
    user='root',
    port=3306,
    database='moodle_test',
    passwd='')
print(db_connector)
    # db_cursor = db_connector.cursor()
# db_cursor.execute("DROP TABLE miniuser")
# db_cursor.execute("CREATE TABLE mikimaus (id INT, username VARCHAR (255), fullname VARCHAR (255))")
# db_cursor.execute("INSERT INTO mikimaus (id, username, fullname)"
#                   "VALUE ('1', 'test.user', 'Test User')")
# db_cursor.execute("SELECT * FROM  mikimaus")
# for i in db_cursor:
#     print(i)
