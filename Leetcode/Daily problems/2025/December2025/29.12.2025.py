class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        def generate_combinations(char_dict):
            keys = list(char_dict.keys())
            lists = [char_dict[k] for k in keys]
            return ["".join(combo) for combo in product(*lists)]

        @lru_cache
        def f(s):
            n = len(s)
            if n==1:
                return True
            d = defaultdict(list)
            for i in range(n-1):
                found = False
                for j in 'ABCDEF':
                    if s[i:i+2]+j in allowed:
                        d[i].append(j)
                        found =  True
                if found == False:
                    return False
            xx = generate_combinations(d)
            for i in xx:
                if f(i)==True:
                    return True
            return False
        return f(bottom)
