#!/usr/bin/env python

# Author: Annika Laberge, alaberge@uoregon.edu

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''
 

__version__ = "0.2"         # Read way more about versioning here:
# https://en.wikipedia.org/wiki/Software_versioning


DNA_bases = set('ATGCNatcgn')
RNA_bases = set('AUGCNaucgn')


def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter)-33


def qual_score(phred_score: str) -> float:
    '''Calculates the average quality score of a sequence of phred scores'''
    total_qual = 0
    for char in phred_score:
        total_qual += convert_phred(char)
    return total_qual/len(phred_score)



def validate_base_seq(seq: str, RNAflag: bool = False) -> bool:
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    return set(seq) <= (RNA_bases if RNAflag else DNA_bases)


def gc_content(seq:str) -> float: 
    '''Returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    if validate_base_seq(seq) == False:
        raise AssertionError
    GC: int = 0
    ATU: int = 0
    seq = seq.strip("\n").lower()
    for char in seq:
        if char == 'g' or char == "c":
            GC += 1
        elif char == 't' or char =='a' or char =='u':
            ATU += 1
            
           

    return GC/(ATU + GC)


def calc_median(lst: list) -> float:
    '''
    Calculates and returns the median of a previously sorted list of floats or ints. If the list is empty, None is returned.
    '''
    length = len(lst)
    if length == 0:
        print("The list is empty!")
        return None
    elif length % 2 == 0: # We have an even number of list elements
        return (lst[length//2]+lst[length//2-1])/2
    else: # We have an odd number of list elements
        return lst[(length-1)//2]


def oneline_fasta(file, new_file_name):
    '''Turns a fasta file into 2 lines per record (line 1 = header, line 2 = sequence)'''
    new_seq: str = ""
    with open(file,"r") as fh, open(f"{new_file_name}.fasta","w") as newFile:
        for line in fh:
            if line.startswith(">"):
                if new_seq != "":
                    newFile.write(f"{new_seq}\n")
                    new_seq=""
                newFile.write(line)
            else:
                line = line.strip('\n')
                new_seq += line
        newFile.write(f"{new_seq}\n")


if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")
    assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    assert validate_base_seq("Hi there!") == False, "Validate base seq fails to recognize nonDNA"
    assert validate_base_seq("Hi there!", True) == False, "Validate base seq fails to recognize nonDNA"
    print("Passed DNA and RNA tests")
    assert qual_score("A") == 32.0, "wrong average phred score for 'A'"
    assert qual_score("AC") == 33.0, "wrong average phred score for 'AC'"
    assert qual_score("@@##") == 16.5, "wrong average phred score for '@@##'"
    assert qual_score("EEEEAAA!") == 30.0, "wrong average phred score for 'EEEEAAA!'"
    assert qual_score("$") == 3.0, "wrong average phred score for '$'"
    print("Qual_score works!")
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATCGAT") == 0.5
    print("GC_content works!")
