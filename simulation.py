import pygame
import math
import random
import matplotlib.pyplot as plt

# VARIABLES INITIALIZED
clock = pygame.time.Clock()
simulation_started = False
temp_e = 10
e = 1
selected_ball = "blue"
selected_angle = "blue"
Displacement = 300
deceleration = 0.0
Friction = 0.0
temp_friction = 1
pygame.init()

WIDTH = 800
HEIGHT = 600
velocity1 = 1
velocity2 = -1
Vi1 = velocity1
Vi2 = velocity2
start_v1 = velocity1
start_v2 = velocity2
collided = False
mass1 = 1
mass2 = 1
Before_KE = 0
After_KE = 0
velocity1_y = 0
velocity2_y = 0
Angle1 = 0
Angle2 = 180

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Momentum Simulator")

font = pygame.font.SysFont(None, 27)

ball1_x = 400 - Displacement/2
ball2_x = 400 + Displacement/2
ball1_y = 300
ball2_y = 300

# ARROW FUNCTION
def arrow(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos, 2)
    
    angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
    head_len = 12
    head_angle = math.pi / 6 
    
    left_x = end_pos[0] - head_len * math.cos(angle - head_angle)
    left_y = end_pos[1] - head_len * math.sin(angle - head_angle)
    
    right_x = end_pos[0] - head_len * math.cos(angle + head_angle)
    right_y = end_pos[1] - head_len * math.sin(angle + head_angle)
    
    pygame.draw.polygon(surface, color, [end_pos, (left_x, left_y), (right_x, right_y)])

running = True

# MAIN LOOP
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # KEYBOARD INPUTS (CHANGING VARIABLES)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation_started = True
                speed1 = velocity1
                speed2 = abs(velocity2)
                velocity1_y = speed1 * math.sin(math.radians(Angle1))
                velocity1 = speed1 * math.cos(math.radians(Angle1))
                velocity2_y = speed2 * math.sin(math.radians(Angle2))
                velocity2 = speed2 * math.cos(math.radians(Angle2))
                start_v1 = speed1
                start_v2 = -speed2
                Before_KE = 0.5 * mass1 * (velocity1**2 + velocity1_y**2) + 0.5 * mass2 * (velocity2**2 + velocity2_y**2)

            if event.key == pygame.K_r:
                simulation_started = False
                velocity1 = start_v1
                velocity2 = start_v2
                velocity1_y = 0
                velocity2_y = 0
                ball1_x = 400 - Displacement/2
                ball2_x = 400 + Displacement/2
                ball1_y = 300
                ball2_y = 300
                collided = False
                Before_KE = 0
                After_KE = 0
                Vi1 = velocity1
                Vi2 = velocity2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_ball = "blue"
                selected_angle = "blue"
            if event.key == pygame.K_2:
                selected_ball = "red"
                selected_angle = "red"

        if not simulation_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if selected_ball == "blue":
                        mass1 += 0.1
                    else:
                        mass2 += 0.1

                if event.key == pygame.K_q:
                    if selected_ball == "blue":
                        mass1 = max(0.1, mass1 - 0.1)
                    else:
                        mass2 = max(0.1, mass2 - 0.1)

                if event.key == pygame.K_d:
                    if selected_ball == "blue":
                        velocity1 += 0.1
                    else:
                        velocity2 -= 0.1

                if event.key == pygame.K_a:
                    if selected_ball == "blue":
                        velocity1 -= 0.1
                    else:
                        velocity2 += 0.1

                if event.key == pygame.K_w and temp_e != 10:
                    temp_e += 1
                    e = temp_e/10
                if event.key == pygame.K_s and temp_e != 0:
                    temp_e -= 1
                    e = temp_e/10
                if event.key == pygame.K_RIGHT:
                    temp_friction += 1
                    Friction = temp_friction / 10
                if event.key == pygame.K_LEFT and Friction != 0:
                    temp_friction -= 1
                    Friction = temp_friction / 10

                if Friction != 0:
                    if event.key == pygame.K_UP and Displacement < 800:
                        Displacement += 0.5
                        ball1_x = 400 - Displacement/2
                        ball2_x = 400 + Displacement/2

                    if event.key == pygame.K_DOWN and Displacement > 50:
                        Displacement -= 0.5
                        ball1_x = 400 - Displacement/2
                        ball2_x = 400 + Displacement/2
                else:
                    Displacement = 300
                    ball1_x = 400 - Displacement/2
                    ball2_x = 400 + Displacement/2

                if event.key == pygame.K_PERIOD:
                    if selected_angle == "blue":
                        Angle1 = (Angle1 + 1) % 360
                    else:
                        Angle2 = (Angle2 + 1) % 360
                if event.key == pygame.K_COMMA:
                    if selected_angle == "blue":
                        Angle1 = (Angle1 - 1) % 360
                    else:
                        Angle2 = (Angle2 - 1) % 360

                if event.key == pygame.K_m:
                    iterations = 5000
                    
                    # TRACK X AND Y VELOCITY FOR BOTH BALLS
                    blue_final_vx = []
                    blue_final_vy = []
                    red_final_vx = []
                    red_final_vy = []
                    
                    
                    for i in range(iterations):
                        # ADDS RANDOMNESS TO MASS AND VELOCITY (5% VARIATION)
                        sim_mass1 = mass1 * random.uniform(0.95, 1.05)
                        sim_mass2 = mass2 * random.uniform(0.95, 1.05)
                        sim_speed1 = velocity1 * random.uniform(0.95, 1.05)
                        sim_speed2 = abs(velocity2) * random.uniform(0.95, 1.05)
                        
                        # CALCULATE X AND Y VELOCITY COMPONENTS FOR BOTH BALLS
                        sim_v1_x = sim_speed1 * math.cos(math.radians(Angle1))
                        sim_v1_y = sim_speed1 * math.sin(math.radians(Angle1))
                        sim_v2_x = sim_speed2 * math.cos(math.radians(Angle2))
                        sim_v2_y = sim_speed2 * math.sin(math.radians(Angle2))
                        
                        # ADD RANDOM IMPACT ANGLE VARIATION (-15° TO +15°)
                        impact_angle = math.radians(random.uniform(-15, 15))
                        nx = math.cos(impact_angle)
                        ny = math.sin(impact_angle)
                        tx = -ny
                        ty = nx
                        
                        # FIND NORMAL AND TANGENTIAL VELOCITY COMPONENTS FOR BOTH BALLS
                        v1n = sim_v1_x * nx + sim_v1_y * ny
                        v1t = sim_v1_x * tx + sim_v1_y * ty
                        v2n = sim_v2_x * nx + sim_v2_y * ny
                        v2t = sim_v2_x * tx + sim_v2_y * ty

                        # CALCULATE NEW NORMAL VELOCITIES AFTER COLLISION
                        new_v1n = ((sim_mass1 - e * sim_mass2) * v1n + (1 + e) * sim_mass2 * v2n) / (sim_mass1 + sim_mass2)
                        new_v2n = ((sim_mass2 - e * sim_mass1) * v2n + (1 + e) * sim_mass1 * v1n) / (sim_mass1 + sim_mass2)
                        
                        # RECONSTRUCT FINAL VELOCITY COMPONENTS IN X AND Y DIRECTIONS
                        final_v1_x = new_v1n * nx + v1t * tx
                        final_v1_y = new_v1n * ny + v1t * ty
                        final_v2_x = new_v2n * nx + v2t * tx
                        final_v2_y = new_v2n * ny + v2t * ty
                        
                        #RECORD FINAL VELOCITY COMPONENTS FOR BOTH BALLS
                        blue_final_vx.append(final_v1_x)
                        blue_final_vy.append(final_v1_y)
                        red_final_vx.append(final_v2_x)
                        red_final_vy.append(final_v2_y)


                    # RENDERING THE SCATTER PLOT FOR FINAL VELOCITY DISTRIBUTION
                    plt.figure(figsize=(10, 6))
                    

                    plt.scatter(blue_final_vx, blue_final_vy, alpha=0.2, color='blue', edgecolors='none', s=20, label='Blue Ball')
                    #PLOT RED BALL FINAL VELOCITY DISTRIBUTION
                    plt.scatter(red_final_vx, red_final_vy, alpha=0.2, color='red', edgecolors='none', s=20, label='Red Ball')
                    
                    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
                    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
                    plt.title(f"SIMULATION: Final Velocity Distribution ({iterations} Runs)")
                    plt.xlabel("Final X Velocity (m/s)")
                    plt.ylabel("Final Y Velocity (m/s)")
                    plt.legend()
                    plt.grid(True, alpha=0.3)
                    
                    plt.show()
            Vi1 = velocity1
            Vi2 = velocity2

    # FRICTION AND MOVEMENT CALCULATIONS
    if simulation_started:
        if Friction != 0:
            blue_decel_step = (Friction / mass1) / 60
            red_decel_step = (Friction / mass2) / 60

            current_speed1 = math.sqrt(velocity1**2 + velocity1_y**2)
            if current_speed1 > 0:
                if current_speed1 <= blue_decel_step:
                    velocity1 = 0
                    velocity1_y = 0
                else:
                    scale1 = (current_speed1 - blue_decel_step) / current_speed1
                    velocity1 *= scale1
                    velocity1_y *= scale1

            current_speed2 = math.sqrt(velocity2**2 + velocity2_y**2)
            if current_speed2 > 0:
                if current_speed2 <= red_decel_step:
                    velocity2 = 0
                    velocity2_y = 0
                else:
                    scale2 = (current_speed2 - red_decel_step) / current_speed2
                    velocity2 *= scale2
                    velocity2_y *= scale2

        ball1_x += velocity1 * (1/6)
        ball1_y += velocity1_y * (1/6)
        ball2_x += velocity2 * (1/6)
        ball2_y += velocity2_y * (1/6)

    screen.fill((255, 255, 255))

    # DISPLAYING TEXT AND BALLS
    if not simulation_started:
        text = font.render("SPACE to start | R to reset | M for SIMULATION (No Friction)", True, (0, 0, 0))
        controls = font.render("1/2 select ball | E/Q mass | A/D speed | W/S e | Arrows friction/displacement | ,/. angle", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, 370))
        screen.blit(text, text_rect)
        controls_rect = controls.get_rect(center=(WIDTH // 2, 400))
        screen.blit(controls, controls_rect)

    current_speed1 = math.sqrt(velocity1**2 + velocity1_y**2)
    current_speed2 = math.sqrt(velocity2**2 + velocity2_y**2)

    text1 = font.render(f"Blue Mass: {mass1:.1f}kg", True, (0, 0, 0))
    text2 = font.render(f"Red Mass: {mass2:.1f}kg", True, (0, 0, 0))
    text3 = font.render(f"Speed (u): {abs(Vi2):.2f} m/s", True, (0, 0, 0))
    text4 = font.render(f"Speed (u): {abs(Vi1):.2f} m/s", True, (0, 0, 0))
    text5 = font.render(f"Speed (v): {current_speed1:.2f} m/s", True, (255, 140, 0))
    text6 = font.render(f"Speed (v): {current_speed2:.2f} m/s", True, (255, 140, 0))
    text7 = font.render(f"KE Before: {Before_KE:.3f} J", True, (0, 0, 0))
    text8 = font.render(f"KE After: {After_KE:.3f} J", True, (255, 140, 0))
    text9 = font.render(f"Coeff of Res: {e}", True, (0, 0, 0))
    text10 = font.render(f"Displacement: {(Displacement/10) - 5:.2f} m", True, (0, 0, 0))
    text11 = font.render(f"Friction: {Friction:.1f} N", True, (0, 0, 0))
    text12 = font.render(f"Blue Angle: {Angle1}°  Red Angle: {Angle2}°  (editing: {selected_angle})", True, (0, 0, 0))

    screen.blit(text1, (10, 20))
    screen.blit(text2, (10, 45))
    screen.blit(text3, (200, 45))
    screen.blit(text4, (200, 20))
    screen.blit(text7, (200, 70))
    
    if simulation_started and After_KE != 0:
        screen.blit(text5, (420, 20))
        screen.blit(text6, (420, 45))
        screen.blit(text8, (420, 70))
        
    screen.blit(text9, (10, 70))
    screen.blit(text10, (10, 95))
    screen.blit(text11, (10, 120))
    screen.blit(text12, (10, 145))
    pygame.draw.circle(screen, (0, 0, 255), (int(ball1_x), int(ball1_y)), 25)
    pygame.draw.circle(screen, (255, 0, 0), (int(ball2_x), int(ball2_y)), 25)

    # VECTOR ARROW DISPLAYS
    VECTOR_SCALE = 30

    if not simulation_started:
        preview_speed1 = velocity1
        preview_speed2 = abs(velocity2)
        
        if abs(preview_speed1) > 0.01:
            preview_v1_x = preview_speed1 * math.cos(math.radians(Angle1))
            preview_v1_y = preview_speed1 * math.sin(math.radians(Angle1))
            end1_x = ball1_x + (preview_v1_x * VECTOR_SCALE)
            end1_y = ball1_y + (preview_v1_y * VECTOR_SCALE)
            arrow(screen, (0, 0, 0), (ball1_x, ball1_y), (end1_x, end1_y))
            
        if preview_speed2 > 0.01:
            preview_v2_x = preview_speed2 * math.cos(math.radians(Angle2))
            preview_v2_y = preview_speed2 * math.sin(math.radians(Angle2))
            end2_x = ball2_x + (preview_v2_x * VECTOR_SCALE)
            end2_y = ball2_y + (preview_v2_y * VECTOR_SCALE)
            arrow(screen, (0, 0, 0), (ball2_x, ball2_y), (end2_x, end2_y))
    else:
        if current_speed1 > 0.01:
            end1_x = ball1_x + (velocity1 * VECTOR_SCALE)
            end1_y = ball1_y + (velocity1_y * VECTOR_SCALE)
            arrow(screen, (0, 0, 0), (ball1_x, ball1_y), (end1_x, end1_y))

        if current_speed2 > 0.01:
            end2_x = ball2_x + (velocity2 * VECTOR_SCALE)
            end2_y = ball2_y + (velocity2_y * VECTOR_SCALE)
            arrow(screen, (0, 0, 0), (ball2_x, ball2_y), (end2_x, end2_y))

    # 2D COLLISION CALCULATIONS
    dist = math.sqrt((ball2_x - ball1_x)**2 + (ball2_y - ball1_y)**2)

    if dist <= 50 and not collided:
        nx = (ball2_x - ball1_x) / dist
        ny = (ball2_y - ball1_y) / dist
        tx = -ny
        ty = nx

        v1n = velocity1 * nx + velocity1_y * ny
        v1t = velocity1 * tx + velocity1_y * ty
        v2n = velocity2 * nx + velocity2_y * ny
        v2t = velocity2 * tx + velocity2_y * ty

        new_v1n = ((mass1 - e * mass2) * v1n + (1 + e) * mass2 * v2n) / (mass1 + mass2)
        new_v2n = ((mass2 - e * mass1) * v2n + (1 + e) * mass1 * v1n) / (mass1 + mass2)

        velocity1 = new_v1n * nx + v1t * tx
        velocity1_y = new_v1n * ny + v1t * ty
        velocity2 = new_v2n * nx + v2t * tx
        velocity2_y = new_v2n * ny + v2t * ty

        After_KE = 0.5 * mass1 * (velocity1**2 + velocity1_y**2) + 0.5 * mass2 * (velocity2**2 + velocity2_y**2)
        collided = True

    if dist > 50:
        collided = False

    pygame.display.flip()

pygame.quit()