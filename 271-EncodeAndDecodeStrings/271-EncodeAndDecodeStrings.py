# Last updated: 11/11/2025, 1:57:01 AM
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        string = ""
        for i in range(len(strs)):
            string += str(len(strs[i])) + "#" + strs[i]
        return string

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ds = []
        i = 0
        while i < len(s):
            subnum = ""
            while s[i].isnumeric():
                subnum += s[i]
                i += 1
            num = int(subnum)
            i += 1
            ds.append(s[i:i+num])
            i += num
        return ds
        
                


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))