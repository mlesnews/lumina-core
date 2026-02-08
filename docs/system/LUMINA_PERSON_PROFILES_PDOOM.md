# LUMINA Person Profiles with P-Doom Statistics

**Status**: 🟢 INITIALIZED  
**P-Doom**: Mapped as Core Statistic for ALL Entities

---

## 🎯 Mission

**"PDOM OR PDOOM SHOULD BE A MAPPED PERSON PROFILE STATISTIC FOR ALL PERSONS, 
AI, HUMANS, ALIENS, ACTORS \ ACTRESSES AND THE CHARACTORS THEY PORTRAY."**

P-Doom (Probability of Doom) is mapped as a core statistic in person profiles for 
ALL entity types: AI, Humans, Aliens, Actors/Actresses, and the Characters they portray.

---

## 👤 Entity Types Supported

### 1. **Human**
- Real human beings
- P-Doom rating based on personal circumstances
- Contextual and situational

### 2. **AI**
- Artificial intelligence entities
- JARVIS, @MARVIN, etc.
- P-Doom rating based on AI perspective

### 3. **Alien**
- Extraterrestrial entities
- Future support for alien profiles

### 4. **Actor**
- Male actors
- Can portray multiple characters
- Linked to character profiles

### 5. **Actress**
- Female actors
- Can portray multiple characters
- Linked to character profiles

### 6. **Character**
- Fictional characters portrayed by actors
- Linked to actor/actress who portrays them
- Separate P-Doom rating from actor

### 7. **Hybrid**
- Mixed entity types
- Future support for hybrid entities

---

## 📊 P-Doom Categories

### Category-Specific Ratings

1. **Existential** - Human extinction, AI takeover
2. **Economic** - Economic collapse
3. **Technological** - Tech failures, dependencies
4. **Environmental** - Climate, resources
5. **Social** - Society collapse, conflict
6. **Personal** - Individual doom
7. **Project** - Project failure
8. **General** - Overall doom probability (primary rating)

---

## 🎭 Actor-Character Relationships

### Linking System

**Actor → Character:**
- One actor can portray multiple characters
- Each character has separate P-Doom rating
- Character profile links to actor via `portrayed_by`

**Example:**
- Actor Profile: "Tom Hanks" (P-Doom: 0.25)
  - Portrays: ["Forrest Gump", "Woody (Toy Story)", "Captain Miller"]
- Character Profile: "Forrest Gump" (P-Doom: 0.20)
  - Portrayed by: "Tom Hanks"

### Character P-Doom Independence

Characters have their own P-Doom ratings independent of actors:
- Character's P-Doom based on their story/narrative
- Actor's P-Doom based on real-world circumstances
- Separate assessments

---

## 📋 Profile Structure

### Core Fields

- **profile_id**: Unique identifier
- **name**: Display name
- **entity_type**: Type of entity (Human, AI, Alien, Actor, Actress, Character)
- **pdoom_rating**: Primary P-Doom rating (0.0 - 1.0)
- **pdoom_ratings**: Category-specific ratings
- **description**: Profile description
- **metadata**: Additional profile data

### Relationship Fields

- **portrayed_by**: Character → Actor link
- **portrays**: Actor → Characters list

### Statistics

- **statistics**: Additional profile statistics
- **created_date**: Profile creation timestamp
- **updated_date**: Last update timestamp

---

## 🤖 Default Profiles

### JARVIS (AI)
- **P-Doom**: 20.0%
- **Reasoning**: "Challenges exist, but they're solvable. We build systems, we adapt, we solve problems."
- **Assessed By**: JARVIS

### @MARVIN (AI)
- **P-Doom**: 80.0%
- **Reasoning**: "Everything is doomed. Everything is pointless. <SIGH> Life, the universe, and everything. Mostly meaningless."
- **Assessed By**: @MARVIN

### User (Human)
- **P-Doom**: 35.0%
- **Reasoning**: "Personal P-Doom is hard to assess - contextual, situational, varies over time. Reality is nuanced."
- **Assessed By**: System

---

## 📊 Usage

### Create Profile

```bash
python scripts/python/lumina_person_profiles_pdoom.py --create "Name" "human" "0.35" "Description"
```

### Update P-Doom Rating

```bash
python scripts/python/lumina_person_profiles_pdoom.py --update-pdoom profile_id general 0.40 "Reasoning"
```

### Link Actor to Character

```bash
python scripts/python/lumina_person_profiles_pdoom.py --link actor_profile_id character_profile_id
```

### Get Profile

```bash
python scripts/python/lumina_person_profiles_pdoom.py --get profile_id
```

### List All Profiles

```bash
python scripts/python/lumina_person_profiles_pdoom.py --list
```

### Get Summary

```bash
python scripts/python/lumina_person_profiles_pdoom.py --summary
```

---

## 🔗 Integration Points

### P-Doom Assessment System
- Profiles use P-Doom assessments
- Category-specific ratings
- Multiple assessment perspectives (JARVIS, @MARVIN, Human, System)

### Person Management
- Centralized person profile system
- All entities tracked
- Relationships mapped

### Statistics Tracking
- P-Doom as core statistic
- Additional statistics supported
- Profile metadata

---

## 💡 Key Features

1. **Universal P-Doom Mapping**: All entity types have P-Doom ratings
2. **Category-Specific**: Multiple P-Doom categories per profile
3. **Actor-Character Linking**: Support for actor/character relationships
4. **Flexible Entity Types**: AI, Human, Alien, Actor, Actress, Character, Hybrid
5. **Assessment Tracking**: Who assessed, when, reasoning
6. **Profile Statistics**: P-Doom as core statistic, extensible

---

## 🎯 Example Use Cases

### AI Entities
- JARVIS: P-Doom 20% (optimistic)
- @MARVIN: P-Doom 80% (pessimistic)
- Custom AI: P-Doom assessed per entity

### Human Profiles
- User: P-Doom 35% (contextual)
- Team members: Individual P-Doom ratings
- Public figures: Public P-Doom assessments

### Actors & Characters
- Tom Hanks (Actor): P-Doom 25%
  - Forrest Gump (Character): P-Doom 20%
  - Woody (Character): P-Doom 15%
- Character P-Doom based on narrative
- Actor P-Doom based on real-world

### Future: Aliens
- Extraterrestrial entities
- Alien P-Doom assessments
- Inter-species comparisons

---

**Status**: System initialized with default profiles  
**Next**: Create additional profiles, link actors to characters, track P-Doom over time

