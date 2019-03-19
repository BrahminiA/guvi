input_str = input()
 
final_str = ""
rev = reversed(input_str)
 
if list(input_str) == list(rev):
    print("yes")
else:
    print("no")
