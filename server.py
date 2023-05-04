import socketserver
import random
from Crypto.Util.number import *
from Crypto.Random import random

class Fiat(socketserver.BaseRequestHandler):
   def handle(self):
      p = getPrime(15)
      q = getPrime(15)
      n = p*q

      self.secret = str(self.request.recv(1024).strip(), "utf-8")
      S = bytes_to_long(b"self.secret")        #Client

      v = pow(S, 2, n)

      count = 0
      no_of_iterations = 20
      print("Message    = ", S)
      print("Prime      = ", n)

      for i in range(no_of_iterations):
         r = random.randint(1, n - 1)
         x = pow(r, 2, n)

         e = random.randint(0, 1)

         y = (r*(S**e))%n

         if(pow(y,2,n) == (x*(v**e))%n):
            print("Iteration "+str(i+1) + " Passed")
            count += 1
         else:
            print("Iteration "+str(i+1) + " Failed")

      if(count == no_of_iterations):
         print("You has the secret.")
      else:
         print("You does not have the secret.")


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 1234
    with socketserver.TCPServer((HOST,PORT), Fiat) as server:
       server.serve_forever()
