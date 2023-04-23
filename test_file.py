# ================== Testing section: Function ===================
def example_function():
    print("Hello, world!")

                    #dsadasasdasda
                #saddfasdasdasdasd
            #saddfasdasdasdasd       
        #dsadasasdasda
    #saddfasdasdasdasd
#saddfasdasdasdasd


# ================== Testing section: If, Elif, Else ===================
x = 5

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is not greater than 5")


# ================== Testing section: If, Elif, Else ===================
x = 5

if x > 10:
    print("x is greater than 10")
    # ================== Testing section: If, Elif, Else ===================
    x = 5

    if x > 10:
        print("x is greater than 10")
        
    elif x > 5:
        try:
            print(5 / 0)
            try:
                print(5 / 0)

            except ZeroDivisionError:
                print("Division by zero")

            finally:
                print("This will always be executed")


        except ZeroDivisionError:
            print("Division by zero")

        finally:
            print("This will always be executed")


        # ================== Testing section: If, Elif, Else ===================
        x = 5

        if x > 10:
            print("x is greater than 10")
        elif x > 5:
            print("x is greater than 5 but not greater than 10")
        else:
            print("x is not greater than 5")
        
        print("x is greater than 5 but not greater than 10")
    else:
        print("x is not greater than 5")

elif x > 5:
    print("x is greater than 5 but not greater than 10")
    i = 0
    while i < 5:
        i = 0
        while i < 5:
            print(i)
        i += 1  
        print(i)
        i += 1
else:
    print("x is not greater than 5")

# ================== Testing section: While ===================
i = 0
while i < 5:
    print(i)
    i += 1
    
    
# ================== Testing section: While 2 ===================
while i < 5:
    print(i)
    i += 1
        
        # Random comment
        
        # Random comment
        
        # Random comment
        # Random comment
        # Random comment
        
    while i < 5:
        
        print(i)
        i += 1
        # Random comment

        while i < 5:
            print(i)
            print(i)
            i += 1               
                    
        print(i)
        print(i)

                # Random comment
        
        
# ================== Testing section: While 3 ===================
while i < 5:
    print(i)
    i += 1
        
        # Random comment
        
        # Random comment
        
        # Random comment
        # Random comment
        # Random comment
        
        while i < 5:       
        
        print(i)
        i += 1
        # Random comment
        
                    while i < 5:
                        print(i)
                        i += 1
                        # Random comment
                        
                        
                                while i < 5:                              
                                
                                print(i)
                                i += 1
                                # Random comment
                                
                                
                                        while i < 5:
                                            print(i)
                                            i += 1                                      
                    

                                        
                    

                                            # Random comment

# ================== Testing section: For ===================
for i in range(5):
    print(i)


# ================== Testing section: Try, Except, Finally ===================
try:
    print(5 / 0)

except ZeroDivisionError:
    print("Division by zero")

finally:
    print("This will always be executed")


# ================== Testing section: With ===================
with open('test.txt', 'w') as file:
    file.write("Test")


# ================== Testing section: Nested blocks ===================
def nested_function():
    if x > 10:
        for i in range(10):
            if i % 2 == 0:
                print("Even number:", i)
            
            
            else:
                print("Odd number:", i)
         

    elif x > 5:
        while x > 0:
            x -= 1
            print("Countdown:", x)
         
        
    
    else:
        try:
            print(5 / x)
        
        
        except ZeroDivisionError:
            print("Division by zero")
        
        
        finally:
            print("Nested function executed")
        
    
        
    


# ================== Testing section: Single-line comments ===================
# This is a single-line comment

# ================== Testing section: Multi-line comments ===================
'''
This is a
multi-line
comment
'''

"""
This is another
multi-line
comment
"""

# ================== Testing section: Inline comments ===================
print("Inline comment example")  # This is an inline comment

# ================== Testing section: Spaces ===================



# ================== Testing section ===================

# Testing single-line comments
def func1():
    # This is a single-line comment
    print("Hello world")



# Testing multi-line comments
def func2():
    """
    This is a
    multi-line
    comment
    """
    print("Hello world")



# Testing if-else statements
def func3():
    x = 10
    if x < 5:
        print("x is less than 5")
    elif x > 5:
        print("x is greater than 5")
    else:
        print("x is equal to 5")
    

# Testing if-else statements
def func3():
    x = 10
    if x < 5:
        print("x is less than 5")


    elif x > 5:
        print("x is greater than 5")
        print("x is greater than 5")

        

        print("x is greater than 5")
     



    else:
        print("x is equal to 5")
    

    


# Testing while loops
def func4():
    i = 0
    while i < 5:
        print(i)
        i += 1
    

    


# Testing for loops
def func5():
    for i in range(5):
        print(i)
    

    


# Testing try-except-finally blocks
def func6():
    try:
        x = 1 / 0
    
    
    except ZeroDivisionError:
        print("Cannot divide by zero")
    
    
    finally:
        print("This will always execute")
    

    


# Testing with statement
def func7():
    with open("test.txt", "w") as f:
        f.write("Hello world")
    

    


# Testing indentation levels
def func8():
    for i in range(3):
        if i < 2:
            print("i is less than 2")
        
        
        else:
            print("i is greater than or equal to 2")
            for j in range(2):
                print("Nested loop")
            
            

            if True:
                print("Nested if")
            
        
    

            
        
    


# ================== Inline examples ===================

x = 5  # Testing inline comments

y = (1 +
     2 +
     3)  # Testing multi-line statements

z = [i for i in range(10)
     if i % 2 == 0]  # Testing list comprehension
     
     

# ================== Multi case examples ===================


def example_1():
    if True:
        print("True")
    
    elif False:
        print("False")
    
    else:
        print("Neither")
    


def example_2():
    try:
        x = 1 / 0
    
    except ZeroDivisionError:
        print("Zero division error")
    
    except Exception as e:
        print("Some other error:", e)
    
    finally:
        print("Finally executed")
    



def example_2_():
    try:
        x = 1 / 0
    
    except ZeroDivisionError:
        print("Zero division error")
        
        a =1
    

    except Exception as e:
        print("Some other error:", e)
    



    finally:
        print("Finally executed")
    

    try:
        x = 1 / 0
    

        

def example_2__():
    try:
        x = 1 / 0
    

    except ZeroDivisionError:
        print("Zero division error")
        
        a =1
    


    except Exception as e:
        print("Some other error:", e)
    



    finally:
        print("Finally executed")

        a = 3

        b = 1+a
    



def example_3():
    if True:
        if False:
            print("True and False")
        
        else:
            print("True and not False")
        
    
    else:
        if False:
            print("False and False")
        
        else:
            print("False and not False")
        
    


def example_4():
    for i in range(3):
        if i == 0:
            print("i is 0")
        
        elif i == 1:
            print("i is 1")
        
        else:
            print("i is 2")
        
    


def example_5():
    try:
        x = 1 / 0
    
    except ZeroDivisionError:
        try:
            y = int("a")
        
        except ValueError:
            print("ValueError")
        
        finally:
            print("Inner finally")
        
    
    except Exception as e:
        print("Some other error:", e)
    
    finally:
        print("Outer finally")
    


def example_6():
    with open("test.txt", "r") as file:
        try:
            content = file.read()
        
        except IOError:
            print("IOError")
        
        finally:
            print("Finally in with block")
        
    


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()

