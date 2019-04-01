import math
from rate_price_check import rate_check
from rate_price_check import price_check
from database_importing import dict_create
from output_str_fin import otpt

di = dict_create()

def match_code(i,min_p,max_p,rating,tpe):
      outpt = {}
      if min_p<= (di[i]['Price'])<= max_p:
            if di[i]['Rating']>= rating:
                  if tpe == "Dish":
                        outpt[len(outpt)+1] = [di[i]['Canteen'], str(di[i]['Rating']), str(di[i]['Price'])]
                  elif tpe == "Canteen":
                        outpt[len(outpt)+1] = [di[i]['Dish'],  str(di[i]['Rating']), str(di[i]['Price'])]
                  elif tpe == "Cuisine":
                        outpt[len(outpt)+1] = [di[i]['Dish'],  str(di[i]['Rating']), str(di[i]['Price']), di[i]['Canteen']]
      return outpt

def matching_code(i,min_p,max_p,rating,tpe, search_type, each_chr):
      if min_p<= (di[i]['Price'])<= max_p:
            if di[i]['Rating']>= rating:
                  match = 0
                  spl = list(di[i][search_type])
                  if len(spl)< len(each_chr):
                        maxi= len(spl)
                  else:
                        maxi = len(each_chr)
                  for x in range(maxi):
                        if each_chr[x] == spl[x]:
                              match +=1
                  if len(each_chr)>5:
                        if match>=math.floor(0.7*len(each_chr)):
                              matching.append(di[i][search_type])
                  else:
                        if match>=3:
                              matching.append(di[i][search_type])

def search(inpt,rating_str,price, veg, halal, search_type):
      veg = veg.upper()
      halal = halal.upper()
      if search_type == 'Dish':
            tpe = 'Dish'
      elif search_type == 'Canteen':
            tpe = 'Canteen'
      elif search_type == 'Cuisine':
            tpe = 'Cuisine'
            
      while True:
            findfood = inpt.upper()
            
            output_str=""
            rating=int(rating_str)
            distinct_match = []
            exact_match = 0
           
            rating_checked = rate_check(rating_str)

            try:
                  rating = int(rating_checked)
            except ValueError:
                  return rating_checked
            try: 
                  min_p,max_p = price_check(price)
            except ValueError:
                  return price_check(price)

                  
            matching=[]
            for i in range(0,len(di)):
                  if di[i][tpe] == findfood:
                        exact_match += 1
                        check_veg = (str(di[i]["Vegetarian"])).upper()
                        check_halal = (str(di[i]["Halal"])).upper()
                        if veg == "TRUE" and halal=="TRUE": 
                              if veg == check_veg:
                                    if halal == check_halal:                              
                                          outpt = match_code(i,min_p,max_p,rating,tpe)
                        elif veg == "TRUE" and halal=="FALSE": 
                              if veg == check_veg:                            
                                    outpt = match_code(i,min_p,max_p,rating,tpe)
                        elif veg == "FALSE" and halal=="TRUE": 
                              if halal == check_halal:                              
                                   outpt = match_code(i,min_p,max_p,rating,tpe)
                        elif veg == "FALSE" and halal=="FALSE":                            
                              outpt = match_code(i,min_p,max_p,rating,tpe)
            if outpt == None:
                  print ("None")
            if len(outpt) == 0 and exact_match != 0:
                  return "\nNo "+ tpe+ " of this choice found in the given rating and price range"
                                    
            elif len(outpt) == 0:
                  for x in range(len(di)):
                        check_veg = (str(di[x]["Vegetarian"])).upper()
                        check_halal = (str(di[x]["Halal"])).upper()
                        if veg == check_veg:
                              if halal == check_halal:                            
                                    if min_p<= (di[x]['Price'])<= max_p:
                                          if di[x]['Rating']>= int(rating):
                                                split_chr = di[x][search_type].split()
                                                for i in range(len(split_chr)):
                                                      if split_chr[i] == findfood:
                                                            matching.append(di[x][search_type])

                  each_chr = list(findfood)
                  for i in range(0, len(di)):
                        check_veg = (str(di[i]["Vegetarian"])).upper()
                        check_halal = (str(di[i]["Halal"])).upper()

                        if veg == "TRUE" and halal=="TRUE": 
                              if veg == check_veg:
                                    if halal == check_halal:
                                          matching_code(i,min_p,max_p,rating,tpe,search_type, each_chr)
                        elif veg == "TRUE" and halal=="FALSE": 
                              if veg == check_veg:
                                    matching_code(i,min_p,max_p,rating,tpe,search_type, each_chr)
                        elif veg == "FALSE" and halal=="TRUE": 
                              if halal == check_halal:
                                    matching_code(i,min_p,max_p,rating,tpe,search_type, each_chr)
                        elif veg == "FALSE" and halal=="FALSE":
                              matching_code(i,min_p,max_p,rating,tpe,search_type, each_chr)                                   

                  if len(matching) == 0:
                        return "\nNo "+tpe+" of this choice found in the given rating and price"
                        
                  else:
                        output_str += "Did you mean "
                        for i in range(len(matching)-1):
                              if matching[i] in distinct_match:
                                    continue
                              else:
                                    output_str += matching[i]
                                    output_str += ","
                                    distinct_match.append(matching[i])
                        if matching[len(matching)-1] in distinct_match:
                              output_str += "?"
                        else:     
                              output_str += "and "
                              output_str += matching[len(matching)-1]
                        return output_str
            
                    
            elif len(outpt)==1:
                  if search_type=='Canteen':
                        return ("You can find " + outpt[1][0] +" at "+ inpt + " with these specifications.")
                  elif search_type =='Dish':
                        return("You can find "+ inpt + " at " + outpt[1][0] + " with these specifications.")
                  elif search_type == 'Cuisine':
                        return ("In "+ inpt+ " cuisine, you can find "+outpt[1][0]+" at "+outpt[1][3] + " with these specifications.")

            else:
                  print ("else")
                  output_str = otpt(search_type ,outpt,inpt)
                  
                  return output_str
                  



