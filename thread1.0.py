import threading
import time


class BOT_THREAD (threading.Thread):
   def __init__(self,function):
      threading.Thread.__init__(self)
      self.function = function
   def run(self):
      print ("Starting a thread")
      self.function()
