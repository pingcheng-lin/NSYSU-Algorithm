# Alogorithm is SA

## Command:
	python3 hw3.py
	Input file name: readfile.txt
## Output is output.txt and city result.png

## Process:
Primarily, it generate a list to put all cities, the first and the last is initial cities.
Then, randomly exchanges two cities, except the initial cities.
If distance becomes shorter, saves it.
Otherwise, use thermodynamic formula: P(dE) = exp(dE/(kT)) compare with random number from 0 to 1.
Make it possible to accept worse solution.
When program runs to late period, the probability to accept worse solution will decrease.
At the end, when temperature decreases to practical value, output the result.
