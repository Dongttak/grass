def solution(tickets):
    tickets.sort()  # (from, to) 사전순 정렬
    n = len(tickets)
    used = [False] * n
    path = ["ICN"]

    def dfs(cur, used_count):
        # 종료조건: 티켓을 다 썼으면 경로 완성
        if used_count == n:
            return True  # 찾았다고 위로 알림

        for i in range(n):
            if not used[i] and tickets[i][0] == cur:
                used[i] = True
                path.append(tickets[i][1])

                if dfs(tickets[i][1], used_count + 1):
                    return True  # 첫 정답(사전순 최소)면 바로 끝

                # 원상복구(백트래킹)
                path.pop()
                used[i] = False

        return False

    dfs("ICN", 0)
    return path