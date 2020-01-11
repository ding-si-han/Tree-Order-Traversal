def generatePreorder(length, inorder, postorder):
    # Try Catch to lookout for unexpected error: Root not found in inorder
    try:
        head = inorder.index(postorder[length - 1])
    except :
        print("Error: Element not found in list")
    
    # Print out root
    print(postorder[length - 1], end = " ")

    # Print out left side if available
    if head != 0:
        generatePreorder(len(inorder[:head]), inorder[:head], postorder[:head])
    
    # Print out right side if available
    if head != length - 1 :
        generatePreorder(len(inorder[head+1:]), inorder[head + 1:], postorder[head:-1])


  