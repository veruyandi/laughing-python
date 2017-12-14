import time
#https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
#A talking clock takes a 24-hour time and translates it into words.
#input: 12:05
#output: It's twelve oh five pm
def talking_clock(hour24format):
  #define a dictionary to store clock numbers in words
  number2word = {0: 'oh', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', \
				20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty' }
  try:
    #parse the input time string into a time struct
    my_time = time.strptime(hour24format, '%H:%M')

  except:
    print('Error: Invalid hour format, please enter a 24-hour time format \'HH:MI\'')
    quit()

  #time translation into words is composed of three variables: hour_part, minute_part, am_pm_part
  #get hour in 12-hour format
  hour, min = my_time[3]%12, my_time[4]  #get 3-tm_hour, 4-tm_min from time_struct

  #build the hour part of the translation
  if hour == 0:
    hour_part = number2word[12] # `twelve hour` for both 00:00 or 12:00
  else:
    hour_part = number2word[hour]

  #build the minute part of the translation
  if min == 0:
    min_part = ' ' #min is empty when it is 2 pm e.g. -> It's two pm
  elif min >= 10 and min < 20 :
    min_part = ' ' + number2word[min] + ' '
  else: # 0 < min < 10 or 20 < min < 60
    tens, ones = divmod(min,10) #separate decimal places of the minute by dividing 10
    if ones == 0:
      min_part = ' ' + number2word[tens*10] + ' '
    else: # 0 < ones < 10
      min_part = ' ' + number2word[tens*10] + ' ' + number2word[ones] + ' '

  #check if am or pm
  am_pm_part = time.strftime('%p', my_time).lower()

  #concatenate all parts to obtain translation
  translation = 'It\'s '  + hour_part + min_part + am_pm_part
  return translation

for hour in range(24):
    for min in range(60):
        #input_time = str(hour) + ':' + str(min)
        hour24format = '%02d:%02d' % (hour, min)
        #print(hour24format)
        print(hour24format, '-----' , talking_clock(hour24format))


