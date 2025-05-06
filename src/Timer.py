class Timer:
    def __init__(self, temp_total_time):
        self.saved_time = 0
        self.total_time = temp_total_time

    def start(self):
        self.saved_time = millis()

    def done(self):
        passed_time = millis() - self.saved_time
        return passed_time > self.total_time
