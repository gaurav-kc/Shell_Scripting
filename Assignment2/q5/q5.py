sum_all=0

class tree_node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def word_for_num(n):
	n = str(n)
	length = (len(n))
	if length is 0:
		print("No number")
	ones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
	twos = ["","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]              
	big = ["hundred","thousand"]

	if(length == 1):
		print(ones[ord(n[0])-48])
		return
	x=0
	while(x<(len(n))):
		if(length >= 3):
			if((ord(n[x])-48)!= 0):
				print(ones[ord(n[x])-48],end=" ")
				print(big[length-3],end=" ")
			length = length-1
		else:
			if(ord(n[x])-48 == 1):
				temp = (ord(n[x])-48 + ord(n[x+1])-48)
				print(twos[temp])
				return
			elif(ord(n[x])-48 == 2 and ord(n[x+1]) -48 == 0):
				print("twenty")
				return
			else:
				k = ord(n[x])-48
				if(k>0):
					print(tens[k],end=" ")
				else:
					print("",end=" ")
				x = x+1
				if(ord(n[x])-48 != 0):
					print(ones[ord(n[x])-48])
		x = x+1			


def leftside(root):
	global sum_all
	if(root is None):
		return root
	if(root.left is None and root.right is None):
		return
	if(root.left):
		word_for_num(root.data)
		sum_all = sum_all + root.data
		leftside(root.left)
	else:
		word_for_num(root.data)
		sum_all = sum_all + root.data
		leftside(root.right)

def rightside(root):
	global sum_all
	if(root is None):
		return root
	if(root.left is None and root.right is None):
		return
	if(root.right):
		rightside(root.right)
		sum_all = sum_all + root.data
		word_for_num(root.data)
	else:
		rightside(root.left)
		sum_all = sum_all + root.data
		word_for_num(root.data)

def leaves(root):
	global sum_all
	if(root is not None):
		leaves(root.left)
		if(root.left is None and root.right is None):
			sum_all = sum_all + root.data
			word_for_num(root.data)
		leaves(root.right)

def display(root):
	global sum_all
	sum_all = sum_all - root.data
	print("Order in which the Repellant is to be applied is : ")
	leftside(root)
	leaves(root)
	rightside(root)

def inorder(root):
	if(root == None):
		return
	inorder(root.left)
	print(root.data);
	inorder(root.right)

def maketree(root,a,i,n):
	if i < n:
		if(a[i] == -1):
		  	return None
		temp = tree_node(a[i])
		root = temp
		root.left = maketree(root.left,a,2*i+1,n)
		root.right = maketree(root.right,a,2*i+2,n)
	return root	


n = int(input())
g = n
nodes = []
while(g):
	f = int(input())
	nodes.append(f)
	if f == '-1':
		n = n - 1
	g = g - 1
# print(n,g);	
root=None	
root = maketree(root,nodes,0,n)
sum_all = 0
display(root)
print("\nTotal repellant  : ",end="")
word_for_num(sum_all)





























# root = tree_node(40) 
# root.left = tree_node(20) 
# root.left.left = tree_node(10) 
# root.left.right = tree_node(30) 
# root.left.left.right = tree_node(5) 
# root.left.left.right.right = tree_node(45) 
# root.right = tree_node(60) 
# root.right.right = tree_node(70)
# root.right.left=tree_node(50)
# root.right.left.right=tree_node(55) 