import pygame
import serial

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Car states
left = False
right = False
forward = True
backwards = True

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

ser = serial.Serial('/dev/ttyACM0')
print(ser.name)  # check which port was really used

pygame.init()

# Set the width and height of the screen [width,height]
size = [200, 100]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rollin' and hatin'")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done == False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # textPrint.print(screen, "Joystick {}".format(i))
        # textPrint.indent()
        #
        # # Get the name from the OS for the controller/joystick
        # name = joystick.get_name()
        # textPrint.print(screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
            if i == 0:
                if axis > 0.7 and not right:
                    print("Right")
                    right = True
                    ser.write(b'y')
                if axis < 0.5 and right:
                    print("Not right")
                    right = False
                    ser.write(b'h')
                if axis < -0.7 and not left:
                    print("Left")
                    left = True
                    ser.write(b't')
                if axis > -0.5 and left:
                    print("Not left")
                    left = False
                    ser.write(b'g')
            if i == 1:
                if axis < 0.5 and not forward:
                    print("Accelerating")
                    forward = True
                    ser.write(b'u')
                if axis > 0.6 and forward:
                    print("Stop")
                    forward = False
                    ser.write(b'j')
            elif i == 2:
                if axis < 0.5 and not backwards:
                    print("Back")
                    backwards = True
                    ser.write(b'i')
                if axis > 0.6 and backwards:
                    print("not back")
                    backwards = False
                    ser.write(b'k')

        textPrint.unindent()

        textPrint.unindent()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(80)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
ser.close()  # close port