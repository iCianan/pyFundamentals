def groupAnagrams(words):
    anagrams = {}
    for word in words:
      sortedWord = "".join(sorted(word))
      if sortedWord in anagrams:
        anagrams[sortedWord].append(word)
      else:
        anagrams[sortedWord] = [word];
    return list(anagrams.values())

def main():
    print(groupAnagrams(["yo","act", "flop","tac","cat","oy","olfp"]))

if __name__ == "__main__":
    main()
    
