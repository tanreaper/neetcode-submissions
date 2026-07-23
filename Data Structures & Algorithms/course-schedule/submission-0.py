class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        in_progress = set()
        fully_done = set()

        def dfs(course):
            in_progress.add(course)

            for neighbor in graph[course]:
                if neighbor in in_progress:
                    return True
                if neighbor not in fully_done:
                    if dfs(neighbor):
                        return True
            in_progress.remove(course)
            fully_done.add(course)
            return False

        for course in range(numCourses):
            if course not in fully_done:
                if dfs(course):
                    return False
        return True