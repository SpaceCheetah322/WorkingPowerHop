# Inspired by a Processing class written by Daniel Shiffman. Rewritten by Katelyn.
# Should work as a countdown; use start() when you want to start counting down, and done() to check if it's finished.
class Timer:
    def __init__(self, temp_total_time):
        self.saved_time = 0
        self.total_time = temp_total_time
        
    def start():
        self.saved_Time = millis()
    
    def done():
        passed_time = millis() - saved_Time
        if (passed_time > self.total_time):
            return True
        else:
            return False
"""
Example Usage:
def setup():
    new_timer = Timer(1000) # 1000 = 1 second timer
    new_timer.start()

def draw():
    if new_timer.done():
        print("Finished!")
"""
