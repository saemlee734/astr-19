#define a function f(x) that returns x**3+8
#call f(x) with x = 9 and print the result
#use an if statement that executes if the result is larger than 27 and prints "YAY!"

#define the function f(x) that returns x**3+8
def f(x):
    return x**3+8

#define main function
def main():

    #set variable x = 9
    x = 9
    
    #set variable result = f(x)
    result = f(x)

    #print result
    print("Result: ", result)

    #create an if statement that executes if result is > 27
    if result > 27:
        #print YAY! if true
        print("YAY!")

#execute main function as seen in lecture 1 hello world example
if __name__ == "__main__":
    main()
















