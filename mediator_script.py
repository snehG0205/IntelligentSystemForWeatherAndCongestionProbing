import datetime
import math
from flask import Flask, render_template, request
from traffic_predictor import trafficTime
from temperature_predictor import tempPred
from rainfall_predictor import rainPred

app = Flask(__name__)


@app.route('/traffic')
def main_traffic():
	day_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
	travel_times = []
	travel_times = trafficTime()
	
	today_index = datetime.datetime.today().weekday()
	k = today_index

	new_day_of_week = []
	new_travel_times = []
	traffic_condition = []

	# SORTING DATA SO THAT IT STARTS FROM "TODAY"
	for i in range(len(day_of_week)):
		index=k%7
		new_day_of_week.append(day_of_week[index])
		new_travel_times.append(travel_times[index])
		k=k+1
		if(k==7):
			k=0
		if(k==today_index):
			break
		

	# ROUNDING OFF TO NEAREST INT -> CEIL FOR APPROXIMATION
	for i in range(len(new_travel_times)):
		temp = float(new_travel_times[i])
		new_travel_times[i] = math.ceil(temp)


	# TO APPEND AN APPROPRIATE MESSAGE
	for i in range(len(new_travel_times)):
		if new_travel_times[i] < 15:
			traffic_condition.append("low. Have another cup of coffee. You've got a little time.")
		elif float(new_travel_times[i]) < 20:
			traffic_condition.append("moderate. You better be ready to leave. You don't want to be late.")
		else:
			traffic_condition.append("high. If you're still here, then you're probably already late.")

	# FOR DEBUGGING PURPOSES ONLY -> VISIBLE IN TERMINAL
	for i in range(len(day_of_week)):
		print("For %s, the travel time is %s minutes.\nThe traffic is %s\n"%(new_day_of_week[i],new_travel_times[i],traffic_condition[i]))

	return render_template("traffic_portal.html", time_var_1 = new_travel_times[0], traff_var_1 = traffic_condition[0], time_var_2 = new_travel_times[1], traff_var_2 =traffic_condition[1], time_var_3 = new_travel_times[2], traff_var_3 = traffic_condition[2], time_var_4 = new_travel_times[3], traff_var_4 =traffic_condition[3], time_var_5 = new_travel_times[4], traff_var_5 = traffic_condition[4], time_var_6 = new_travel_times[5], traff_var_6 =traffic_condition[5], time_var_7 = new_travel_times[6], traff_var_7 =traffic_condition[6])





@app.route('/weather')
def main_weather():
	x = []
	x = tempPred()
	temperature = []
	for i in range(len(x)):
		temperature.append(0.9*x[i])
		print(temperature[i])

	y = []
	y = rainPred()
	rainfall = []
	vidhi = 0
	for i in range(len(y)):
		if y[i]<0.10:
			vidhi = y[i]*100
		else:
			vidhi = y[i]*100

		rainfall.append(vidhi)

		# print(rainfall[i])


	day_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
	today_index = datetime.datetime.today().weekday()
	k = today_index

	new_day_of_week = []
	new_temperature = []
	new_rainfall = []

	# SORTING DATA SO THAT IT STARTS FROM "TODAY"
	for i in range(len(day_of_week)):
		index=k%7
		new_day_of_week.append(day_of_week[index])
		new_temperature.append(temperature[index])
		new_rainfall.append(rainfall[index])
		k=k+1
		if(k==7):
			k=0
		if(k==today_index):
			break

	# ROUNDING OFF
	for i in range(len(day_of_week)):
		temp = float(new_temperature[i])
		new_temperature[i] = math.floor(temp)

		temp = float(new_rainfall[i])
		# if new_rainfall[i]>80:
		# 	new_rainfall[i] = new_rainfall[i]/2

		new_rainfall[i] = math.floor(temp)

	# FOR APPENDING AN APPROPRIATE MESSAGE
	day_type = []
	for i in range(len(day_of_week)):
		if new_rainfall[i]<20:
			day_type.append("be sunny")
		elif new_rainfall[i]<50:
			day_type.append("be overcast")
		elif new_rainfall[i]<90:
			day_type.append("have thunderstorms")
		else:
			day_type.append("have heavy rains")


	# FOR DEBUGGING PURPOSES ONLY -> VISIBLE IN TERMINAL
	print("TEMPERATURE")
	for i in range(len(day_of_week)):
		print("%s\t%s"%(day_of_week[i],new_temperature[i]))

	print("RAINFALL")
	for i in range(len(day_of_week)):
		print("%s\t%s"%(day_of_week[i],new_rainfall[i]))

	print("Type of Rains")
	for i in range(len(day_of_week)):
		print("%s\t%s"%(day_of_week[i],day_type[i]))

		
	return render_template("weather_portal.html",temp_var_1=new_temperature[0],rain_var_1=new_rainfall[0],day_var_1=day_type[0],temp_var_2=new_temperature[1],rain_var_2=new_rainfall[1],day_var_2=day_type[1],temp_var_3=new_temperature[2],rain_var_3=new_rainfall[2],day_var_3=day_type[2],temp_var_4=new_temperature[3],rain_var_4=new_rainfall[3],day_var_4=day_type[3],temp_var_5=new_temperature[4],rain_var_5=new_rainfall[4],day_var_5=day_type[4],temp_var_6=new_temperature[5],rain_var_6=new_rainfall[5],day_var_6=day_type[5],temp_var_7=new_temperature[6],rain_var_7=new_rainfall[6],day_var_7=day_type[6])



if __name__ == '__main__':
   app.run(debug = True)