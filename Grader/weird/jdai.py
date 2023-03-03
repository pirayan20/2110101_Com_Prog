# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self,head=None):
#         self.head = head

#     def print(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data)
#             temp = temp.next

#     def count(self):
#         count = 0
#         temp = self.head
#         while temp is not None:
#             count += 1
#             temp = temp.next
#         return count

# class Stack(LinkedList):
#     def __init__(self,head=None):
#         self.head = head

#     def is_empty(self):
#         return self.head is None

#     def push(self,node):
#         node.next = self.head
#         self.head = node

#     def pop(self):
#         if not self.is_empty():
#             node = self.head
#             self.head = self.head.next
#             return node


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling