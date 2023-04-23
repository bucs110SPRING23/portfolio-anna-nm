class StringUtility(): 
    def __init__(self, string = None): 
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self): 
        vowel = ['a', 'e', 'o', 'u', 'i']
        count = 0
        for i in self.string: 
            if i in vowel: 
                count += 1
        if count < 5: 
            return str(count)
        else: 
            return 'many'
    def bothEnds(self): 
        result = self.string[:2] + self.string[-2:]
        if len(result) < 2: 
            return ''
        else: 
            return result
    def fixStart(self): 
        if len(self.string) <= 1: 
            return self.string
        start = self.string[0]
        fixed = start 
        for i in range(1, len(self.string)): 
            if self.string[i] == start: 
                fixed += '*'
            else: 
                fixed += self.string[i]
        return fixed
    def asciiSum(self): 
        total = 0
        for char in self.string: 
            total += ord(char)
        return total
    def cipher(self): 
        length = len(self.string)
        encoded = ''
        for char in self.string: 
            if char.isalpha() == False: 
                encoded += char
            else: 
                base = ord('a') if char.islower() else ord('A')
                after = chr(base + (ord(char) - base + length) % 26)
                encoded += after
        return encoded





