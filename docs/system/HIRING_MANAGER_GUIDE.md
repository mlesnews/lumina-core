# JARVIS Hiring Manager System Guide

## Overview

Hiring Manager system for technical/financial opportunities that:
- Compares candidate skills to job requirements
- Matches candidates to appropriate role levels
- Evaluates grooming potential (promoting from lower positions)
- Uses #Merit-based assessment
- Implements compromise strategy (candidate grows, company provides opportunity)

## Role Levels (Power Structure)

1. **Junior Engineer** (Level 1) - High grooming potential
2. **Assistant Engineer** (Level 2) - High grooming potential ⭐
3. **Engineer** (Level 3) - Medium grooming potential
4. **Senior Engineer** (Level 4) - Medium grooming potential
5. **Lead Engineer** (Level 5) - Low grooming potential
6. **Principal Engineer** (Level 6) - Low grooming potential
7. **Architect** (Level 7) - Very low grooming potential

## #Merit Assessment

The system uses **#Merit** (case-insensitive) for evaluation:

- **Technical Skills** (30%): Average skill level across domains
- **Experience** (25%): Years of relevant experience
- **Achievements** (20%): Notable accomplishments
- **Growth Potential** (15%): Ability to grow and learn
- **Cultural Fit** (10%): Alignment with company culture

**Merit Levels**:
- 85-100: EXCEPTIONAL
- 70-84: HIGH
- 55-69: GOOD
- 40-54: ADEQUATE
- 0-39: NEEDS_IMPROVEMENT

## Grooming Strategy

**Compromise Approach**:
- Candidate takes lower position to grow
- Company provides opportunity and mentorship
- Both parties invest in growth
- Success based on **#Merit** (their own merit)

**Grooming Criteria**:
- Growth Potential ≥ 70%
- Merit Score ≥ 60
- High grooming potential slot available

## Usage

### Compare Skills to Opportunities

```bash
python scripts/python/jarvis_hiring_manager_system.py --compare "Candidate Name"
```

### Fill Slots with Compromise Strategy

```bash
python scripts/python/jarvis_hiring_manager_system.py --fill-slots
```

### Example Output

```
📊 Slot Matches:
   Assistant Engineer: 83.7% (EXCELLENT) ✅ Available
   Engineer: 73.7% (GOOD) ✅ Available

🎯 Recommended Slot: Assistant Engineer
   Match Score: 83.7%
   Fit: EXCELLENT

🌱 Grooming Recommendation:
   High grooming potential - can grow from lower position
   Current Level: 2
   Target Level: 3
   Compromise: Candidate grows while company provides opportunity

⭐ #Merit Assessment: 45.5/100 (ADEQUATE)
```

## Case-Insensitive Matching

For regex/pattern matching (like "#Merit", "#MERIT", "#merit"):

The system handles case-insensitive matching automatically:
- `#Merit` = `#MERIT` = `#merit` (all treated the same)
- Use `re.IGNORECASE` flag for regex patterns
- Example: `re.search(r'#merit', text, re.IGNORECASE)`

## Key Concepts

### Compromise Strategy
- **Candidate Compromise**: Takes lower position to grow
- **Company Compromise**: Provides opportunity and mentorship
- **Mutual Benefit**: Both invest in growth
- **Merit-Based**: Success determined by #Merit

### Power Structure
- Clear hierarchy from Junior to Architect
- Lower levels have higher grooming potential
- Allows for internal growth and promotion

### Skill Matching
- Compares candidate skills to job requirements
- Calculates match score (0-100%)
- Determines fit level (EXCELLENT, GOOD, ADEQUATE, MARGINAL, POOR)

## Notes

- **#Merit**: Case-insensitive merit assessment system
- **Grooming**: Promoting candidates from lower positions
- **Compromise**: Mutual investment in candidate growth
- **Power Structure**: Clear role hierarchy for career progression

@JARVIS @LUMINA #HIRING #RECRUITMENT #MERIT #SKILL_MATCHING #GROOMING
