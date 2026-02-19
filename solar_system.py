import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Solar System Simulation")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
YELLOW = (255, 204, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

cx, cy = WIDTH // 2, HEIGHT // 2

zoom = 1
paused = False
speed_multiplier = 1.0

planets = [
    ("Mercury", (169, 169, 169), 50, 5, 0.24),
    ("Venus", (255, 140, 0), 80, 8, 0.62),
    ("Earth", (0, 100, 255), 110, 9, 1.0),
    ("Mars", (255, 50, 50), 150, 7, 1.88),
    ("Jupiter", (210, 180, 140), 210, 18, 11.86),
    ("Saturn", (218, 165, 32), 270, 16, 29.46),
    ("Uranus", (0, 255, 255), 330, 14, 84.01),
    ("Neptune", (0, 0, 200), 390, 14, 164.8),
]

earth_speed = 0.02
planet_angles = [random.random() * 2 * math.pi for _ in planets]
planet_speeds = [earth_speed / p[4] for p in planets]

stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1,3)) for _ in range(200)]

asteroids = [random.uniform(180, 200) for _ in range(200)]
asteroid_angles = [random.uniform(0, 2*math.pi) for _ in range(200)]

font = pygame.font.SysFont("arial", 16)

running = True

while running:
    screen.fill(BLACK)

    for star in stars:
        brightness = random.randint(150,255)
        pygame.draw.circle(screen, (brightness,brightness,brightness), (star[0],star[1]), star[2])

    pygame.draw.circle(screen, YELLOW, (cx, cy), int(30 * zoom))

    for planet in planets:
        pygame.draw.circle(screen, GRAY, (cx, cy), int(planet[2] * zoom), 1)

    for i in range(len(asteroids)):
        r = asteroids[i] * zoom
        angle = asteroid_angles[i]
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        pygame.draw.circle(screen, GRAY, (int(x), int(y)), 1)

    for i, planet in enumerate(planets):
        name, color, radius, size, period = planet

        r = radius * zoom
        angle = planet_angles[i]

        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)

        pygame.draw.circle(screen, color, (int(x), int(y)), max(1, int(size * zoom)))

        if name == "Saturn":
            pygame.draw.ellipse(screen, (200,200,150),
                                (int(x - 25*zoom), int(y - 10*zoom),
                                 int(50*zoom), int(20*zoom)), 1)

        if not paused:
            planet_angles[i] += planet_speeds[i] * speed_multiplier

    y_offset = HEIGHT - 25
    x_offset = 20
    for planet in planets:
        label = font.render(planet[0], True, WHITE)
        screen.blit(label, (x_offset, y_offset))
        x_offset += 110

    if paused:
        pause_text = font.render("PAUSED", True, WHITE)
        screen.blit(pause_text, (WIDTH//2 - 40, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                zoom += 0.1
            if event.key == pygame.K_DOWN:
                zoom = max(0.2, zoom - 0.1)
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_RIGHT:
                speed_multiplier = min(5.0, speed_multiplier + 0.2)
            if event.key == pygame.K_LEFT:
                speed_multiplier = max(0.2, speed_multiplier - 0.2)

    pygame.display.update()
    clock.tick(60)

pygame.quit()