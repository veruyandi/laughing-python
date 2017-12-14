# begin isZeroCountOdd = False
def get_baum_sweet_sequence(upto_number):
    bsseq = []
    for i in range(upto_number+1):
        bsseq.append(get_baum_sweet_binary(i))
    return bsseq

# return b_n = 1 if no consecutive zeros of odd numbers
def get_baum_sweet_binary(number):
  #True if there is only consecutive zeros of even numbers
  is_count_even = True

  if number in (0,1):
    return 1
  else:
    dividend = number
    while True:
        #get next binary digit(remainder) by dividing 2, begin from the ones, go through tens, hundreds etc.
        quotient, remainder = divmod(dividend, 2)

        #if next is 1, a zero block end occurs, so check if no odd count
        if remainder == 0:
            is_count_even = not is_count_even
        else: #rem == 1
            if quotient > 0 and is_count_even is True:
                pass
            elif quotient > 0 and is_count_even is False:
                return 0
            else: #at the last digit can be either even or odd
                return int(is_count_even)

        dividend = quotient # continue dividing by 2 for next iteration

my_list = get_baum_sweet_sequence(21)
print(my_list)
