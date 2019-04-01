import pygame
import operator
import pygame, sys
from pygame.locals import *
def main_map():
      pygame.init()

      width=900;
      height=700
      screendimension = pygame.display.set_mode((width, height ))
      pygame.display.set_caption('NTU map')
      image = pygame.image.load("images/NTU Campus4.png").convert()
       
      x = 0; # x coordnate of image
      y = 0; # y coordinate of image
      screendimension.blit(image ,  (x,y)) # paint to screen
      pygame.display.flip() # paint screen one time

      graphmap = {'Nanyang_Cres/Walk':{'Hall_12_Busstop':140,'Hall_16':155},
                  'Hall_12_Busstop':{'Nanyang_Cres/Walk':140,'Hall_13':55,'Hall_15_Busstop':210},
                  'Hall_13':{'Hall_12_Busstop':55,'Hall_14':170,'Hall_16':200},
                  'Hall_15_Busstop':{'Hall_12_Busstop':210,'Hall_14':55,'Tamarind':350},
                  'Hall_14':{'Hall_13':170,'Hall_15_Busstop':55},
                  'Hall_16':{'Nanyang_Cres/Walk':155,'Hall_13':200,'NTUitive_Roundabout':190},
                  'Tamarind':{'Hall_15_Busstop':350,'Graduate_Hall_Busstop':195,'Hall_11':205},
                  'Graduate_Hall_Busstop':{'Tamarind':195,'Hall_11':95,'Northhill_Roundabout':215},
                  'Hall_11':{'Tamarind':205,'Graduate_Hall_Busstop':95,'Hall_11_Busstop':90},
                  'Northhill_Roundabout':{'Graduate_Hall_Busstop':215,'Hall_11_Busstop':155,'Northhill':95,'Nanyang_Cres_Housing':450},
                  'Hall_11_Busstop':{'Hall_11':90,'Northhill_Roundabout':155,'Northhill':115,'Ananda_Kitchen':100,'Nanyang_Ave':170},
                  'Northhill':{'Hall_11_Busstop':115,'Northhill_Roundabout':95,'Ananda_Kitchen':65},
                  'Ananda_Kitchen':{'Northhill':65,'Hall_11_Busstop':115,'Nanyang_Ave':140},
                  'Nanyang_Ave':{'Hall_11_Busstop':175,'Ananda_Kitchen':140,'Hall_9':165},
                  'Nanyang_Cres_Housing':{'Northhill_Roundabout':450,'Lien_Ying_Chow_Dr':600,'Crespion_Roundabout':475},
                  'Hall_9':{'Nanyang_Ave':165,'ADM_Roundabout':235},
                  'ADM_Roundabout':{'NTUitive_Roundabout':350,'MSE_Carpark':320,'Hall_9':235,'Nanyang_Hill/Student_Walk':140},
                  'NTUitive_Roundabout':{'Hall_16':190,'LWN_Busstop':215,'LWN_Library':240,'ADM_Roundabout':350},
                  'LWN_Busstop':{'NTUitive_Roundabout':215,'North_Spine':100},
                  'North_Spine':{'LWN_Busstop':100,'LWN_Library':115},
                  'LWN_Library':{'North_Spine':115,'NTUitive_Roundabout':240,'MSE_Carpark':285,'Nanyang_Auditorium':300},
                  'MSE_Carpark':{'LWN_Library':285,'ADM_Roundabout':320},
                  'Nanyang_Auditorium':{'SBS_Busstop':170,'WeeKimWee_Busstop':255,'LWN_Library':300,'South_Spine':330,'Quad_Cafe':80},
                  'Quad_Cafe':{'SBS_Busstop':160,'Nanyang_Auditorium':80},
                  'South_Spine':{'WeeKimWee_Busstop':360, 'Nanyang_Auditorium':330,'Innovation_Centre':150,'SPMS_Busstop':360},
                  'SPMS_Busstop':{'South_Spine':360,'Einvar_Pte':300},
                  'Einvar_Pte':{'SPMS_Busstop':300,'Innovation_Centre':420},
                  'Innovation_Centre':{'Einvar_Pte':420,'South_Spine':150,'Chinese_Heritage_Centre':220},
                  'Chinese_Heritage_Centre':{'Innovation_Centre':220,'Hall_5_Busstop':230},
                  'Hall_5_Busstop':{'Chinese_Heritage_Centre':230,'Nanyang_Drive':200},
                  'Nanyang_Drive':{'Hall_1':130,'Hall_5_Busstop':200,'Crespion':150,'Crespion_Roundabout':280},
                  'Crespion_Roundabout':{'Nanyang_Drive':280,'Nanyang_Cres_Housing':475,'Crespion':180},
                  'Crespion':{'Crespion_Roundabout':180,'Nanyang_Drive':150,'Hall_1':115,'Lien_Ying_Chow_Dr':210},
                  'Hall_1':{'Crespion':115,'Nanyang_Drive':130,'Lien_Ying_Chow_Dr':170},
                  'Lien_Ying_Chow_Dr':{'Hall_1':170,'Crespion':210,'Nanyang_Cres_Housing':600,'Hall_2':120},
                  'Hall_2':{'Lien_Ying_Chow_Dr':120,'Nanyang_Hill/Student_Walk':110},
                  'Nanyang_Hill/Student_Walk':{'Hall_2':110,'ADM_Roundabout':140},
                  'SBS_Busstop':{'Nanyang_Auditorium':170, 'Quad_Cafe':160},
                  'WeeKimWee_Busstop':{'Nanyang_Auditorium':255, 'South_Spine':360}}

      Location = { 'Northhill': (709,294),
                   'Ananda_Kitchen': (687,291),
                   'Hall_11':(689,242),
                   'Hall_9': (591,285),
                   'Hall_14': (504,198),
                   'Hall_13': (457,170),
                   'Hall_16': (399,240),
                   'Hall_1': (479,446),
                   'Hall_2': (451,556),
                   'Tamarind': (633,190),
                   'Crespion': (495,562),
                   'Quad_Cafe': (202,338),
                   'North_Spine': (270,288),
                   'South_Spine': (218,495) }

      Locationnode = {   'Northhill': (709,294),
                         'Ananda_Kitchen': (687,291),
                         'Hall_11':(689,242),
                         'Hall_9': (591,285),
                         'Hall_14': (504,198),
                         'Hall_13': (457,170),
                         'Hall_16': (399,240),
                         'Hall_1': (479,446),
                         'Hall_2': (451,556),
                         'Tamarind': (633,190),
                         'Crespion': (495,562),
                         'Quad_Cafe': (202,338),
                         'North_Spine': (270,288),
                         'South_Spine': (218,495),
                         'Nanyang_Cres/Walk': (385,160),
                         'Hall_12_Busstop': (430,152),
                         'Hall_15_Busstop': (514,156),
                         'Graduate_Hall_Busstop': (715,205),
                         'Northhill_Roundabout': (737,280),
                         'Hall_11_Busstop': (694,274),
                         'Nanyang_Ave': (634,290),
                         'Nanyang_Cres_Housing': (678,450),
                         'ADM_Roundabout': (494,358),
                         'NTUitive_Roundabout': (384,288),
                         'LWN_Busstop': (316,265),
                         'LWN_Library': (321,294),
                         'MSE_Carpark': (383,398),
                         'Nanyang_Auditorium': (208,374),
                         'SPMS_Busstop': (164,485),
                         'Einvar_Pte': (126,540),
                         'Innovation_Centre': (248,536),
                         'Chinese_Heritage_Centre': (297,520),
                         'Hall_5_Busstop': (400,594),
                         'Nanyang_Drive': (457,592),
                         'Crespion_Roundabout': (546,591),
                         'Lien_Ying_Chow_Dr': (467,478),
                         'Nanyang_Hill/Student_Walk': (500,408) }

      redline = {'LWN_Library':1,
                 'SBS':2,
                 'WKWSCI':3,
                 'Hall_7':4,
                 'Innovation_Centre':5,
                 'Hall_4':6,
                 'Hall_1':7,
                 'Hall_2':8,
                 'Hall_8_9':9,
                 'Hall_11':10,
                 'Grad_Hall':11,
                 'Nanyang_Crescent_Hall':12,
                 'Hall_12_13':13 }

      redstop = {'LWN_Library':(319,273),
                 'SBS':(172,317),
                 'WKWSCI':(112,410),
                 'Hall_7':(125,538),
                 'Innovation_Centre':(246,534),
                 'Hall_4':(403,591),
                 'Hall_1':(466,558),
                 'Hall_2':(483,459),
                 'Hall_8_9':(565,326),
                 'Hall_11':(695,278),
                 'Grad_Hall':(713,206),
                 'Nanyang_Crescent_Hall':(635,178),
                 'Hall_12_13':(432,156) }

      blueline = {    'Opp_LWN_Library':1,
                      'Opp_Hall_3_16':2,
                      'Opp_Hall_14_15':3,
                      'Opp_Nanyang_Crescent_Hall':4,
                      'Opp_Hall_10_11':5,
                      'Opp_Hall_8':6,
                      'Hall_6':7,
                      'Opp_Hall_4':8,
                      'Opp_Innovation_Centre':9,
                      'Opp_SPMS':10,
                      'Opp_WKWSCI':11,
                      'Opp_CEE':12}

      bluestop = {    'Opp_LWN_Library':(317,265),
                      'Opp_Hall_3_16':(389,202),
                      'Opp_Hall_14_15':(499,151),
                      'Opp_Nanyang_Crescent_Hall':(634,174),
                      'Opp_Hall_10_11':(695,277),
                      'Opp_Hall_8':(556,341),
                      'Hall_6':(475,469),
                      'Opp_Hall_4':(378,588),
                      'Opp_Innovation_Centre':(240,552),
                      'Opp_SPMS':(166,490),
                      'Opp_WKWSCI':(105,406),
                      'Opp_CEE':(200,270) }

      newlocation = {}

      def message_display(text):
            '''
            center = (900,0)
            largeText = pygame.font.SysFont('arial',50)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = ((100),(100))
            screendimension.blit(TextSurf, TextRect)
            pygame.display.update()
            '''
            pygame.display.set_caption('NTU map')
             
            basicfont = pygame.font.SysFont(None, 35)
            text = basicfont.render(text, True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screendimension.get_rect().centerx
            textrect.centery = screendimension.get_rect().centery
             
            screendimension.fill((0, 0, 0))
            screendimension.blit(text, (900,0))
             
            pygame.display.update()

      def mouseclick():
            running = True
            while running:
                  mouse_pos = pygame.mouse.get_pos()
                  if (Location['Northhill'][0]-20<mouse_pos[0]<(Location['Northhill'][0]+10)) and (Location['Northhill'][1]-20<mouse_pos[1]<(Location['Northhill'][1]+20)):
                      screendimension.blit(pygame.image.load("images/NORTHHILL.png"), ((Location['Northhill'][0]-22), (Location['Northhill'][1]-3)))
                  elif (Location['Ananda_Kitchen'][0]-20<mouse_pos[0]<(Location['Ananda_Kitchen'][0]+20)) and (Location['Ananda_Kitchen'][1]-20<mouse_pos[1]<(Location['Ananda_Kitchen'][1]+20)):
                      screendimension.blit(pygame.image.load("images/ANANDA.png"), ((Location['Ananda_Kitchen'][0]), (Location['Ananda_Kitchen'][1])))
                  elif (Location['Hall_11'][0]-10<mouse_pos[0]<(Location['Hall_11'][0]+20)) and (Location['Hall_11'][1]-20<mouse_pos[1]<(Location['Hall_11'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL11.png"), ((Location['Hall_11'][0]), (Location['Hall_11'][1])))
                  elif (Location['Hall_9'][0]-20<mouse_pos[0]<(Location['Hall_9'][0]+20)) and (Location['Hall_9'][1]-20<mouse_pos[1]<(Location['Hall_9'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL9.png"), ((Location['Hall_9'][0]), (Location['Hall_9'][1])))
                  elif (Location['Hall_14'][0]-20<mouse_pos[0]<(Location['Hall_14'][0]+20)) and (Location['Hall_14'][1]-20<mouse_pos[1]<(Location['Hall_14'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL14.png"), ((Location['Hall_14'][0]), (Location['Hall_14'][1])))
                  elif (Location['Hall_13'][0]-20<mouse_pos[0]<(Location['Hall_13'][0]+20)) and (Location['Hall_13'][1]-20<mouse_pos[1]<(Location['Hall_13'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL13.png"), ((Location['Hall_13'][0]), (Location['Hall_13'][1])))
                  elif (Location['Hall_16'][0]-20<mouse_pos[0]<(Location['Hall_16'][0]+20)) and (Location['Hall_16'][1]-20<mouse_pos[1]<(Location['Hall_16'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL16.png"), ((Location['Hall_16'][0]), (Location['Hall_16'][1])))
                  elif (Location['Hall_1'][0]-20<mouse_pos[0]<(Location['Hall_1'][0]+20)) and (Location['Hall_1'][1]-20<mouse_pos[1]<(Location['Hall_1'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL1.png"), ((Location['Hall_1'][0]), (Location['Hall_1'][1])))
                  elif (Location['Hall_2'][0]-20<mouse_pos[0]<(Location['Hall_2'][0]+20)) and (Location['Hall_2'][1]-20<mouse_pos[1]<(Location['Hall_2'][1]+20)):
                      screendimension.blit(pygame.image.load("images/HALL2.png"), ((Location['Hall_2'][0]), (Location['Hall_2'][1]-74)))
                  elif (Location['Tamarind'][0]-20<mouse_pos[0]<(Location['Tamarind'][0]+20)) and (Location['Tamarind'][1]-20<mouse_pos[1]<(Location['Tamarind'][1]+20)):
                      screendimension.blit(pygame.image.load("images/TAMARIND.png"), ((Location['Tamarind'][0]), (Location['Tamarind'][1])))
                  elif (Location['Crespion'][0]-20<mouse_pos[0]<(Location['Crespion'][0]+20)) and (Location['Crespion'][1]-20<mouse_pos[1]<(Location['Crespion'][1]+20)):
                      screendimension.blit(pygame.image.load("images/CRESPION.png"), ((Location['Crespion'][0]), (Location['Crespion'][1]-80)))
                  elif (Location['Quad_Cafe'][0]-20<mouse_pos[0]<(Location['Quad_Cafe'][0]+20)) and (Location['Quad_Cafe'][1]-20<mouse_pos[1]<(Location['Quad_Cafe'][1]+20)):
                      screendimension.blit(pygame.image.load("images/QUAD.png"), ((Location['Quad_Cafe'][0]), (Location['Quad_Cafe'][1])))
                  elif (Location['North_Spine'][0]-20<mouse_pos[0]<(Location['North_Spine'][0]+20)) and (Location['North_Spine'][1]-20<mouse_pos[1]<(Location['North_Spine'][1]+20)):
                      screendimension.blit(pygame.image.load("images/NS.png"), ((Location['North_Spine'][0]), (Location['North_Spine'][1])))
                  elif (Location['South_Spine'][0]-20<mouse_pos[0]<(Location['South_Spine'][0]+20)) and (Location['South_Spine'][1]-20<mouse_pos[1]<(Location['South_Spine'][1]+20)):
                      screendimension.blit(pygame.image.load("images/KOUFU.png"), ((Location['South_Spine'][0]), (Location['South_Spine'][1]-100)))
                  else:
                      screendimension.blit(image,(0,0))
                      print_loc(Location)
                  pygame.display.update()
                  
                  for event in pygame.event.get():   
                        if event.type == pygame.QUIT:
                              running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:# Set the x, y postions of the mouse click
                              x, y = event.pos
                              print("(",x,",",y,")")
                              return x,y
                              running = False

      def print_loc(locloc):
            locatcord = list(locloc.values())
            for i in locatcord:
                  screendimension.blit(pygame.image.load("images/white.png"), (i[0] - 10,i[1] - 20))
                  pygame.display.update()

      def printblue(locloc):
              locatcord = list(locloc.values())
              for i in locatcord:
                  screendimension.blit(pygame.image.load("images/blue.png"), (i[0] - 10,i[1] - 20))
                  pygame.display.update()

      def printred(locloc):
              locatcord = list(locloc.values())
              for i in locatcord:
                  screendimension.blit(pygame.image.load("images/red.png"), (i[0] - 10,i[1] - 20))
                  pygame.display.update()
                  
      def bubblesort(alist):
          for passnum in range (len(alist) - 1):
              for i in range(len(alist) - passnum - 1):
                  if alist[i] > alist[i+1]:
                      temp = alist[i]
                      alist[i] = alist[i +1]
                      alist[i + 1] = temp

      def mappingdist(Location,x,y):
            newlocation.clear()
            if image.get_rect().collidepoint(x, y):
                  locatcord = list(Location.values())
                  diff = []
                  for i in locatcord:
                    u,v = i
                    diffx = u - x
                    diffy = v - y
                    moddiffx = abs(diffx)
                    moddiffy = abs(diffy)
                    #print(moddiffx) #checking
                    totaldiff = int(moddiffx + moddiffy)
                    for key, element in Location.items():
                          if element == i:
                            value = totaldiff
                            newlocation[key] = value;
                    diff.append(totaldiff)
                  bubblesort(alist = diff)
                  s = [(k, newlocation[k]) for k in sorted(newlocation, key=newlocation.get, reverse=False)]
                  return s
                      
      def dijkstra(graph,start,goal):
          #copy all the points in the graph
          initialpoint = graph.copy()
          #empty dictionary for the distance
          dist= {}
          #empty dictionary for the points that has passed
          passpoint = {}
          #empty list for the path that has been taken
          path = []
          #define infinity
          infinity = 999999
          #make the distance to all other location be infinity
          for point in initialpoint:
              dist[point] = infinity
              #print(dist)
          #make the distance from the start location be 0
          dist[start] = 0

          while initialpoint:
              #to restart at every loop for the minpoint to be zero
              minpoint = None
              for point in initialpoint:
                  if minpoint is None:
                      minpoint = point #set minpoint as the first point
                  elif dist[point] < dist[minpoint]:
                      minpoint = point
              for nextpoint, length in graph[minpoint].items():#for paths that are connected to minpoint
                  alternatepath = length + dist[minpoint]
                  if alternatepath < dist[nextpoint]: #shorter path found
                      dist[nextpoint] = alternatepath #replace with the alternative path
                      passpoint[nextpoint] = minpoint #adding to passpoint the point that have been passed
              initialpoint.pop(minpoint) #to removed the used path from the dictionary

          currentpoint = goal #finding the path taken
          while currentpoint != start:
              try:
                  path.append(currentpoint) #adding the point to the path
                  currentpoint = passpoint[currentpoint] #replacing thr currentpoint variable with points that has been passed
              except KeyError:
                  print("Path could not be found :(")
                  break
          path.append(start)
          path.reverse()
          if dist[goal] != infinity: #make sure if no path is found then print message
              print("Shortest distance from " + start + " to " + goal + " is from " + str(path))
              totaldist = []
              numpass = len(path)
              for element in range(0,numpass-1):
                  distvalue = graphmap[path[0]][path[1]]
                  #print(distvalue)
                  totaldist.append(distvalue)
                  #print(totaldist)
                  path.remove(path[0])
                  sumtotaldist = sum(totaldist)
              print("Approximate distance: " , (sumtotaldist) , "meters")

      def nearestdist(location,x,y):
              s = []
              newlocation.clear()
              locatcord = list(location.values())
              #print(locatcord)
              diff = []
              for i in locatcord:
                      u,v = i
                      diffx = u - x #finding difference
                      diffy = v - y
                      moddiffx = abs(diffx) #modulus the values to get positive
                      moddiffy = abs(diffy)
                      #print(moddiffx) #checking
                      totaldiff = int(moddiffx + moddiffy)
                      for key, element in location.items():
                          if element == i:
                              value = totaldiff
                              newlocation[key] = value;
              diff.append(totaldiff) #add the diff to the list of diff
              bubblesort(alist = diff) #sort the diff
              s = [(k, newlocation[k]) for k in sorted(newlocation, key=newlocation.get, reverse=False)]
              #print(s)
              #print(locatcord)
              return s[0][0] #(only return the value if need for dijkstra)
              
      def displacement(goal,x,y):
          KeepLooping = True
          while KeepLooping:
              for event in pygame.event.get():
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      x, y = event.pos
                      if image.get_rect().collidepoint(x, y):
                          #print('clicked on image')
                          #print("(",x,",",y,")")
                          g1 = nearestdist(goal,x,y)
                          return g1
                          #print(g1)
                          KeepLooping = False

      def displacementstart(goal,x,y):
            if image.get_rect().collidepoint(x, y):
                          #print('clicked on image')
                          #print("(",x,",",y,")")
                          g1 = nearestdist(goal,x,y)
                          return g1
                          #print(g1)
                          KeepLooping = False

      def getbus(x,y):
            printblue(bluestop)
            printred(redstop)
            print("Please enter where you want to go(double click)")
            goalblue = displacement(bluestop,x,y)
            goalred = displacement(redstop,x,y)
            print("Please enter where you are(double click)")
            startblue = displacementstart(bluestop,x,y)
            startred = displacementstart(redstop,x,y)
            #print(goalred,startred)
            goalr = int(redline[goalred])
            startr = int(redline[startred])
            goalb = int(blueline[goalblue])
            startb = int(blueline[startblue])
            if goalb < startb:
                  nostopb = goalb - startb 
            elif goalb > startb:
                  nostopb = goalb - startb 
            if goalr < startr:
                  nostopr = goalr - startr + 1
            elif goalr > startr:
                  nostopr = goalr - startr + 1
            #print(nostopb)
            #print(nostopr)
            mod_nostopr = abs(nostopr)
            mod_nostopb = abs(nostopb)
            print("Option 1: Campus Red")
            print("Please head to busstop ", startred, " and take the Campus Red for ", mod_nostopb, "stops, alighting at busstop ", goalred)
            print("or")
            print("Option 2: Campus Blue")
            print("Please head to busstop ", startblue, " and take the Campus Blue for ", mod_nostopr, "stops, alighting at busstop ", goalblue)


      def mapinterface():
            print("Please select your location:")
            x,y = mouseclick()
            print("Welcome to NTU food recomendation,")
            while True:
                  print("Input 1 to find canteen nearest to you" +
                        "\nInput 2 to find shortest route walking to the canteen of your choice"
                        "\nInput 3 to find bus route to the canteen of your choice "
                        "\nInput 4 to Quit")
                  choice = input("What would you like to do today:")
                  choice_int = int(choice)
                  if choice_int == 1:
                        print("Please click your location on the image")
                        s = mappingdist(Location,x,y)
                        print("The coordinates you are in are","(",x,",",y,")")
                        print("The closest Restaurant by displacement for you is ", s[0][0], " with distance ", s[0][1]," \nfollowed by ", s[1][0]," with distance ", s[1][1], " \nfollowed by ", s[2][0], " with distance ", s[2][1],)

                  elif choice_int == 2:
                        print("Where would you like to visit?")
                        print("1.Hall_1\n2.Hall_2\n3.Hall_9\n4.Hall_11\n5.Hall_13\n6.Hall_14\n7.Hall_16\n8.Ananda_Kitchen"+
                              "\n9.Crespion\n10.Northhill\n11.Tamarind\n12.North_Spine\n13.Quad_Cafe\n14.South_Spine")
                        Canteen = {1:'Hall_1', 2:'Hall_2', 3:'Hall_9', 4:'Hall_11', 5:'Hall_13', 6:'Hall_14', 7:'Hall_16', 8:'Ananda_Kitchen',
                                   9:'Crespion', 10:'Northhill', 11:'Tamarind', 12:'North_Spine', 13:'Quad_Cafe', 14:'South_Spine'}

                        endno = input("Enter where you want to go(number): ")
                        endnoint = int(endno)
                        if endnoint in range(1,15):
                              print("Please click your location on the image")
                              s = mappingdist(Location,x,y)
                              t = s[0][0]
                              startpos = t
                              print("Your nearest landmark is: " + startpos)
                              endpos = Canteen[endnoint]
                              dijkstra(graphmap, startpos, endpos)
                        else:
                              print("Please enter a number between 1 and 14")
                  elif choice_int == 3:
                        getbus(x,y)
                  elif choice_int == 4:
                        break
                        pygame.quit()
                  
      message_display("Welcome to NTU food recomendation:")
      mapinterface()
