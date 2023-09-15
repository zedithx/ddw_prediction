from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	result = []
	for i in range(0, number):
		result.append(i)
	random.seed(seed)
	random.shuffle(result)
	return result

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array = gen_random_int(number, seed)

	# convert the items into one single string
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = ','.join(array) + '.'

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"
	console.log(array_str)
	document.getElementById("generate").innerHTML = array_str

def bubble_sort(array):
    n = len(array)
    for outer_index in range(1, n):
        for inner_index in range(1, n):
            first_number = array[inner_index - 1]
            second_number = array[inner_index]
            if int(first_number) > int(second_number):
                array[inner_index] = first_number
                array[inner_index - 1] = second_number

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_str = document.getElementById("generate").innerHTML
	array_str = array_str[:-1]
	array = array_str.split(',')
	bubble_sort(array)
	array_str = ','.join(array) + '.'
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	value_list = value.split(',')
	bubble_sort(value_list)
	array_str = ','.join(value_list) + '.'

	document.getElementById("sorted").innerHTML = array_str


