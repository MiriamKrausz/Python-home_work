
import random
import os
import inspect
# ===========Iterator=========
# 1
class RandomNumbers:
  def __init__(self, count):
    self.count = count


  def __iter__(self):
    self.num_generated = 0
    return self

  def __next__(self):
    if self.num_generated < self.count:
      self.num_generated += 1
      return random.randint(1, 100)  # Generate a random number between 1 and 100
    else:
      raise StopIteration

random_nums = RandomNumbers(5)
for num in random_nums:
  print(num)
# ===============2=============
# =========3======
os.chdir("D:\תשפג\English")
def context(file_name):
  for dirpath, dirnames, filenames in os.walk('.'):
    yield dirpath, dirnames, filenames

for con in context("D:\תשפג\English") :
  print(con)
# ==============4============
def isGenerator(str):
  return inspect.isgenerator(str)
print(isGenerator("nice"))
# ======6======
# *************
def increase(num):
  yield num+1
for i in increase(6):
  print(i)
# *****************
def decrease(num):
  yield num-1
for i in decrease(6):
  print(i)
# ==============5=============
def yieldFrom():
  yield from context("D:\תשפג\English")
  yield from decrease(6)
gen=yieldFrom()
for g in gen:
  print(g)
# ********************
# slots
# 1
class slots:
  _slots_=('name','address','age');
  def __init__(self):
    self.name="miri"
    self.address="Hazon Ish"
    self.age=19
  def __iter__(self):
    yield self

slo=slots()
print(slo.age)