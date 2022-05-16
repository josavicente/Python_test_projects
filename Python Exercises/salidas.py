x = 1000
y = 100
z = 10

print("{:04d}".format(10))
print("{:04d}".format(100))
# Printing the value of 1000 with 4 characters, and filling in the empty spaces with 0s.
print("{:04d}".format(1000))


x2 = 10.5
y2 = 45.3
z2 = 3.1415926

# Printing the value of z2 with 7 characters, 3 of which are after the decimal point.
print("{:7.3f}".format(z2))
print("{:7.3f}".format(z2*100))