from preorder import generatePreorder

# Initialise test example:
inorder = [4, 2, 1, 5, 3]; 
postorder = [4, 2, 5, 3, 1]; 

# Generate preorder for test Example
print("Generate Preorder Test Result:")
generatePreorder(len(inorder), inorder, postorder)
print()
