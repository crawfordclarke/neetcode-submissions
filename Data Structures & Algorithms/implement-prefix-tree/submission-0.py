class PrefixTree:

    def __init__(self):
        self.trie = {}

        

    def insert(self, word: str) -> None:
        current = self.trie
        for i,character in enumerate(word):
            if character not in current:
                current[character] = {"children":{}, "is_word":False }
                if i == len(word)-1:
                    current[character]["is_word"] = True  
                current = current[character]["children"]
            else:
                if i == len(word)-1:
                    current[character]["is_word"] = True    
                current = current[character]["children"]


    def search(self, word: str) -> bool:
        current = self.trie

        for character in word:
            if character not in current:
                return False
            node = current[character]    
            current = current[character]["children"]
        return node["is_word"]    
           
        

    def startsWith(self, prefix: str) -> bool:
        current = self.trie

        for character in prefix:
            if character not in current:
                return False  
            current = current[character]["children"]
        return True
           


        
        