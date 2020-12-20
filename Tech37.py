# Management Errors

# print 'hello' => syntax error
# print (1/0) => zero division error
# print (str.upper(23)) => type error
# f = open('textf.txt) => file not found error if you bad type name.txt

x = 2
try:
    print(1 / 4)
    print(str.upper('amir'))
    if x == 2:
        raise Exception
except TypeError:
    print('wrong date type....')
except ZeroDivisionError:
    print('division by zero')
except Exception:
    print('x is equals two')
else:
    print('Else block...')
finally:
    print('finally block always runs...')

# try:
#   pass (objects)
# except Exception:
#   pass error
# else:
#   pass error
# finally:
#   pass error