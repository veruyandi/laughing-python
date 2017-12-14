# begin isZeroCountOdd = False
def get_baum_sweet_sequence(upto_number):
    bsseq = []
    for i in range(1,upto_number+1):
        bsseq.append(get_baum_sweet_binary(i))
    return bsseq

# return b_n = 1 if no consecutive zeros of odd numbers
def get_baum_sweet_binary(number):
  #True if there is only consecutive zeros of even numbers
  is_count_even = True

  if number == 1:
    return 1
  else:
    dividend = number
    quotient = 1
    while quotient > 0:

        #if quot > 1 : get next binary digit(remainder) by dividing 2, begin from the ones, go through tens, hundreds etc.
        #if quotient == 1:
            #then count is even till the last 2 digits, so the result depends on the two last digits which are rem & quot
            #return quotient and remainder  ## 11 returns 1 | 10 returns 0 since "0" is a seq of zero of odd count
        #else:
        quotient, remainder = divmod(dividend, 2)
        #if next is 1, a zero block end occurs, so check if no odd count
        if remainder == 1:
            if not is_count_even:
                return 0
            elif quotient == 0: #came to last digit
                return 1
            #else: Then no_odd_count and not the last digit, so continue with next digit
        else: #rem = 0
            is_count_even = not is_count_even

        dividend = quotient # continue dividing by 2 for next iteration

my_list = get_baum_sweet_sequence(100)
print(my_list)

