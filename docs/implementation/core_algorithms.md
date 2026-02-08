# Core Algorithms Documentation

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines the core algorithms used throughout the JARVIS Master Agent system. Algorithms are specified at a high level with pseudocode and implementation guidance.

---

## Table of Contents

1. [Workflow Execution Algorithm](#workflow-execution-algorithm)
2. [Pattern Extraction Algorithm](#pattern-extraction-algorithm)
3. [Droid Assignment Algorithm](#droid-assignment-algorithm)
4. [Authentication Token Generation](#authentication-token-generation)
5. [Rate Limiting Algorithm](#rate-limiting-algorithm)
6. [Search Algorithm](#search-algorithm)

---

## Workflow Execution Algorithm

### Purpose

Execute workflows step-by-step with error handling, retry logic, and state management.

### Algorithm

```
FUNCTION ExecuteWorkflow(workflow_id):
    workflow = LoadWorkflow(workflow_id)

    IF workflow.status != 'pending':
        RETURN Error("Workflow not in pending status")

    workflow.status = 'running'
    workflow.started_at = NOW()
    SaveWorkflow(workflow)

    PublishMessage('lumina.workflows', {
        type: 'WorkflowStatusUpdate',
        workflow_id: workflow_id,
        status: 'running'
    })

    FOR EACH step IN workflow.steps ORDER BY step.order:
        step.status = 'running'
        step.started_at = NOW()
        SaveStep(step)

        TRY:
            result = ExecuteStep(step)
            step.status = 'completed'
            step.completed_at = NOW()
            step.result = result
            SaveStep(step)

            PublishMessage('lumina.workflows', {
                type: 'WorkflowStatusUpdate',
                workflow_id: workflow_id,
                status: 'running',
                current_step: step.step_id,
                progress: CalculateProgress(workflow)
            })

        CATCH error:
            step.status = 'failed'
            step.error = error.message
            step.completed_at = NOW()
            SaveStep(step)

            workflow.status = 'failed'
            workflow.error = error.message
            workflow.completed_at = NOW()
            SaveWorkflow(workflow)

            PublishMessage('lumina.workflows', {
                type: 'WorkflowCompleted',
                workflow_id: workflow_id,
                status: 'failed',
                error: error.message
            })

            RETURN Error("Workflow failed at step: " + step.step_id)

    workflow.status = 'completed'
    workflow.completed_at = NOW()
    workflow.execution_time = CalculateExecutionTime(workflow)
    SaveWorkflow(workflow)

    PublishMessage('lumina.workflows', {
        type: 'WorkflowCompleted',
        workflow_id: workflow_id,
        status: 'completed',
        execution_time: workflow.execution_time
    })

    RETURN Success(workflow)
END FUNCTION
```

### Implementation Notes

- **State Management**: Workflow state persisted after each step
- **Error Handling**: Failures at any step stop workflow execution
- **Progress Tracking**: Progress calculated as (completed_steps / total_steps) * 100
- **Async Support**: Algorithm supports both sync and async execution
- **Retry Logic**: Step-level retry handled by ExecuteStep function

---

## Pattern Extraction Algorithm

### Purpose

Extract patterns from R5 knowledge entries using frequency analysis and relationship detection.

### Algorithm

```
FUNCTION ExtractPatterns(entry):
    patterns = []

    // Extract n-grams (1-gram, 2-gram, 3-gram)
    ngrams = ExtractNGrams(entry.content, max_n=3)

    FOR EACH ngram IN ngrams:
        // Check if ngram matches existing pattern
        existing_pattern = FindPattern(ngram)

        IF existing_pattern:
            existing_pattern.frequency += 1
            existing_pattern.last_seen = NOW()
            UpdatePattern(existing_pattern)

            // Create occurrence record
            CreateOccurrence({
                pattern_id: existing_pattern.id,
                entry_id: entry.id,
                context: GetContext(entry, ngram),
                confidence: CalculateConfidence(ngram, entry)
            })
        ELSE:
            // Create new pattern
            new_pattern = CreatePattern({
                pattern_id: GenerateUUID(),
                name: ngram,
                frequency: 1,
                first_seen: NOW(),
                last_seen: NOW(),
                categories: entry.categories,
                metadata: {
                    source: entry.source,
                    initial_context: GetContext(entry, ngram)
                }
            })

            patterns.append(new_pattern)

    // Detect relationships between patterns
    relationships = DetectRelationships(patterns)

    FOR EACH relationship IN relationships:
        UpdatePatternRelationships(relationship)

    RETURN patterns
END FUNCTION

FUNCTION ExtractNGrams(text, max_n):
    ngrams = []
    words = Tokenize(text)

    FOR n FROM 1 TO max_n:
        FOR i FROM 0 TO (words.length - n):
            ngram = words[i:i+n].join(' ')
            ngrams.append(ngram)

    RETURN ngrams
END FUNCTION

FUNCTION DetectRelationships(patterns):
    relationships = []

    FOR EACH pattern1 IN patterns:
        FOR EACH pattern2 IN patterns:
            IF pattern1.id != pattern2.id:
                similarity = CalculateSimilarity(pattern1, pattern2)

                IF similarity > THRESHOLD:
                    relationship = {
                        pattern1_id: pattern1.id,
                        pattern2_id: pattern2.id,
                        relationship_type: DetermineRelationshipType(similarity),
                        strength: similarity
                    }
                    relationships.append(relationship)

    RETURN relationships
END FUNCTION
```

### Implementation Notes

- **N-gram Extraction**: Extracts 1-grams, 2-grams, and 3-grams from text
- **Frequency Tracking**: Tracks pattern frequency and last seen timestamp
- **Relationship Detection**: Detects similar and related patterns
- **Confidence Scoring**: Calculates confidence score for pattern matches
- **Performance**: Algorithm optimized for batch processing

---

## Droid Assignment Algorithm

### Purpose

Assign workflows to appropriate droids based on workload, capabilities, and priority.

### Algorithm

```
FUNCTION AssignDroid(workflow):
    // Get available droids
    available_droids = GetDroids({
        status: 'available',
        capabilities: workflow.required_capabilities
    })

    IF available_droids.length == 0:
        // No available droids, check busy droids with capacity
        busy_droids = GetDroids({
            status: 'busy',
            capabilities: workflow.required_capabilities,
            queue_length: '< 10'  // Has capacity
        })

        IF busy_droids.length == 0:
            RETURN Error("No droids available")

        available_droids = busy_droids

    // Score each droid
    scored_droids = []

    FOR EACH droid IN available_droids:
        score = CalculateDroidScore(droid, workflow)
        scored_droids.append({droid: droid, score: score})

    // Sort by score (highest first)
    scored_droids.sort(key=lambda x: x.score, reverse=True)

    // Select best droid
    selected_droid = scored_droids[0].droid

    // Assign workflow
    workflow.droid_assigned = selected_droid.droid_id
    selected_droid.current_workflows += 1

    IF selected_droid.current_workflows > 0:
        selected_droid.status = 'busy'

    SaveWorkflow(workflow)
    SaveDroid(selected_droid)

    PublishMessage('helpdesk.coordination', {
        type: 'DroidAssignment',
        workflow_id: workflow.id,
        droid_id: selected_droid.droid_id
    })

    RETURN selected_droid
END FUNCTION

FUNCTION CalculateDroidScore(droid, workflow):
    score = 0

    // Workload factor (lower is better)
    workload_factor = droid.current_workflows + droid.queue_length
    score += (10 - workload_factor) * 10

    // Success rate factor
    score += droid.success_rate * 20

    // Processing time factor (faster is better)
    avg_time = droid.average_processing_time
    IF avg_time > 0:
        time_factor = max(0, 60 - avg_time) / 60  // Normalize to 0-1
        score += time_factor * 15

    // Priority match factor
    IF workflow.priority == 'critical' AND droid.type == 'IG-88':
        score += 30  // IG-88 for critical workflows

    IF workflow.priority == 'high' AND droid.type IN ['K-2SO', 'IG-88']:
        score += 20

    // Preference factor
    IF workflow.droid_preference == droid.droid_id:
        score += 25

    RETURN score
END FUNCTION
```

### Implementation Notes

- **Load Balancing**: Distributes work across available droids
- **Capability Matching**: Only considers droids with required capabilities
- **Priority Handling**: Critical workflows prefer specialized droids (IG-88)
- **Workload Consideration**: Considers current workload and queue length
- **Performance Metrics**: Uses success rate and processing time in scoring

---

## Authentication Token Generation

### Purpose

Generate JWT access tokens and refresh tokens for user authentication.

### Algorithm

```
FUNCTION GenerateAccessToken(user, device):
    // Create JWT payload
    payload = {
        sub: user.id,
        username: user.username,
        permissions: user.permissions,
        iat: NOW().timestamp(),
        exp: (NOW() + 1 HOUR).timestamp(),
        jti: GenerateUUID(),
        device_id: device.id
    }

    // Get signing secret from Key Vault
    secret = GetSecretFromKeyVault('jwt-secret-key')

    // Sign token
    token = JWT.encode(payload, secret, algorithm='HS256')

    // Store token metadata
    StoreTokenMetadata({
        token_jti: payload.jti,
        user_id: user.id,
        device_id: device.id,
        expires_at: payload.exp,
        created_at: NOW()
    })

    RETURN token
END FUNCTION

FUNCTION GenerateRefreshToken(user, device):
    // Generate random token
    token = GenerateCryptographicallySecureRandomString(64)

    // Hash token
    token_hash = BCrypt.hash(token)

    // Store refresh token
    StoreRefreshToken({
        token_hash: token_hash,
        user_id: user.id,
        device_id: device.id,
        expires_at: (NOW() + 30 DAYS).timestamp(),
        created_at: NOW()
    })

    RETURN token
END FUNCTION

FUNCTION ValidateToken(token):
    TRY:
        // Get secret from Key Vault
        secret = GetSecretFromKeyVault('jwt-secret-key')

        // Decode and verify token
        payload = JWT.decode(token, secret, algorithms=['HS256'])

        // Check expiration
        IF payload.exp < NOW().timestamp():
            RETURN Error("Token expired")

        // Check revocation
        token_metadata = GetTokenMetadata(payload.jti)
        IF token_metadata.is_revoked:
            RETURN Error("Token revoked")

        RETURN Success(payload)

    CATCH error:
        RETURN Error("Invalid token: " + error.message)
END FUNCTION
```

### Implementation Notes

- **JWT Standard**: Uses JWT (JSON Web Token) standard
- **HS256 Algorithm**: Uses HMAC-SHA256 for signing
- **Token Expiration**: Access tokens expire in 1 hour
- **Refresh Tokens**: Long-lived (30 days) for token renewal
- **Revocation**: Tokens can be revoked and checked
- **Security**: Secrets stored in Azure Key Vault

---

## Rate Limiting Algorithm

### Purpose

Implement rate limiting to prevent API abuse and ensure fair resource usage.

### Algorithm

```
FUNCTION CheckRateLimit(user_id, endpoint):
    // Get rate limit configuration
    config = GetRateLimitConfig(endpoint)

    // Get current window
    window_start = GetCurrentWindowStart(config.window_size)

    // Get request count for current window
    key = f"ratelimit:{endpoint}:{user_id}:{window_start}"
    count = Redis.INCR(key)

    IF count == 1:
        // First request in window, set expiration
        Redis.EXPIRE(key, config.window_size)

    // Check if limit exceeded
    IF count > config.limit:
        RETURN Error({
            code: "RATE_LIMIT_EXCEEDED",
            message: "Rate limit exceeded",
            retry_after: CalculateRetryAfter(window_start, config.window_size),
            limit: config.limit,
            remaining: 0
        })

    RETURN Success({
        limit: config.limit,
        remaining: config.limit - count,
        reset: window_start + config.window_size
    })
END FUNCTION

FUNCTION GetCurrentWindowStart(window_size):
    current_time = NOW().timestamp()
    window_start = (current_time // window_size) * window_size
    RETURN window_start
END FUNCTION

FUNCTION CalculateRetryAfter(window_start, window_size):
    next_window = window_start + window_size
    retry_after = next_window - NOW().timestamp()
    RETURN max(0, retry_after)
END FUNCTION
```

### Implementation Notes

- **Sliding Window**: Uses fixed window rate limiting
- **Redis Storage**: Uses Redis for distributed rate limiting
- **Per-Endpoint**: Different limits for different endpoints
- **Per-User**: Rate limits applied per user
- **Headers**: Returns rate limit info in response headers

---

## Search Algorithm

### Purpose

Search R5 knowledge base with relevance scoring and filtering.

### Algorithm

```
FUNCTION SearchR5(query, filters):
    // Tokenize query
    query_tokens = Tokenize(query)

    // Get matching entries
    matching_entries = []

    FOR EACH entry IN GetAllEntries():
        // Calculate relevance score
        score = CalculateRelevanceScore(entry, query_tokens, filters)

        IF score > MIN_RELEVANCE_THRESHOLD:
            matching_entries.append({
                entry: entry,
                score: score,
                matches: FindMatches(entry, query_tokens)
            })

    // Sort by relevance score
    matching_entries.sort(key=lambda x: x.score, reverse=True)

    // Apply pagination
    paginated_results = ApplyPagination(matching_entries, filters.limit, filters.offset)

    RETURN {
        results: paginated_results,
        total: matching_entries.length
    }
END FUNCTION

FUNCTION CalculateRelevanceScore(entry, query_tokens, filters):
    score = 0

    // Text match score
    FOR EACH token IN query_tokens:
        token_lower = token.lower()

        // Exact match in content
        IF token_lower IN entry.content.lower():
            score += 10

        // Match in title/category
        IF token_lower IN entry.category.lower():
            score += 5

        // Match in tags
        FOR EACH tag IN entry.tags:
            IF token_lower IN tag.lower():
                score += 3

    // Category filter
    IF filters.category AND entry.category == filters.category:
        score += 20

    // Tag filter
    IF filters.tags:
        matching_tags = Intersection(entry.tags, filters.tags)
        score += matching_tags.length * 5

    // Date range filter
    IF filters.date_range:
        IF entry.timestamp WITHIN filters.date_range:
            score += 10
        ELSE:
            RETURN 0  // Exclude if outside date range

    // Pattern match bonus
    IF entry.patterns:
        FOR EACH pattern IN entry.patterns:
            FOR EACH token IN query_tokens:
                IF token.lower() IN pattern.name.lower():
                    score += 15

    // Normalize score to 0-1
    normalized_score = min(1.0, score / 100.0)

    RETURN normalized_score
END FUNCTION

FUNCTION FindMatches(entry, query_tokens):
    matches = {
        query_terms: query_tokens,
        matched_sections: []
    }

    // Find matching sections in content
    content_lower = entry.content.lower()

    FOR EACH token IN query_tokens:
        token_lower = token.lower()
        positions = FindAllPositions(content_lower, token_lower)

        FOR EACH position IN positions:
            // Extract context around match
            start = max(0, position - 50)
            end = min(len(content_lower), position + len(token_lower) + 50)
            context = entry.content[start:end]

            matches.matched_sections.append(context)

    RETURN matches
END FUNCTION
```

### Implementation Notes

- **Relevance Scoring**: Multi-factor relevance scoring
- **Token Matching**: Case-insensitive token matching
- **Filtering**: Supports category, tag, and date range filters
- **Pagination**: Results paginated for performance
- **Context Extraction**: Extracts context around matches

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
