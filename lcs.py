def lcs(list_a, list_b):
    """
    Compute the Longest Common Subsequence of two lists.

    Args:
        list_a: A list of elements (typically strings).
        list_b: Another list of elements (typically strings).

    Returns:
        A list containing the common elements in the order they appear
        in both input lists.

    Example:
        >>> lcs(['a', 'b', 'c'], ['a', 'x', 'b', 'y', 'c'])
        ['a', 'b', 'c']
    """
    m, n = len(list_a), len(list_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if list_a[i - 1] == list_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if list_a[i - 1] == list_b[j - 1]:
            result.append(list_a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result[::-1]