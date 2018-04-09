#author: Dominic Manthoko (MNTDOM001)
#date: 2018-03-25
import numpy as np
import random
import math
import matplotlib.pyplot as plt

class UserGeneration:
	def generate_user_positions(self):
		"""
			Creates 20 randomly positioned users for base stations located at (0,0), (5,0), (0,5) and (5,5).
			The user positions for each station, and C=1,2,3,4 and P=0.1,0.2,...1, are saved in files
		"""

		base_stations = []
		base_stations.append([0,0])
		base_stations.append([5,0])
		base_stations.append([0,5])
		base_stations.append([5,5])
		r=5

		for base in base_stations:
			#for each base station
			Xc = base[0]
			Yc = base[1]

			for C in range(1,5):
				#for each value of C
				prob = 1
				while(prob <= 10):
					#for probality 0.1,0.2,...,1
					#divide prob by 10 when using it
					pb=prob/10

					fileName =  "positions/B" + repr(Xc) + repr(Yc) + "-C" + repr(C) +"-P" +repr(pb).replace(".","-") + ".txt"

					file = open(fileName,"w")

					test_param = repr(Xc) + "," + repr(Yc) + "," +repr(C) +"," +repr(pb) + "\n"
					file.write(test_param)

					for i in range(20):
						possible_position 	= np.random.choice([1,2],p=[pb,1-pb])
						user_x_pos 			= 0
						user_y_pos 			= 0

						if (possible_position == 1):
							#user is within the C cicle
							user_x_pos = random.uniform(Xc-C,Xc+C)
							user_x_pos = round(user_x_pos,4)
							user_y_pos = self.findY_userc(user_x_pos,r,Xc,Yc,C)
						else:
							user_x_pos = random.uniform(Xc-r,Xc+r)
							user_x_pos = round(user_x_pos,4)
							user_y_pos = self.findY_userf(user_x_pos,r,Xc,Yc,C)

						if(i!=19):
							file.write(repr(user_x_pos) + "," + repr(user_y_pos) + "\n")
						else:
							file.write(repr(user_x_pos) + "," + repr(user_y_pos))

					file.close()

					prob += 1

		return

	def findY_userf(self,x,radius,a,b,C):
		"""Find the value of y given x such that (x,y) is a point with a circle
		of the given radius for Uf users

		Keyword arguments:
		x -- value of x within circle
		radius -- radius of the circle
		a -- x co-ordinate of the center of the circle
		b -- y co-ordinate of the center of the circle
		C -- the radius of the C circle

		"""

		lowerlimit = b-math.sqrt(radius**2-(x-a)**2)
		upperlimit = b+math.sqrt(radius**2-(x-a)**2)
		y=random.uniform(lowerlimit,upperlimit)

		
		while(math.sqrt((a-x)**2+(b-y)**2) < C):
			y=random.uniform(lowerlimit,upperlimit)

		return round(y,4)

	def findY_userc(self,x,radius,a,b,C):
		"""Find the value of y given x such that (x,y) is a point with a circle
		of the given radius for Uc users

		Keyword arguments:
		x -- value of x within circle
		radius -- radius of the circle
		a -- x co-ordinate of the center of the circle
		b -- y co-ordinate of the center of the circle
		C -- the radius of the C circle

		"""
		lowerlimit = b-math.sqrt(radius**2-(x-a)**2)
		upperlimit = b+math.sqrt(radius**2-(x-a)**2)
		y=random.uniform(lowerlimit,upperlimit)

		
		while(math.sqrt((a-x)**2+(b-y)**2) > C):
			y=random.uniform(lowerlimit,upperlimit)

		return round(y,4)

	def getUserPos(self,X,Y,C,P):
		fileName = "positions/B" + repr(X) + repr(Y) + "-C" + repr(C) +"-P" +repr(P).replace(".","-") + ".txt"
		file = open(fileName, "r")
			
		data = []

		for line in file:
			data.append(line)
		file.close()

		users = []

		for i in range(1,21):
			# key = "U" + repr(i)
			x,y = data[i].rstrip().split(",")
			x = float(x)
			y = float(y)
			users.append([x,y])

		return users


	def myplot(self):
		"""Generate plots of the base stations and that connection to said base station
		"""

		base_stations = []
		base_stations.append([0,0])
		base_stations.append([5,0])
		base_stations.append([0,5])
		base_stations.append([5,5])

		for base in base_stations:
			#for each base station
			Xc = base[0]
			Yc = base[1]

			for C in range(1,5):
				#for each value of C
				prob = 1
				while(prob <= 10):
					#for probality 0.1,0.2,...,1
					#divide prob by 10 when using it
					pb=prob/10

					# position = self.getUserPos(0,0,3,0.7)
					position = self.getUserPos(Xc,Yc,C,pb)
					x_pos = []
					y_pos = []
					for pos in position:
						x_pos.append(pos[0])
						y_pos.append(pos[1])

					fig = plt.gcf()
					ax = fig.gca()

					ax.set_xlim((Xc-5, Xc+5))
					ax.set_ylim((Yc-5, Yc+5))

					#plot user positions
					ax.plot(x_pos,y_pos,'o',color='black')
					#plot a point to represent base station i.e. center of circle 
					ax.plot((Xc), (Yc), 'o', color='y') 

					circle1 = plt.Circle((Xc,Yc),5,color='b',fill=False)
					circle2 = plt.Circle((Xc,Yc),C,color='r',fill=False)
					ax.add_artist(circle1)
					ax.add_artist(circle2)
					title = 'Base station (' + repr(Xc) + ','+  repr(0) + ') when C=' + repr(C) + ' and P=' + repr(pb)
					plt.title(title)
					# plt.show()

					#save to file
					fileName =  'positions_plots/B' + repr(Xc) + repr(Yc) + '-C' + repr(C) +'-P' +repr(pb).replace(".","-") + '.png'
					fig.savefig(fileName)

					fig.clf()

					prob += 1
		return