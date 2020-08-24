
def get_maximum_value_recursion(weight,values,capacity, n):
    '''
    Function to get maximum value
    Function uses recursion to get maximum value
    '''
    if n==0 or capacity == 0:
          return 0
    if weight[n-1]>capacity:
          return get_maximum_value_recursion(weight,values,capacity, n-1)
    else:
          return max( 
            values[n-1] + get_maximum_value_recursion( 
                weight, values,capacity-weight[n-1], n-1),  
                get_maximum_value_recursion(weight,values,capacity, n-1))  


'''
Function driver code
'''
weight = [5,4,6,4] 
values = [10,40,30,50]
capacity = 10
n = len(values) 

maximum_value = get_maximum_value_recursion(weight,values,capacity,n)
print(maximum_value)
