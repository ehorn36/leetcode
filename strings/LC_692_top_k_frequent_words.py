class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        # Add words to hashmap and count frequency
        hashmap = {}
        for word in words:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1

        # Sort hashmap by descending value -hashmap[x], then by alphabetical value x
        sorted_hashmap = sorted(hashmap.keys(), key=lambda x: (-hashmap[x], x))

        return sorted_hashmap[:k]




