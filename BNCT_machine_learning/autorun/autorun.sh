#!/bin/bash

PHITS_COMMAND="phits.sh"

#Input file folder location
BASE_DIR="data"

#Check the input
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <start_number> <end_number>"
	echo "Example: $0 1 5 (this will run file run_001 until run_005)"
	exit 1
fi

START=$1
END=$2

#Save current directory
CURRENT_DIR=$(pwd)

echo "Start to run PHITS file from $START to $END ...."

for (( i=$START; i<=$END; i++))
do 
	#Formatting the number to 3 digits
	ID=$(printf "%03d" $i)

	FOLDER="$BASE_DIR/run_$ID"
	INPUT_FILE="run_$ID.inp"
	FULL_PATH="$FOLDER/$INPUT_FILE"

	#Check if the input file exist
	if [ -f "$FULL_PATH" ]; then
		echo "---------------------------------------------------"
		echo "[RUNNING] processing: $INPUT_FILE"

		#Enter the foder
		cd "$FOLDER" || exit

		#Run the PHITS
		$PHITS_COMMAND "$INPUT_FILE"

		#Back to initial folder
		cd "$CURRENT_DIR" || exit

		echo "[DONE] Finished processing: $INPUT_FILE"
	else
		echo "---------------------------------------------------"
		echo "[SKIPPED] File it's not found: $FULL_PATH"
	fi
done

echo "========================================="
echo "All work is finished!"
