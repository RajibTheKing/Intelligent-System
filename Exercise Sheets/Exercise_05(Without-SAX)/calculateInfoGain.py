

import math

class InfoGain:
    def __init__(self):
        pass

    def calculateLogarithms(self, y, n):
        t = y + n
        return -(y/t)*math.log2(y/t) - (n/t)*math.log2(n/t)

    def calculateIG(self, t1, t2, t3):
        t = t1 + t2 + t3
        return 0.94 - ( t1/t * 1 + t2/t * 0.9182 + t3/t * 0.811278 )



def main():
  print("Hello World!")
  infoGain = InfoGain()
  print(infoGain.calculateLogarithms(1,3))
  print(infoGain.calculateIG(4,6,4))

  
if __name__== "__main__":
  main()