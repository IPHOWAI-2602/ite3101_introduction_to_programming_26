def hotel_cost(nights: int) -> int:
    return 140 * nights


def plane_ride_cost(city: str) -> int:
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def finish_game(score): 
  tickets = 10 * score 
  if score >= 10: 
    tickets += 50 
  elif score >= 7: 
    tickets += 20 
  return tickets
