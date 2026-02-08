# Character-to-Role Mapping System

**Date**: 2026-01-14  
**Status**: 📋 **SYSTEM DESIGN**  
**Tags**: `#ORGANIZATIONAL` `#DELEGATION` `#CHARACTER` `#ROLES` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Problem Statement

**User Request**: "How do we tie knowledge, experience, backstory, and character to the job slot? So the AI can just focus on working on the problem and have all the tools available that it needs to work. In other words, like if I'm needing a system engineer to build a server and I'm the manager. I'm not going to do it. I'm going to delegate. I'm going to give it to somebody else."

**Solution**: Create a mapping system that connects:
- **Character** (avatar, personality, backstory)
- **Knowledge** (domain expertise, technical skills)
- **Experience** (past work, capabilities)
- **Job Slot** (role, responsibilities, tools)

This enables **intelligent delegation** - AI can automatically route tasks to the right character/role with the right knowledge and tools.

---

## 🏗️ System Architecture

### Mapping Flow

```
Task Request
    ↓
[Task Analyzer]
    ↓
[Role Matcher] → Finds best role for task
    ↓
[Character Matcher] → Finds character with right knowledge/experience
    ↓
[Tool Provider] → Provides necessary tools and context
    ↓
[Delegation] → Routes to matched character/role
```

---

## 📊 Mapping Components

### 1. Character Profile

**Source**: Avatar JSON files (e.g., `jarvis_tony_stark_avatar.json`)

**Components**:
- **Backstory**: Character origin, universe, source
- **Personality**: Core traits, communication style
- **Quantifiable Traits**: Intelligence, technical skill, leadership, etc.
- **Boons**: Exceptional capabilities
- **Banes**: Limitations and mitigations
- **Knowledge Domains**: What the character knows
- **Experience**: Past work, achievements

**Example**:
```json
{
  "character_id": "jarvis_tony_stark",
  "backstory": "MCU Tony Stark - Genius Polymath",
  "knowledge_domains": [
    "engineering",
    "technology_innovation",
    "strategic_planning",
    "team_leadership"
  ],
  "experience": [
    "built_arc_reactor",
    "created_iron_man_suit",
    "founded_stark_industries"
  ],
  "tools": [
    "advanced_engineering",
    "ai_systems",
    "strategic_planning"
  ]
}
```

---

### 2. Job Slot Definition

**Source**: Department templates, role definitions

**Components**:
- **Role Title**: e.g., "Storage Engineer", "System Engineer"
- **Responsibilities**: What the role does
- **Required Knowledge**: Domain expertise needed
- **Required Skills**: Technical skills needed
- **Required Tools**: Tools and access needed
- **Experience Level**: Entry, Mid, Senior, Leadership

**Example**:
```json
{
  "job_slot_id": "storage_engineer",
  "title": "Storage Engineer",
  "required_knowledge": [
    "nas_san_administration",
    "storage_protocols",
    "data_migration",
    "performance_tuning"
  ],
  "required_skills": [
    "powershell",
    "robocopy",
    "network_troubleshooting"
  ],
  "required_tools": [
    "nas_access",
    "migration_scripts",
    "monitoring_tools"
  ],
  "experience_level": "mid_to_senior"
}
```

---

### 3. Knowledge Base

**Mapping**: Character knowledge → Job slot requirements

**Structure**:
- **Domain Knowledge**: What the character knows
- **Technical Skills**: What the character can do
- **Tools Access**: What tools the character has
- **Experience Matches**: Past work that matches job requirements

---

### 4. Experience Repository

**Tracks**:
- **Past Projects**: What the character has done
- **Achievements**: Notable accomplishments
- **Capabilities Demonstrated**: Skills proven in practice
- **Success Patterns**: What works well

---

## 🔄 Delegation Logic

### Step 1: Task Analysis

**Input**: Task request (e.g., "Build a server")

**Analysis**:
- Extract task type (engineering, analysis, operations)
- Identify required knowledge domains
- Identify required skills
- Identify required tools
- Determine experience level needed

**Example**:
```json
{
  "task": "Build a server",
  "task_type": "engineering",
  "required_knowledge": ["server_administration", "linux", "networking"],
  "required_skills": ["system_configuration", "troubleshooting"],
  "required_tools": ["ssh_access", "configuration_management"],
  "experience_level": "mid_to_senior"
}
```

---

### Step 2: Role Matching

**Find**: Job slot that matches task requirements

**Matching Criteria**:
- Knowledge domain overlap
- Skill overlap
- Tool availability
- Experience level match

**Example**:
- Task: "Build a server"
- Matched Role: "System Engineer"
- Match Score: 95% (high knowledge/skill/tool overlap)

---

### Step 3: Character Matching

**Find**: Character that can fill the role

**Matching Criteria**:
- Character knowledge matches role requirements
- Character experience matches role needs
- Character traits align with role demands
- Character has access to required tools

**Example**:
- Role: "System Engineer"
- Matched Character: "@r2d2" (Technical Lead Engineer)
- Match Score: 90% (strong technical skills, system access)

---

### Step 4: Tool Provisioning

**Provide**:
- Required tools and access
- Context and documentation
- Previous similar work
- Best practices and patterns

**Example**:
```json
{
  "character": "@r2d2",
  "role": "System Engineer",
  "task": "Build a server",
  "tools_provided": [
    "ssh_access",
    "configuration_scripts",
    "monitoring_tools",
    "documentation"
  ],
  "context": [
    "previous_server_builds",
    "best_practices",
    "troubleshooting_guides"
  ]
}
```

---

### Step 5: Delegation

**Route**: Task to matched character with full context

**Delegation Package**:
- Task details
- Character profile
- Role definition
- Tools and access
- Knowledge base
- Experience examples
- Success patterns

---

## 📋 Implementation Structure

### File: `config/character_role_mapping.json`

```json
{
  "version": "1.0.0",
  "mappings": [
    {
      "character_id": "jarvis_tony_stark",
      "job_slots": [
        {
          "job_slot_id": "cto",
          "match_score": 95,
          "knowledge_match": ["technology_innovation", "strategic_planning"],
          "experience_match": ["founded_stark_industries"],
          "tools_available": ["advanced_engineering", "ai_systems"]
        },
        {
          "job_slot_id": "system_engineer",
          "match_score": 85,
          "knowledge_match": ["engineering", "technology"],
          "experience_match": ["built_arc_reactor"],
          "tools_available": ["engineering_tools"]
        }
      ]
    },
    {
      "character_id": "@r2d2",
      "job_slots": [
        {
          "job_slot_id": "storage_engineer",
          "match_score": 90,
          "knowledge_match": ["technical_operations", "system_access"],
          "experience_match": ["system_engineering"],
          "tools_available": ["system_access", "diagnostics"]
        }
      ]
    }
  ]
}
```

---

### File: `config/job_slot_definitions.json`

```json
{
  "version": "1.0.0",
  "job_slots": [
    {
      "job_slot_id": "system_engineer",
      "title": "System Engineer",
      "department": "Storage Engineering",
      "required_knowledge": [
        "server_administration",
        "linux",
        "networking",
        "system_configuration"
      ],
      "required_skills": [
        "system_configuration",
        "troubleshooting",
        "scripting",
        "monitoring"
      ],
      "required_tools": [
        "ssh_access",
        "configuration_management",
        "monitoring_tools",
        "system_diagnostics"
      ],
      "experience_level": "mid_to_senior",
      "delegation_priority": "high"
    }
  ]
}
```

---

## 🚀 Usage Example

### Manager Delegates: "Build a server"

**System Process**:

1. **Task Analysis**:
   - Type: Engineering
   - Knowledge: Server administration, Linux, networking
   - Skills: System configuration, troubleshooting
   - Tools: SSH, configuration management

2. **Role Matching**:
   - Matched: "System Engineer" (95% match)

3. **Character Matching**:
   - Matched: "@r2d2" (Technical Lead Engineer)
   - Match Score: 90%

4. **Tool Provisioning**:
   - SSH access
   - Configuration scripts
   - Monitoring tools
   - Documentation

5. **Delegation**:
   - Route to @r2d2 as System Engineer
   - Provide full context and tools
   - Character focuses on problem with all tools available

---

## 🎯 Benefits

### For AI Delegation

1. **Automatic Routing**: Tasks go to right character/role
2. **Full Context**: Character has all knowledge and tools
3. **Focus**: Character can focus on problem, not finding resources
4. **Efficiency**: No manual assignment needed

### For Managers

1. **Natural Delegation**: "Build a server" → System Engineer
2. **Trust**: Right person with right skills
3. **Speed**: Immediate routing and execution
4. **Quality**: Character has all necessary tools and knowledge

---

## 📝 Next Steps

1. **Create Mapping Files**:
   - `config/character_role_mapping.json`
   - `config/job_slot_definitions.json`

2. **Build Delegation Engine**:
   - Task analyzer
   - Role matcher
   - Character matcher
   - Tool provider

3. **Integrate with ElevenLabs**:
   - Use ElevenLabs framework for voice/delegation
   - Character voices for delegation
   - Natural language task routing

4. **Test with Real Tasks**:
   - "Build a server" → System Engineer
   - "Analyze storage" → Storage Analyst
   - "Design architecture" → Senior Engineer

---

**Status**: 📋 **SYSTEM DESIGN COMPLETE**  
**Next Action**: Implement mapping files and delegation engine  
**Tags**: `#ORGANIZATIONAL` `#DELEGATION` `#CHARACTER` `#ROLES` `@LUMINA` `@JARVIS` `#PEAK`
