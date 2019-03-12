import pymysql
import sys
import re

isSuccess = True
connectionError = False

try:
	arguements = sys.argv

	# Open database connection
	connection = pymysql.connect(
		host=arguements[1], #HOST
		port=int(arguements[2]), #PORT
		user=arguements[3], #USER
		passwd=arguements[4], #PASSWORD
		db=arguements[5]  #DB_NAME
	)

	sql_file = arguements[6]

	with open('execution.log', 'a') as file:
		file.write("\n\n")
		file.write("-------------------------------------------------------------------------------------------\n")
		file.write("Log for SQL Rollback. File Name : '{}'\n".format(sql_file))
		file.write("-------------------------------------------------------------------------------------------\n")
		file.flush()

	cursor = connection.cursor()

	statement = ""

	for line in open(sql_file, 'r'):
		if re.match(r'--', line):  # ignore sql comment lines
			continue
		if not re.search(r'[^-;]+;', line):  # keep appending lines that don't end in ';'
			statement = statement + line
		else:  # when you get a line ending in ';' then exec statement and reset for next statement
			statement = statement + line
		#print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
			try:
				with open('execution.log', 'a') as file:
					file.write('Executing SQL statement:\n')
					file.write(statement)
					file.write('\n')
					file.flush()
				cursor.execute(statement)
			except Exception as e:
				isSuccess = False
				with open('execution.log', 'a') as file:
					file.write(str(e))
					file.write('\n')
					file.flush()
			statement = ""

	if isSuccess:
		connection.commit()
	else:
		connection.rollback()
	connection.close()
except Exception as e:
	connectionError = True
	with open('execution.log', 'a') as file:
		file.write(str(e))
		file.write('\n')
		file.flush()
	pass

if connectionError:
	print('connection failed', end='')
elif isSuccess:
	print("Success", end='')
else:
	print("Failed", end='')
