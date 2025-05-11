import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.timer = 0

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)

  def rotate(self, dt):
    self.rotation += (TURN_SPEED * dt)

  def update(self, dt):
    self.timer -= dt
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
      self.rotate(-dt)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      self.rotate(dt)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
      self.move(dt)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
      self.move(-dt)
    if keys[pygame.K_SPACE]:
      if self.timer > 0:
        return
      self.shoot()

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    shot = Shot(self.position.x, self.position.y)
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    shot.velocity = forward * PLAYER_SHOT_SPEED
    self.timer = PLAYER_SHOOT_COOLDOWN

