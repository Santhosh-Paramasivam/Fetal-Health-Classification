import pandas
import numpy

values = []
with open(r"scripts\\new_results\Normalizer Timings.txt", "r") as file:
    item_list = file.readlines()
    item_string = ''
    for item in item_list:
        item_string += item

    item_list = item_string.split("\n")
    number_list = []
    item_list.remove('')
    for item in item_list:
        number_list.append(float(item))
    values = number_list

print("Avg. " + str(numpy.average(values)) + "  Std." + str(numpy.std(values)))