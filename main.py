class query:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

q1 = query("horse", 20)
q2 = query("bird", 20)
q3 = query("tiger", 20)
q4 = query("fish", 20)
q5 = query("zebra", 20)
q6 = query("bear", 20)
q7 = query("dog", 20)
q8 = query("monkey", 20)
q9 = query("shark", 20)
q10 = query("snake", 20)
q11 = query("lizard", 20)
q12 = query("bat", 20)
q13 = query("lion", 20)
q14 = query("cat", 20)
q15 = query("wolf", 20)
q16 = query("cow", 20)
q17 = query("sheep", 20)
q18 = query("pig", 20)
q19 = query("donkey", 20)
q20 = query("shark", 20)
queryList = (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20)

import ImageGetter
ImageGetter.imageGetter(queryList)
import ShadowMaker
