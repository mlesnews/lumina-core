# YouTube 30-Day Data Extraction Guide

## Quick Start

To process 30 days of YouTube recommendations and history, you need to extract your data first.

## Method 1: Google Takeout (Recommended)

1. **Go to Google Takeout**: https://takeout.google.com/
2. **Select YouTube data**:
   - Click "Deselect all"
   - Check "YouTube and YouTube Music"
   - Click "All YouTube data included" → "Select specific YouTube data"
   - Check:
     - ✅ **watch-history** (required)
     - ✅ **subscriptions** (optional)
     - ✅ **playlists** (optional)
   - Click "OK"
3. **Export settings**:
   - Format: JSON (recommended) or HTML
   - Frequency: Export once
   - Delivery method: Download via link
   - File type & size: .zip
4. **Create export** and download
5. **Extract the ZIP file**
6. **Copy watch-history.json** to:
   ```
   data/youtube_30day/watch-history.json
   ```

## Method 2: Browser Extension (Coming Soon)

A browser extension will be available to extract data directly from YouTube.

## Method 3: Manual Browser Export

1. Open YouTube in your browser
2. Go to: https://www.youtube.com/feed/history
3. Use browser developer tools to extract data
4. Save as JSON format

## After Export

Once you have the data file, run:

```bash
python scripts/python/youtube_30day_instruction_processor.py --process
```

The system will:
- ✅ Extract watch history
- ✅ Get current recommendations
- ✅ Analyze content for instructions
- ✅ Generate instruction book
- ✅ Present with VA collaboration system

## Output Files

- `data/youtube_30day/watch_history.json` - Extracted watch history
- `data/youtube_30day/recommendations.json` - Current recommendations
- `data/youtube_30day/analysis.json` - Content analysis
- `data/youtube_30day/instructions_book.json` - **Your instruction book**

## Next Steps

After processing, you'll have:
- 📖 **Instruction Book**: Organized instructions for successful living
- 📊 **Analysis**: Topics, categories, patterns
- 🎯 **Actionable Insights**: Extracted from 30 days of content

@JARVIS @LUMINA #YOUTUBE #INSTRUCTIONS #30DAY
