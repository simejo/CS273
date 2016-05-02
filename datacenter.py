import socket               # Import socket module
import timeTable
import event
import threading
import json

class Replicated_log(object):
   def __init__(self):
      self.log = []

   def input_in_log(self, event):
      self.log.append(message)

   def lookup_log(self):
      print self.log

   def delete_in_log(self, event):
      self.log.remove(event)

class ReplicatedDict(object):
   def __init__(self):
      self.dict = {}
      


class datacenter(object):
   def __init__(self, node_id, port_in, port_out):
      self.node_id = node_id
      self.s = socket.socket()
      self.timeTable = timeTable.TimeTable(2,node_id)
      self.hostname = socket.gethostname() # get local machine name
      self.port_in = port_in
      self.port_out = port_out

   def handle_post(self, message):
      print "Handle Post .... " + str(message)
      self.timeTable.tick()
      print self.timeTable.toString()

   def handle_lookup(self):
      print 'Handle lookup ....'

   def handle_sync(self, d2):
      #d2 is an IPadress
      try:
         s = socket.socket()
         s.connect((d2, self.port_out))
         s.send("sync_server " + str(self.hostname))
         s.close()



         
      except Exception, e:
         print "Could not connect. " + str(e)
      print 'Handle sync with .... ' + str(d2)

   def handle_sync_with_server(self):
      data = json.dumps(self.timeTable)
      s = socket.socket()
      s.connect((d2, self.port_out))
      s.send("sync_time_table " + data)
      s.close()

   def handle_time_table(self, data):
      print data

   def initialize_connection(self):
      s = self.s
      s.bind((self.hostname, self.port_in))
      s.listen(5)
      while True:
         print "Server running... HOST: " + self.hostname
         c, addr = s.accept()     # Establish connection with client.
         print 'Got connection from', addr
         c.send('Thank you for connecting')
         message = c.recv(1024)


         try:
            input_string = message.split(' ', 1)
            print input_string
            if (input_string[0] == "post"):
               self.handle_post(input_string[1])
            elif (input_string[0] == 'lookup'):
               self.handle_lookup()
            elif (input_string[0] == 'sync'):
               self.handle_sync(input_string[1])
            elif (input_string[0] == 'quit'):
               s.close_connection()
               s.shutdown()
               break
            elif (input_string[0] == 'sync_server'):
               self.handle_sync_with_server()
            elif (input_string[0] == 'sync_time_table'):
               self.handle_time_table(input_string[1])
         except Exception, e:
            print e
            print 'Something wrong happened. Server shutting down...'
            c.close()
            break
         c.close()                # Close the connection

   def close_connection(self):
      self.s.close()


   def shutdown(self):
      self.s.shutdown()

   def connect_to(self, addr, message, ):
      s = self.s
      s.connect((addr, self.port_out))

      #if(message == "sync")

      """input_text = raw_input('Enter your command:')
      isNotDone = True
      while(isNotDone):
         input_string = input_text.split(' ', 1)
         if(input_string[0] == 'post'):
            s.send(input_text)
            print "Your message: " + input_string[1]
            isNotDone = False
         elif(input_string[0] == 'lookup'):
            s.send(input_text)
            print "MATTAFACKA"
            isNotDone = False
         elif(input_string[0] == 'sync'):
            s.send(input_text)
            print "sync with " + input_string[1]
            isNotDone = False
         else:
            input_text = raw_input('Wrong argument. Use post, lookup or sync? ')"""

      s.close


#PROBLEM: HOW TO LISTEN FOR MESSAGES IN THE SAME TIME AS IT SHOULD BE ABLE TO SEND? CREATE SOME TYPE OF LISTENER?
server = datacenter(0, 12345, 10000)
threading.Thread(target=server.initialize_connection()).start()