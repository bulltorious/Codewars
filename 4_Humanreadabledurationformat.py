# https://www.codewars.com/kata/52742f58faf5485cae000b9a/python
def format_duration(seconds):
    
    # 3600 seconds in an hour
    # 86,400 seconds in a day
    # 31,536,000 seconds in a year
    if seconds == 0:
        return 'now'
    zeroes = []
    dic = {}
    commas = 0
    
    dic['year'] = seconds // 31536000
    dic['day'] = (seconds % 31536000) // 86400
    dic['hour'] = (seconds % 86400) // 3600
    dic['minute'] = (seconds % 3600) // 60
    dic['second'] = (seconds % 60)
    
    for key, value in dic.items():
        if value == 0:
            zeroes.append(key)
            
    for val in zeroes:
        dic.pop(val)
        
    if len(dic) > 2:
        commas = len(dic) - 2
    
    result = f''
    
    ctr = 0
    for key, value in dic.items():
        ctr +=1
        result = result + f'{value} {key}{"" if value == 1 else "s"}'
        if commas > 0:
            result +=','
            commas -= 1
        if len(dic) > 1 and ctr == len(dic) - 1:
            result += f' and'
        if ctr < len(dic):
            result += f' '

    return result

print(format_duration(3662))
#test.assert_equals(format_duration(1), "1 second")
#test.assert_equals(format_duration(62), "1 minute and 2 seconds")
#test.assert_equals(format_duration(120), "2 minutes")
#test.assert_equals(format_duration(3600), "1 hour")
#test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")