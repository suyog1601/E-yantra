# Function to calculate Euclidean distance between two points
def dec_to_binary(n):
  bin_num = bin(n).replace("0b", "")
  # Complete this function to return binary equivalent output of the given number 'n' in 8-bit format
  return bin_num
# Main function
if __name__ == '__main__':
  # take the T (test_cases) input
  test_cases = int(input())
  b = []
  # Write the code here to take the n value
  for case in range(1,test_cases+1):
    # take the n input values
    n = int(input())
    # print (n)
    # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
    bin_num = dec_to_binary(n)
    c = int(bin_num)
    b.append(c)
  print(b)
  for i in range(0,test_cases):
    r = str(b[i])
    l = len(r)
    for j in range(0,8-l):
      print("0",end="")
  
    if(i == (test_cases-1)):
      print(b[i], end="")
    else:
      print(b[i])
