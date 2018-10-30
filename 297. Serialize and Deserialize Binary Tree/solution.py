# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized_string = ""
        def dfs_serialize(node,serialized_string):

            if node is None:
                serialized_string+="null,"
                return serialized_string
            serialized_string+=str(node.val)+","
            serialized_string=dfs_serialize(node.left,serialized_string)
            serialized_string=dfs_serialize(node.right,serialized_string)
            return serialized_string
        return dfs_serialize(root,serialized_string)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list_of_data=data.split(',')
        
        def deserialize_dfs(list_of_data):

            if len(list_of_data)==0:
                return None

            if list_of_data[0] == 'null':
                list_of_data.pop(0)
                return None
            val = list_of_data[0]
            node = TreeNode(val)
            list_of_data.pop(0)
            node.left = deserialize_dfs(list_of_data)
            node.right = deserialize_dfs(list_of_data)
            return node
        return deserialize_dfs(list_of_data)




#Your Codec object will be instantiated and called as such:
codec = Codec()
root=codec.deserialize("1,2,3,null,null,4,null,None,5,None,None,")
print(codec.serialize(root))