#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import math
import csv
import numpy as np
import pandas as pd

def histogram_times(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for line in csv_reader:
            timeVal = line[1].split(':')
            hour = timeVal[0]
            try: 
                hourInt = int(hour)
                counter[hourInt - 1] += 1
            except:
                continue
    return counter

def weigh_pokemons(filename, weight):
    pokemon_names = []

    with open(filename) as json_file:
        json_data = json.load(json)
        for pokemon in range(len(json_data["pokemon"])):
            real_weight = float(json_data["pokemon"][pokemon]["weight".split("")[0])
            if json_data["pokemon"][pokemon]["weight"] == weight:
                pokemon_names.append(json_data["pokemon"][pokemon]["names"])
    return pokemon_names        

def single_type_candy_count(filename):
    with open(filename) as json_file:
        json_data = json.load(json)
        sum = 0
        for pokemon in range(len(json_data["pokemon"])):
            if len(json_data["pokemon"[pokemon]["type"] == 1:
                try:
                    sum += int(json_data["pokemon"[pokemon]["candy_count"])
                except:
                    continue
    return sum

def reflections_and_projections(points):
    for i in range(len(points[1])):
        distance = 1 - points[1][i]
        points[1][i] = 1 + distance

    angle_matrix = np.array( [ [math.cos(math.pi/2) ,-math.sin(math.pi/2)], [math.cos(math.pi/2) , -math.sin(math.pi/2)] ])
    for i in range(len(points[i])):
        points[i] = np.dot(angle_matrix, points[i])
    constant = 1/(10)
    constant_matrix = np.array( [ [1 ,3], [3 , 9] ])
    for i in range(len(points[i])):
        points[i] = np.dot(constant_matrix, points[i])
    return points

def normalize(image):
    maximum = image[0][0]
    mimimum = image[0][0]
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] > maximum:
                maximum = image[i][j]
            if image[i][j] < minimum:
                minimum = image[i][j]
    constant = 255/(maximum - mimimum)
    for index in range(len(image)):
        for point in range(len(image[index])):
            prime = constant * (image[index][point] - minimum)
    return image

def sigmoid_normalize(image):
    pass

