# support fx
import math

def log(variable):
    return math.log10(variable)


def logn(base, variable):
    return round(math.log(variable, base), 5)


def sin(variable):
    return round(math.sin(math.radians(variable)), 5)


def cos(variable):
    return round(math.cos(math.radians(variable)), 5)


def tan(variable):
    return round(math.tan(math.radians(variable)), 5)


def rm(num):
    x = str(num).lstrip("0")
    if x == "":
        return "0"
    else:
        return str(float(x))


def expn(b, n):
    return math.pow(b, n)

def sqrt(n):
    return math.sqrt(n)


def iter(str):
    f = ""
    temp = ""
    for i in range(0, len(str)):

        if str[i].isdigit() or str[i] == ".":
            temp = temp + str[i]
           # print(temp)
        else:
            if temp != "":
                temp = rm(temp)
            f = f + temp + str[i]
            temp = ""
    if temp == "":
        return f
    else:
        return f + rm(temp)
    return


def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i

def auto_complete(str1):
    stack = []
    brackets_in = ['(','{','[']
    bracket_out = [')','}',']']
    str1_mod = ""
    for i in str1:
        if i in brackets_in:
            str1_mod = str1_mod + '('
            stack.append('(')
            continue
        if i in bracket_out:
            str1_mod = str1_mod + ')'
            stack.pop()
            continue

        str1_mod += i


    for i in reversed(stack):
        #if i == '(':
        str1_mod = str1_mod + ')'
        # elif i == '{':
        #     str1 = str1 + '}'
        # elif i == '[':
        #     str1 =  str1 + ']'
    
    return str1_mod



