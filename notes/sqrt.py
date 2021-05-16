"""practice by python for lessone 01"""

def is_good_enough(guess,target):
    l = 0.0001
    m = guess*guess-target
    if m>=-l and m<= l:
        return True
    else:
        False
  
def improve_guess(guess,target):
    guess = (guess + target/guess)/2
    return guess

def sqrt(target):
    guess = 1
    print(f"square of {target} is guessing to:")
    while True:
        print(guess,end="; ")
        if is_good_enough(guess,target):
            print(f"the result is {guess}")
            return guess
        else:
            guess = improve_guess(guess,target)
      
testcases = [2, 100, 1024, 3.14]
for t in testcases:
    sqrt(t)

# square of 2 is guessing to:
# 1; 1.5; 1.4166666666666665; 1.4142156862745097; the result is 1.4142156862745097
# square of 100 is guessing to:
# 1; 50.5; 26.24009900990099; 15.025530119986813; 10.840434673026925; 10.032578510960604; 10.000052895642693; 10.000000000139897; the result is 10.000000000139897
# square of 1024 is guessing to:
# 1; 512.5; 257.2490243902439; 130.61480157022683; 69.22732405448895; 42.00958563100827; 33.19248741685438; 32.02142090500024; 32.0000071648159; 32.0000000000008; the result is 32.0000000000008
# square of 3.14 is guessing to:
# 1; 2.0700000000000003; 1.7934541062801932; 1.7721327825101891; 1.7720045193089797; the result is 1.7720045193089797