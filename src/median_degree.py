# This python program runs successfully with Python 3.5.1.
#
# The program is for Insight Data Engineering Program - Coding Challenge.
# The challenge is about Venmo payments, which requires calculation of median degree of
# a vertex in a user relationship graph and keep updating it each time a new payment is
# read from a input file, across a 60-second window of transaction time (exclusive).

import json
import time
class PaymentNode:
	def __init__(self,ptime,target,actor):
		"""Form unit for a linked list of payments arranged with payment time.""" 
		self.userpair=tuple(sorted([actor,target]))
		self.ptime=ptime
		self.next=None
class LinkedList:
	def __init__(self):
		"""
		Initialize an object that includes all important information of
		the linked list of payments, including two dictionaries to represent
		adjacency list and degree of vertex for the user relationship graph.
		"""
		self.head=None     # First payment node
		self.tail=None     # Last payment node
		self.user_deg={}   # Key is username, value is degree of vertex in graph.
		self.edge_red={}   # Key is user pair (tuple), value is number of transactions (redundancy).
	def addNode(self,node):
		"""
		Add a new payment node into linked list of payments, which may involve -
		find the right position for new node;
		insert the new node;
		remove nodes out of the order, i.e. older than 60 seconds;
		use user pair information in new node to update graph information.
		"""
		if self.head==None:
			self.head=node
			self.tail=node
		else:
			node0=self.findPosition(node)
			if node0==None:
				node.next=self.head
				self.head=node
			else:
				node.next=node0.next
				node0.next=node
				if node.next==None:
					self.tail=node
					while (node.ptime-self.head.ptime)>=60:
						self.removeHead()
		if node.userpair in self.edge_red:
			self.edge_red[node.userpair]+=1
		else:
			self.edge_red[node.userpair]=1
			for username in node.userpair:
				if username in self.user_deg:
					self.user_deg[username]+=1
				else:
					self.user_deg[username]=1
	def removeHead(self):
		"""Remove the first node in the linked list and update graph information."""
		self.edge_red[self.head.userpair]-=1
		if self.edge_red[self.head.userpair]==0:
			del self.edge_red[self.head.userpair]
			for username in self.head.userpair:
				self.user_deg[username]-=1
				if self.user_deg[username]==0:
					del self.user_deg[username]
		self.head=self.head.next
	def findPosition(self,node):
		"""Find the node in the linked list after which the new node should be inserted."""
		if node.ptime<self.head.ptime:
			return None
		if node.ptime>=self.tail.ptime:
			return self.tail
		np=self.head
		while np.next and node.ptime>=np.next.ptime:
			np=np.next
		return np
	def medianDegree(self):
		"""Calculate the median value of degrees of vertexes."""
		degree=list(self.user_deg.values())
		degree.sort()
		n=len(degree)
		return (degree[(n-1)//2]+degree[n//2])/2.0
def main(inputfile,outputfile):
	"""
	Read payment information, one line each time from input file, process the data to update
	payment list and user relationship graph, and write updated median degree to output file.
	"""
	fr=open(inputfile,'r')
	fw=open(outputfile,'w')
	n_ve=0                        # Record number of rows with missing data or errors.
	paylist=LinkedList()          # Initilize an empty payment list object.
	for line in fr:
		try:                  # Exception handling to exclude transactions with missing values.
			parsed_json=json.loads(line)
			time_str=parsed_json["created_time"]
			target_str=parsed_json["target"]
			actor_str=parsed_json["actor"]
			ptime=time.mktime(time.strptime(time_str,"%Y-%m-%dT%H:%M:%SZ"))
			target=target_str.lower().strip()
			actor=actor_str.lower().strip()
		except ValueError:
			n_ve+=1
			continue
		if not target or not actor:    # Exclude transactions with missing username (empty or space only).
			n_ve+=1
			continue
		newnode=PaymentNode(ptime,target,actor)
		if paylist.head==None:
			paylist.addNode(newnode)
			s=format(paylist.medianDegree(),'.2f')+'\n'
			fw.write(s)
		else:
			elapsedseconds=newnode.ptime-paylist.tail.ptime
			if elapsedseconds<=-60.0:
				fw.write(s)
				continue
			else:
				paylist.addNode(newnode)
				s=format(paylist.medianDegree(),'.2f')+'\n'
				fw.write(s)
	fw.close()
	fr.close()
	print("Data processed with ",n_ve," rows of value missings/errors")
	return

if __name__=='__main__':
	import sys
	main(sys.argv[1],sys.argv[2])
