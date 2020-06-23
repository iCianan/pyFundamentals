def nodeDepth(root):
    return calculateNodeDepth(root, 0)

def calculateNodeDepth(node, depth):
  if node is None: return 0
  return depth + calculateNodeDepth(node.left, depth + 1) + calculateNodeDepth(node.right, depth + 1)
  

def main():
  test = 'abc'
  key = 2
  print(caesarCipherEncryptor(test, key))


if __name__ == "__main__":
  main()
