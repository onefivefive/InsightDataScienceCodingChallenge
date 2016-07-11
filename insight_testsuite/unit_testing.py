# This test program is for unit tests of median_degree.py
# The focus is on methods of LinkedList class, which is the key portion of median_degree.py

import unittest
import sys
sys.path.append('../src')
from median_degree import PaymentNode,LinkedList

class TestLinkedListMethods(unittest.TestCase):
	def setUp(self):
		"""Setup a LinkedList object for all tests."""
		self.node1=PaymentNode(1100,"jack","mary")
		self.node2=PaymentNode(1103,"emily","mary")
		self.node3=PaymentNode(1135,"jack","mary")
		self.node4=PaymentNode(1140,"jack","nancy")
		self.node5=PaymentNode(1158,"mary","nancy")
		self.node1.next=self.node2
		self.node2.next=self.node3
		self.node3.next=self.node4
		self.node4.next=self.node5
		self.list0=LinkedList()
		self.list0.head=self.node1
		self.list0.tail=self.node5
		self.list0.user_deg={"emily":1,"jack":2,"mary":3,"nancy":2}
		self.list0.edge_red={("emily","mary"):1,("jack","mary"):2,("jack","nancy"):1,("mary","nancy"):1}
	def test_findPosition(self):
		nodenew=PaymentNode(1095,"mary","nancy")
		self.assertEqual(self.list0.findPosition(nodenew),None)
		nodenew=PaymentNode(1102,"mary","nancy")
		self.assertEqual(self.list0.findPosition(nodenew),self.node1)
		nodenew=PaymentNode(1140,"mary","nancy")
		self.assertEqual(self.list0.findPosition(nodenew),self.node4)
		nodenew=PaymentNode(1159,"mary","nancy")
		self.assertEqual(self.list0.findPosition(nodenew),self.node5)
	def test_removeHead(self):
		self.list0.removeHead()
		self.assertEqual(self.list0.head,self.node2)
		shared_items=set(self.list0.user_deg.items()) & set({"emily":1,"jack":2,"mary":3,"nancy":2}.items())
		self.assertEqual(len(shared_items),4)
		self.assertEqual(len(self.list0.user_deg),4)
		shared_items=set(self.list0.edge_red.items()) & set({("emily","mary"):1,("jack","mary"):1,("jack","nancy"):1,("mary","nancy"):1}.items())
		self.assertEqual(len(shared_items),4)
		self.assertEqual(len(self.list0.edge_red),4)
		self.list0.removeHead()
		self.assertEqual(self.list0.head,self.node3)
		shared_items=set(self.list0.user_deg.items()) & set({"jack":2,"mary":2,"nancy":2}.items())
		self.assertEqual(len(shared_items),3)
		self.assertEqual(len(self.list0.user_deg),3)
		shared_items=set(self.list0.edge_red.items()) & set({("jack","mary"):1,("jack","nancy"):1,("mary","nancy"):1}.items())
		self.assertEqual(len(shared_items),3)
		self.assertEqual(len(self.list0.edge_red),3)
	def test_addNode_1(self):
		nodenew=PaymentNode(1159,"emily","nancy")
		self.list0.addNode(nodenew)
		self.assertEqual(self.list0.tail,nodenew)
		shared_items=set(self.list0.user_deg.items()) & set({"emily":2,"jack":2,"mary":3,"nancy":3}.items())
		self.assertEqual(len(shared_items),4)
		self.assertEqual(len(self.list0.user_deg),4)
		shared_items=set(self.list0.edge_red.items()) & set({("emily","mary"):1,("emily","nancy"):1,("jack","mary"):2,("jack","nancy"):1,("mary","nancy"):1}.items())
		self.assertEqual(len(shared_items),5)
		self.assertEqual(len(self.list0.edge_red),5)
	def test_addNode_2(self):
		nodenew=PaymentNode(1099,"emily","mary")
		self.list0.addNode(nodenew)
		self.assertEqual(self.list0.head,nodenew)
		shared_items=set(self.list0.user_deg.items()) & set({"emily":1,"jack":2,"mary":3,"nancy":2}.items())
		self.assertEqual(len(shared_items),4)
		self.assertEqual(len(self.list0.user_deg),4)
		shared_items=set(self.list0.edge_red.items()) & set({("emily","mary"):2,("jack","mary"):2,("jack","nancy"):1,("mary","nancy"):1}.items())
		self.assertEqual(len(shared_items),4)
		self.assertEqual(len(self.list0.edge_red),4)
	def test_addNode_3(self):
		nodenew=PaymentNode(1100,"ann","jack")
		self.list0.addNode(nodenew)
		self.assertEqual(self.list0.head.next,nodenew)
		shared_items=set(self.list0.user_deg.items()) & set({"ann":1,"emily":1,"jack":3,"mary":3,"nancy":2}.items())
		self.assertEqual(len(shared_items),5)
		self.assertEqual(len(self.list0.user_deg),5)
		shared_items=set(self.list0.edge_red.items()) & set({("ann","jack"):1,("emily","mary"):1,("jack","mary"):2,("jack","nancy"):1,("mary","nancy"):1}.items())
		self.assertEqual(len(shared_items),5)
		self.assertEqual(len(self.list0.edge_red),5)
	def test_addNode_4(self):
		nodenew=PaymentNode(1170,"jack","nancy")
		self.list0.addNode(nodenew)
		self.assertEqual(self.list0.head,self.node3)
		shared_items=set(self.list0.user_deg.items()) & set({"jack":2,"mary":2,"nancy":2}.items())
		self.assertEqual(len(shared_items),3)
		self.assertEqual(len(self.list0.user_deg),3)
		shared_items=set(self.list0.edge_red.items()) & set({("jack","mary"):1,("jack","nancy"):2,("mary","nancy"):1}.items())
		self.assertEqual(len(shared_items),3)
		self.assertEqual(len(self.list0.edge_red),3)
	def test_addNode_5(self):
		nodenew=PaymentNode(1258,"emily","nancy")
		self.list0.addNode(nodenew)
		self.assertEqual(self.list0.head,nodenew)
		shared_items=set(self.list0.user_deg.items()) & set({"emily":1,"nancy":1}.items())
		self.assertEqual(len(shared_items),2)
		self.assertEqual(len(self.list0.user_deg),2)
		shared_items=set(self.list0.edge_red.items()) & set({("emily","nancy"):1}.items())
		self.assertEqual(len(shared_items),1)
		self.assertEqual(len(self.list0.edge_red),1)
	def test_medianDegree(self):
		nd=self.list0.medianDegree()
		self.assertEqual(nd,2.0)

if __name__=='__main__':
	unittest.main()
