def otpt(search_type,search_file,userinput):
    distinct_val = []
    if search_type == "Canteen":
        first_str = "At "
        last_str = " you can find \n"
    elif search_type == "Dish":
        first_str = "You can find "
        last_str = " at \n"
    elif search_type == "Cuisine":
        first_str = "In " 
        last_str = " cuisine, you can find: \n"
    output_str = ""    
    output_str += first_str
    output_str += userinput
    output_str += last_str

    for i in range(1,len(search_file)):
        if search_file[i][0] in distinct_val:
              continue
        else:
              output_str += str(i)
              output_str += ") "
              output_str += search_file[i][0]
              if search_type == "Cuisine":
                  output_str += " at "
                  output_str += search_file[i][3]
              output_str += ", rating: "
              output_str += search_file[i][1]
              output_str += ", price: $"
              output_str += search_file[i][2]
              output_str += "\n"
              distinct_val.append(search_file[i][0])
              
    output_str += "and "
    output_str += str(len(search_file))
    output_str += ") "
    output_str += search_file[len(search_file)][0]
    if search_type == "Cuisine":
                  output_str += " at "
                  output_str += search_file[i][3]
    output_str += ", rating: "
    output_str += search_file[len(search_file)][1]
    output_str += ", price: $"
    output_str += search_file[len(search_file)][2]
    output_str += "."

    return output_str
