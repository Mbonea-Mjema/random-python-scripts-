import schedule
import time
import threading
import time


class BOT_THREAD (threading.Thread):
   def __init__(self,function):
      threading.Thread.__init__(self)
      self.function = function
   def run(self):
      print ("Starting a thread")
      self.function()




t=0
def do():
    obj=BOT_THREAD (job)
    obj.start()
def job():
    nums=[]
    global t
    print("I'm working...",t)
    for i in range(2,1000000000):
        ans=1
        for j in range(2,i):
            if i%j==0:
                ans=0
                break
        if ans!=0:
           nums.append(i)
    print(nums)
                
    t+=1

schedule.every(0.1).minutes.do(do)

while True:
    schedule.run_pending()
    print('what does this button d0..?!?!?! ')
