import pygame
import time
from update_btn import main
from search_by_food_btn import search_food
from search_by_canteen_btn import search_canteen
from search_by_cusine_btn import search_cuisine
from update_btn import main
from udpate_del import delete
from maps import main_map
from sort_by_rank_btn import mainrank

def mainfile():
      pygame.init()
      screen_size_x = 900
      screen_size_y = 650
      pygame.display.set_caption('NTU Food Fingers')
      screen = pygame.display.set_mode((screen_size_x,screen_size_y))

      def button_img(img, img_hover, pos_x, pos_y, task = None):
            img_pos = img.get_rect()
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (pos_x<mouse_pos[0]<(pos_x+img_pos[2])) and (pos_y<mouse_pos[1]<(pos_y+img_pos[3])):
                  screen.blit(img_hover, (pos_x, pos_y))
                  if click[0]==1 and task!= None:
                      if task=="start":
                              time.sleep(0.2)
                              third()
                              pygame.quit()
                              quit()
                      elif task=="new_entry":
                          pygame.quit()
                          main()
                          quit()
                          
                      elif task == "current_entry":
                          pygame.quit()
                          delete()
                          quit()
                          
                      elif task=="food":
                          pygame.quit()
                          search_food()
                          quit()
                          
                      elif task == "canteen":
                          pygame.quit()
                          search_canteen()
                          quit()
                          
                      elif task == "location":
                          pygame.quit()
                          main_map()
                          quit()
                          
                      elif task == "cuisine":
                          pygame.quit()
                          search_cuisine()
                          quit()

                      elif task == "first":
                            time.sleep(0.2)
                            introduction()
                            pygame.quit()
                            
                      elif task =="update":
                            time.sleep(0.2)
                            sec_page()
                            pygame.quit()
                      elif task == "rank":
                            time.sleep(0.2)
                            mainrank()
                            
                            
            else:
                  screen.blit(img, (pos_x,pos_y))

      def introduction():
            introScreenImage = pygame.image.load("images/bacl.jpeg")
            start_but=pygame.image.load("images/Picture1.png")
            start_but_big = pygame.image.load("images/Picture2.png")
            admin = pygame.image.load("images/admin.png")
            admin_hover = pygame.image.load("images/admin_hover.png")
            screen.blit(introScreenImage,(0,0))
            while True:
                  for event in pygame.event.get():      
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                  button_img(start_but,start_but_big, 1.12*screen_size_x//2, 2.8*screen_size_y//4, task = "start")
                  button_img(admin,admin_hover, screen_size_x-200, 10, task = "update")
                  pygame.display.flip()


      def sec_page():
            secscreen = pygame.image.load("images/bac.jpg")
            search_but=pygame.image.load("images/new_entry.png")
            search_but_hover=pygame.image.load("images/new_entry_hover.png")
            rec_but=pygame.image.load("images/delete_entry.png")
            rec_but_hover=pygame.image.load("images/delete_entry_hover.png")
            back_but = pygame.image.load("images/back.png")
            back_but_hover = pygame.image.load("images/back_hover.png")
            screen.blit(secscreen, (0,0))
            while True:
                  for event in pygame.event.get():      
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                  button_img(search_but,search_but_hover, screen_size_x//8.5, screen_size_y//2.7, task = "new_entry")
                  button_img(rec_but,rec_but_hover, screen_size_x//8.5, (screen_size_y//2.7)+80, task = "current_entry")
                  button_img(back_but,back_but_hover, screen_size_x//8.5, (screen_size_y//2.7)+160, task = "first")

                  pygame.display.flip()

      def third(): 
          thirdscreen = pygame.image.load("images/bac.jpg")
          search_but=pygame.image.load("images/food.png")
          search_but_hover=pygame.image.load("images/food_hover.png")
          rec_but=pygame.image.load("images/canteen.png")
          rec_but_hover=pygame.image.load("images/canteen_hover.png")
          both_but = pygame.image.load("images/location.png")
          both_but_hover = pygame.image.load("images/location_hover.png")
          no_but = pygame.image.load("images/cuisine.png")
          no_but_hover = pygame.image.load("images/cuisine_hover.png")
          back_but = pygame.image.load("images/back.png")
          back_but_hover = pygame.image.load("images/back_hover.png")
          rank_but = pygame.image.load("images/rank.png")
          rank_but_hover = pygame.image.load("images/rank_hover.png")
          screen.blit(thirdscreen, (0,0))
          while True:
                  for event in pygame.event.get():      
                        if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()                              
                  button_img(rank_but,rank_but_hover, screen_size_x//8.5, (screen_size_y//2.7)-80, task = "rank")
                  button_img(search_but,search_but_hover, screen_size_x//8.5, screen_size_y//2.7, task = "food")
                  button_img(rec_but,rec_but_hover, screen_size_x//8.5, (screen_size_y//2.7)+80, task = "canteen")
                  button_img(both_but,both_but_hover, screen_size_x//8.5, (screen_size_y//2.7)+160, task = "location")
                  button_img(no_but,no_but_hover, screen_size_x//8.5, (screen_size_y//2.7)+240, task = "cuisine")
                  button_img(back_but,back_but_hover, screen_size_x//8.5, (screen_size_y//2.7)+320, task = "first")

                  pygame.display.flip()
            
      introduction()
mainfile()
