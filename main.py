import pygame
import random

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Memory')
   # get the display surface
   w_surface = pygame.display.get_surface()
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play()
   # quit pygame and clean up the pygame window
   pygame.quit()


# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')

      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True

      # === game specific objects
      self.tile = Tile(self.surface)
      self.max_frames = 150
      self.frame_counter = 0
      self.image_list = self.tile.create_list()
      self.start_ticks=pygame.time.get_ticks()


      #print(self.image_list)

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.
      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.seconds=(pygame.time.get_ticks()-self.start_ticks)//1000

         #print("here",self.seconds)
         # self.tile.check()
         self.handle_events()
         self.draw()


         if self.continue_game:

            self.update()

            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         elif event.type == pygame.MOUSEBUTTONUP:
             self.tile.user_click()

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw

      self.surface.fill(self.bg_color) # clear the display surface first

      self.tile.draw_score(self.seconds)


      self.tile.check()
      self.tile.create(self.image_list)

      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update

      self.tile.move()
      self.frame_counter = self.frame_counter + 1

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check

      if self.frame_counter > self.max_frames:
         self.continue_game = False


class Tile:
   # An object in this class represents a Dot that moves

   def __init__(self, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.surface = surface
      self.current_pic = 0
      self.prev_pic = 0
      self.clicked = []
   def move(self):
      # Change the location of the Dot by adding the corresponding
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      pass

   def create_list(self):
       image_list = []

       for i in range (1,9):
           image_list.append('image{}.bmp'.format(i))
       self.image_list_init=['image0.bmp']*16
       image_list = image_list*2
       random.shuffle(image_list)
       self.image_list = image_list

       return self.image_list_init

   def create(self,image_list):
       b = [0,0]
       counter = 0

       for ele in self.image_list_init:
           image = pygame.image.load(r'{}'.format(ele))
           self.surface.blit(image, (b[0], b[1]))
           b[0]+=100
           counter+=1
           if counter % 4 ==0:
              b[1]+=100
              b[0]=0

   def draw_score(self,seconds):
       #print(self.image_list)
       seconds -= 2
       #print(seconds)
       text_color = pygame.Color('white')
       text_font = pygame.font.SysFont('Times New Roman', 98, bold=True)

       text_pos = (400, 10)
       if ('image0.bmp') in self.image_list_init:
           text_image = text_font.render(str(seconds), True, text_color)
           self.surface.blit(text_image, text_pos)
           self.final_score = seconds

       else:
           text_image = text_font.render(str(self.final_score), True, text_color)
           self.surface.blit(text_image, text_pos)

   def user_click(self):

       width, height = 500, 400
       press = pygame.mouse.get_pos()
       pressed = pygame.mouse.get_pressed()
       if(press[0]>0 and press[0]<100 and press[1]<100):
           self.pic = 1
       elif(press[0]>100 and press[0]<200 and press[1]<100):
           self.pic = 2
       elif(press[0]>200 and press[0]<300 and press[1]<100):
           self.pic = 3
       elif(press[0]>300 and press[0]<400 and press[1]<100):
           self.pic = 4
       elif(press[0]>0 and press[0]<100 and press[1]>100 and press[1]<200):
           self.pic = 5
       elif(press[0]>100 and press[0]<200 and press[1]>100 and press[1]<200):
           self.pic = 6
       elif(press[0]>200 and press[0]<300 and press[1]>100 and press[1]<200):
           self.pic = 7
       elif(press[0]>300 and press[0]<400 and press[1]>100 and press[1]<200):
           self.pic = 8
       elif(press[0]>0 and press[0]<100 and press[1]>200 and press[1]<300):
           self.pic = 9
       elif(press[0]>100 and press[0]<200 and press[1]>200 and press[1]<300):
           self.pic = 10
       elif(press[0]>200 and press[0]<300 and press[1]>200 and press[1]<300):
           self.pic = 11
       elif(press[0]>300 and press[0]<400 and press[1]>200 and press[1]<300):
           self.pic = 12
       elif(press[0]>0 and press[0]<100 and press[1]>300 and press[1]<400):
           self.pic = 13
       elif(press[0]>100 and press[0]<200 and press[1]>300 and press[1]<400):
           self.pic = 14
       elif(press[0]>200 and press[0]<300 and press[1]>300 and press[1]<400):
           self.pic = 15
       elif(press[0]>300 and press[0]<400 and press[1]>300 and press[1]<400):
           self.pic = 16
       else:
           self.pic = 0
       if self.pic in self.clicked:
           pass
       else:
           self.clicked.append(self.pic)
           #print(self.clicked)
           #print(self.pic)
           self.prev_pic = self.current_pic
           self.current_pic = self.pic

           self.prev_pic_name = self.image_list[self.prev_pic-1]
           self.current_pic_name = self.image_list[self.current_pic-1]
       # print("PREV PIC",self.prev_pic, self.image_list[self.prev_pic-1])
       # print("CURRENT PIC",self.current_pic, self.image_list[self.current_pic-1])
       # print(self.image_list)

       #print(self.clicked)
       #print(self.image_list)


       if self.pic == 0:
           pass
       else:
           self.image_list_init[self.pic-1] = self.image_list[self.pic-1]

   def check(self):
       if len(self.clicked) < 3:
           pass

       else:
           index = self.clicked[-3]
           index_second = self.clicked[-2]
           # print(self.image_list_init[index_second-1])
           # print(self.image_list_init[index-1])
           if self.image_list_init[index_second-1] == self.image_list_init[index-1]:
               # print("YESSS")
               self.prev_pic = 0
               self.current_pic = 0

           else:
               self.image_list_init[index-1] = 'image0.bmp'
               self.image_list_init[index_second-1] = 'image0.bmp'
           self.clicked=self.clicked[len(self.clicked)-4:]
main()
