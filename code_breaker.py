#!/usr/bin/python3
#written by antymijaljevic@gmail.com

import os
from random import shuffle
from time import sleep
from hacked import hacked, welcome, bye

#generate random 3 digit random number
def generateNumber():
	threeDigit =''
	listOfNum = list(range(9))
	random.shuffle(listOfNum)
	for num in listOfNum:
		threeDigit += str(num)
	return threeDigit[:3] 

#check input  for possible errors;cheat mode;exit
def errorFilter(userInput):
	while True:
		os.system('clear')
		print(welcome)
		
		if userInput.lower() =='exit':
			os.system('clear')
			print(bye)
			exit(0)
		
		elif userInput.lower() == "cheat":
			userInput = input(f"The code is: {compRandomNo}\n\nEasy to guess now: ")
		
		elif userInput.isdigit() and len(userInput) == 3:
			results(userInput)
		
		else:
			userInput = input("Wrong input! Has to be 3-digit number!\n\nTry to guess: ")

#search for one match
def findItOne(compString, userString):
	for i in range(3):
		if compString[i] == userString[i]:
			return True
	return False

#search for double match
def findItTwo(compString, userString):
	for i in range(-1,2):
		if compString[i]+compString[i+1] == userString[i]+userString[i+1]:
			return True
	return False

#possible outcomes
def results(userInput):
		global compRandomNo

		if compRandomNo == userInput:
			os.system('clear')
			print(f"\tThe code is: {compRandomNo}"+"\n"+hacked)
			compRandomNo = generateNumber()
			errorFilter(input("\nType 'exit' or guess again: "))

		elif findItTwo(compRandomNo, userInput):
			errorFilter(input("You have double match digit, nearly got it :)\n\nTry to guess again: "))
		
		elif findItOne(compRandomNo, userInput):
			errorFilter(input("You have one match digit, two digits more to hack ;)\n\nTry to guess again: "))
		
		else:
			errorFilter(input("You're not even close...\n\nTry to guess again: "))

os.system('clear')
compRandomNo = generateNumber()
print(welcome)
errorFilter(input("Try to guess: "))
