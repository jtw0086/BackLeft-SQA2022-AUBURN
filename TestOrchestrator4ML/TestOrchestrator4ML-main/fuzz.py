import detect_test
import random
import string
from label_perturbation_attack import cliffsDelta
from label_perturbation_attack import knn
from fuzz_values import fuzz_values

# Author - Devin Spivey

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
        print("Passed! Ran without error.")
    except Exception as e:
        print("Failed! Method: checkTestFile. Input: " + str(fuzz_input))
        print("Exception: ")
        print(e)
    fuzz_input = random_fuzz_string()
    try:
        detect_test.checkTestFile(fuzz_input)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: checkTestFile. Input: " + str(fuzz_input))
        print("Exception: ")
        print(e)
    fuzz_input = random.choice(fuzz_values)
    try:
        detect_test.checkTestFile(fuzz_input)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: checkTestFile. Input: " + str(fuzz_input))
        print("Exception: ")
        print(e)
    return


def fuzz_function2():
    print("\n" + "=" * 50)
    print("Fuzzing Method: cliffsDelta")
    print("=" * 50)
    fuzz_input1 = random_fuzz_int()
    fuzz_input2 = random_fuzz_int()
    try:
        cliffsDelta.cliffsDelta(fuzz_input1, fuzz_input2, dull=[0.147, 0.33, 0.474][0])
        print("Passed! Ran without error.")
    except Exception as e:
        print("Failed! Method: cliffsDelta. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
        print("Exception: ")
        print(e)
    fuzz_input1 = random_fuzz_string()
    fuzz_input2 = random_fuzz_string()
    try:
        cliffsDelta.cliffsDelta(fuzz_input1, fuzz_input2, dull=[0.147, 0.33, 0.474][0])
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: cliffsDelta. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
        print("Exception: ")
        print(e)
    fuzz_input1 = random.choice(fuzz_values)
    fuzz_input2 = random.choice(fuzz_values)
    try:
        cliffsDelta.cliffsDelta(fuzz_input1, fuzz_input2, dull=[0.147, 0.33, 0.474][0])
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: cliffsDelta. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
        print("Exception: ")
        print(e)
    return


def fuzz_function3():
    print("\n" + "=" * 50)
    print("Fuzzing Method: attack_model")
    print("=" * 50)
    fuzz_input1 = random_fuzz_int()
    fuzz_input2 = random_fuzz_int()
    fuzz_input3 = random_fuzz_int()
    fuzz_input4 = random_fuzz_int()
    # detection.py_parser.getPythonParseObject(fuzz_input)
    try:
        knn.calculate_k(fuzz_input1, fuzz_input2, fuzz_input3, fuzz_input4)
        print("Passed! Ran without error.")
    except Exception as e:
        print("Failed! Method: attack_model. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2) + ", " +\
            str(fuzz_input3) + ", " + str(fuzz_input4))
        print("Exception: ")
        print(e)
    fuzz_input1 = random_fuzz_string()
    fuzz_input2 = random_fuzz_string()
    fuzz_input3 = random_fuzz_string()
    fuzz_input4 = random_fuzz_string()
    try:
        knn.calculate_k(fuzz_input1, fuzz_input2, fuzz_input3, fuzz_input4)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: attack_model. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2) + ", " + \
        str(fuzz_input3) + ", " + str(fuzz_input4))
        print("Exception: ")
        print(e)
    fuzz_input1 = random.choice(fuzz_values)
    fuzz_input2 = random.choice(fuzz_values)
    fuzz_input3 = random.choice(fuzz_values)
    fuzz_input4 = random.choice(fuzz_values)
    try:
        knn.calculate_k(fuzz_input1, fuzz_input2, fuzz_input3, fuzz_input4)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: attack_model. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2) + ", " + \
        str(fuzz_input3) + ", " + str(fuzz_input4))
        print("Exception: ")
        print(e)
    return


def fuzz_function4():
    print("\n" + "=" * 50)
    print("Fuzzing Method: runs")
    print("=" * 50)
    fuzz_input = random_fuzz_int()
    # label_perturbation_attack.cliffsDelta.runs(fuzz_input)
    try:
        cliffsDelta.runs(fuzz_input)
        print("Passed! Ran without error.")
    except Exception as e:
        print("Failed! Method: runs. Input: " + str(fuzz_input))
        print("Exception: ")
        print(e)
    fuzz_input = random_fuzz_string()
    try:
        cliffsDelta.runs(fuzz_input)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: runs. Input: " + str(fuzz_input))
        print("Exception: ")
        print(e)
    fuzz_input = random.choice(fuzz_values)
    try:
        cliffsDelta.runs(fuzz_input)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: runs. Input: " + str(fuzz_input))
        print("Exception: ")
        print(e)
    return


def fuzz_function5():
    print("\n" + "=" * 50)
    print("Fuzzing Method: eucDist")
    print("=" * 50)
    fuzz_input1 = random_fuzz_int()
    fuzz_input2 = random_fuzz_int()
    # label_perturbation_attack.knn.euc_dist(fuzz_input1, fuzz_input2)
    try:
        knn.euc_dist(fuzz_input1, fuzz_input2)
        print("Passed! Ran without error.")
    except Exception as e:
        print("Failed! Method: eucDist. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
        print("Exception: ")
        print(e)
    fuzz_input1 = random_fuzz_string()
    fuzz_input2 = random_fuzz_string()
    try:
        knn.euc_dist(fuzz_input1, fuzz_input2)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: eucDist. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
        print("Exception: ")
        print(e)
    fuzz_input1 = random.choice(fuzz_values)
    fuzz_input2 = random.choice(fuzz_values)
    try:
        knn.euc_dist(fuzz_input1, fuzz_input2)
        print("\nPassed! Ran without error.")
    except Exception as e:
        print("\nFailed! Method: eucDist. Inputs: " + str(fuzz_input1) + ", " + str(fuzz_input2))
        print("Exception: ")
        print(e)
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
