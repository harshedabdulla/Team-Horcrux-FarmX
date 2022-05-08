import threading
import time
import CURRENTLOCATION   

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, nooftimes, delay, functtorun):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.exitFlag = 0
      self.nooftimes = nooftimes
      self.functorun = functtorun
   def run(self):
      print ("Starting " + self.name)
      self.functorun(self.delay)
      print ("Exiting " + self.name)

def print_time(delay):
   while 1:
     ########################
    print("sdfsdfsdf")
    time.sleep(delay)
      

# Create new threads
thread1 = myThread(1, "Thread-1", 5, 2, CURRENTLOCATION.runthis)   #currentloaation.runthis
#thread2 = myThread(2, "Thread-2", 5, 1, print_time)


def runboth():
         
   # Start new Threads
   thread1.start()
   #thread2.start()
   #thread1.join()
   # Start new Threads
   #thread1.start()
   #thread2.start()


runboth()