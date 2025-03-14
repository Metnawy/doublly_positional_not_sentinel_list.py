import copy 
class doublly_positional_not_sentinel_list:
    '''
    objective:creating a list with using the feature of the doublly references and interacting mostly via tool of positon ...building that without the technique of sentinel
    data :accepting numeric as the only data in the list and None as space/list holder
    '''
    #composite/nested classes 
    class _node:
        def __init__(self,data,container,next=None,prev=None):
            self.container=container
            self.data=data
            self._next=next
            self._prev=prev
        @property
        def data(self):
            return self._data
        @data.setter
        def data(self,data):
        
            if self.container.size==0:
                self._data=data
            else:
                if isinstance(data,(int,float)):
                    self._data=data
                else:
                   raise TypeError("the type of the objects of nodes in that list should be numeric ")
                    
        def __repr__(self) -> str:
            return f"{self.data}"
    class _position:
        def __init__(self,node,continer):
           if node!=None:
              self.node=node
              self.continer=continer
           else:
               raise TypeError
        def __repr__(self) -> str:
            return f"{self.node.data}"
    #basic methods 
    def __init__(self,data=None):
        if type(data)==type(None):
            self.size=0
        else:
            self.size=1
        self.head=self._node(data,self)
        self.last=self.head
    #operations
    def add_first(self,data):
        #adding a new node/value as the first value/node in the list 
        #case of non-empty list 
        if self.size>0:
            new_node=self._node(data,self,self.head,None)
            self.head._prev=new_node
            self.head=new_node
            self.size+=1
            return self._position(new_node,self)
        else:
            if isinstance(data,(int,float)):
                self.head.data=data
                self.size+=1
                return self._position(self.head,self)
            else:
                raise TypeError("the type of the objects of nodes in that list should be numeric ")

    def delete_first(self):
        if self.size==0:
            return "the list is already empty ..nothing to delete "
        elif  self.size==1:
            element=self.head.data
            self.size-=1
            self.head.data=None
            return element
        else:
            #saving references to avoid losting in the changing of the pointers 
            next=self.head._next
            data=self.head.data
            concerned_first=self.head
            #changing the pointers
            self.head=next
            self.head._prev=None
            #ending the deleting node 
            concerned_first._next=concerned_first._prev=None
            concerned_first._data=None
            self.size-=1
            return data             
    def add_last(self,data):
        if self.size==0:
            if isinstance(data,(int,float)):
                self.last.data=data
                self.size+=1
                return self._position(self.last,self)
            else:
                raise TypeError("the type of the objects of nodes in that list should be numeric ")
        else:
            new_node=self._node(data,self,None,self.last)
            self.last._next=new_node
            self.last=new_node
            self.size+=1
            return self._position(new_node,self)     
    def delete_last(self):
        if self.size==0:
            return "the list is empty nothing to delete"     
        if self.size==1:
            element=self.last.data
            self.size-=1
            self.last.data=None
            return element
        else:
            element=self.last.data
            new_last=self.last._prev
            new_last._next=None
            #ending the deleted node
            self.last._data=self.last._next=self.last._prev=None
            self.last=new_last
            self.size-=1
            return element
    def change_at_position(self,p,data):
        if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self:
            if self.size==0:
                if isinstance(data,(int,float)):
                    p.node.data=data
                    self.size+=1
                    return p
                else:
                    raise TypeError("the type of the objects of nodes in that list should be numeric ")
            else:
                p.node.data=data
                return p 
    def add_at_position(self,p,data):
        # here we add new node (not just change the value of the node)..with putting in the order of that position (concerned) pushing the old one step forward 
        if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self:
            #in case of empty list 
            if self.size==0:
                if isinstance(data,(int,float)):
                    self.head.data=data
                    self.size+=1
                    return self._position(self.head,self)
                else:
                    raise TypeError
            else:
                pre=p.node._prev
                new_node=self._node(data,self,p.node,pre)
                p.node._prev=new_node
                #handling the cases of the add at the positon of self.head with it's speciality
                if p.node==self.head:
                    self.head=new_node
                else:
                    pre._next=new_node
                    
                self.size+=1
                
                return self._position(new_node,self)
        else:
            raise TypeError("that position doesn't belong to _position composite class")

    def delete_at_position(self,p):
      #delete the node at this position
      if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self:
        if self.size==0:
            return "the list is already empty nothing to delete"
        
        if self.size==1 :
            if p.node==self.head:
                element=p.node.data
                self.size-=1
                p.node.data=None
                p.continer=None
                return element
            else:
               raise ValueError("there is something wrong in the object of position ")
        elif p.node==self.head:
            element=p.node.data
            new_head=p.node._next
            concerned=p.node

            self.head=new_head
            self.head._prev=None
            self.size-=1

            concerned._next=concerned._prev=concerned.container=None
            concerned._data=None
            p.continer=None
            return element
        elif p.node==self.last:
            #saving reference to concerned points
            element=p.node.data
            new_last=p.node._prev
            concerned=p.node
            
            #changes
            self.last=new_last
            self.last._next=None
            self.size-=1

            #ending the deleted node
            concerned._next=concerned._prev=concerned.container=None
            concerned._data=None
            p.continer=None

            return element
        
        else:
            if p.node._next!=None and p.node._prev!=None:
                pre=p.node._prev
                next=p.node._next
                concerned=p.node

                pre._next=next
                next._prev=pre
                self.size-=1
                element=concerned.data

                concerned._next=concerned._prev=concerned._data=None
                p.continer=None
                return element
      else:
          raise TypeError("this object either doesn't belong to list or it's not _position object")
    
    def add_after_position(self,p,data):
        #add new_node to the list according /in reference to a position of another node 
        if isinstance(p,(doublly_positional_not_sentinel_list._position)) and p.continer==self:
            if self.size==0:
                return "the list is empty we need initilize it with head node firstly"
            elif p.node==self.head and self.size==1:
                new_node=self._node(data,self,None,p.node)
                p.node._next=new_node
                self.last=new_node
                self.size+=1
                return self._position(new_node,self)

            elif p.node==self.head:
                new_node=self._node(data,self,p.node._next,p.node)
                p.node._next=new_node
                p.node._next._prev=new_node
                self.size+=1
                return self._position(new_node,self)
            
            elif p.node==self.last:
                
                new_node=self._node(data,self,None,p.node)
                p.node._next=new_node
                self.last=new_node
                self.size+=1
                return self._position(new_node,self)
            
            elif  p.node._next!=None and p.node._prev!=None:
             
                concerned=p.node
                after_concerned=concerned._next
                new_node=self._node(data,self,after_concerned,concerned)
                concerned._next=new_node
                after_concerned._prev=new_node

                self.size+=1
                return self._position(new_node,self)

        else:
            raise TypeError
        
    def add_before_position(self,p,data):
        if isinstance(p,(doublly_positional_not_sentinel_list._position)) and p.continer==self:
           if self.size==0:
               return "there is no value to add before"

           if p.node==self.head :
               new_node=self._node(data,self,p.node,None)
               p.node._prev=new_node
               self.head=new_node
               self.size+=1
               return self._position(new_node,self)
           elif p.node==self.last:               
                   new_node=self._node(data,self,p.node,p.node._prev)
                   #changing the pointers 
                   p.node._prev._next=new_node
                   p.node._prev=new_node
                   self.size+=1
                   return self._position(new_node,self)              
           else:               
               if (p.node._next!=None) and (p.node._prev!=None):
                   new_node=self._node(data,self,p.node,p.node._prev)

                   #changing the pointers 
                   p.node._prev._next=new_node
                   p.node._prev=new_node
                   self.size+=1
                   return self._position(new_node,self)         
        else:
            raise TypeError
    def delete_before_position(self,p):
        if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self:
            if self.size==0:
                return"nothing to delete before"
            elif self.head==p.node:
                return "this position is the first one nothing to delete before it "
            elif p.node._prev==self.head:
                to_delete=p.node._prev
                concerned=p.node
                element=to_delete.data

                #changing the pointers 
                concerned._prev=None
                self.head=concerned
                self.size-=1

                #ending the deleted node
                to_delete._data=to_delete._next=to_delete._prev=None
                to_delete.container=None
                return element
            else:
                if p.node._next !=None and p.node._prev!=None:
                       to_delete=p.node._prev
                concerned=p.node
                element=to_delete.data

                #changing the pointers 
                concerned._prev=None
                self.size-=1

                #ending the deleted node
                to_delete._data=to_delete._next=to_delete._prev=None
                to_delete.container=None
                return element
        else:
            raise TypeError

    def delete_after_position(self,p):
        if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self:
            if self.size==0:
                return"there is nothing in the list to delete after"
            if p.node==self.last:
                return"this concerned node is the last node nothing after to delete"
            if p.node._next==self.last:
                concerned=p.node
                to_delete=concerned._next
                element=to_delete.data

                concerned._next=None
                self.last=concerned
                self.size-=1

                to_delete._data=to_delete._next=to_delete._prev=to_delete.container=None

                return element
            else:
                if p.node._next._next!=None:
                    concerned=p.node
                    to_delete=concerned._next
                    element=to_delete.data
                    new_next=to_delete._next

                    concerned._next=new_next
                    new_next._prev=concerned
                    self.size-=1

                    to_delete._next=to_delete._prev=to_delete.data=to_delete.container=None

                    return element
                
        else:
            raise TypeError

    def add_at_index(self,index,data):
        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        #it's equivilant to the method of add specific position with using the ordinary index 
        if self.size==0 :
                if index!=0:
                    return IndexError
                else:
                    if isinstance(data,(int,float)) :
                        self.head.data=data
                        self.size+=1
                        return self._position(self.head,self)
                    else:
                        raise TypeError
        if 1<=index<=self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.add_at_position(self._position(curser,self),data)
            
        else:
            raise IndexError

    def change_at_index(self,index,data):

        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        if self.size==0 :
                if index!=0:
                    return IndexError
                else:
                  if isinstance(data,(int,float)):
                    self.head.data=data
                    self.size+=1
                    return self._position(self.head,self)
                  else:
                      raise TypeError
        if 1<=index<=self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.change_at_position(self._position(curser,self),data)
        else:
            raise IndexError

    def delete_at_index(self,index):

        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        if self.size==0 :
                if index!=0:
                    return IndexError
                else:
                    return "there is nothing to delete..list is empty"
        if 1<=index<=self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.delete_at_position(self._position(curser,self))
            
        else:
            raise IndexError

    def add_before_index(self,index,data):
        if not isinstance(index,int):
            raise TypeError("the index should be intger")

        if 1<=index<=self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.add_at_position(self._position(curser,self),data)        
        else:
            raise IndexError
    def add_after_index(self,index,data):
        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        
        if 1<=index<=self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.add_after_position(self._position(curser,self),data)
            
        else:
            raise IndexError
        
    def delete_before_index(self,index):
        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        if 2<=index<=self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.delete_before_position(self._position(curser,self))
            
        else:
              raise IndexError
        
    def delete_after_index(self,index):
        if  not isinstance(index,int):

            raise TypeError("the index shoud be intger")

        
        if 1<=index<self.size:
            curser=self.head
            for _ in range(index-1):
                curser=curser._next
            return self.delete_after_position(self._position(curser,self))
            
        else:
            raise IndexError
    def get_position_before(self,p):
      if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self :
        if p.node==self.head:
            return "no nodes before that position "
        else:
          
            return self._position(p.node._prev,self)
      else:
          raise TypeError("there is either type error or doesn't related to the concerned list")

    def get_position_after(self,p):
        if isinstance(p,doublly_positional_not_sentinel_list._position) and p.continer==self :
            if p.node==self.last:
               return "no nodes before that position "
            else:
               return self._position(p.node._next,self)
        else:
            raise TypeError("there is either type error or doesn't related to the concerned list")
    def reverse(self):
        if self.size==0 or self.size==1:
            return self
        self.last._next=self.last._prev
        self.last._prev=None
        pre_concerned=self.last
        for i in range(self.size-2):
            concerned=pre_concerned._next
            after_concerned=concerned._prev

            concerned._prev=pre_concerned
            concerned._next=after_concerned

            pre_concerned=concerned
        self.head._prev=self.head._next
        self.head._next=None

        self.head,self.last=self.last,self.head
      
        return self
    
    def reverse_another_way(self):
        if self.size==0 or self.size==1:
            return self
        curser=self.head
        last=self._node(0,self,None,curser)
        for _ in range(self.size):
            new_curser=curser._next
            curser._next=last
            curser._prev=None
            last._prev=curser

            last=curser
            curser=new_curser
        self.head._next=None
        
        old_last=self.last
        old_head=self.head
        self.last=old_head
        self.head=old_last
        return self
    
    def swap_data_at_positions(self,first,second):
        #here we swapping the values of the nodes without changing nodes' positions
        if isinstance(first,doublly_positional_not_sentinel_list._position) and isinstance(second,doublly_positional_not_sentinel_list._position) and first.continer==self and second.continer==self:
            first.node.data,second.node.data=second.node.data,first.node.data
        else:
            raise Exception("there problem either in the type of object inserted as position or existing that objects in the concerned list ")
 

    def swap_nodes(self,first,second):
        #here we swap the nodes themselves ..it sounds no differ than the previous one but in case of adding new features related to the nodes interactions ..that would be useful 

        if isinstance(first,doublly_positional_not_sentinel_list._position) and isinstance(second,doublly_positional_not_sentinel_list._position) and first.continer==self and second.continer==self :
           if  first.node!=second.node:
                if self.size!=0:
                  # 1&2 consecutive nodes
                  #1
                  if first.node._next==second.node :
                     #pre & next
                     pre=first.node._prev
                     next=second.node._next

                     #changing the pointers
                     first.node._prev=second.node
                     first.node._next=next
                     second.node._next=first.node
                     second.node._prev=pre
                     
                     #chaning the pointers related to the surrounding nodes 
                     if pre!=None:
                         pre._next=second.node
                     else:
                         self.head=second.node
                     if next!=None:
                         next._prev=first.node
                     else:
                         self.last=first.node
                     
                  #2
                  elif second.node._next==first.node:
                     #pre & next
                     pre=second.node._prev
                     next=first.node._next

                     #changing the pointers
                     second.node._prev=first.node
                     second.node._next=next
                     first.node._next=second.node
                     first.node._prev=pre
                     
                     #chaning the pointers related to the surrounding nodes 
                     if pre!=None:
                         pre._next=first.node
                     else:
                         self.head=first.node
                     if next!=None:
                         next._prev=second.node
                     else:
                         self.last=second.node

                  #3&4 handling the mutual node between both concerned nodes 
                  #3
                  elif  (  first.node._next==second.node._prev!=None):
                    
                      #saving the surrounding nodes
                      pre=first.node._prev
                      next=second.node._next
                      mutual=first.node._next
                     

                      #changing pointers of first and second
                      second.node._next=mutual
                      second.node._prev=pre
                      mutual._prev=second.node
                      mutual._next=first.node
                      first.node._prev=mutual
                      first.node._next=next

                      #the outer surrounding 
                      if pre!=None:
                          pre._next=second.node
                      else:
                          self.head=second.node
                      if next!=None:
                          next._prev=first.node
                      else:
                          self.last=first.node
                  #4
                  elif second.node._next==first.node._prev!=None:
                        #saving the surrounding nodes
                      pre=second.node._prev
                      next=first.node._next
                      mutual=second.node._next

                      #changing pointers of first and second
                      first.node._next=mutual
                      first.node._prev=pre
                      mutual._prev=first.node
                      mutual._next=second.node
                      second.node._prev=mutual
                      second.node._next=next

                      #the outer surrounding 
                      if pre!=None:
                          pre._next=first.node
                      else:
                          self.head=first.node
                      if next!=None:
                          next._prev=second.node
                      else:
                          self.last=second.node

                  else:
                      
                      #first_tracking the surrounding nodes 
                      pre_first=first.node._prev
                      next_first=first.node._next
                      

                      #second_tracking the surrounding nodes
                      pre_second=second.node._prev
                      next_second=second.node._next
                      #swapping nodes 
                      second.node._prev=pre_first
                      second.node._next=next_first
                      next_first._prev=second.node

                      first.node._next=next_second
                      first.node._prev=pre_second
                      pre_second._next=first.node


                      #handling special cases of self.head & self.last
                      if pre_first!=None:
                          pre_first._next=second.node
                      
                      if next_second!=None:
                          next_second._prev=first.node

                      if first.node==self.head and second.node==self.last:
                          self.head=second.node
                          self.last=first.node

                          return
                        
                      elif  first.node==self.last and second.node==self.head:
                            self.head=first.node
                            self.last=second.node

                            return 
                      
                      if first.node==self.head:
                          self.head=second.node
                          return
                      elif second.node==self.head:
                          self.head=first.node
                          return 
                      elif first.node==self.last:
                          self.last=second.node
                          return 
                      elif second.node==self.last:
                          self.last=first.node
                          return            
                else:
                   return"it's empty list nothing to swap"
           else:
               return"the positions shouldn't refer to the same node or we just have one node in the whole list "
        else:
            raise Exception("there problem either in the type of object inserted as position or existing that objects in the concerned list or even being both of them different to swap")
 

    def ordering_asending(self):

        def get_mid(first,new_size):
            curser=first
            for _ in range(new_size-1):
                curser=curser._next
            return curser

        def merge(left,right):
            curser_left=left.head
            curser_right=right.head
            new=doublly_positional_not_sentinel_list()
            while curser_left and curser_right:
                if curser_left.data<=curser_right.data:
                    new.add_last(curser_left.data)
                    curser_left=curser_left._next
                else:
                    new.add_last(curser_right.data)
                    curser_right=curser_right._next
            
            while curser_left:
                new.add_last(curser_left.data)
                curser_left=curser_left._next

            while curser_right:
                new.add_last(curser_right.data)
                curser_right=curser_right._next
        
            return new
        def helper(first,last,size):
            if size==1:
                new=doublly_positional_not_sentinel_list(first.data)
                return new 
            else:
                new_size=size//2
                l=get_mid(first,new_size)
                left_side=helper(first,l,new_size)
                right_side=helper(l._next,last,size-new_size)

                return merge(left_side,right_side)
         
        return helper(self.head,self.last,self.size)
    def ordering_desending(self):

        def get_mid(first,new_size):
            curser=first
            for _ in range(new_size-1):
                curser=curser._next
            return curser

        def merge(left,right):
            curser_left=left.head
            curser_right=right.head
            new=doublly_positional_not_sentinel_list()
            while curser_left and curser_right:
                if curser_left.data>=curser_right.data:
                    new.add_last(curser_left.data)
                    curser_left=curser_left._next
                else:
                    new.add_last(curser_right.data)
                    curser_right=curser_right._next
            
            while curser_left:
                new.add_last(curser_left.data)
                curser_left=curser_left._next

            while curser_right:
                new.add_last(curser_right.data)
                curser_right=curser_right._next
            
            return new


        def helper(first,last,size):
            if size==1:
                new=doublly_positional_not_sentinel_list(first.data)
                
                return new 
            
            else:
                new_size=size//2
                l=get_mid(first,new_size)
                left_side=helper(first,l,new_size)
                right_side=helper(l._next,last,size-new_size)

                return merge(left_side,right_side)
         
        return helper(self.head,self.last,self.size)

    def merge_with_changes(self,second):

        if isinstance(second,doublly_positional_not_sentinel_list):
        
            new_second=copy.deepcopy(second)
       
            self.last._next=new_second.head
            new_second.head._prev=self.last
            self.last=new_second.last
            self.size+=new_second.size

            return self

        else:
            raise TypeError(f"the list should be :{doublly_positional_not_sentinel_list}")

    def merge_no_changes(self,second):
        if isinstance(second,doublly_positional_not_sentinel_list):
            new_first=copy.deepcopy(self)
          
            new_second=copy.deepcopy(second)
       
            new_first.last._next=new_second.head
            new_second.head._prev=new_first.last
            new_first.last=new_second.last
            new_first.size+=new_second.size

            return new_first

        else:
            raise TypeError(f"the list should be :{doublly_positional_not_sentinel_list}")

    #info 

    def __repr__(self) -> str:
        if self.size==0:
            return "none"

        else:
            curser=self.head
            string=""
            while curser:
                
                string=string+f"({curser.data})"+"  "
                curser=curser._next
            return string
            
            
    def the_size(self):
        return self.size

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def search(self,data):
        if self.size==0:
            return "the list is empty nothing to find here"
        if isinstance(data,(int,float)):
            
            for i in self:
                
                if i.data==data:
                    return self._position(i,self)

        else:
            raise TypeError("this not numeric...absolutly we won't find it here")

    def first_node(self):
        return self.head

    def first_positon(self):
        return self._position(self.head,self)
    
    def last_node(self):
        return self.last
    
    def last_position(self):
        return self._position(self.last,self)

    def get_node_at_positon(self,p):
        if isinstance(p,doublly_positional_not_sentinel_list._position):
            return p.node
                
        else:
            raise TypeError("it's not position instance")

    def get_node_at_index(self,index):
         if isinstance(index,int):
             if 1<=index<=self.size:
                 counter=1
                 for i in self:
                     if counter==index:
                         return i
                     counter+=1
                    
             else:
                 raise IndexError("this index out of range")

         else:
             raise TypeError

    def __iter__(self):
        #iterting through tools of iteration for -comperhensive
        curser=self.head
        for i in range(self.size):
            yield curser
            curser=curser._next


x=doublly_positional_not_sentinel_list()
print(x)

z=x.change_at_position(x._position(x.head,x),1000)
print(x)
z=x.change_at_position(x._position(x.head,x),500)
print(x)

g=x.add_at_position(x._position(x.head,x),250)
print(g)
print(x)
g=x.add_at_position(x._position(x.last,x),300)
print(g)
print(x)
for i in range(10,0,-1):
    x.add_first(i)
    if x.size==1:
      print(x)
   

print(x)
x.delete_first()
print(x)

x.delete_last()
print(x)
print(x.delete_at_position(x._position(x.head._next._next._next,x)))
print(x)
print(x.delete_at_position(x._position(x.head,x)))
print(x)
print(x.delete_at_position(x._position(x.last,x)))
print(x)


x.delete_before_position(x._position(x.head._next,x))
print(x)
x.add_at_index(1,400)
x.add_at_index(x.size,2500)
x.add_at_index(x.size//2,222)
print(x)
print(x.head,x.last,x.size)
y=doublly_positional_not_sentinel_list(57)

y.add_before_index(1,60)
print(y)
print(y.head,y.last,y.size)
y.add_after_index(2,60)
print(y)
y.delete_before_index(2)
print(y)
print(y.head,y.last,y.size)
print(y.delete_after_index(1))
print(x)
print(x.reverse())
print(x.reverse_another_way())
print(x.head._next,x.head._prev)
print(y.add_first(100))
print(y)
print(y.reverse())
print(y.reverse_another_way())
y.swap_data_at_positions(y._position(y.head,y),y._position(y.last,y))
print(y)

z=doublly_positional_not_sentinel_list()
z.add_first(500)
z.add_last(1000)
z.add_last(1500)
z.add_last(2000)
z.add_last(2500)
z.add_last(3000)
print(z)
print(z.head._next,z.last._prev)
(z.swap_nodes(z._position(z.last._prev,z),z._position(z.head._next,z)))
print(z)
g=z.search(1)
print(g,type(g))

g=z.get_node_at_index(z.size)
print(g,type(g))
print(x)
print(y)
print(x.merge_no_changes(y))
print(x)
print(y)
print(x.merge_with_changes(y))

print("\n")
print(x)
print(x.ordering_asending())
print(x.ordering_desending())
print(x)

