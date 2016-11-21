import numpy as np
import decimal


# get a formatted trajectory to do some analysis
def get_formatted_trajectory(filename):
	trajectory_formatted = open(filename.replace('.', '-formatted.'), "w")
	with open(filename, "r") as taxi_trajectory:
		# date = eval(''.join(digit for digit in filename if digit.isdigit()))
		for line in taxi_trajectory.readlines():
			if len(line) > 1:
				line = line.replace(","," ").replace("-", "").replace(':', '')
				line_list_str = line.split()
				line_list = np.array(np.fromstring(line, sep=' '), dtype=np.dtype(decimal.Decimal))
				if len(line_list_str[0]) == 7 and (113 < line_list[1] < 115) and (22 < line_list[2] < 23) and (0 <= line_list[3] <= 200) and \
				(0 <= line_list[4] <= 360) and (line_list[7] == 0 or line_list[7] == 1) and (line_list[8] == 0 or line_list[8] == 1):
					trajectory_formatted.write(line)
		trajectory_formatted.close()
		taxi_trajectory.close()
# get_formatted_trajectory("2014-10-1.txt")


# get trajectory slice
def trajectory_slice(trajectory_formatted, slice_len):
	trajectory = open(trajectory_formatted, 'r')
	trajectory_slice = open(trajectory_formatted.replace(".", "-slice."), 'w')
	for i in range(slice_len):
		trajectory_slice.write(trajectory.readline())
	trajectory.close()
	trajectory_slice.close()
# trajectory_slice("2014-10-1.txt", 10000)


# get the trajectory of one car in one day and store its trajectory
def taxi_clusttering(trajectory, ID):
	''' to clustter the taxis with the same ID, return a numpy array that has all elements'''
	trajectory_matrix = []
	example = open(trajectory.replace('.', '-{}.'.format(ID)), 'w')
	with open(trajectory, "r") as trajectory_read:
		for line in open(trajectory, 'r'):
			line = trajectory_read.readline()
			line_list = line.split()
			if line_list[0] == ID:
				trajectory_matrix.append(line_list)
				example.write(line)
		example.close()
		trajectory_read.close()
	return np.array(trajectory_matrix)


# analyze the trajectory data in one day of one taxi
def oneday_onetaxi(trajectory):
	trajectory_read = open(trajectory, 'r')
	trajectory_matrix = []
	for line in open(trajectory, 'r'):
		line = trajectory_read.readline()
		line_list = line.split()
		trajectory_matrix.append(line_list)
	trajectory_matrix = np.array(trajectory_matrix)
	return trajectory_matrix
#trajectory_matrix = oneday_onetaxi("2014-10-1-formatted-1439141.txt")


