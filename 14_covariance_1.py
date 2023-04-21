#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    cov = 0 
    length= len(input_x)

    mean_x= statistics.mean(input_x)
    mean_y= statistics.mean(input_y)
    
    cov= sum([(input_x[index]-mean_x)*(input_y[index]-mean_y) for index in range(length)])/length

    print(f'Input x:{input_x}, Input y: {input_y}')
    print(f'Mean x : {statistics.mean(input_x)}, Mean y : {statistics.mean(input_y)} ')
    
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')
