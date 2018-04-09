#author: Dominic Manthoko (MNTDOM001)
#date: 2018-03-25
from user_generation import UserGeneration
from optimization import Optimization

if __name__ == '__main__':
	usergen = UserGeneration()
	print("Generating users...")
	usergen.generate_user_positions()
	usergen.myplot()
	print("User generation completed.")

	#optimization
	optimize = Optimization()
	print("Performing Optimization Calculations...")
	optimize.maximize_achievable_rate()
	print("Optimization completed.")
	print("Finding the optimum base station location")
	optimize.optimum_location()
