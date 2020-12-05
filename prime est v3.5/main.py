import math
import time
import random
import functions

#### enter search data here: ####
number = 2211282552952966643528108525502623092761208950247001539441374831912882294140200198651272972656974659908590033003140005117074220456085927635795375718595429883895870922923849100670303412462054578456641366454068421436129301769402084639106587591479425143514458199
how_many_to_search = 1000000
start = 2
end = round((number ** 0.5) + 0.5)

#### search function, dont change ####
t1 = time.perf_counter()
for i in range(how_many_to_search+1):
    ran_num = random.randrange(start, end+1)
    if functions.find_init_est(ran_num) != 0:
        div_num = number/ran_num
        if div_num == int(div_num):
            if functions.find_init_est(div_num) != 0:
                if len(str(ran_num)) == len(str(div_num)):
                    print("2 numbers have been found!")
                    print(ran_num, div_num)
t2 = time.perf_counter()
print ("run time:",t2-t1)