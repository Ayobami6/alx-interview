#!/usr/bin/bash

# shell variables
FIRSTVAR="This is the first var"
NAME="Ayobami"
AGE=24

# passing a command to a variable
MACHINE=`uname -n`

# print out the vars

echo "Name is $NAME age is $AGE"
echo $MACHINE


# commandline args

echo "This takes command line arg 1 $1"
echo "This takes all  $*"


# read input from user
read -p "Enter your firstname and Lastname: " FIRSTNAME LASTNAME
echo "Your full name is $FIRSTNAME $LASTNAME"

# Arithmetic operations

let RESULT=20/5

echo $RESULT

OTHER=$((RESULT * 2))

echo $OTHER


I=0

echo "This is prefix incremented I $((++I))"

echo "This is postfix $((I++)) result after postfix increment $I"

# shell programming construct

read -p "Enter a Value: " VAR

if [[ $VAR -eq 1 ]]; then
	echo "$VAR is equal to 1"
else
	echo "$VAR not equal to 1"
fi

DAY="SUNDAY"

if [ $DAY != "MONDAY" ]; then
	echo "Atleat its Not Monday"
fi

filename=$HOME

if [ -f $filename ]; then
	echo "This is a regular file"
elif [[ -d $filename ]]; then
	echo "This is a directory"
else
	echo "I don't know what it is"
fi

read -p "Enter something: " something

# if len something is zero
if [ -z $something ]; then
	echo "Nothing passed" 
else
	echo "There is something"
fi

# case statement 

var=3

case $var in 
	2)
		echo "The var is 2";;
	3)
		echo "The var is 3";;
	*)
		echo "This is a defaul";;
esac


# arrays data structures

myArray=(1 2 3 5)

echo "${myArray[0]}"


# map data structure

declare -A myDict=(
	["name"]="Ayo"
	["age"]=23
	["height"]=5.6
	)


echo "${myDict["name"]}"

# loops (for)
# 1
for num in "${myArray[@]}";
do
	echo "$num"
done

# 2
counter=1

for (( counter; counter <=10; counter++ ));
do
	echo $counter
done

# while loops

N=0

while [[ $N -lt 10 ]]; do
	echo $N
	let N=$((N+1))
done

# until loop
P=0
until [ $P -eq 10 ]; do
	echo $P
	let P=$((P+1))
done 

# add ! for keys, no ! for values
for key in "${!myDict[@]}"; do
	echo $key
done



# functions

printHello () {
	echo "Hello World"
}

printHello

#  function with params

sum () {
	RESULT=$(($1 + $2))
	echo "$RESULT"
}


sum 2 3
# for NUMBER in 0 1 2 3 4 5 6 7 8 9
# do
# echo The number is $NUMBER
# done