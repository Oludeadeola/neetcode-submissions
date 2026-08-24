class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] #crate an empty list
        for s in strs:
            res.append(str(len(s)))
            res.append("*")
            res.append(s)
        return "".join(res)   

    def decode(self, s: str) -> List[str]:
        i =0
        res = []#create the empty set to decode
        while i <len(s):
            j =i


            while s[j]!="*": #keep running while s[J] is  not equal to "*"
                j+=1
            lenght = int(s[i:j]) 
            i = j+1
            j = i+lenght
            res.append(s[i:j])
            i = j
        return res 


            


        
