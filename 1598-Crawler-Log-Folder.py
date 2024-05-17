class Solution:
    def minOperations(self, logs: list[str]) -> int:
        child = 0

        for log in logs:
            if log == "./":
                continue

            if log == "../":
                if child > 0:
                    child -= 1
                continue

            child +=1
        return child