import detect_test
import random
import string
import detection
import label_perturbation_attack
from detection import main
from fuzz_values import fuzz_values


def fuzz():

    # Fuzz: checkTestFile(path2dir)
    fuzz_function1()

    # Fuzz: get_test_details(test_script)
    fuzz_function2()

    # Fuzz: getPythonParseObject(pyFile)
    fuzz_function3()

    # Fuzz: runs(lst)
    fuzz_function4()

    # Fuzz: euc_dist(x1, x2)
    fuzz_function5()
    return


def fuzz_function1():
    print("="*50)
    print("Fuzzing Method: checkTestFile")
    print("="*50)
    fuzz_input = random_fuzz_int()
    # detect_test.checkTestFile(fuzz_input)
    try:
        detect_test.checkTestFile(fuzz_input)
    except:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
    fuzz_input = random_fuzz_string()
    try:
        detect_test.checkTestFile(fuzz_input)
    except:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
    fuzz_input = random.choice(fuzz_values)
    try:
        detect_test.checkTestFile(fuzz_input)
    except:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
    return


def fuzz_function2():
    print("\n" + "=" * 50)
    print("Fuzzing Method: get_test_details")
    print("=" * 50)
    fuzz_input = random_fuzz_int()
    # main.get_test_details(fuzz_input)
    try:
        main.get_test_details(fuzz_input)
    except:
        print("Failed! Method: get_test_details. Input: " + str(fuzz_input))
    fuzz_input = random_fuzz_string()
    try:
        main.get_test_details(fuzz_input)
    except:
        print("Failed! Method: get_test_details. Input: " + str(fuzz_input))
    fuzz_input = random.choice(fuzz_values)
    try:
        main.get_test_details(fuzz_input)
    except:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
    return


def fuzz_function3():
    print("\n" + "=" * 50)
    print("Fuzzing Method: getPythonParseObject")
    print("=" * 50)
    fuzz_input = random_fuzz_int()
    # detection.py_parser.getPythonParseObject(fuzz_input)
    try:
        detection.py_parser.getPythonParseObject(fuzz_input)
    except:
        print("Failed! Method: getPythonParseObject. Input: " + str(fuzz_input))
    fuzz_input = random_fuzz_string()
    try:
        detection.py_parser.getPythonParseObject(fuzz_input)
    except:
        print("Failed! Method: getPythonParseObject. Input: " + str(fuzz_input))
    fuzz_input = random.choice(fuzz_values)
    try:
        detection.py_parser.getPythonParseObject(fuzz_input)
    except:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
    return


def fuzz_function4():
    print("\n" + "=" * 50)
    print("Fuzzing Method: runs")
    print("=" * 50)
    fuzz_input = random_fuzz_int()
    # label_perturbation_attack.cliffsDelta.runs(fuzz_input)
    try:
        label_perturbation_attack.cliffsDelta.runs(fuzz_input)
    except:
        print("Failed! Method: getPythonParseObject. Input: " + str(fuzz_input))
    fuzz_input = random_fuzz_string()
    try:
        label_perturbation_attack.cliffsDelta.runs(fuzz_input)
    except:
        print("Failed! Method: getPythonParseObject. Input: " + str(fuzz_input))
    fuzz_input = random.choice(fuzz_values)
    try:
        label_perturbation_attack.cliffsDelta.runs(fuzz_input)
    except:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
    return


def fuzz_function5():
    print("\n" + "=" * 50)
    print("Fuzzing Method: eucDist")
    print("=" * 50)
    fuzz_input1 = random_fuzz_int()
    fuzz_input2 = random_fuzz_int()
    # label_perturbation_attack.knn.euc_dist(fuzz_input1, fuzz_input2)
    try:
        label_perturbation_attack.knn.euc_dist(fuzz_input1, fuzz_input2)
    except:
        print("Failed! Method: getPythonParseObject. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
    fuzz_input1 = random_fuzz_string()
    fuzz_input2 = random_fuzz_string()
    try:
        label_perturbation_attack.knn.euc_dist(fuzz_input1, fuzz_input2)
    except:
        print("Failed! Method: getPythonParseObject. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
    fuzz_input1 = random.choice(fuzz_values)
    fuzz_input1 = random.choice(fuzz_values)
    try:
        label_perturbation_attack.knn.euc_dist(fuzz_input1, fuzz_input2)
    except:
        print("Failed! Method: checkTestFile. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
    return


def random_fuzz_int():
    fuzz_int = 0
    fuzz_int = random.randint(-1000000000, 1000000000)
    return fuzz_int


def random_fuzz_string():
    fuzz_string = ''
    characters = string.printable
    fuzz_string = ''.join(random.choice(characters) for i in range(random.randint(0, 100)))
    return fuzz_string


if __name__ == '__main__':
    fuzz()
