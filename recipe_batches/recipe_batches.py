#!/usr/bin/python

import math


# PLAN
# function will receive recipe as {}
# function will also receive ingredients as {}

def recipe_batches(recipe, ingredients):
    # compare recipe ingredients to ingredients passed in
    # when recipe key and ingredients key are the same, see if recipe value is less than or equal to ingredients value
    # if it is increment batches
    # else return 0
    for key, val in recipe.items():
        if key not in ingredients:
            return 0
        else:
            if ingredients[key] >= recipe[key]:
                batches = ingredients[key] // recipe[key]
                return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 232, 'butter': 150, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
