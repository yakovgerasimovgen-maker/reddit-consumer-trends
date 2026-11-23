
from collections import defaultdict

# Demonstration data — not retrieved from Reddit API.
posts = [
    {"topic": "Smart home", "period": "previous", "score": 35},
    {"topic": "Smart home", "period": "recent", "score": 72},
    {"topic": "3D printing", "period": "previous", "score": 28},
    {"topic": "3D printing", "period": "recent", "score": 65},
    {"topic": "Portable electronics", "period": "previous", "score": 42},
    {"topic": "Portable electronics", "period": "recent", "score": 56},
]

def analyze_trends(data):
    totals = defaultdict(lambda: {"previous": 0, "recent": 0})

    for post in data:
        totals[post["topic"]][post["period"]] += post["score"]

    results = []
    for topic, periods in totals.items():
        previous = periods["previous"]
        recent = periods["recent"]
        growth = (
            round((recent - previous) / previous * 100, 1)
            if previous else None
        )
        results.append({
            "topic": topic,
            "previous_engagement": previous,
            "recent_engagement": recent,
            "growth_percent": growth,
        })

    return sorted(
        results,
        key=lambda item: item["growth_percent"] or 0,
        reverse=True,
    )

if __name__ == "__main__":
    import json
    print(json.dumps(analyze_trends(posts), indent=2))
