#author: Dominic Manthoko (MNTDOM001)
#date: 2018-03-25

import math


class Optimization:

	def maximize_achievable_rate(self):
		"""
		Class function that determines the maximum aggregate achievable rate for all 
		values of C = 1,2,3,4 and P = 0.1,0.2,0.3,...,1 
		"""
		R = 1000  
		base_radius=5.0
		base_stations = []
		base_stations.append([0,0])
		base_stations.append([5,0])
		base_stations.append([0,5])
		base_stations.append([5,5])

		fileName = "optimization_results/result.txt"
		file = open(fileName, "w")
		test_param = "C,P,max_ra,l1,l2,l3,l4\n"
		file.write(test_param)

		for C in range(1,5):
				#for each value of C
				prob = 1
				while(prob <= 10):
					#for probality 0.1,0.2,...,1
					#divide prob by 10 when using it
					pb=prob/10

					#get the postion of users from all base station
					all_user_positins = []
					for base in base_stations:
						Xc = base[0]
						Yc = base[1]
						all_user_positins.append(self.getUserPos(Xc,Yc,C,pb))

					new_user_positions = [[],[],[],[]]
					number_users = [0,0,0,0]

					max_ra = 0
					for u in all_user_positins:
						for pos in u:

							ra = 0
							user_x_p = pos[0]
							user_y_p = pos[1]
							currentb = 0
							b=0

							for base in base_stations:
								Xc = base[0]
								Yc = base[1]
								D = math.sqrt((Xc-user_x_p)**2+(Yc-user_y_p)**2)
								new_ra = (1.0-(D/base_radius))*R
								#determine if the new_ra value is greater than the previous value
								if (new_ra > ra):
									ra = new_ra
									currentb = b
									b+=1
								else:
									b+=1


							max_ra += ra
							number_users[currentb]+=1
							new_user_positions[currentb].append(pos)

					#write C, P, maximum ra and load of each base station to file
					data = repr(C) + "," + repr(pb) + "," + repr(max_ra) + "," \
							+ repr(number_users[0]) + "," + repr(number_users[1]) \
							+ "," +repr(number_users[2]) + "," +repr(number_users[3]) + "\n"

					file.write(data)

					prob += 1

		file.close()

		return


	def getUserPos(self,X,Y,C,P):
		"""
		Class function that returns the user positions of a base station as an array of values

		Keyword arguments:
		X -- x value of the location of the base station
		Y -- y value of the location of the base station
		C -- the radius of the C circle
		P -- probability that user is within C circle

		return users --  2-d array of user positions
		"""
		fileName = "positions/B" + repr(X) + repr(Y) + "-C" + repr(C) +"-P" +repr(P).replace(".","-") + ".txt"
		file = open(fileName, "r")
			
		data = []

		#get user postion information from appropriate file
		for line in file:
			data.append(line)
		file.close()

		users = []

		#append positions to an array as array values [x,y]
		for i in range(1,21):
			x,y = data[i].rstrip().split(",")
			x = float(x)
			y = float(y)
			users.append([x,y])

		return users

	def optimum_location(self):
		base_stations = []
		base_stations.append([0,0])
		base_stations.append([5,0])
		base_stations.append([0,5])
		base_stations.append([5,5])
		base_radius=5
		R=1000

		all_user_positins = []
		for base in base_stations:
			Xc = base[0]
			Yc = base[1]
			all_user_positins.append(self.getUserPos(Xc,Yc,2,0.9))

		max_ra = 0
		currentx = 0
		currenty=0
		for y in range(-5,11):
			for x in range(-5,11):

				ra = 0
				for u in all_user_positins:
					for pos in u:

						user_x_p = pos[0]
						user_y_p = pos[1]
						
						D = math.sqrt((x-user_x_p)**2+(y-user_y_p)**2)
						new_ra = (1.0-(D/base_radius))*R

						ra += new_ra

				if(ra > max_ra):
					max_ra = ra
					currenty=y
					currentx=x

		print("The optimum base station location is for C=2 and P=0.9: (" + repr(currentx) +"," + repr(currenty) + ")")

		return