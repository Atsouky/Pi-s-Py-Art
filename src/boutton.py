import pygame

class Boutonsprite():
    def __init__(self, x, y, image, scale):
        image = pygame.image.load(image)
        width = image.get_width()
        height = image.get_height()
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                self.clicked = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        
        
        screen.blit(self.image, self.rect)
        return action
    
    
class Bouton():
    def __init__(self, x , y , w , h, txt , colo , colo1  ):
        
        self.x = x
        self.y = y
        self.color = colo
        self.color1 = colo1
        self.width = w
        self.height = h
        self.txt = txt
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
        self.clicked = False
        
    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font('freesansbold.ttf', 20)

        txt = font.render(self.txt, True, self.color1)

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(txt, (self.x, self.height // 3 + self.y))
        return action
    
    
import pygame

class Checkbox:
    def __init__(self, x, y, width, height, label, color, checked=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.label = label
        self.checked = checked
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        if not screen:
            raise ValueError("The screen parameter cannot be None")

        try:
            if self.checked:
                pygame.draw.rect(screen, (255, 0, 0), self.rect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

            font = pygame.font.Font(None, 36)
            text = font.render(self.label, True, (255, 255, 255))
            screen.blit(text, (self.x, self.y))

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.rect.collidepoint(mouse_pos) and not self.clicked:
                if mouse_pressed[0] == 1:
                    self.clicked = True
                    self.checked = not self.checked

            if mouse_pressed[0] == 0:
                self.clicked = False

            return self.checked
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return self.checked

    
class TextInput:
    def __init__(self, x, y, width, height, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ''
        self.active = False
        self.font_size = font_size

    def draw(self, screen):
        color = (255, 255, 255) if self.active else (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect)
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def analyse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        return self.text
    
    
class Slider:
    def __init__(self, x, y, width, min_value, max_value, initial_value):
        self.rect = pygame.Rect(x, y, width, 10)  
        self.knob_radius = 10  
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.dragging = False

    def update(self, screen, event=None):
        if event:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                knob_x = self.rect.x + (self.value / self.max_value) * self.rect.width
                if abs(mouse_x - knob_x) <= self.knob_radius and abs(mouse_y - self.rect.y) <= self.knob_radius:
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False

        if self.dragging:
            mouse_x, _ = pygame.mouse.get_pos()
            self.value = min(max((mouse_x - self.rect.x) / self.rect.width * self.max_value, self.min_value), self.max_value)

        pygame.draw.rect(screen, (200, 200, 200), self.rect) 
        knob_x = self.rect.x + (self.value / self.max_value) * self.rect.width
        pygame.draw.circle(screen, (0, 0, 255), (int(knob_x), self.rect.y + self.rect.height // 2), self.knob_radius) 

        font = pygame.font.SysFont(None, 30)
        value_text = font.render(f"Value: {int(self.value)}", True, (0, 0, 0))
        screen.blit(value_text, (self.rect.centerx - value_text.get_width() // 2, self.rect.top - 30))

    def get_value(self):
        return self.value