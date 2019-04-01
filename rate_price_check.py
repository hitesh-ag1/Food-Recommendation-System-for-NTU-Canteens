def rate_check(rating_str):
    try:
        rating=int(rating_str)
        if rating<1 or rating>5:
            return ("Please enter a rating only between 0 and 5!")
        elif rating_str == "":
            return ("Please enter a rating!")
        else:
            return rating                              
    except ValueError:
        return ("Please enter an Integral rating!")

def price_check(price):
    try:        
        price = price.split("-")
        min_p = int(price[0])
        max_p = int(price[1])
        if min_p>=max_p:
            return ("Maximum price must be greater than minimum Price!")
            
        elif min_p<1 or max_p>26:
            return ("Price range should be inclusive and between $1 and $26!")
        elif price == "":
            return ("Please enter a price range!")
        else:
            return min_p,max_p
    except IndexError:
          return ("Please enter price in Proper format! e.g: 3-4")
          
    except ValueError:
          return ("Enter only integral price in the right format! e.g: 3-4")
    
