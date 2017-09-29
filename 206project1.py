import os
import csv
import operator
import filecmp
def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		reader = list(reader)
		return reader

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	from operator import itemgetter
	data = sorted(data, key = itemgetter(col))
	val1 = data[0]["First"] 
	val2 = data[0]["Last"]
	return val1 + " " + val2

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	value_counter = {}
	for item1 in data:
		if "Class" in item1:
			value_counter[item1["Class"]] = value_counter.get(item1["Class"], 0) + 1
	listoftuples = list()
	for key, val in value_counter.items():
		listoftuples.append((key, val))
	return sorted(listoftuples, key = lambda x:-x[1])

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	dictofdates = {}
	for item1 in a:
		item1 = item1["DOB"].split("/")
		dictofdates[item1[1]] = dictofdates.get(item1[1], 0) + 1
	dictofdates = sorted(dictofdates.items(), key=lambda x:-x[1])
	return(int(dictofdates[0][0]))

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	from datetime import datetime
	list1 = []
	for date1 in a:
		b_date = datetime.strptime(date1["DOB"], '%m/%d/%Y')
		b_date = int("%d" % ((datetime.today() - b_date).days/365))
		list1.append(b_date)
	return(round(sum(list1) / len(list1)))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	from operator import itemgetter
	for item1 in a:
		del(item1["DOB"])
		del(item1["Class"])
	a = sorted(a, key = itemgetter(col))
	with open('results.csv', 'w', newline = "\n") as outfile:
		writer = csv.DictWriter(outfile, a[0].keys(), lineterminator = '\n')
		writer.writerows(a)
	#Your code here:
	pass



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each afunction returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

