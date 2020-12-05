# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def remove_forbidden_characters(sentence, forbidden_characters):
    res = ""
    for c in sentence:
        check = True
        for i in forbidden_characters:
            if c == i:
                check = False
        if check:
            res += c
    print (c)
    pass


def reverse(word):
    return word[::-1]
    pass


def is_palindrome(word):
    rev = reverse(word)
    if rev == word:
        return True
    return False
    pass


def find_largest_palindrome():
    num1 = 0
    for i in range(100, 999):
        for j in range(i, 999):
            if is_palindrome(str(i * j)) & (i * j > num1):
                num1 = i * j
    num2 = str(num1)[::2]
    print(num1, num2)
    pass


def validate_israeli_id(id_number):
    sum = 0
    eveStr = str(id_number)[::2]
    oddStr = str(id_number)[1::2]
    for c in eveStr:
        sum += int(c)
    for c in oddStr:
        add = 2 * int(c)
        if add > 9:
            sum += add - 9
        else:
            sum += add
    if sum % 10 == 0:
        print "valid"
    else:
        print "invalid"
    pass



# def evaluate_formula(formula):
#     spl = formula.split()
#     if len(spl) == 1:
#         print (eval(formula))
#     else:
#         num2 = ""
#         num1 = spl.pop()
#         num0 = spl.pop()
#         math = spl.pop()
#         while math not in "+-*/":
#             num2 = num1 + " " + num2
#             num1 = num0
#             num0 = math
#             math = spl.pop()
#         add = "(" + num0 + math + num1 + ") " + num2
#         spl.append(add)
#         evaluate_formula(' '.join(spl))
#     pass

def evaluate_formula(formula):
    spl = formula.split()[::-1]
    if spl[0] in "-+*/":
        spl.append(str(eval(f'{spl.pop()}{spl.pop(0)}{spl.pop()}')))
        evaluate_formula(' '.join(spl)[::-1])
    else:
        print (eval(formula))

# Press the green button in the gutter to run the script.
evaluate_formula(" whats up flash ")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
