import csv
import tensorflow as tf 

def trafficTime():
	training_set = []
	training_set_y = []
	day_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
	travel_time = []
	traffic_condition = []
	

	with open("TRAIN_SET.csv","r") as file:
		reader = csv.reader(file)
		for row in reader:
			training_set.append([row[3], row[4], row[5]])
			training_set_y.append(row[6])

	training_set = training_set[1:]
	training_set_y = training_set_y[1:]
	testing_set = []


	with open("TEST_SET.csv","r") as file:
		reader = csv.reader(file)
		for row in reader:
			testing_set.append([row[3], row[4], row[5]])

	# Excluding the first column from the list (which is nothing but name column)
	testing_set = testing_set[1:]

	training_values = tf.placeholder("float",[None,len(training_set[0])])
	test_values     = tf.placeholder("float",[len(training_set[0])])

	# This is the distance formula to calculate the distance between the test values and the training values
	distance = tf.reduce_sum(tf.abs(tf.add(training_values,tf.negative(test_values))),reduction_indices=1) 	
	# Returns the index with the smallest value across dimensions of a tensor
	prediction = tf.arg_min(distance,0)

	# Initializing  the session
	init = tf.initialize_all_variables()

	with tf.Session() as sess:
		sess.run(init)	
		# Looping through the test set to compare against the training set
		for i in range (len(testing_set)):
			# Tensor flow method to get the prediction nearer to the test parameters from the training set.
			index_in_trainingset = sess.run(prediction,feed_dict={training_values:training_set,test_values:testing_set[i]})	

			# print("Test %d, and the prediction is %s"%(i,training_set_y[index_in_trainingset]))
			travel_time.append(training_set_y[index_in_trainingset])
			# print("For index -> %s, the prediction is %s"%(day_of_week[i],travel_time[i]))


	return travel_time



var = trafficTime()
print(var)





