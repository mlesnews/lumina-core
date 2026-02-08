# WakaTime Sharing Features - Complete Setup Guide

## Overview

This guide covers all WakaTime sharing features available for the LUMINA project. WakaTime allows you to share your coding statistics through various methods including badges, charts, goals, insights, and more.

## Table of Contents

1. [Repo Badges](#repo-badges)
2. [Project Badges](#project-badges)
3. [Embeddable Charts](#embeddable-charts)
4. [Goals](#goals)
5. [Insights](#insights)
6. [Animated GIFs](#animated-gifs)
7. [Email Reports](#email-reports)
8. [JSON API](#json-api)

---

## 1. Repo Badges

Share collaborator's code time in a repository.

### Setup

1. Go to [WakaTime Share Page](https://wakatime.com/share)
2. Navigate to "Repo Badges" section
3. Select your repository
4. Copy the badge markdown code

### Usage in README

Add to your `README.md`:

```markdown
![WakaTime](https://wakatime.com/badge/github/username/repo-name.svg)
```

### Example

```markdown
![WakaTime](https://wakatime.com/badge/github/mlesn/.lumina.svg)
```

### Customization Options

- **Time Range**: Last 7 days, last 30 days, all time
- **Style**: Flat, flat-square, plastic
- **Color**: Custom colors available

---

## 2. Project Badges

Share your code time per project.

### Setup

1. Ensure your project has a `.wakatime-project` file (already configured for LUMINA)
2. Go to WakaTime dashboard → Settings → Projects
3. Enable public sharing for your project
4. Copy the badge URL

### Current Configuration

- **Project Name**: LUMINA (from `.wakatime-project` file)
- **Badge URL Format**: `https://wakatime.com/badge/user/{user_id}/project/{project_name}.svg`

### Usage in README

```markdown
![WakaTime](https://wakatime.com/badge/user/{user_id}/project/LUMINA.svg)
```

### Example Badge

```markdown
[![wakatime](https://wakatime.com/badge/user/{user_id}/project/LUMINA.svg)](https://wakatime.com/@username/projects/LUMINA)
```

---

## 3. Embeddable Charts

Real-time charts for your website or documentation.

### Setup

1. Go to WakaTime dashboard
2. Navigate to Settings → Embeddable Charts
3. Create a new chart or use existing ones
4. Copy the embed code

### Chart Types Available

- **Coding Activity**: Daily/weekly/monthly coding time
- **Languages**: Language breakdown pie chart
- **Projects**: Project time distribution
- **Editors**: Editor usage statistics
- **Operating Systems**: OS usage breakdown

### Usage in Documentation

#### HTML Embed

```html
<iframe
  src="https://wakatime.com/share/@username/{chart_id}.svg"
  width="600"
  height="400"
  frameborder="0"
  style="border: 1px solid #ddd; border-radius: 4px;">
</iframe>
```

#### Markdown (GitHub)

```markdown
![WakaTime Chart](https://wakatime.com/share/@username/{chart_id}.svg)
```

### Chart Configuration

- **Time Range**: Last 7 days, last 30 days, last year, all time
- **Chart Type**: Bar, line, pie, donut
- **Theme**: Light, dark
- **Size**: Customizable width and height

---

## 4. Goals

Share your personal programming goals.

### Setup

1. Go to WakaTime dashboard → Goals
2. Create a new goal (e.g., "Code 20 hours this week")
3. Enable public sharing
4. Copy the goal badge URL

### Goal Types

- **Daily Goals**: Code X hours per day
- **Weekly Goals**: Code X hours per week
- **Monthly Goals**: Code X hours per month
- **Streak Goals**: Code X days in a row

### Usage

```markdown
[![WakaTime Goal](https://wakatime.com/badge/user/{user_id}/goal/{goal_id}.svg)](https://wakatime.com/@username/goals/{goal_id})
```

### Example Goals for LUMINA

- **Weekly Coding**: 20+ hours per week
- **Daily Consistency**: Code every day
- **Project Focus**: 80%+ time on LUMINA project

---

## 5. Insights

Tweet insights and fun facts about your code stats.

### Setup

1. Go to WakaTime dashboard → Insights
2. Browse available insights
3. Click "Share" on any insight
4. Choose platform (Twitter/X, LinkedIn, etc.)

### Insight Types

- **Weekly Summary**: Total hours, top languages, top projects
- **Fun Facts**: Interesting statistics about your coding habits
- **Achievements**: Milestones reached
- **Comparisons**: This week vs last week

### Automation

You can automate insight sharing using the WakaTime API:

```python
import requests

def share_weekly_insight():
    """Share weekly coding insight automatically."""
    # Use WakaTime API to get insights
    # Post to social media via API
    pass
```

---

## 6. Animated GIFs

Show how your coding has progressed over time.

### Setup

1. Go to WakaTime dashboard → Share → Animated GIFs
2. Select time range (last 7 days, 30 days, etc.)
3. Choose chart type
4. Generate and download GIF
5. Upload to your repository or documentation

### Usage

```markdown
![Coding Progress](https://raw.githubusercontent.com/username/repo/main/docs/wakatime-progress.gif)
```

### Best Practices

- Update GIFs weekly or monthly
- Use consistent time ranges for comparison
- Include in project documentation or README

---

## 7. Email Reports

Send your weekly coding reports to others by email.

### Setup

1. Go to WakaTime dashboard → Settings → Email Reports
2. Add recipient email addresses
3. Configure report frequency (weekly, monthly)
4. Customize report content

### Report Content

- **Summary Statistics**: Total hours, languages, projects
- **Daily Breakdown**: Hours per day
- **Language Distribution**: Pie chart of languages
- **Project Time**: Time spent per project
- **Top Editors**: Editor usage statistics

### Automation

Email reports are automatically sent based on your schedule. No additional setup required once configured.

---

## 8. JSON API

Build your own charts using WakaTime's public JSON API.

### API Endpoints

#### Get Summary

```bash
curl "https://wakatime.com/api/v1/users/current/summaries?start=2024-01-01&end=2024-01-31" \
  -H "Authorization: Basic {api_key}"
```

#### Get Stats

```bash
curl "https://wakatime.com/api/v1/users/current/stats/last_7_days" \
  -H "Authorization: Basic {api_key}"
```

#### Get Projects

```bash
curl "https://wakatime.com/api/v1/users/current/projects" \
  -H "Authorization: Basic {api_key}"
```

### Python Integration Example

```python
"""
PUBLIC: WakaTime API Integration
Location: scripts/python/wakatime_integration.py
License: MIT
"""

import requests
from typing import Dict, Any
from datetime import datetime, timedelta
import base64


class WakaTimeAPI:
    """WakaTime API client for LUMINA project."""

    def __init__(self, api_key: str):
        """
        Initialize WakaTime API client.

        Args:
            api_key: WakaTime API key
        """
        self.api_key = api_key
        self.base_url = "https://wakatime.com/api/v1"
        self.headers = {
            "Authorization": f"Basic {base64.b64encode(api_key.encode()).decode()}"
        }

    def get_summary(
        self,
        start_date: str,
        end_date: str,
        project: str = "LUMINA"
    ) -> Dict[str, Any]:
        """
        Get coding summary for date range.

        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            project: Project name filter

        Returns:
            Summary data dictionary
        """
        url = f"{self.base_url}/users/current/summaries"
        params = {
            "start": start_date,
            "end": end_date,
            "project": project
        }

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_stats(self, range_type: str = "last_7_days") -> Dict[str, Any]:
        """
        Get coding statistics.

        Args:
            range_type: Time range (last_7_days, last_30_days, etc.)

        Returns:
            Stats data dictionary
        """
        url = f"{self.base_url}/users/current/stats/{range_type}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_projects(self) -> Dict[str, Any]:
        """
        Get all projects.

        Returns:
            Projects data dictionary
        """
        url = f"{self.base_url}/users/current/projects"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_custom_chart_data(self, days: int = 30) -> Dict[str, Any]:
        """
        Create custom chart data for LUMINA project.

        Args:
            days: Number of days to include

        Returns:
            Chart-ready data structure
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        summary = self.get_summary(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
            project="LUMINA"
        )

        # Process data for charting
        chart_data = {
            "labels": [],
            "datasets": [{
                "label": "Coding Hours",
                "data": []
            }]
        }

        # Extract daily data from summary
        for day in summary.get("data", []):
            chart_data["labels"].append(day.get("range", {}).get("date", ""))
            chart_data["datasets"][0]["data"].append(
                day.get("grand_total", {}).get("hours", 0)
            )

        return chart_data


def main():
    """Example usage of WakaTime API."""
    # Get API key from environment or config
    api_key = "YOUR_API_KEY_HERE"

    client = WakaTimeAPI(api_key)

    # Get last 7 days stats
    stats = client.get_stats("last_7_days")
    print(f"Total coding time: {stats.get('total_seconds', 0) / 3600:.2f} hours")

    # Get LUMINA project summary
    summary = client.get_summary("2024-01-01", "2024-01-31", project="LUMINA")
    print(f"LUMINA project summary: {summary}")


if __name__ == "__main__":
    main()
```

### API Key Setup

1. Go to WakaTime dashboard → Settings → API
2. Generate a new API key
3. Store securely (use Azure Key Vault for LUMINA)
4. Never commit API keys to repository

---

## Integration with LUMINA

### Configuration File

Create `config/wakatime_config.json`:

```json
{
  "_public_marker": "PUBLIC - WakaTime Configuration Template",
  "project_name": "LUMINA",
  "badges": {
    "enabled": true,
    "repo_badge": true,
    "project_badge": true
  },
  "charts": {
    "enabled": true,
    "embed_in_docs": true
  },
  "goals": {
    "enabled": true,
    "weekly_hours": 20
  },
  "email_reports": {
    "enabled": false,
    "recipients": []
  },
  "api": {
    "enabled": false,
    "api_key_storage": "azure_key_vault"
  }
}
```

### Automated Updates

Create a script to update badges and charts automatically:

```python
"""
PUBLIC: WakaTime Badge Updater
Location: scripts/python/update_wakatime_badges.py
License: MIT
"""

import json
from pathlib import Path
from datetime import datetime


def update_readme_badges(project_root: Path):
    """Update WakaTime badges in README."""
    readme_path = project_root / "README_LUMINA.md"

    if not readme_path.exists():
        return

    # Read current README
    content = readme_path.read_text(encoding="utf-8")

    # Add badges section if not present
    badge_section = """
## 📊 Coding Statistics

[![WakaTime](https://wakatime.com/badge/user/{user_id}/project/LUMINA.svg)](https://wakatime.com/@username/projects/LUMINA)

*Tracked with [WakaTime](https://wakatime.com)*
"""

    if "WakaTime" not in content:
        # Insert after main title
        content = content.replace(
            "# Lumina - Light Through Perfect Balance",
            f"# Lumina - Light Through Perfect Balance{badge_section}"
        )
        readme_path.write_text(content, encoding="utf-8")
        print(f"✅ Updated {readme_path} with WakaTime badges")


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent.parent
    update_readme_badges(project_root)
```

---

## Best Practices

1. **Privacy**: Only share statistics you're comfortable making public
2. **Consistency**: Update badges and charts regularly
3. **Documentation**: Include WakaTime setup in project documentation
4. **Automation**: Use scripts to keep badges updated
5. **Security**: Never commit API keys; use secure storage

---

## Resources

- [WakaTime Share Page](https://wakatime.com/share)
- [WakaTime API Documentation](https://wakatime.com/developers)
- [WakaTime Badge Generator](https://wakatime.com/badge)
- [WakaTime Dashboard](https://wakatime.com/dashboard)

---

## Next Steps

1. ✅ Configure `.wakatime-project` file (already done)
2. ⏳ Set up badges in README
3. ⏳ Create embeddable charts
4. ⏳ Set up coding goals
5. ⏳ Configure email reports (optional)
6. ⏳ Integrate JSON API (optional)

---

**Last Updated**: 2026-01-09
**Maintained by**: LUMINA Team
