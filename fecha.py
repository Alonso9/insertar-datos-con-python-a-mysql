import mysql.connector #importamos el modulo para conectar con mysql 
from datetime import datetime

def save_server01(x):

	vhost = 'localhost'
	vuser = 'root'
	vpasswd = ''
	vdb = 'PI4'
	fecha = datetime.now()

	try:
		conn = mysql.connector.connect(host=vhost,user=vuser,passwd=vpasswd,database=vdb)
		cursor = conn.cursor()
		query = "INSERT INTO `sensor01`(`nombre`, `dato`, `fecha`) VALUES (%s,%s,%s)"
		val = ('Pedro',x,fecha)
		cursor.execute(query,val)
		conn.commit()
	except:
		print("Ha ocurrido un error, no pudo crear una conexion con el servidor!")
	finally:
		print(f"Se han insertado {cursor.rowcount} dato en la BD")
		conn.close()


def save_server02(x1,x2):

	vhost = 'localhost'
	vuser = 'root'
	vpasswd = ''
	vdb = 'PI4'
	fecha = datetime.now()

	try:
		conn = mysql.connector.connect(host=vhost,user=vuser,passwd=vpasswd,database=vdb)
		cursor = conn.cursor()
		query = "INSERT INTO `sensor02`(`nombre`, `dato1`, `dato2`, `fecha`) VALUES (%s,%s,%s,%s)"
		val = ('Pedro',x1,x2,fecha)
		cursor.execute(query,val)
		conn.commit()
	except:
		print("Ha ocurrido un error, no pudo crear una conexion con el servidor!")
	finally:
		print(f"Se han insertado {cursor.rowcount} dato en la BD")
		conn.close()


def main():
	temp = 33.12
	rc = 180
	os = 90
	save_server01(temp)
	save_server02(rc,os)


main()