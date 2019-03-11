import PyMySQL
import sys

isSuccess = True

try:
	arguements = sys.argv

	# Open database connection
	db = PyMySQL.connect(
		arguements[1], #HOST
		arguements[2], #USER
		arguements[3], #PASSWORD
		arguements[4]  #DB_NAME
	)

	sql_file = arguements[5]

	with open('execution.log', 'a') as file:
		file.write("\n\n")
		file.write("-------------------------------------------------------------------------------------------\n")
		file.write("Log for SQL Execution. File Name : '{}'\n".format(sql_file))
		file.write("-------------------------------------------------------------------------------------------\n")
		file.flush()

	cursor = db.cursor()

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
			cursor.execute(statement)
		except (OperationalError, ProgrammingError) as e:
			isSuccess = False
			with open('execution.log', 'a') as file:
				file.write(str(e))
				file.write('\n')
				file.flush()
			break
		statement = ""

	if isSuccess:
		db.commit()
		print("Success", end='')
	else:
		db.rollback()
		print("Failed", end='')
	db.close()

except Exception as e:
	isSuccess = False
	with open('execution.log', 'a') as file:
		file.write(str(e))
		file.write('\n')
		file.flush()
	print("Failed", end='')
