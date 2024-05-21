import pygame,asyncio
from sys import exit
from random import randint

def display_score():
    
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    
    
    
    score_surface=test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rectangle=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rectangle)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:   
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5
            
            if  obstacle_rect.bottom==300:
            
                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]
        return obstacle_list
    else:
        return []

def collision(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                global obstacle_rect_list
                
                return False
    return True
    
def player_animation():
    global player_surf, player_index
    if player_rectangle.bottom<300:
        player_surf=player_jump
    else:
        player_index+=0.1
        if player_index>=len(player_walk):
            player_index=0
        player_surf=player_walk[int(player_index)]
        
    #player walking animation if the player is on floor
    #player walking animation if the player is not on floor

pygame.init()

screen= pygame.display.set_mode((800,400))
pygame.display.set_caption('My First Game')
clock=pygame.time.Clock()
test_font=pygame.font.Font('font\Pixeltype.ttf',50)
game_active= False
start_time=0
score=0

Sky_surface=pygame.image.load('graphics/Sky.png').convert()#Sky surface
ground_surface=pygame.image.load('graphics/ground.png').convert()#ground surface
My_First_Game=test_font.render("My First Game ",False,"Black")
My_First_Game_rect=My_First_Game.get_rect(center=(400,50))
Second_tittle=test_font.render("Press Space To Play Game",False,"Black")
Second_tittle_rect=Second_tittle.get_rect(midbottom=(450,350))

#snail
snail_frame_1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()#importing snail image
snail_frame_2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()#importing snail image
snail_frame_index=0
snail_frame=[snail_frame_1,snail_frame_2]
snail_surface=snail_frame[snail_frame_index]

#Fly
fly_frame_1=pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2=pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frame_index=0
fly_frame=[fly_frame_1,fly_frame_2]
fly_surf=fly_frame[fly_frame_index]

obstacle_rect_list=[]

player_walk_1= pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()#importing player image
player_walk_2= pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()#importing player image
player_jump=pygame.image.load('graphics/player/jump.png').convert_alpha()
player_walk=[player_walk_1,player_walk_2]
player_index=0
player_surf=player_walk[player_index]

player_rectangle=player_walk_1.get_rect(midbottom=(80,300))#using rectangle to put player in

player_gravity=0
#intro screen

player_stand=pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

# Timer:

obstacle_timer=pygame.USEREVENT + 1

pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer,200)


while True:
    #Daw all our elements and update it inside while true
    for event in pygame.event.get():#pygame.event.get() gets all the event used in the and loops
        if event.type==pygame.QUIT:# event.type is used to identify if the Quit event is used Quit is synonyms to X in windows
            pygame.quit() # Closes windows
            exit()# used to immediately close loop so that it does not throw errors
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom>=300:
                    player_gravity=-20
            if event.type==pygame.KEYDOWN:
                if player_rectangle.bottom>=300:
                    if event.key==pygame.K_SPACE:
                        player_gravity=-20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                
                start_time=int(pygame.time.get_ticks()/1000)
                
        if game_active:
            if event.type==obstacle_timer and game_active:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(1000,1500),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(1000,1500),210)))
                
            if event.type==snail_animation_timer:
                if snail_frame_index==0:
                    snail_frame_index=1
                else:
                    snail_frame_index==0
                snail_surface=snail_frame[snail_frame_index]
                
            if event.type==fly_animation_timer:
                if fly_frame_index==0:
                    fly_frame_index=1
                else:
                    fly_frame_index=0
                fly_surf=fly_frame[fly_frame_index]
                
            
                
    
    
    # pygame.draw.rect(screen,'#c0e8ec',score_rect)
    # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    
    if game_active:
        # screen.blit(score_surface,score_rect)
        screen.blit(Sky_surface,(0,0))#blit=block image transfer- helps to put one surface on another
        screen.blit(ground_surface,(0,300))
        score=display_score()
        # snail_rectangle.x-=3.5
        # if snail_rectangle.right<=0:
        #     snail_rectangle.left=800
        # screen.blit(snail_surface,snail_rectangle)
        
        #player:
        player_gravity+=1
        player_rectangle.y+=player_gravity
        if player_rectangle.bottom>=300:
            player_rectangle.bottom=300
        
        player_animation()
        screen.blit(player_surf,player_rectangle)
        #obstacle MOvement
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        
        # collision:
        game_active=collision(player_rectangle,obstacle_rect_list)
        
    else:
        
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rectangle.midbottom=(80,300)
        player_gravity=0
        Score_message=test_font.render(f'Your Score is {score}',False,'Black')
        Score_message_rect=Score_message.get_rect(center=(400,330))
        screen.blit(My_First_Game,My_First_Game_rect)
        if score==0:
            screen.blit(Second_tittle,Second_tittle_rect)
        else:
            screen.blit(Score_message,Score_message_rect)
        
        
    pygame.display.update()
    clock.tick(60)
    
