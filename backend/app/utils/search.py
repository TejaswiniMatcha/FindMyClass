def calculate_score(text: str, query: str) -> int:
    """
    Simple relevance scoring for search results.
    Higher score = better match.
    """

    text = (text or "").lower().strip()
    query = (query or "").lower().strip()

    if not text or not query:
        return 0

    # Exact match
    if text == query:
        return 100

    # Starts with query
    if text.startswith(query):
        return 90

    # Contains query
    if query in text:
        return 75

    # Match individual words
    score = 0
    query_words = query.split()

    for word in query_words:
        if word in text:
            score += 20

    return score