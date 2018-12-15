class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s)==0 or len(words)==0:
            return []

        dict_of_words={}
        length_of_s=len(s)
        length_of_words = len(words)
        for w in words:
            if w in dict_of_words:
                dict_of_words[w]+=1
            else:
                dict_of_words[w] = 1


        window=len(words[0])*length_of_words
        i=0
        sol=[]
        while i < length_of_s-window+1:
            subs=s[i:i+window]
            dict_of_word_used=self.getListOfWords(subs,length_of_words,dict_of_words)




            if dict_of_words==dict_of_word_used:
                sol.append(i)
                i=i+1
            else:
                i=i+1
        return sol



    def getListOfWords(self,subs,len_of_words,dict_of_words):
        length_of_subs=len(subs)
        i=0
        last_index = int(length_of_subs / len_of_words)
        dict_of_word_used = {}
        while i < length_of_subs:
            word=subs[i:i+last_index]
            i=i+last_index
            if word not in dict_of_words:
                    is_sol = False
                    break
            if word in dict_of_word_used:
                    dict_of_word_used[word] += 1
            else:
                    dict_of_word_used[word] = 1
        return dict_of_word_used

a=Solution()
print(a.findSubstring("foobarfoo",["foo","bar"]))