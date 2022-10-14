from math import remainder


height = 195
feet = height / 30.48
remainderdecimal = feet - int(feet)
feet = int(feet)
print(int(feet))
remdecimal = int(round(remainderdecimal * 12, 0))
print(f"I am {height} tall, i.e. {feet} feet and {remdecimal}")
