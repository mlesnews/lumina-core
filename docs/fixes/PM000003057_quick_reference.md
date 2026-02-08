# PM000003057: Quick Reference Guide - Agent History Features

## Overview

This guide provides quick reference for using the new agent history features: search, pin/unpin, and timeout protection.

---

## 🔍 Search Agent History

### API Usage
```typescript
// Search with keyword
const result = await apiClient.searchAgentHistory("keyword", 20, 0);

// Result structure
{
  items: [...],      // Array of history items
  total: 100,        // Total number of results
  hasMore: true,     // Whether more results exist
  offset: 0,         // Current offset
  limit: 20          // Results per page
}

// Load next page
const nextPage = await apiClient.searchAgentHistory("keyword", 20, 20);
```

### Python Usage
```python
from agent_history_manager import AgentHistoryManager

manager = AgentHistoryManager()

# Search with pagination
result = manager.search_histories(
    keyword="search_term",
    limit=20,
    offset=0
)

# Access results
items = result["items"]
total = result["total"]
has_more = result["hasMore"]
```

---

## 📌 Pin/Unpin Agent History

### API Usage
```typescript
// Pin a history
await apiClient.pinAgentHistory("history_123");

// Unpin a history
await apiClient.unpinAgentHistory("history_123");

// Get all pinned histories
const pinned = await apiClient.getPinnedAgentHistories();
```

### Python Usage
```python
# Pin history
manager.pin_history("history_123")

# Unpin history
manager.unpin_history("history_123")

# Get pinned histories
pinned = manager.get_pinned_histories()
```

---

## 📖 Get Agent History

### API Usage
```typescript
// Get history by ID (with timeout protection)
try {
    const history = await apiClient.getAgentHistory("history_123");
    // Use history data
} catch (error) {
    if (error.message === 'History retrieval timed out') {
        // Handle timeout
    }
}
```

### Python Usage
```python
# Get history by ID
history = manager.get_history_by_id("history_123")

if history:
    # Use history data
    print(history.agent_name)
    print(history.pinned)
```

---

## ⏱️ Timeout Configurations

### Default Timeouts
- **Default**: 30 seconds (general API calls)
- **Search**: 60 seconds (search operations)
- **History Retrieval**: 45 seconds (loading history items)

### Customizing Timeouts
```typescript
// In apiClient.ts, modify these constants:
private defaultTimeout: number = 30000;  // 30 seconds
private searchTimeout: number = 60000;   // 60 seconds
private historyTimeout: number = 45000;  // 45 seconds
```

---

## 🎨 Frontend UI Usage

### Search Interface
1. Enter keyword in search input
2. Click "Search" button or press Enter
3. Results display with pagination controls
4. Click "Previous" or "Next" to navigate pages

### Pin/Unpin Interface
1. Each history item has a "Pin" or "Unpin" button
2. Click button to toggle pin status
3. Pinned items have a colored left border
4. Status updates immediately

### Loading History Details
1. Click on a history item to load full details
2. Details open in a new panel or modal
3. Timeout protection prevents indefinite hangs

---

## 🔗 API Endpoints

### Search
```
GET /api/v1/agent/history/search?keyword={keyword}&limit={limit}&offset={offset}
Authorization: Bearer {token}
```

### Get History
```
GET /api/v1/agent/history/{history_id}
Authorization: Bearer {token}
```

### Pin History
```
POST /api/v1/agent/history/{history_id}/pin
Authorization: Bearer {token}
```

### Unpin History
```
POST /api/v1/agent/history/{history_id}/unpin
Authorization: Bearer {token}
```

### Get Pinned Histories
```
GET /api/v1/agent/history/pinned
Authorization: Bearer {token}
```

---

## ⚠️ Error Handling

### Timeout Errors
```typescript
// Search timeout
if (error.code === 'ECONNABORTED') {
    vscode.window.showErrorMessage('Search request timed out. Try a more specific query.');
}

// History retrieval timeout
if (error.message === 'History retrieval timed out') {
    // Handle timeout - maybe show partial data or retry
}
```

### Not Found Errors
```python
# Python
history = manager.get_history_by_id("invalid_id")
if history is None:
    print("History not found")
```

---

## 📊 Best Practices

### Search
1. Use specific keywords for better results
2. Use pagination for large result sets
3. Limit results per page (20-50 items)
4. Cache search results when possible

### Pin/Unpin
1. Pin important histories for quick access
2. Unpin when no longer needed
3. Use pinned histories list for quick navigation
4. Pin status persists across sessions

### Performance
1. Use pagination to avoid loading all results
2. Set appropriate timeout values for your network
3. Handle timeout errors gracefully
4. Consider caching frequently accessed histories

---

## 🧪 Testing

### Run Test Suite
```bash
python scripts/python/test_agent_history_api.py
```

### Test Coverage
- ✅ Search functionality (4 tests)
- ✅ Pin/Unpin functionality (4 tests)
- ✅ Get history by ID (2 tests)
- ✅ Error handling (2 tests)
- **Total**: 12 tests, 100% pass rate

---

## 📚 Related Documentation

- `docs/fixes/PM000003057_agent_history_fixes.md` - Initial fixes
- `docs/fixes/PM000003057_implementation_complete.md` - Implementation details
- `docs/fixes/PM000003057_test_results.md` - Test results

---

**Tags**: #QUICK_REFERENCE #AGENT_HISTORY #PIN_UNPIN #SEARCH #API @JARVIS @LUMINA

**Created**: 2026-01-15  
**Ticket**: PM000003057
