# Last updated: 11/11/2025, 1:57:03 AM
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        reverse_adj_list = {c: [] for word in words for c in word}

        for first_word, second_word in zip(words, words[1:]):
            for c,d in zip(first_word, second_word):
                if c!= d:
                    reverse_adj_list[d].append(c)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""

        seen = {}
        output = []
        def visit(node):
            if node in seen:
                return seen[node]

            seen[node] = False
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False
            seen[node] = True
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)

        
        