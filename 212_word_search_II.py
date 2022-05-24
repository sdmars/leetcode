class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def adj(i, j):
            ls = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            ans = []
            for ni, nj in ls:
                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue
                ans.append((ni, nj))
            return ans

        def backtrack(i, j, par):
            letter = board[i][j]
            curNode = par[letter]

            word_matched = curNode.pop(WORD_KEY, False)
            if word_matched != False:
                matched.append(word_matched)

            # mark as visited
            board[i][j] = '#'

            for ni, nj in adj(i, j):
                if not board[ni][nj] in curNode:
                    continue
                backtrack(ni, nj, curNode)

            # restore cell status
            board[i][j] = letter

            if not curNode:
                par.pop(letter)

        WORD_KEY = '$'
        trie = {}

        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        n, m = len(board), len(board[0])
        matched = []

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return matched
