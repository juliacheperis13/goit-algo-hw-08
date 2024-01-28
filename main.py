import heapq


def calculate(cables):
    total_cost = 0
    heapq.heapify(cables)

    while len(cables) > 1:
        cost = heapq.heappop(cables) + heapq.heappop(cables)
        total_cost = cost + total_cost

        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    cables = [5, 22, 1, 6, 4, 9]
    print(calculate(cables))
