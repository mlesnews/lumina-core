# 📇 Holocron Card Catalog Format

**TCC&DDS Format with Comma Separator**

---

## 🎯 Format Specification

### Card Catalog Number Format

**Format:** `[PREFIX-@CCDDS[#CARDCATALOG-DEWEYDECIMAL-ID+NUM#, TITLE]`

**Components:**
- **PREFIX** - Prefix identifier (default: `@ACS` for Agent Chat Session)
- **@CCDDS** - Card Catalog & Dewey-Decimal System identifier
- **#CARDCATALOG-DEWEYDECIMAL-ID+NUM#** - Base catalog number in brackets
- **Comma Separator** - `, ` (comma and space) to differentiate from title
- **TITLE** - Holocron entry title

---

## 📋 Format Breakdown

### Example

```
@ACS-@CCDDS[#CC-Ω-000-0001#, Test Title]
```

**Components:**
1. `@ACS` - Prefix (Agent Chat Session)
2. `-` - Separator
3. `@CCDDS` - Card Catalog & Dewey-Decimal System
4. `[` - Opening bracket
5. `#` - Hash marker
6. `CC-Ω-000-0001` - Base catalog number (CC-DEWEY-CHAPTER)
7. `#` - Hash marker
8. `, ` - **Comma separator** (differentiates catalog from title)
9. `Test Title` - Holocron title

---

## 🔧 Base Catalog Number

**Format:** `CC-{DEWEY}-{CHAPTER:04d}`

**Example:**
- `CC-Ω-000-0001` - Command & Control, Chapter 1
- `CC-Σ-001-0002` - Knowledge Management, Chapter 2
- `CC-000-0003` - Computer Science, Chapter 3

---

## 📝 Usage

### Create Holocron Entry

```bash
python scripts/python/holocron_compound_logging_system.py \
  --create "Title" "Content" "Ω-000" "1" "book,video" "laff_studio_1" "@ACS" \
  --save
```

**Parameters:**
1. `Title` - Holocron title
2. `Content` - Holocron content
3. `Ω-000` - Dewey classification
4. `1` - Chapter number
5. `book,video` - Media formats
6. `laff_studio_1` - @LAFF studio
7. `@ACS` - Prefix (optional, defaults to @ACS)

### Result

**Card Catalog Number:**
```
@ACS-@CCDDS[#CC-Ω-000-0001#, Title]
```

---

## 🎯 Why Comma Separator?

The comma separator (`, `) differentiates:
- **Catalog/Dewey-Decimal identifier** (before comma)
- **@ACS TITLE** (after comma)

This ensures clear parsing and prevents confusion between:
- Catalog number: `#CC-Ω-000-0001#`
- Title: `Title`

---

## 📊 Format Examples

### Different Prefixes

```bash
# Agent Chat Session
@ACS-@CCDDS[#CC-Ω-000-0001#, JARVIS Voice Status]

# Subagent Chat Session
@SACS-@CCDDS[#CC-Σ-001-0002#, Memory System Update]

# Custom Prefix
@CUSTOM-@CCDDS[#CC-Δ-002-0003#, Education Module]
```

---

## 🔍 Parsing the Format

### Extract Components

**Full Format:**
```
@ACS-@CCDDS[#CC-Ω-000-0001#, Test Title]
```

**Extracted:**
- **Prefix:** `@ACS`
- **System:** `@CCDDS`
- **Base Catalog:** `CC-Ω-000-0001`
- **Dewey:** `Ω-000`
- **Chapter:** `0001`
- **Title:** `Test Title`

---

## ✅ Benefits

1. **Clear Differentiation** - Comma separates catalog from title
2. **Parseable** - Easy to extract components
3. **Human Readable** - Clear format for humans
4. **Machine Readable** - Structured for parsing
5. **Flexible** - Supports different prefixes (@ACS, @SACS, custom)

---

## 📋 Implementation

### Code Location

**File:** `scripts/python/holocron_compound_logging_system.py`

**Method:** `create_holocron_entry()`

**Format Generation:**
```python
card_catalog_dewey_id = f"CC-{dewey_classification}-{chapter_number:04d}"
prefix = acs_prefix or "@ACS"
card_catalog_number = f"{prefix}-@CCDDS[#{card_catalog_dewey_id}#, {title}]"
```

---

## 🎯 Current Status

- ✅ Format implemented
- ✅ Comma separator added
- ✅ @CCDDS identifier included
- ✅ Prefix support (@ACS default)
- ✅ Base catalog number extraction
- ✅ Card catalog entry creation

---

**Tags:** #holocron #card_catalog #dewey_decimal #tcc #dds #format #comma_separator #@CCDDS

**Last Updated:** 2026-01-03

---

*"Format: [PREFIX-@CCDDS[#CARDCATALOG-DEWEYDECIMAL-ID+NUM#, TITLE] - Comma separator differentiates catalog from title."*
