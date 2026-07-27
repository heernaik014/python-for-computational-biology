# File: 03_Find_ATG.py
seq = input("Enter the dna sequence")
if "ATG" in seq:
    print("ATG found at", seq.find("ATG"))
    print("ATG found at", seq.find("ATG", seq.find("ATG")+1))