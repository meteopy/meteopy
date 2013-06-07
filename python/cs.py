#!/usr/bin/python
# -*- coding: iso-8859-3 -*-

import sys, time, serial, os, tweepy, datetime
import urllib, httplib, string
import smtplib
import MySQLdb as db

ser = serial.Serial('/dev/ttyUSB0', 9600)

#twitter
CONSUMER_KEY = '7b2oDTe9YRj8imAIR1ctFQ'
CONSUMER_SECRET = 'cv1rQ76hdm06jzsf3rXP8HrUeEjt71H69hMrifTo'

ACCESS_KEY = '1064818908-9fh01byiwrQNeE3YcVezC1QrsKvdvkey7akGNoT'
ACCESS_SECRET = 'FdV1rUa9rJVx9ft5DkApAgRtK8Aldl1gZ4p6MLWM3A'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

enviado = 0
gmail_user="meteopy@gmail.com"
gmail_pwd="smx.smx.smx"
msg="Alarma, la temperatura de MeteoPY, ha sobrepassat el limit indicat!"
emails="jordig1994@gmail.com, coverantwarrior@gmail.com"




def enviado5 ():
	enviado = 5
def enviado0 ():
	enviado = 0

ser.flushInput()
ser.flushOutput()

bucle=1

while bucle==1: 
	now = datetime.datetime.now()
	hora= datetime.datetime(2003, 8, 4, 21, 41, 43)
	if ser.inWaiting() > 1 :
		print " "
		inici = ser.read()
		if inici == "*" :

			line = ser.readline()
			#print line
			list=0
			list = line.split()
			print list
			print len(list)
			numero = len(list)
						
			print numero
			if numero == 4:
				print "ok"
			try:
				temp=list[+0]
				pa=list[+1]
				llum=list[+2]
				print "temp= " + temp
				print "pressio atmosferica= " + pa
				print "llum= " + llum

				#T = open("temperatura.csv", "a")
		 		#T.write("Hum: "+hum+" Temp_1: "+temp_1+" Temp_2: "+temp_2+" Pression: "+pa+" Altitud "+alt+"\n")
		 		#T.close()
				enviado = 0
				
				print now.minute
				try:
				    con = db.connect('localhost', 'root', 'smx', 'meteopy');
				 
				    cursor = con.cursor()
				    cursor.execute("UPDATE temperatura SET temp="+str(temp)+" WHERE id=1")
				    cursor.execute("UPDATE llum SET llum="+str(llum)+" WHERE id=1")
				    cursor.execute("UPDATE press SET press="+str(pa)+" WHERE id=1")
				 
				    con.commit()
				 
				    cursor.close()
				    con.close()
				 
				except dbapi.Error, e:
				 
				    print "Error %d: %s" % (e.args[0],e.args[1])
				    sys.exit(1)

				if str(now.minute)[-1] == "5":
					if temp>=35 :
						smtpserver.ehlo()
						smtpserver.starttls()
						smtpserver.ehlo
						smtpserver.login(gmail_user, gmail_pwd)
						header = 'To:' + str(emails) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Alarma \n'
						print header
						msg = header +"\n"+ "Alarma, la temperatura de MeteoPY, ha sobrepassat el limit indicat" +"\n\n"
						print msg
						smtpserver.sendmail(gmail_user, emails, msg)
						print 'done!'
						smtpserver.close()
						f.close()





				if str(now.minute)[-1] == "5":
		 			if enviado5 == 1 :
				 		tweet = "Llum: " + llum + " Temp: " + temp + "ºC" + " Patm: " + pa + "Pa " + str(hora)+"  (+INFO: http://bit.ly/meteopy)"
		 				api.update_status(tweet)
		 				print "tweet enviado" + "   " + str(now)


		 				# enviado = open("enviado.txt", "w")
		 				# enviado.write("zero")
		 				# enviado.close()


		 			# 	form_json='''{"title":"MeteoPY","version":"1.0.0","datastreams" : [ {"id" : "temperatura","current_value" : "$temp"}{"id" : "Pa","current_value" : "$pa"}{"id" : "llum","current_value" : "$llum"}]}'''
						# data1=form_json.replace("$temp", str(temp))
						# data2=data1.replace("$pa", str(pa))
						# data3=data2.replace("$llum", str(llum))
						# J = open("cosm.json", "w")
						# J.write(data3)
						# J.close()
						# os.system('curl --request PUT --data-binary @cosm.json --header "X-ApiKey: 5iYzOGo0ry-1G_tRxeycjxWSplGSAKwwMVZlNWozTS9JST0g" --verbose http://api.cosm.com/v2/feeds/72412')
						enviado5=0


				if str(now.minute)[-1] == "0":
		 			if enviado5 == 0 :
				 		tweet = "Llum: " + llum + " Temp: " + temp + "ºC" + " Patm: " + pa + "Pa " + str(hora)+"  (+INFO: http://bit.ly/meteopy)"
		 				api.update_status(tweet)
		 				print "tweet enviado" + "   " + str(now)
		 				# enviado = open("enviado.txt", "w")
		 				# enviado.write("zero")
		 				# enviado.close()


		 			# 	form_json='''{"title":"MeteoPY","version":"1.0.0","datastreams" : [ {"id" : "temperatura","current_value" : "$temp"}{"id" : "Pa","current_value" : "$pa"}{"id" : "llum","current_value" : "$llum"}]}'''
						# data1=form_json.replace("$temp", str(temp))
						# data2=data1.replace("$pa", str(pa))
						# data3=data2.replace("$llum", str(llum))
						# J = open("cosm.json", "w")
						# J.write(data3)
						# J.close()
						# os.system('curl --request PUT --data-binary @cosm.json --header "X-ApiKey: 5iYzOGo0ry-1G_tRxeycjxWSplGSAKwwMVZlNWozTS9JST0g" --verbose http://api.cosm.com/v2/feeds/72412')
						enviado5=1

						try:
							conn = MySQLdb.connect(db="yourdatabasename",host="localhost",user="login",passwd="password");
							print "Connected<br/>"
						except:
							print "Cannot connect to server.</br>"
						sys.exit(1)

						try:
							cursor = conn.cursor()
							cursor.execute("UPDATE temperatura SET temp="+ str(temp)+" WHERE id=1");
							print "%d row(s) were updated<br/>" % cursor.rowcount
							cursor.close()
						except MySQLdb.Error, e:
							print "query failed<br/>"
							print e

						conn.close()



				if str(now.minute)[+1] == "3":
		 			if enviado30 == 1 :
		 				smtpserver.ehlo()
						smtpserver.starttls()
						smtpserver.ehlo
						smtpserver.login(gmail_user, gmail_pwd)
						header = 'To:' + str(emails) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Datos Meteorologicos \n'
						print header
						f = open("temperatura.csv", "r")
						msg = header +"\n"+ f.read()+"\n\n"
						print msg
						smtpserver.sendmail(gmail_user, emails, msg)
						print 'done!'
						smtpserver.close()
						f.close()

						enviado30=0



				if str(now.minute)[+1] == "0":
		 			if enviado30 == 0 :
		 				smtpserver.ehlo()
						smtpserver.starttls()
						smtpserver.ehlo
						smtpserver.login(gmail_user, gmail_pwd)
						header = 'To:' + str(emails) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Datos Meteorologicos \n'
						print header
						f = open("temperatura.csv", "r")
						msg = header +"\n"+ f.read()+"\n\n"
						print msg
						smtpserver.sendmail(gmail_user, emails, msg)
						print 'done!'
						smtpserver.close()
						f.close()

						enviado=1


			except:
	 			print "error"

T.close()
