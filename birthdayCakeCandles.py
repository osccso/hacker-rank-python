def birthdayCakeCandles(candles):
  #find the max value (tallest candle)
  tallest = max(candles)
  #marking tallest candles
  marked = [num == tallest for num in candles]
  #counting them
  count = 0
  for item in marked:
    if item :
      count += 1
  return count