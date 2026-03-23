class  Queue :
    def __init__(self):
        self.qlist=list()
    def isempty(self):
        return len(self.qlist)==0
    def enqueue(self,item):
           print("inserted element =",item)
           self.qlist.append(item)
    def display(self):
        print(self.qlist)
    def dequeue(self):
           if self.isempty()==True:
               print("cannot delete from an empty queue.")
           else:
                print(" deleted element =", self.qlist.pop(0) )
q=Queue ()
print("queue operation")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print("queue element are")
q.display()
q.dequeue()
q.dequeue()
print("after deleting first twoelements")
q.display()
                              
                           
                         
            
            