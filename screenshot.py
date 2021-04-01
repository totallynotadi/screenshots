from datetime import datetime, timedelta
from time import sleep
import os
import pyautogui
import getpass

def time(time_duration):

	the_dict = {'hour' : False, 'minute' : False, 'second' : False}

	def which_true():

		true_list = []
	
		for i in the_dict:
			if the_dict [i] == True:
				true_list.append(i)

		return true_list

	if 'h' in time_duration or 'H' in time_duration:
		the_dict ['hour'] = True
	if 'm' in time_duration or 'M' in time_duration:
		the_dict ['minute'] = True
	if 'c' in time_duration or 'C' in time_duration:
		the_dict ['second'] = True

	time_duration = time_duration.split(' ')

	true_list = which_true()

	index = 0
	for time in true_list:
		to_be_placed = time_duration [index]
		the_dict [time] = to_be_placed
		index = index + 2

	for i in the_dict:
		if the_dict [i] == False:
			the_dict [i] = 0
	
	return the_dict

nums_list = [str(i) for i in range(10)]

print("enter the time duration you want to run this program for")
print("say if you want to run for 2 hours and 15 minutes, enter '2 hours and 15 minutes'")
print("if you want to run for just 25 minutes, enter '25 minutes'")
print("similarly for 1 hour, enter '1 hour'")

print("enter the path to the folder to store the screenshots in")
print("or just press enter without entering a path so that a folder with the specified folder name will be created on the dektop automatically")
print("and all the screenshots will be stored in that folder")

user = getpass.getuser()

if os.path.exists('C:\\Users\\' + user + '\\screenshots') == False:
	os.mkdir('C:\\Users\\' + user + '\\screenshots')

folder_name = str(input("enter the name for the folder to save the screenshots taken in this session"))
session_folder_path = 'C:\\Users\\' + user + '\\screenshots' + '\\' + folder_name

os.mkdir(session_folder_path)
time_input = time(str(input("enter the time duration for which to capture the screenshots")))
print('time input', time_input)
waiting_time = time(str(input("enter the time gap between two consecutive screenshots")))
print('waiting time', waiting_time)

'''
os.chdir('')
path = os.getcwd() + '\\screenhots'
os.mkdir(path)

folder_name = str(input("enter the name of the folder you want to put the screenshots taken in this session \n"))

screenshot_folder_path = path + '\\' + folder_name
os.mkdir(screenshot_folder_path)

waiting_time = time(str(input("enter the time gap between two screenshots in the above specified format \n")))

time_input = time(str(input("enter the time duration in the above specified format")))
'''

index = 2
sec_sum = 0
for i in waiting_time:
	sec_time = int(int(waiting_time [i]) * (60 ** index))
	sec_sum += sec_time
	index -= 1
waiting_time = sec_sum
print(f"waiting time in seconds {waiting_time}")

print(waiting_time)

current_time = datetime.now() 
delta_time = timedelta(hours = int(time_input ['hour']), minutes = int(time_input ['minute']), seconds = int(time_input['second']))
target_time = current_time + delta_time

x = 1
while current_time < target_time:
	pyautogui.screenshot(session_folder_path + '\\image' + str(x) + '.png') 
	sleep(waiting_time)
	current_time = datetime.now()
	x += 1
