import time
import os
A=["#     #   #######   #     #",
   "##   ##      #      ##   ##",
   "# # # #      #      # # # #",
   "#  #  #      #      #  #  #"]
B=("                           ")
for l in range(10):
      for n in range(4+l):
         print (A[n])
      time.sleep(1)
      i = os.system('cls')
      for k in range(4+l):
        A[k]='  '+A[k]
      A.insert(0,B)
