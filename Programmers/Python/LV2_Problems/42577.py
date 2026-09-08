# 42577
# 13'49"

'''
phone_book	                        return
["119", "97674223", "1195524421"]	false
["123","456","789"]	                true
["12","123","1235","567","88"]	    false
'''

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
        

print(solution(["119", "97674223", "1195524421"]))

# or: hash
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer