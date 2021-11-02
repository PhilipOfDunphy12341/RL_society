a= 0
b=10
def Integrate (n,w_values,a,b,x_values):
    sum_part = 0
    for i in range(n):
        x_i = x_values[i]
        w_i = w_values[i]
        d_area = w_i * (x_i**3 + x_i**2)
        sum_part += d_area
        print (d_area)
    output = (b-a)*(sum_part)
    error = output - 2833.333
    return output, error

print (str(Integrate(2,[0.5,0.5],a,b,[a,b])) + " part_a")

print (str(Integrate(3,[0.166667,2/3,0.166667],a,b,[a,(a+b)/2,b])) + " part b")

#print (str(Integrate(2,[0.5,0.5],a,b,[(1/2*(a+b+(b-a))/(3**1/2)),(1/2*(a+b-(b-a))/(3**1/2))])+ " part c")
