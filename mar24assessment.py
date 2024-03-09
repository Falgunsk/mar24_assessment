#q1
def bill(pizzas,puffs,cooldrinks):
    pizza_price=100
    puff_price=20
    cooldrink_price=10
    total_price=(pizzas*pizza_price)+(puffs*puff_price)+(cooldrinks*cooldrink_price)
    print("Bill Details")
    print("No of pizzas:",pizzas)
    print("No of puffs:",puffs)
    print("No of cooldrinks:",cooldrinks)
    print("Total price=",total_price)
    
pizzas=int(input("Enter the no of pizzas bought:"))
puffs=int(input("Enter the no of puffs bought:"))
cooldrinks=int(input("Enter the no of cool drinks bought:"))
bill(pizzas,puffs,cooldrinks)

#q2
def steps(m,n):
    total_steps=m//n
    remaining_rows=m%n
    if remaining_rows!=0:
        total_steps+=1
        print("Total steps taken:",total_steps)
    else:
        print("Total steps taken:",total_steps)
           
m=int(input("Enter the number of stairs:"))
n=int(input("Enter the number of steps:"))
steps(m,n)


#q8

def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')

    for num in reversed(arr):
        if num > max_from_right:
            leaders.append(num)
            max_from_right = num

    return leaders[::-1]

arr = [23, 22, 24, 8, 9, 10]
result = find_leaders(arr)
print(result)

#q9

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = 'coding'
str2 = 'ingodc'
result = is_anagram(str1, str2)
print(result)
str1 = 'hello' 
str2 = 'hoeli'
print(is_anagram(str1, str2))

#q10

def saveIronman(s):
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]

s = "I am :IronnorI Ma, i"
result = "YES" if saveIronman(s) else "NO"
print(result)

