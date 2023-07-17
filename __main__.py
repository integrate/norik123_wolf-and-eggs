import time
from time import sleep
import model,view,controller


while True:
    sleep(1 / 60)
    controller.process_events()
    model.run()
    view.draw_screen()



