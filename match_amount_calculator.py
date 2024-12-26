def compute_total_comparisons(n):
    total_min_comparisons = 0
    total_max_comparisons = 0
    total_avg_comparisons = 0.0

    for k in range(1, n):
        depths = [0] * k

        def helper(left, right, depth):
            if left >= right:
                return
            mid = (left + right) // 2
            depths[mid] = depth
            helper(left, mid, depth + 1)
            helper(mid + 1, right, depth + 1)

        helper(0, k, 1)

        min_depth = min(depths)
        max_depth = max(depths)
        avg_depth = sum(depths) / k

        total_min_comparisons += min_depth
        total_max_comparisons += max_depth
        total_avg_comparisons += avg_depth

    return total_min_comparisons, total_max_comparisons, total_avg_comparisons

if __name__ == '__main__':
    n = int(input("Enter the number of ideas: "))
    min_comparisons, max_comparisons, avg_comparisons = compute_total_comparisons(n)

    print(f"Minimum total comparisons: {min_comparisons}")
    print(f"Maximum total comparisons: {max_comparisons}")
    print(f"Average total comparisons: {avg_comparisons:.2f}")
