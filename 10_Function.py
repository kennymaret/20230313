def my_add(input):
    sum = 0
    for x in input :
        sum += int(x)
    return sum

# 1. Input 
input = [10,20,30]

# 2. Process 
answer = my_add(input)

# 3. Output 
print(f'answer: {answer}')

def my_add(input):
    sum = 0
    for x in input :
        sum += int(x)
    return sum

# 1. Input 
input = [874,345,623,6345,13423,6434]

# 2. Process 
answer = my_add(input)

# 3. Output 
print(f'answer: {answer}')

def my_add(input):
    sum = 1
    for x in input :
        sum *= int(x)
    return sum

# 1. Input 
input = [874,345,623,6345,13423,6434]

# 2. Process 
answer = my_add(input)

# 3. Output 
print(f'answer: {answer}')
import statistics,math 
def my_sd(input):
    print(f'input : {input}')
    length = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'Mean :{mean}')
    for x in input:
        sum += (int(x)-mean )**2
    sum = sum / length
    output = math.sqrt(sum)
    return output
