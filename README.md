# Reddit Consumer Trends

A lightweight Python project for discovering and analyzing emerging consumer trends using publicly available Reddit discussions, subject to authorized API access.

**Status:** Early prototype — API access pending approval.

## Overview

Reddit Consumer Trends is designed to help users identify growing interest in products, consumer technologies, and emerging topics across selected Reddit communities.

The application focuses on aggregated discussion activity rather than profiling individual users.

## Planned Features

- Retrieve permitted public posts and metadata through the official Reddit Data API.
- Monitor selected communities related to gadgets, consumer electronics, home products, and 3D printing.
- Measure discussion frequency and engagement.
- Compare topic activity across different time periods.
- Identify emerging consumer interests.
- Generate structured trend reports.
- Respect API rate limits and data retention requirements.

## Prototype Workflow

1. Load a small demonstration dataset.
2. Group discussions by consumer topic.
3. Calculate post counts and engagement totals.
4. Compare recent activity against an earlier period.
5. Rank topics by growth.
6. Export results as JSON.

## Example Output

| Topic | Previous posts | Recent posts | Growth |
|---|---:|---:|---:|
| Smart home devices | 12 | 27 | +125% |
| 3D printing accessories | 8 | 19 | +137.5% |
| Portable electronics | 15 | 24 | +60% |

*Illustrative sample data, not actual Reddit API results.*

## Technology

- Python 3.11+
- JSON-based reports
- Modular data processing
- Optional Reddit OAuth integration after authorization

## Reddit API Integration

The application is intended to use Reddit's official Data API only after the necessary permissions have been granted.

The initial prototype operates with demonstration data and does not require Reddit credentials.

## Privacy and Compliance

The application is designed to produce aggregated topic-level insights, avoid individual user profiling, and follow applicable Reddit API terms, privacy requirements, and data deletion obligations.

## Development Status

This project is under development. Live Reddit API integration is not currently enabled.
