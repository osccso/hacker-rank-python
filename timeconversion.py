def timeConversion(s):
  ampm = s[-2]+s[-1]
  hours = int(s[0:2])
  minutes = s[3:5]
  seconds = s[6:8]
  
  if ampm == 'PM' and hours != 12:
    hours += 12
    
  if ampm == 'AM' and hours == 12:
    hours = '00'
  
  hours = str(hours)
  
  result = hours+':'+minutes+':'+seconds
  
  return result  
    