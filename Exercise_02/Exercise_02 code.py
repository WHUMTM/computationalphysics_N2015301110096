import time
import os
A=["#     #   #######   #     #",
   "##   ##      #      ##   ##",
   "# # # #      #      # # # #",
   "#  #  #      #      #  #  #"]
B=("                           ")
for l in range(10):
      time.sleep(1)
      i = os.system('cls')
      for k in range(4+l):
        A[k]='  '+A[k]
      A.insert(0,B)
