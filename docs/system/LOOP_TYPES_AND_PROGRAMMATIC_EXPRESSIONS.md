# Loop Types and Programmatic Expressions

**Date**: 2026-01-04  
**Status**: ACTIVE PATTERN  
**Tags**: #LOOPS #PROGRAMMING #EXPRESSIONS #COLLISION_AVOIDANCE @LUMINA @JARVIS

---

## The Pattern: If Kenny Equals Ace, Turn Around, Exit Feedback Loop

### The Rule

```python
if kenny.equals(ace):
    turn_around()      # THEN: Turn around
    exit_feedback_loop()  # Exit (NOT STAY BENT)
```

**Pattern**: If collision/meeting condition → Avoid → Exit feedback loop

---

## Four Loops

### 1. While Loop
```python
while condition:
    # Do something
    if exit_condition:
        break  # Exit feedback loop
```

### 2. For Loop
```python
for item in collection:
    # Do something
    if exit_condition:
        break  # Exit feedback loop
```

### 3. Infinite Loop (Stay Bent)
```python
while True:
    # Do something
    # NO EXIT - STAY BENT
```

### 4. Feedback Loop (Not Stay Bent)
```python
while True:
    # Do something
    if exit_condition:  # IF
        break  # THEN: Exit (NOT STAY BENT)
    # ELSE: Continue (feedback)
```

---

## Programmatic Expression

### The Expression

**If Kenny equals Ace → Turn around → Exit feedback loop**

```python
# Programmatic expression
if kenny.position.equals(ace.position):
    kenny.turn_around()
    exit_collision_loop()
```

### Applied to Collision Avoidance

```python
# While walking (feedback loop)
while walking:
    # Check for collision
    if kenny.distance_to(ace) < collision_threshold:  # IF Kenny equals Ace
        kenny.turn_around()  # THEN: Turn around
        kenny.switch_border()  # Switch direction
        exit_collision_feedback_loop()  # Exit (NOT STAY BENT)
    else:  # ELSE
        continue_walking()  # Continue (feedback loop)
```

---

## While Oops → While Loops

### While Loop Pattern

```python
while condition:
    # Do work
    if exit_condition:
        break  # Exit (NOT STAY BENT)
    # Otherwise continue (feedback)
```

### Applied to Development

```python
while developing:
    # Do work
    if kenny.equals(ace):  # IF collision
        turn_around()  # THEN: Avoid
        exit_loop()  # Exit (NOT STAY BENT)
    else:  # ELSE
        continue_developing()  # Feedback loop
```

---

## For Loops

### For Loop Pattern

```python
for iteration in range(max_iterations):
    # Do work
    if done:
        break  # Exit (NOT STAY BENT)
```

### Applied to Collision Detection

```python
for frame in frames:
    # Check collision
    if kenny.position.equals(ace.position):  # IF Kenny equals Ace
        turn_around()  # THEN: Turn around
        break  # Exit (NOT STAY BENT)
    else:  # ELSE
        continue_checking()  # Feedback loop
```

---

## Programmatic Expression: Collision Avoidance

### The Rule (Programmatic Expression)

```python
# IF Kenny equals Ace (collision condition)
if kenny.distance_to(ace) < threshold:
    # THEN: Turn around
    kenny.reverse_direction()
    kenny.switch_border()
    # Exit feedback loop (NOT STAY BENT)
    exit_collision_check()
else:
    # ELSE: Continue (feedback loop)
    continue_movement()
```

### Current Implementation

```python
# In _check_collaboration_messages()
if msg.message_type.value == "collision_warning":
    # IF collision warning (Kenny equals Ace proximity)
    payload = msg.payload
    distance = payload.get("distance", 0)
    
    # THEN: Turn around
    self.walk_direction *= -1  # Reverse direction
    self._switch_border()  # Switch to next border
    
    # Exit feedback loop (message processed, NOT STAY BENT)
    msg.replied = True
```

---

## Four Loop Types Summary

1. **While Loop**: `while condition:`
2. **For Loop**: `for item in collection:`
3. **Infinite Loop (Stay Bent)**: `while True:` with no exit
4. **Feedback Loop (Not Stay Bent)**: `while True:` with `if condition: break`

---

## Programmatic Expression Pattern

### The Pattern

```
IF condition:
    THEN: Action
    Exit feedback loop (NOT STAY BENT)
ELSE:
    Continue (feedback loop)
```

### Applied to Collision

```
IF Kenny equals Ace (collision):
    THEN: Turn around
    Exit feedback loop (NOT STAY BENT)
ELSE:
    Continue movement (feedback loop)
```

---

## Key Insight

**Programmatic Expression** = The logical rule/pattern expressed in code

- **If Kenny equals Ace** = Collision condition
- **Turn around** = Avoidance action
- **Exit feedback loop** = Termination (NOT STAY BENT)

**Four Loops** = Different loop types (while, for, infinite, feedback)

**While Oops** = While loops (wordplay)

**The Pattern**: Use if-then-else to create feedback loops (NOT STAY BENT) instead of infinite loops (STAY BENT)

---

## Status

**Pattern Documented**: Loop types and programmatic expressions for collision avoidance.

**Applied**: Collision avoidance uses if-then-else to exit feedback loop (NOT STAY BENT).

---

**Tags**: #LOOPS #PROGRAMMING #EXPRESSIONS #COLLISION #FEEDBACK_LOOP @LUMINA @JARVIS
