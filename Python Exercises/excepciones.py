# The above code is asking the user to input a value, and then it is dividing that value by 4. If the
# user inputs a value that cannot be divided by 4, the code will print "Error". If the user inputs a
# value that can be divided by 4, the code will print "Todo ok!" and then break. Finally, the code
# will print "Fin de la iteración" no matter what.
while(True):
    try:
        n = float(input("Introduce un valor: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Error")
    else:
        print("Todo ok!")
        break
    finally:
        print("Fin de la iteración")
        
        
try:
    n = input("Introduce un número: ")
    5/n
except TypeError:
    print("Error TypeError")
except Exception as e:
    print(f"Error: {e}")
