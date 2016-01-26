import time
import random

class TrafficLight():
    traffic_status = [1, 2, 3];
    traffic_side = "down";
    def __init__(self, status):
        self.status = status
    def Switch(self):
        if self.status == 1:
            self.status = 2
            self.traffic_side = "down";
        elif self.status == 2:
            if self.traffic_side == "down":
                self.status = self.traffic_status[2];
            elif self.traffic_side == "up":
                self.status = self.traffic_status[0];
        elif self.status == 3:
            self.status = 2;
            self.traffic_side = "up";
    def GetStatus(self):
        if self.status == 1:
            return "Red - 1"
        elif self.status == 2:
            return "Yellow - 2"
        elif self.status == 3:
            return "Green - 3"
    def GetSleepLength(self):
        if self.status == self.traffic_status[1]:
            return 3;
        else:
            return random.randint(3, 5);
        
tl = TrafficLight(1);
while True:
    time.sleep(tl.GetSleepLength());
    print tl.GetStatus();
    tl.Switch();
    
    
