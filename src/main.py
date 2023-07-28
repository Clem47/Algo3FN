import algo
import read

path_file = "./BD/exple_jouet_cours.txt"
F = read.read_file(path_file)
A = set({})
t = algo.DecompoDFen3FN(F,A)
print("----------------------------------------------")
for table in t:
    print(" ")
    print(table.get_name() + "( " +table.get_value()+ ") The primary key is " + table.get_key())
print(" ") 
print("----------------------------------------------")