class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None



class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        

    def get(self, index: int) -> int:
        
        if self.head == None:
            return -1
        else:
            i=0
            cur=self.head
            while cur is not None:
                
                if index==i:
                    return cur.val

                cur=cur.next
                i+=1
            return -1


    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node

        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node=Node(val)
        
        if index<=0:
            self.addAtHead(val)

        else:
            cur=self.head
            i=1
    

            while i!=index and cur is not None :
                cur=cur.next
                i+=1
                
            if cur is not None :
                if cur.next==None:
                    self.addAtTail(val)
                else:
                
                    saver = cur.next
                    new_node.prev=cur
                    new_node.next=cur.next
                    cur.next=new_node
                    saver.prev=new_node


        

    def deleteAtIndex(self, index: int) -> None:
        
        if self.head!= None:
                

            if index==0:
            
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else :
                    self.head=self.head.next
                    self.head.prev=None
                    

        
            else:
                i=1
                cur=self.head
                while i!=index and cur is not None:
                    cur=cur.next
                    i+=1
                    

                if cur is not None and cur.next is not None:
                    if  cur.next.next==None:
                        cur.next=None
                        self.tail=cur
                    else:

                        saver=cur.next.next
                        cur.next=saver
                        saver.prev=cur
            

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)