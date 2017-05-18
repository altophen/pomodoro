#
#   my time module for the console pomodermo timer project
#   what it does is 

#   how it works:
#        import this module and use the source... it's a generator which yields a 

import datetime
import time

class timeinfo(object):
    #   the object that represents elapsed and remaining time
    #   accepts the length of the period we're looking at in whole minutes (1-60)
    #   notes the moment of it's creation to the end of the timeperiod
    def __init__(self,period):
        if type(period) != int:
            raise TypeError ("not an int")
        if (period <1) or (period >60):
            raise ValueError("length < 1 || length > 60")
        else:
            self.TotalMinutes = period
            self.Start = datetime.datetime.now()
            self.End = self.Start + datetime.timedelta(minutes=period)
            self.OneSecond = datetime.timedelta(seconds=1)
    def get_now(self):
        return datetime.datetime.now()
    Now = property(get_now)

    def get_elapsed_seconds(self):
        return int(time.strftime("%S",time.gmtime((self.Now - self.Start).total_seconds())))
    seconds = property(get_elapsed_seconds)
    
    def get_elapsed_minutes(self):
        return int(time.strftime("%M",time.gmtime((self.Now - self.Start).total_seconds())))
    minutes = property(get_elapsed_minutes)

    def get_remaining_seconds(self):
        return int(time.strftime("%S",time.gmtime((self.End - self.Now).total_seconds())))
    RemainingSeconds = property(get_remaining_seconds)

    def get_remaining_minutes(self):
        return int(time.strftime("%M",time.gmtime((self.End - self.Now).total_seconds())))
    RemainingMinutes = property(get_remaining_minutes)

def timesource(liLength) :
        #   accepts a length in minutes
        #   yields timeinfo objects which tell everything about the period of time in consideration
    info = timeinfo(liLength)
    NextSecond = info.Start + info.OneSecond
    while True:
        if info.Now > NextSecond :
            NextSecond = NextSecond + info.OneSecond
            if info.Now > info.End:
                yield (info)
                break
            else: 
                yield (info)
        else:
            time.sleep(0.01)
            
        
    
