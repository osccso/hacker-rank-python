def hurdleRace(k, height):
    max_height = max(height)
    if k >= max_height:
      return 0
    doses = max(height) - k
    return doses