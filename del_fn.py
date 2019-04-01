import pandas
from database_importing import dict_create



def delet(can, dish):
      di = dict_create()
      for i in range(len(di)):
            if (di[i]['Canteen'] == can) and (di[i]['Dish'] == dish):
                  del di[i]

      dl = pandas.DataFrame()

      for i in range(len(di)):
            try:
                  dz = pandas.DataFrame(data=di[i], index=[i])
                  dl = dl.append(dz)
            except KeyError:
                  continue
            
      dl.to_excel('Canteen.xlsx', index = False)


            
      
