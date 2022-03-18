from enum import Enum
class FoodCategory(Enum):
  VEGETABLE = 1
  FRUIT = 2
  GRAIN = 3
  PROTEIN = 4
  DAIRY = 5
  OIL = 6
  OTHER = 7

class FoodItem(object):
  def __init__(self, name, category, calories_per_100g):
    self.name = name
    self.category = FoodCategory(category)
    self.calories = int(calories_per_100g)

  def get_name(self):
    return self.name

  def get_category(self):
    return self.category

  def calories_per_100g(self):
    return self.calories

  def __str__(self):
    return f"{self.name} ({self.category}) {self.calories}cal/100g"

class FoodServing(object):
  def __init__(self, fooditem, grams):
    self.fooditem = fooditem
    self.grams = int(grams)

  def food(self):
    return self.fooditem

  def amount(self):
    return self.grams

  def calories(self):
    return int(self.fooditem.calories_per_100g()/100 * self.grams)

  def __str__(self):
    return f"{self.grams}g of {self.fooditem}"
    
class Meal(object):  
  def __init__(self):
    self.list = [] 

  def addFood(self, serving):
    self.list.append(serving)

  def calories(self):
    sum_calories = 0
    for s in self.list:
      sum_calories += s.calories()
    return sum_calories

  def __str__(self):
    newfoods = ""
    for s in self.list:
      newfoods += str(s) + '\n'
    return newfoods