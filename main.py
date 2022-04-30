class query:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

q1 = query("horse", 15)
q2 = query("bird", 15)
q3 = query("tiger", 15)
q4 = query("fish", 15)
q5 = query("zebra", 15)
q6 = query("bear", 15)
q7 = query("dog", 15)
q8 = query("monkey", 15)
q9 = query("shark", 15)
q10 = query("snake", 15)
q11 = query("lizard", 15)
q12 = query("bat", 15)
q13 = query("lion", 15)
q14 = query("cat", 15)
q15 = query("wolf", 15)
q16 = query("cow", 15)
q17 = query("sheep", 15)
q18 = query("pig", 15)
q19 = query("donkey", 15)
q20 = query("shark", 15)
queryList = (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20)

import ImageGetter
ImageGetter.imageGetter(queryList)
import ShadowMaker
