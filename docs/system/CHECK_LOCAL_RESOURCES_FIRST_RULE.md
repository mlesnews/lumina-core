# ✅ Check Local Resources First - Critical Rule Implementation

**Date**: 2026-01-28
**Status**: ✅ **IMPLEMENTED**

---

## 🚨 Problem Statement

**PRIMARY PET PEEVE #1**: When given a request, AI often:
1. ❌ Doesn't check local resources first
2. ❌ Rushes out and writes dirty code or dirty documentation
3. ❌ Leaves a HOT MESS

---

## ✅ Solution Implemented

### Rule Created

**File**: `.cursor/rules/check_local_resources_first.mdc`

**Priority**: `critical`
**Always Apply**: `true`

### Integration

**Added to**: `.cursorrules` (main rules file)

**Location**: Top of file, right after header

---

## 📋 Mandatory Workflow

### Step 1: Search Before Creating

**BEFORE writing ANY code or documentation:**

1. **Search for existing implementations**
   - Use `codebase_search` to find similar functionality
   - Use `grep` to find related code patterns
   - Use `glob_file_search` to find related files
   - Check `docs/` directory for existing documentation

2. **Check for existing systems**
   - Look for similar scripts in `scripts/python/`
   - Check `config/` for existing configurations
   - Review `data/` for existing data structures
   - Examine `.cursor/rules/` for related rules

3. **Review existing patterns**
   - Read existing code to understand patterns
   - Check documentation for established conventions
   - Look for integration points with existing systems

### Step 2: Understand Before Modifying

**BEFORE modifying existing code:**

1. **Read the entire file first**
   - Use `read_file` to read the complete file
   - Understand the structure and purpose
   - Identify dependencies and integrations

2. **Check for related files**
   - Find imports and dependencies
   - Locate related modules
   - Review test files if they exist

3. **Understand the context**
   - Read documentation
   - Check git history if relevant
   - Review related issues or tickets

### Step 3: Integrate Before Creating

**BEFORE creating new files:**

1. **Check if functionality already exists**
   - Search for similar functionality
   - Check if it's in a different location
   - Verify if it needs extension vs. replacement

2. **Use existing patterns**
   - Follow established code patterns
   - Use existing data structures
   - Follow naming conventions

3. **Integrate with existing systems**
   - Connect to existing APIs
   - Use existing logging systems
   - Follow existing error handling patterns

---

## 🎯 Mandatory Checklist

**Before writing ANY code/documentation, you MUST:**

- [ ] Search codebase for existing implementations
- [ ] Check `docs/` for existing documentation
- [ ] Review `scripts/python/` for similar scripts
- [ ] Check `config/` for existing configurations
- [ ] Read related files to understand context
- [ ] Verify integration points with existing systems
- [ ] Follow established patterns and conventions

---

## 🚫 Prohibited Behaviors

**NEVER:**

- ❌ Write code without searching for existing implementations
- ❌ Create documentation without checking existing docs
- ❌ Create new files without checking for similar functionality
- ❌ Modify files without reading them first
- ❌ Ignore existing patterns and conventions
- ❌ Leave "hot messes" - clean up after yourself

---

## ✅ Required Behaviors

**ALWAYS:**

- ✅ Search first, code second
- ✅ Read existing code before modifying
- ✅ Check documentation before creating new docs
- ✅ Follow existing patterns
- ✅ Integrate with existing systems
- ✅ Clean up after yourself

---

## 📊 Example Workflows

### Bad Workflow (❌ DON'T DO THIS):
```
User: "Create a validation system"
AI: *Immediately writes new code*
Result: Dirty code, duplicates existing functionality, hot mess
```

### Good Workflow (✅ DO THIS):
```
User: "Create a validation system"
AI:
  1. Searches codebase for "validation"
  2. Finds existing validation scripts
  3. Reads existing validation code
  4. Checks documentation for validation patterns
  5. Identifies integration points
  6. Extends existing system OR creates new with proper integration
  7. Follows established patterns
Result: Clean code, proper integration, no mess
```

---

## 🔍 Search Strategy

**When given a request, search for:**

1. **Exact matches**: Search for the exact functionality requested
2. **Similar patterns**: Search for similar functionality
3. **Related systems**: Find systems that might integrate
4. **Documentation**: Check for existing documentation
5. **Configuration**: Look for existing configs
6. **Data structures**: Check for existing data models

---

## 💡 Key Principles

**"Check local resources first" is not optional - it's MANDATORY.**

**Time spent searching is time saved cleaning up messes.**

**Better to find existing code than to write duplicate code.**

**Better to extend existing systems than to create new ones.**

**Better to follow patterns than to create new patterns.**

---

## 📁 Files Created/Modified

1. ✅ `.cursor/rules/check_local_resources_first.mdc` - New rule file
2. ✅ `.cursorrules` - Updated with critical rule reference
3. ✅ `docs/system/CHECK_LOCAL_RESOURCES_FIRST_RULE.md` - This documentation

---

## 🎯 Success Criteria

**This rule is successful when:**

- ✅ AI always searches before writing code
- ✅ AI reads existing files before modifying
- ✅ AI checks for existing functionality before creating
- ✅ AI follows established patterns
- ✅ AI integrates with existing systems
- ✅ No "hot messes" are left behind

---

**Status**: ✅ **RULE IMPLEMENTED AND ACTIVE**

**This rule applies to ALL code and documentation work.**

**Violation of this rule results in dirty code, duplicate functionality, and hot messes.**

**ALWAYS check local resources first.**
