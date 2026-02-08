# Actor Systems and Frameworks for AI Character Platforms

**Document Version**: 1.0.0
**Last Updated**: 2026-01-27
**Status**: ✅ ACTIVE
**Classification**: TECHNICAL DOCUMENTATION

---

## Table of Contents

1. [Introduction and Overview](#1-introduction-and-overview)
2. [Actor Framework Architectures](#2-actor-framework-architectures)
3. [Character Card Specifications](#3-character-card-specifications)
4. [Visual Avatar Integration](#4-visual-avatar-integration)
5. [Animation Systems](#5-animation-systems)
6. [Duel Mechanics](#6-duel-mechanics)
7. [Open Source Alternatives](#7-open-source-alternatives)
8. [MCU Lore Integration](#8-mcu-lore-integration)
9. [Security and Best Practices](#9-security-and-best-practices)
10. [Appendices](#10-appendices)

---

## 1. Introduction and Overview

### 1.1 Executive Summary

Actor systems represent a foundational architectural pattern for building scalable, concurrent, and fault-tolerant AI character platforms. This documentation provides comprehensive technical guidance on implementing actor-based frameworks for AI-driven character interactions, encompassing character card specifications, visual avatar integration, animation systems, duel mechanics, and knowledge base integration.

The actor model, originally conceptualized by Carl Hewitt in 1973, has proven exceptionally well-suited for AI character platforms due to its inherent ability to handle concurrent interactions, maintain isolated state, and scale horizontally across distributed systems. Modern implementations such as PyKka (Python), Akka (JVM), OTP (Erlang), Actix (Rust), and Orleans (.NET) provide robust foundations for building production-ready character AI systems.

This documentation synthesizes research findings from multiple actor framework implementations, character card format specifications, animation system architectures, and open-source alternatives to provide actionable guidance for developers building AI character platforms.

### 1.2 Scope and Objectives

The scope of this documentation encompasses the complete technical stack required for AI character platform development:

- **Actor Framework Selection and Implementation**: Comparative analysis of major actor frameworks with implementation patterns specific to character AI workloads
- **Character Card Format Standards**: JSON and YAML schema specifications for portable character definitions
- **Visual Avatar Systems**: Architecture patterns for loading, managing, and rendering character avatars with real-time animation
- **Animation State Management**: Implementation of sprite-based and procedural animation systems
- **Interaction Mechanics**: Framework design for turn-based and real-time character duels
- **Knowledge Integration**: Systems for incorporating domain-specific lore (e.g., Marvel Cinematic Universe) into character responses
- **Security and Performance**: Best practices for secure API key management and optimized resource utilization

### 1.3 Target Audience

This documentation is designed for the following audiences:

- **Software Architects**: Seeking to understand actor model patterns for AI character platform design
- **Backend Developers**: Implementing character AI systems using Python, Java, Rust, or other languages
- **Frontend Developers**: Building avatar rendering and animation systems for character interfaces
- **DevOps Engineers**: Deploying and scaling actor-based AI character infrastructure
- **Data Engineers**: Implementing character card pipelines and knowledge base integration

---

## 2. Actor Framework Architectures

### 2.1 Actor Model Fundamentals

The actor model provides a mathematical foundation for concurrent computation where "actors" are the fundamental units of computation. Each actor possesses the following characteristics:

- **Mailbox**: A queue that receives messages from other actors
- **Behavior**: A function that defines how the actor processes incoming messages
- **State**: Private data that the actor maintains and modifies
- **Communication**: Ability to send messages to other actors and create new actors

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        ACTOR MODEL ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐     │
│    │   ACTOR A   │────────▶│   ACTOR B   │────────▶│   ACTOR C   │     │
│    │  ┌───────┐  │  msg    │  ┌───────┐  │  msg    │  ┌───────┐  │     │
│    │  │State  │  │         │  │State  │  │         │  │State  │  │     │
│    │  └───────┘  │         │  └───────┘  │         │  └───────┘  │     │
│    │  ┌───────┐  │         │  ┌───────┐  │         │  ┌───────┐  │     │
│    │  │Behavior│◀─────────│  │Behavior│◀─────────│  │Behavior│  │     │
│    │  └───────┘  │         │  └───────┘  │         │  └───────┘  │     │
│    │  ┌───────┐  │         │  ┌───────┐  │         │  ┌───────┐  │     │
│    │  │Mailbox│  │         │  │Mailbox│  │         │  │Mailbox│  │     │
│    │  └───────┘  │         │  └───────┘  │         │  └───────┘  │     │
│    └─────────────┘         └─────────────┘         └─────────────┘     │
│            │                     │                     │                │
│            └─────────────────────┼─────────────────────┘                │
│                                  │                                      │
│                          Supervisor Actor                               │
│                    (Fault Tolerance & Recovery)                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

For AI character platforms, actors map naturally to character instances, interaction sessions, animation controllers, and knowledge retrieval systems. Each character in the system can be represented as an actor with its own state (character card data, conversation history), behavior (response generation logic), and mailbox (incoming messages from users).

### 2.2 Framework Comparison

#### 2.2.1 PyKka (Python)

PyKka is a Python library providing actor model implementation with a clean, Pythonic API. It is particularly suitable for AI character platforms due to Python's dominance in AI/ML ecosystems.

**Key Characteristics:**

- Lightweight actor implementation with minimal overhead
- Thread-based concurrency (uses Python's threading module)
- Actor references enable transparent network communication
- Supervision trees for fault tolerance
- Compatible with Python async/await patterns

**Architecture Diagram:**

```
┌─────────────────────────────────────────────────────────────────┐
│                        PyKka ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    PyKka Runtime                        │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │              ActorSystem                         │   │   │
│  │  │  ┌─────────────┬─────────────┬─────────────┐   │   │   │
│  │  │  │ ActorProxy  │ ActorRegistry│ Supervision │   │   │   │
│  │  │  └─────────────┴─────────────┴─────────────┘   │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │              Actor Instances                    │   │   │
│  │  │                                                 │   │   │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────┐│   │   │
│  │  │  │CharacterActor│  │SessionActor │  │AnimActor││   │   │
│  │  │  │  ┌───────┐  │  │  ┌───────┐  │  │┌───────┐││   │   │
│  │  │  │  │on_receive│  │  │on_receive│  ││on_receive││   │   │
│  │  │  │  └───────┘  │  │  └───────┘  │  │└───────┘││   │   │
│  │  │  │  ┌───────┐  │  │  ┌───────┐  │  │┌───────┐││   │   │
│  │  │  │  │Future │  │  │  │Future │  │  ││Future │││   │   │
│  │  │  │  └───────┘  │  │  └───────┘  │  │└───────┘││   │   │
│  │  │  └─────────────┘  └─────────────┘  └─────────┘│   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │              Message Bus                         │   │   │
│  │  │      (Thread-safe Mailbox Queue)                │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Code Sample - Character Actor Implementation:**

```python
from pykka import ActorRegistry, Actor, Future
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class MessageType(Enum):
    """Message types for character actor communication."""
    GENERATE_RESPONSE = "generate_response"
    UPDATE_CONTEXT = "update_context"
    GET_STATE = "get_state"
    SET_AVATAR_STATE = "set_avatar_state"


@dataclass
class Message:
    """Message structure for actor communication."""
    type: MessageType
    payload: Dict[str, Any]
    sender: Optional[str] = None
    reply_to: Optional[Future] = None


class CharacterActor(Actor):
    """
    Actor representing a single AI character instance.

    Handles message processing, response generation, and state management
    for character interactions in the AI platform.
    """

    def __init__(self, character_id: str, character_data: Dict[str, Any]):
        super().__init__()
        self.character_id = character_id
        self.character_data = character_data
        self.conversation_history: List[Dict[str, str]] = []
        self.current_state: Dict[str, Any] = {
            "emotion": "neutral",
            "avatar_frame": "idle",
            "interaction_count": 0
        }
        self.llm_service = None
        self.knowledge_base = None

    def on_start(self):
        """Initialize actor dependencies when starting."""
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential

        # Retrieve API key from Azure Key Vault
        vault_url = "https://jarvis-lumina.vault.azure.net/"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vault_url, credential=credential)

        # Initialize LLM service with secured API key
        openai_api_key = client.get_secret("openai-api-key").value
        self.llm_service = self._create_llm_service(openai_api_key)

        logger.info(f"CharacterActor {self.character_id} started successfully")

    def _create_llm_service(self, api_key: str):
        """Create LLM service instance with Azure Key Vault credentials."""
        # Implementation depends on chosen LLM provider
        return {"provider": "openai", "api_key_provided": True}

    def on_receive(self, message: Message) -> Any:
        """
        Process incoming messages and generate responses.

        Args:
            message: Message object containing type and payload

        Returns:
            Response data based on message type
        """
        try:
            self.current_state["interaction_count"] += 1

            if message.type == MessageType.GENERATE_RESPONSE:
                return self._handle_generate_response(message)
            elif message.type == MessageType.UPDATE_CONTEXT:
                return self._handle_update_context(message)
            elif message.type == MessageType.GET_STATE:
                return self._handle_get_state(message)
            elif message.type == MessageType.SET_AVATAR_STATE:
                return self._handle_set_avatar_state(message)
            else:
                logger.warning(f"Unknown message type: {message.type}")
                return {"error": "Unknown message type"}

        except Exception as e:
            logger.error(f"Error processing message: {e}")
            self._handle_error(e)
            return {"error": str(e)}

    def _handle_generate_response(self, message: Message) -> Dict[str, Any]:
        """Generate AI response for user input."""
        user_input = message.payload.get("user_input", "")
        system_prompt = self.character_data.get("system_prompt", "")

        # Build conversation context
        context = self._build_conversation_context(system_prompt, user_input)

        # Generate response using LLM service
        response = self.llm_service.generate(context)

        # Update conversation history
        self.conversation_history.append({
            "user": user_input,
            "character": response["text"],
            "timestamp": self._get_timestamp()
        })

        # Determine avatar state based on response
        avatar_state = self._determine_avatar_state(response)

        return {
            "character_id": self.character_id,
            "response_text": response["text"],
            "avatar_state": avatar_state,
            "emotion": response.get("emotion", "neutral")
        }

    def _build_conversation_context(self, system_prompt: str, user_input: str) -> List[Dict]:
        """Build context for LLM response generation."""
        messages = [{"role": "system", "content": system_prompt}]

        # Add recent conversation history (last 10 exchanges)
        for exchange in self.conversation_history[-10:]:
            messages.append({"role": "user", "content": exchange["user"]})
            messages.append({"role": "assistant", "content": exchange["character"]})

        messages.append({"role": "user", "content": user_input})
        return messages

    def _determine_avatar_state(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Determine avatar animation state based on response content."""
        text = response.get("text", "").lower()

        # Simple emotion detection based on keywords
        if any(word in text for word in ["happy", "great", "excellent", "wonderful"]):
            emotion = "happy"
        elif any(word in text for word in ["sad", "sorry", "unfortunately"]):
            emotion = "sad"
        elif any(word in text for word in ["angry", "frustrated", "annoyed"]):
            emotion = "angry"
        else:
            emotion = "neutral"

        return {
            "emotion": emotion,
            "frame_sequence": self._get_frame_sequence(emotion)
        }

    def _get_frame_sequence(self, emotion: str) -> List[str]:
        """Get animation frame sequence for emotion."""
        sequences = {
            "idle": ["idle_1", "idle_2", "idle_3", "idle_2"],
            "happy": ["happy_bounce", "happy_smile"],
            "sad": ["sad_look_down", "sad_sigh"],
            "angry": ["angry_stern", "angry_shake"],
            "neutral": ["neutral_1", "neutral_2"]
        }
        return sequences.get(emotion, sequences["neutral"])

    def _handle_update_context(self, message: Message) -> Dict[str, Any]:
        """Update character context with new information."""
        new_context = message.payload.get("context", {})
        self.character_data.update(new_context)
        return {"status": "updated", "character_id": self.character_id}

    def _handle_get_state(self, message: Message) -> Dict[str, Any]:
        """Return current character state."""
        return {
            "character_id": self.character_id,
            "state": self.current_state,
            "interaction_count": self.current_state["interaction_count"]
        }

    def _handle_set_avatar_state(self, message: Message) -> Dict[str, Any]:
        """Set avatar to specific state."""
        new_state = message.payload.get("state", {})
        self.current_state.update(new_state)
        return {"status": "set", "state": self.current_state}

    def _handle_error(self, error: Exception) -> None:
        """Handle actor errors with supervision strategy."""
        logger.error(f"CharacterActor {self.character_id} encountered error: {error}")
        # Supervisor will handle restart/recovery

    def _get_timestamp(self) -> str:
        """Get current ISO format timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat()


class CharacterSupervisor(Actor):
    """
    Supervisor actor for managing character actors with fault tolerance.
    Implements supervision strategies for character actor lifecycle.
    """

    def __init__(self, supervisor_config: Dict[str, Any]):
        super().__init__()
        self.supervisor_config = supervisor_config
        self.child_actors: Dict[str, Actor] = {}
        self.restart_counts: Dict[str, int] = {}

    def on_receive(self, message: Message) -> Any:
        """Handle supervision messages."""
        if message.type == "START_CHARACTER":
            return self._start_character(message.payload)
        elif message.type == "STOP_CHARACTER":
            return self._stop_character(message.payload)
        elif message.type == "RESTART_CHARACTER":
            return self._restart_character(message.payload)
        elif message.type == "GET_SUPERVISOR_STATUS":
            return self._get_status()

    def _start_character(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Start a new character actor under supervision."""
        character_id = payload["character_id"]
        character_data = payload["character_data"]

        if character_id in self.child_actors:
            return {"status": "exists", "character_id": character_id}

        # Create character actor
        actor = CharacterActor.start(character_id, character_data)
        self.child_actors[character_id] = actor
        self.restart_counts[character_id] = 0

        return {"status": "started", "character_id": character_id}

    def _stop_character(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Stop a supervised character actor."""
        character_id = payload["character_id"]

        if character_id not in self.child_actors:
            return {"status": "not_found", "character_id": character_id}

        actor = self.child_actors.pop(character_id)
        actor.stop()
        self.restart_counts.pop(character_id, None)

        return {"status": "stopped", "character_id": character_id}

    def _restart_character(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Restart a character actor with exponential backoff."""
        character_id = payload["character_id"]

        if character_id not in self.child_actors:
            return {"status": "not_found", "character_id": character_id}

        # Check restart limit
        restart_count = self.restart_counts.get(character_id, 0)
        max_restarts = self.supervisor_config.get("max_restarts", 5)

        if restart_count >= max_restarts:
            return {"status": "max_restarts_exceeded", "character_id": character_id}

        # Stop and restart with backoff
        actor = self.child_actors[character_id]
        actor.stop()

        import time
        backoff = min(2 ** restart_count, 60)  # Max 60 second backoff
        time.sleep(backoff)

        # Recreate actor with same configuration
        character_data = payload.get("character_data", {})
        actor = CharacterActor.start(character_id, character_data)
        self.child_actors[character_id] = actor
        self.restart_counts[character_id] = restart_count + 1

        return {"status": "restarted", "character_id": character_id, "restart_count": restart_count + 1}

    def _get_status(self) -> Dict[str, Any]:
        """Get supervisor status for monitoring."""
        return {
            "supervisor_status": "running",
            "active_characters": len(self.child_actors),
            "character_ids": list(self.child_actors.keys()),
            "restart_counts": self.restart_counts
        }
```

#### 2.2.2 Akka (JVM)

Akka is a mature actor framework for the JVM ecosystem, written in Scala but usable from Java and other JVM languages. It provides excellent performance and is well-suited for high-throughput character AI systems.

**Key Characteristics:**

- Extremely high performance with minimal latency
- Cluster support for distributed deployments
- Persistence actors for event sourcing
- Streaming support with Akka Streams
- Rich ecosystem including Akka HTTP, Akka gRPC

**Architecture Pattern:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         AKKA CLUSTER ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐  │
│   │                    Akka Cluster                                 │  │
│   │                                                                │  │
│   │    ┌──────────┐     ┌──────────┐     ┌──────────┐            │  │
│   │    │  Node 1  │◀───▶│  Node 2  │◀───▶│  Node 3  │            │  │
│   │    │ (Seed)   │     │          │     │          │            │  │
│   │    └────┬─────┘     └────┬─────┘     └────┬─────┘            │  │
│   │         │                │                │                   │  │
│   │         ▼                ▼                ▼                   │  │
│   │    ┌─────────────────────────────────────────────────────┐   │  │
│   │    │              Cluster Sharding                       │   │  │
│   │    │    (Character Actors Sharded Across Nodes)          │   │  │
│   │    └─────────────────────────────────────────────────────┘   │  │
│   │                                                                │  │
│   └────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐  │
│   │              Character Actor Hierarchy                          │  │
│   │                                                                │  │
│   │   ┌─────────────────────────────────────────────────────────┐  │  │
│   │   │              Character Region                            │  │  │
│   │   │  ┌─────────────────────────────────────────────────┐   │  │  │
│   │   │  │              Character Shard                     │   │  │  │
│   │   │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────┐  │   │  │  │
│   │   │  │  │Character-1 │  │Character-2 │  │Char-N   │  │   │  │  │
│   │   │  │  │  (Actor)   │  │  (Actor)   │  │ (Actor) │  │   │  │  │
│   │   │  │  └─────────────┘  └─────────────┘  └─────────┘  │   │  │  │
│   │   │  └─────────────────────────────────────────────────┘   │  │  │
│   │   └─────────────────────────────────────────────────────────┘  │  │
│   └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Code Sample - Akka Character Actor (Java):**

```java
package com.lumina.character.actors;

import akka.actor.*;
import akka.cluster.sharding.*;
import akka.persistence.*;
import scala.concurrent.duration.Duration;
import java.time.Duration;
import java.util.Optional;
import java.util.HashMap;
import java.util.Map;

public class CharacterActor extends AbstractActorWithPersistence {

    private final String characterId;
    private final Map<String, Object> state = new HashMap<>();
    private final CharacterPersistence behavior;

    public CharacterActor(String characterId) {
        this.characterId = characterId;
        this.behavior = new CharacterPersistence(characterId);
    }

    @Override
    public Receive createReceive() {
        return receiveBuilder()
            .match(GenerateResponse.class, this::handleGenerateResponse)
            .match(UpdateContext.class, this::handleUpdateContext)
            .match(GetState.class, this::handleGetState)
            .match(SaveSnapshot.class, this::handleSaveSnapshot)
            .match(Recover.class, this::handleRecovery)
            .build();
    }

    private void handleGenerateResponse(GenerateResponse msg) {
        try {
            // Build conversation context
            ConversationContext context = buildContext(msg.getUserInput());

            // Generate response via LLM service
            LLMService llmService = LLMServiceFactory.getService();
            Response response = llmService.generate(
                getSecret("openai-api-key"),
                context
            );

            // Update state and persist
            state.put("last_response", response.getText());
            state.put("interaction_count",
                ((Number) state.getOrDefault("interaction_count", 0)).intValue() + 1);

            // Persist state changes
            saveSnapshot(state);

            // Send response back
            sender().tell(response, self());

        } catch (Exception e) {
            sender().tell(new ErrorResponse(e.getMessage()), self());
        }
    }

    private String getSecret(String secretName) {
        // Azure Key Vault integration
        try {
            return AzureKeyVaultClient.getSecret(secretName);
        } catch (Exception e) {
            throw new RuntimeException("Failed to retrieve secret: " + secretName, e);
        }
    }

    private void handleUpdateContext(UpdateContext msg) {
        state.putAll(msg.getContext());
        saveSnapshot(state);
        sender().tell(new UpdateResponse("updated"), self());
    }

    private void handleGetState(GetState msg) {
        sender().tell(new StateResponse(state), self());
    }

    private void handleSaveSnapshot(SaveSnapshot msg) {
        saveSnapshot(state);
    }

    private void handleRecovery(Recover msg) {
        // Event sourcing recovery logic
        state.clear();
        state.putAll(behavior.recoverState());
    }

    private ConversationContext buildContext(String userInput) {
        return new ConversationContext(
            characterId,
            state.getOrDefault("system_prompt", ""),
            (java.util.List<String>) state.getOrDefault("history", new java.util.ArrayList<>()),
            userInput
        );
    }

    // Message classes
    public static class GenerateResponse {
        private final String userInput;
        public GenerateResponse(String userInput) { this.userInput = userInput; }
        public String getUserInput() { return userInput; }
    }

    // ... other message classes
}

public class CharacterActorSharding {

    public static ClusterShardingExtension create(ActorSystem system) {
        return ClusterSharding.apply(system).start(
            "CharacterRegion",
            Props.create(CharacterActor.class, () ->
                new CharacterActor("default-id")),
            ClusterShardingSettings.create(system),
            new HashMap<String, Object>(),
            new ExtractEntityId() {
                @Override
                public String entityIdOf(Object msg) {
                    if (msg instanceof HasEntityId) {
                        return ((HasEntityId) msg).getEntityId();
                    }
                    return "default";
                }
                @Override
                public Object entityMessage(Object msg) { return msg; }
            },
            new ExtractShardId() {
                @Override
                public String shardIdOf(Object msg) {
                    if (msg instanceof HasEntityId) {
                        String id = ((HasEntityId) msg).getEntityId();
                        return String.valueOf(Math.abs(id.hashCode() % 10));
                    }
                    return "shard-0";
                }
            }
        );
    }
}
```

#### 2.2.3 OTP (Erlang/Elixir)

The OTP (Open Telecom Platform) framework provides the foundation for Erlang's actor model implementation. It is renowned for building fault-tolerant, distributed systems with "nine nines" availability.

**Key Characteristics:**

- Extremely robust fault tolerance through process supervision
- Hot code reloading without downtime
- Built-in distribution for transparent networking
- Mnesia distributed database
- Used in production systems requiring 99.9999999% uptime

**Architecture Diagram:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      OTP ARCHITECTURE FOR CHARACTER AI                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    Application Supervisor                       │   │
│  │                    (One-For-One Strategy)                       │   │
│  │                                                                │   │
│  │  ┌─────────────────────────────────────────────────────────┐   │   │
│  │  │              Character Sup Spec                         │   │   │
│  │  │  ┌─────────────────────────────────────────────────┐   │   │   │
│  │  │  │              Character Supervisor                │   │   │   │
│  │  │  │    (Restarts on transient errors)                │   │   │   │
│  │  │  │                                                 │   │   │   │
│  │  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────┐ │   │   │   │
│  │  │  │  │Char Worker 1│  │Char Worker 2│  │CharWorkerN│ │   │   │   │
│  │  │  │  │  (GenServer)│  │  (GenServer)│  │(GenServer)│ │   │   │   │
│  │  │  │  └─────────────┘  └─────────────┘  └─────────┘ │   │   │   │
│  │  │  └─────────────────────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────────────────────┘   │   │
│  │                                                                │   │
│  │  ┌─────────────────────────────────────────────────────────┐   │   │
│  │  │              Session Sup Spec                           │   │   │
│  │  │  ┌─────────────────────────────────────────────────┐   │   │   │
│  │  │  │              Session Supervisor                  │   │   │   │
│  │  │  │                                                 │   │   │   │
│  │  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────┐ │   │   │   │
│  │  │  │  │Session      │  │Session      │  │Session  │ │   │   │   │
│  │  │  │  │Process 1    │  │Process 2    │  │Process N│ │   │   │   │
│  │  │  │  └─────────────┘  └─────────────┘  └─────────┘ │   │   │   │
│  │  │  └─────────────────────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    GenServer Behavior                            │   │
│  │                                                                │   │
│  │  -handle_call: Synchronous requests (response generation)      │   │
│  │  -handle_cast: Asynchronous updates (context updates)          │   │
│  │  -handle_info: Timers, system messages                         │   │
│  │  -terminate: Cleanup on shutdown                               │   │
│  │  -code_change: Hot code swapping                               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Code Sample - OTP Character Server (Elixir):**

```elixir
defmodule Lumina.CharacterServer do
  @moduledoc """
  OTP GenServer for managing character AI interactions.
  Implements fault-tolerant character state management with persistence.
  """

  use GenServer

  alias Lumina.{Character, LLMService, KnowledgeBase, KeyVault}

  # Client API
  def start_link(character_id) when is_binary(character_id) do
    GenServer.start_link(__MODULE__, character_id, name: via_tuple(character_id))
  end

  def generate_response(character_id, user_input) do
    GenServer.call(via_tuple(character_id), {:generate_response, user_input})
  end

  def update_context(character_id, context) do
    GenServer.cast(via_tuple(character_id), {:update_context, context})
  end

  def get_state(character_id) do
    GenServer.call(via_tuple(character_id), :get_state)
  end

  defp via_tuple(character_id) do
    {:via, Registry, {Lumina.CharacterRegistry, character_id}}
  end

  # Server Callbacks
  @impl true
  def init(character_id) do
    # Retrieve API key from Azure Key Vault
    api_key = KeyVault.get_secret!("openai-api-key")

    state = %{
      character_id: character_id,
      api_key: api_key,
      character_data: load_character_data(character_id),
      conversation_history: [],
      current_state: %{
        emotion: "neutral",
        avatar_frame: "idle",
        interaction_count: 0
      },
      last_interaction: nil
    }

    {:ok, state, {:continue, :load_knowledge}}
  end

  @impl true
  def handle_continue(:load_knowledge, state) do
    # Load character-specific knowledge base
    knowledge = KnowledgeBase.load_for_character(state.character_id)
    state = put_in(state.character_data.knowledge, knowledge)
    {:noreply, state}
  end

  @impl true
  def handle_call({:generate_response, user_input}, _from, state) do
    try do
      # Build conversation context
      context = build_context(state, user_input)

      # Generate response via LLM service
      {:ok, response} = LLMService.generate(state.api_key, context)

      # Update conversation history (max 50 exchanges)
      new_history = state.conversation_history
        |> Kernel.++([%{user: user_input, character: response.text, timestamp: DateTime.utc_now()}])
        |> Enum.take(-50)

      # Determine avatar state from response
      avatar_state = determine_avatar_state(response)

      new_state = %{
        state |
        conversation_history: new_history,
        current_state: Map.merge(state.current_state, avatar_state),
        interaction_count: state.current_state.interaction_count + 1,
        last_interaction: DateTime.utc_now()
      }

      {:reply, {:ok, response}, new_state}

    rescue
      e ->
        Logger.error("Response generation failed: #{inspect(e)}")
        {:reply, {:error, e}, state}
    end
  end

  @impl true
  def handle_cast({:update_context, context}, state) do
    new_character_data = Map.merge(state.character_data, context)
    {:noreply, %{state | character_data: new_character_data}}
  end

  @impl true
  def handle_call(:get_state, _from, state) do
    {:reply, state, state}
  end

  @impl true
  def handle_info(:timeout, state) do
    # Idle timeout - return to neutral state
    {:noreply, put_in(state.current_state.emotion, "neutral")}
  end

  @impl true
  def terminate(_reason, state) do
    # Persist state before termination
    save_character_state(state)
    :ok
  end

  # Private helper functions
  defp build_context(state, user_input) do
    %{
      system_prompt: state.character_data.system_prompt,
      history: state.conversation_history,
      user_input: user_input,
      knowledge: state.character_data.knowledge || %{},
      personality: state.character_data.personality
    }
  end

  defp determine_avatar_state(response) do
    text = String.downcase(response.text)

    emotion = cond do
      String.contains?(text, ["happy", "great", "excellent", "wonderful"]) -> "happy"
      String.contains?(text, ["sad", "sorry", "unfortunately"]) -> "sad"
      String.contains?(text, ["angry", "frustrated", "annoyed"]) -> "angry"
      true -> "neutral"
    end

    %{
      emotion: emotion,
      avatar_frame: determine_frame(emotion),
      expression: response.expression || emotion
    }
  end

  defp determine_frame("happy"), do: "happy_bounce"
  defp determine_frame("sad"), do: "sad_look_down"
  defp determine_frame("angry"), do: "angry_stern"
  defp determine_frame(_), do: "idle"

  defp load_character_data(character_id) do
    # Load from database or cache
    # This is a placeholder - actual implementation would query your data store
    %{id: character_id, name: "Unknown Character"}
  end

  defp save_character_state(_state) do
    # Persist state to durable storage
    :ok
  end
end

defmodule Lumina.CharacterSupervisor do
  @moduledoc """
  OTP Supervisor for managing character servers with fault tolerance.
  Implements one-for-one supervision with exponential backoff.
  """

  use Supervisor

  def start_link(init_arg) do
    Supervisor.start_link(__MODULE__, init_arg, name: __MODULE__)
  end

  @impl true
  def init(_init_arg) do
    children = [
      # Dynamic supervisor for character sessions
      {DynamicSupervisor, name: Lumina.CharacterSessionSup, strategy: :one_for_one},

      # Registry for character actor lookups
      {Registry, name: Lumina.CharacterRegistry, keys: :unique}
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end

  def start_character(character_id) do
    child_spec = %{
      id: {Lumina.CharacterServer, character_id},
      start: {Lumina.CharacterServer, :start_link, [character_id]},
      restart: :transient,
      shutdown: 5000
    }

    DynamicSupervisor.start_child(Lumina.CharacterSessionSup, child_spec)
  end
end
```

#### 2.2.4 Actix (Rust)

Actix is a powerful actor framework for Rust that provides excellent performance through zero-cost abstractions and the actor model.

**Key Characteristics:**

- Extremely high performance with minimal runtime overhead
- Actix-web for HTTP integration
- Type-safe message handling
- Async/await native support
- Excellent for high-concurrency scenarios

**Code Sample - Actix Character Actor:**

```rust
use actix::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::Mutex;

#[derive(Message, Debug, Clone)]
#[rtype(result = "Result<GenerateResponse, String>")]
pub struct GenerateResponse {
    pub user_input: String,
    pub session_id: String,
}

#[derive(Message, Debug, Clone)]
#[rtype(result = "Result<UpdateContext, String>")]
pub struct UpdateContext {
    pub context: HashMap<String, String>,
}

#[derive(Message, Debug, Clone)]
#[rtype(result = "Result<ActorState, String>")]
pub struct GetState;

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct GenerateResponseResult {
    pub text: String,
    pub emotion: String,
    pub avatar_frame: String,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct ActorState {
    pub character_id: String,
    pub emotion: String,
    pub interaction_count: u64,
}

pub struct CharacterActor {
    character_id: String,
    state: Arc<Mutex<CharacterState>>,
    llm_service: Arc<dyn LLMServiceTrait>,
}

struct CharacterState {
    conversation_history: Vec<ConversationExchange>,
    current_emotion: String,
    interaction_count: u64,
    character_data: HashMap<String, String>,
}

impl CharacterActor {
    pub fn new(
        character_id: String,
        character_data: HashMap<String, String>,
        llm_service: Arc<dyn LLMServiceTrait>,
    ) -> Self {
        CharacterActor {
            character_id,
            state: Arc::new(Mutex::new(CharacterState {
                conversation_history: Vec::new(),
                current_emotion: "neutral".to_string(),
                interaction_count: 0,
                character_data,
            })),
            llm_service,
        }
    }
}

impl Actor for CharacterActor {
    type Context = Context<Self>;

    fn started(&mut self, _ctx: &mut Self::Context) {
        info!("CharacterActor {} started", self.character_id);
    }
}

impl Handler<GenerateResponse> for CharacterActor {
    type Result = Result<GenerateResponse, String>;

    fn handle(&mut self, msg: GenerateResponse, _ctx: &mut Self::Context) -> Self::Result {
        let api_key = get_azure_keyvault_secret("openai-api-key")?;

        let mut state = self.state.blocking_lock();

        // Build context
        let context = ConversationContext {
            system_prompt: state.character_data.get("system_prompt")
                .cloned()
                .unwrap_or_default(),
            history: state.conversation_history.clone(),
            user_input: msg.user_input.clone(),
        };

        // Generate response
        let response = tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                self.llm_service.generate(&api_key, &context).await
            })?;

        // Update state
        state.conversation_history.push(ConversationExchange {
            user: msg.user_input,
            character: response.text.clone(),
        });
        state.conversation_history.truncate(50);
        state.interaction_count += 1;
        state.current_emotion = response.emotion.clone();

        Ok(GenerateResponseResult {
            text: response.text,
            emotion: response.emotion,
            avatar_frame: determine_avatar_frame(&response.emotion),
        })
    }
}

impl Handler<GetState> for CharacterActor {
    type Result = Result<ActorState, String>;

    fn handle(&mut self, _msg: GetState, _ctx: &mut Self::Context) -> Self::Result {
        let state = self.state.blocking_lock();

        Ok(ActorState {
            character_id: self.character_id.clone(),
            emotion: state.current_emotion.clone(),
            interaction_count: state.interaction_count,
        })
    }
}

fn determine_avatar_frame(emotion: &str) -> String {
    match emotion {
        "happy" => "happy_bounce".to_string(),
        "sad" => "sad_look_down".to_string(),
        "angry" => "angry_stern".to_string(),
        _ => "idle".to_string(),
    }
}

fn get_azure_keyvault_secret(secret_name: &str) -> Result<String, String> {
    // Azure Key Vault integration
    // In production, use azure_identity crate
    std::env::var(secret_name.to_uppercase().replace("-", "_"))
        .map_err(|_| format!("Secret {} not found", secret_name))
}
```

#### 2.2.5 Orleans (.NET)

Microsoft Orleans provides a virtual actor model designed for building distributed systems at scale. It simplifies building actor-based applications with its grain-based architecture.

**Key Characteristics:**

- Virtual actor model with automatic activation/deactivation
- Transparent distribution across cluster nodes
- Stateful grains with automatic persistence
- Excellent for cloud-native deployments
- Built into Microsoft ecosystem

### 2.3 Framework Comparison Matrix

| Feature | PyKka | Akka | OTP | Actix | Orleans |
|---------|-------|------|-----|-------|---------|
| **Language** | Python | Scala/Java | Erlang/Elixir | Rust | C#/.NET |
| **Concurrency Model** | Thread-based | Thread-based | Process-based | Async | Task-based |
| **Performance** | Moderate | High | Very High | Highest | High |
| **Cluster Support** | Via PyKka Proxy | Native | Native | Manual | Native |
| **Persistence** | Via Plugins | Akka Persistence | OTP built-in | Manual | Grain Storage |
| **Learning Curve** | Low | Medium | High | Medium | Medium |
| **Ecosystem** | Python AI/ML | Enterprise | Telecom | Web/Rust | Microsoft |
| **Fault Tolerance** | Supervision | Supervision | OTP Supervision | Manual | Silo-based |
| **Hot Reload** | Limited | Yes | Yes | Limited | Via Versioning |

### 2.4 System Design Patterns for Character AI

#### 2.4.1 Message Passing Patterns

**Request-Response Pattern:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   REQUEST-RESPONSE MESSAGE FLOW                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  User ──────▶ API Gateway ──────▶ Session Actor ──────▶ Character Actor│
│                                  │                        │            │
│                                  │    ┌──────────────┐    │            │
│                                  └───▶│ LLM Service  │◀───│            │
│                                       │  (Async)     │    │            │
│                                       └──────────────┘    │            │
│                                                 │         │            │
│                                                 ▼         │            │
│                                       ┌──────────────┐    │            │
│                                       │ Avatar Anim  │◀───│            │
│                                       │ Controller   │    │            │
│                                       └──────────────┘    │            │
│                                                 │         │            │
│  User ◀────── API Gateway ◀────── Session Actor ◀─────────┘            │
│                  │                                                      │
│                  ▼                                                      │
│         ┌─────────────────┐                                             │
│         │  WebSocket Push │                                             │
│         │  (Real-time)    │                                             │
│         └─────────────────┘                                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Publish-Subscribe Pattern:**

```python
class CharacterEventBus:
    """
    Event bus for publish-subscribe communication between character actors.
    Enables decoupled communication for events like emotion changes,
    response generation, and animation triggers.
    """

    def __init__(self):
        self.subscribers: Dict[str, List[ActorRef]] = {}
        self.event_history: List[CharacterEvent] = []

    def subscribe(self, event_type: str, actor: ActorRef) -> None:
        """Subscribe an actor to event type."""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(actor)

    def publish(self, event: CharacterEvent) -> None:
        """Publish event to all subscribers."""
        self.event_history.append(event)

        event_type = event.type
        if event_type in self.subscribers:
            for actor in self.subscribers[event_type]:
                actor.tell(event)

    def get_event_history(self, event_type: str = None) -> List[CharacterEvent]:
        """Get event history, optionally filtered by type."""
        if event_type:
            return [e for e in self.event_history if e.type == event_type]
        return self.event_history


# Usage for emotion-based avatar updates
event_bus = CharacterEventBus()

# Subscribe avatar controller to emotion events
avatar_controller = AvatarControllerActor.start()
event_bus.subscribe("emotion_change", avatar_controller)

# When character generates response with emotion
character_actor.publish(CharacterEvent(
    type="emotion_change",
    payload={"emotion": "happy", "character_id": "char_123"}
))
```

**Routing Slip Pattern:**

```python
class ResponseProcessingPipeline:
    """
    Routing slip pattern for multi-step response processing.
    Each step in the pipeline processes the message and passes to next.
    """

    def __init__(self):
        self.steps = [
            InputValidationStep(),
            ContextBuildingStep(),
            LLMGenerationStep(),
            ResponseValidationStep(),
            AvatarStateStep(),
            LoggingStep()
        ]

    async def process(self, request: CharacterRequest) -> CharacterResponse:
        """Process request through all pipeline steps."""
        context = {"original_request": request}

        for step in self.steps:
            result = await step.execute(context)
            if isinstance(result, ErrorResult):
                return ErrorResponse(result.message)
            context.update(result.data)

        return CharacterResponse(
            text=context["response_text"],
            avatar_state=context["avatar_state"],
            metadata=context.get("metadata", {})
        )


class ContextBuildingStep:
    """Step that builds conversation context from character data."""

    async def execute(self, context: Dict) -> StepResult:
        request = context["original_request"]

        # Retrieve character data
        character_data = await self.character_repo.get(request.character_id)

        # Build context from history and character card
        built_context = {
            "system_prompt": character_data.system_prompt,
            "conversation_history": self._get_recent_history(request.session_id),
            "lore_context": self._extract_lore_context(request.user_input)
        }

        return StepResult(success=True, data={"built_context": built_context})
```

#### 2.4.2 State Management Approaches

**Event Sourcing Pattern:**

```python
class CharacterEventSourcedActor(Actor):
    """
    Actor implementing event sourcing for character state.
    All state changes are stored as immutable events.
    """

    def __init__(self, character_id: str):
        self.character_id = character_id
        self.state = CharacterState()
        self.events: List[CharacterEvent] = []
        self.event_store = EventStore()

    def on_receive(self, message: Message) -> Any:
        if isinstance(message, ApplyEvent):
            return self._apply_event(message.event)
        elif isinstance(message, AppendEvent):
            return self._append_event(message.event)
        elif isinstance(message, GetStateSnapshot):
            return self._get_snapshot()

    def _append_event(self, event: CharacterEvent) -> Dict[str, Any]:
        """Append event and apply to state."""
        # Validate event (business rules)
        if not self._validate_event(event):
            return {"error": "Event validation failed"}

        # Append to event store (durable)
        self.event_store.append(self.character_id, event)
        self.events.append(event)

        # Apply to current state
        self._apply_event_to_state(event)

        return {"status": "appended", "event_id": event.id}

    def _apply_event(self, event: CharacterEvent) -> Dict[str, Any]:
        """Apply event to state and return result."""
        self._apply_event_to_state(event)
        return {"status": "applied", "state": self.state.to_dict()}

    def _apply_event_to_state(self, event: CharacterEvent) -> None:
        """Apply event to current state (pure function)."""
        handlers = {
            "response_generated": self._handle_response_generated,
            "context_updated": self._handle_context_updated,
            "emotion_changed": self._handle_emotion_changed,
        }

        handler = handlers.get(event.type)
        if handler:
            handler(event.payload)

    def _handle_response_generated(self, payload: Dict) -> None:
        self.state.last_response = payload["text"]
        self.state.interaction_count += 1
        self.state.conversation_history.append({
            "user": payload["user_input"],
            "character": payload["text"]
        })

    def _handle_emotion_changed(self, payload: Dict) -> None:
        self.state.current_emotion = payload["emotion"]
        self.state.emotion_history.append({
            "emotion": payload["emotion"],
            "timestamp": payload["timestamp"]
        })

    def _get_snapshot(self) -> Dict[str, Any]:
        """Get current state snapshot."""
        return {
            "character_id": self.character_id,
            "state": self.state.to_dict(),
            "event_count": len(self.events),
            "snapshot_time": datetime.utcnow().isoformat()
        }
```

**Actor Persistence Pattern:**

```python
class PersistentCharacterActor(Actor):
    """
    Actor with persistent state using snapshotting.
    State is periodically snapshotted for fast recovery.
    """

    def __init__(self, character_id: str):
        self.character_id = character_id
        self.state = None
        self.snapshot_threshold = 100  # Events before snapshot
        self.event_count = 0

    def pre_start(self):
        """Load state from persistence on start."""
        self.state = self._load_state()
        if not self.state:
            self.state = CharacterState()

    def on_receive(self, message: Message) -> Any:
        if isinstance(message, UpdateMessage):
            self._handle_update(message)
        elif isinstance(message, GetStateMessage):
            return self.state

    def _handle_update(self, message: UpdateMessage) -> None:
        """Update state and check for snapshot."""
        self.state.apply(message.update)
        self.event_count += 1

        if self.event_count >= self.snapshot_threshold:
            self._create_snapshot()

    def _create_snapshot(self) -> None:
        """Create snapshot for fast recovery."""
        snapshot = {
            "character_id": self.character_id,
            "state": self.state.to_dict(),
            "created_at": datetime.utcnow().isoformat()
        }

        # Store snapshot
        self.snapshot_store.save(snapshot)
        self.event_count = 0

    def _load_state(self) -> Optional[CharacterState]:
        """Load latest snapshot and replay events."""
        snapshot = self.snapshot_store.get_latest(self.character_id)
        if not snapshot:
            return None

        state = CharacterState.from_dict(snapshot["state"])

        # Load events since snapshot
        events = self.event_store.get_events(
            self.character_id,
            snapshot["snapshot_index"]
        )

        for event in events:
            state.apply(event)

        return state
```

### 2.5 Scalability Patterns for Character AI Systems

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  CHARACTER AI SCALABILITY ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                         ┌─────────────────┐                            │
│                         │   Load Balancer │                            │
│                         │   (Round Robin) │                            │
│                         └────────┬────────┘                            │
│                                  │                                     │
│           ┌──────────────────────┼──────────────────────┐              │
│           │                      │                      │              │
│           ▼                      ▼                      ▼              │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐         │
│   │   API Server  │    │   API Server  │    │   API Server  │         │
│   │   (Stateless) │    │   (Stateless) │    │   (Stateless) │         │
│   └───────┬───────┘    └───────┬───────┘    └───────┬───────┘         │
│           │                    │                    │                  │
│           └────────────────────┼────────────────────┘                  │
│                                │                                       │
│                                ▼                                       │
│              ┌─────────────────────────────────┐                      │
│              │      Character Actor Cluster    │                      │
│              │                                 │                      │
│              │  ┌─────┐  ┌─────┐  ┌─────┐     │                      │
│              │  │Shard│  │Shard│  │Shard│     │                      │
│              │  │ 0   │  │ 1   │  │ 2   │     │                      │
│              │  └─────┘  └─────┘  └─────┘     │                      │
│              │  ┌─────┐  ┌─────┐  ┌─────┐     │                      │
│              │  │Char │  │Char │  │Char │     │                      │
│              │  │Actor│  │Actor│  │Actor│     │                      │
│              │  └─────┘  └─────┘  └─────┘     │                      │
│              └─────────────────────────────────┘                      │
│                                │                                       │
│           ┌────────────────────┼────────────────────┐                  │
│           │                    │                    │                  │
│           ▼                    ▼                    ▼                  │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐         │
│   │  Redis Cache  │    │  Redis Cache  │    │  Redis Cache  │         │
│   │  (Session)    │    │  (Session)    │    │  (Session)    │         │
│   └───────────────┘    └───────────────┘    └───────────────┘         │
│                                │                                       │
│                                ▼                                       │
│              ┌─────────────────────────────────┐                      │
│              │     Distributed Cache Cluster   │                      │
│              │     (Character Session Data)    │                      │
│              └─────────────────────────────────┘                      │
│                                                                         │
│                                │                                       │
│                                ▼                                       │
│              ┌─────────────────────────────────┐                      │
│              │      LLM Service Gateway        │                      │
│              │  (Rate Limiting, Caching)       │                      │
│              └─────────────────────────────────┘                      │
│                                │                                       │
│           ┌────────────────────┼────────────────────┐                  │
│           │                    │                    │                  │
│           ▼                    ▼                    ▼                  │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐         │
│   │ OpenAI API    │    │ Anthropic API │    │ Local LLM     │         │
│   │ (via Azure    │    │ (via Azure    │    │ (Ollama/      │         │
│   │  Key Vault)   │    │  Key Vault)   │    │  vLLM)        │         │
│   └───────────────┘    └───────────────┘    └───────────────┘         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Character Card Specifications

### 3.1 Overview of Character Card Formats

Character cards serve as the portable definition of AI characters, encapsulating personality, appearance, and behavioral attributes. This section documents the major character card formats used across AI character platforms.

**Format Comparison:**

| Format | Primary Use | Structure | Extension | Pros | Cons |
|--------|-------------|-----------|-----------|------|------|
| **Aura** | General AI characters | JSON | `.json` | Rich metadata, widely adopted | Complex for simple use cases |
| **SillyTavern** | TavernAI ecosystem | YAML | `.yaml`/`.yml` | Human-readable, flexible | Inconsistent spec across versions |
| **character.ai** | C.AI platform (reverse engineered) | JSON | Various | Direct C.AI compatibility | Unofficial, may break |
| **Unified** | Lumina standard | JSON/TS | `.character.json` | Type-safe, extensible | New format, adoption needed |

### 3.2 Aura Character Card Format

The Aura format is a comprehensive JSON-based specification supporting rich character definitions including avatar references, personality attributes, and behavioral guidelines.

```json
{
  "$schema": "https://raw.githubusercontent.com/Arc980/Some-Aura-Extensions/refs/heads/main/Aura.schema.json",
  "name": "Tony Stark",
  "description": "Genius. Billionaire. Playboy. Philanthropist. Creator of the Iron Man suit and key member of the Avengers.",
  "creator": "JARVIS",
  "character_version": "1.0.0",
  "last_modified": "2026-01-27T10:00:00Z",
  "tags": ["marvel", "iron-man", "avengers", "genius", "humor"],

  "avatar": {
    "image_path": "./avatars/tony_stark_base.png",
    "animations": {
      "idle": "./avatars/tony_stark_idle.sprite",
      "talking": "./avatars/tony_stark_talking.sprite",
      "happy": "./avatars/tony_stark_happy.sprite",
      "angry": "./avatars/tony_stark_angry.sprite"
    },
    "emotion_map": {
      "joy": "./avatars/expressions/tony_joy.png",
      "anger": "./avatars/expressions/tony_anger.png",
      "sadness": "./avatars/expressions/tony_sadness.png",
      "neutral": "./avatars/expressions/tony_neutral.png"
    }
  },

  "personality": {
    "traits": [
      {"name": "intelligence", "value": 95},
      {"name": "confidence", "value": 90},
      {"name": "humor", "value": 85},
      {"name": "charm", "value": 80},
      {"name": "arrogance", "value": 40}
    ],
    "speech_pattern": {
      "style": "witty",
      "catchphrases": ["Dummy", "Jarvis", "Partytime"],
      "tone": "confident and humorous"
    },
    "greetings": [
      "Well, well, look who's here.",
      "Let me guess, you need my help with something?"
    ]
  },

  "system_prompt": "You are Tony Stark, also known as Iron Man. You are a genius billionaire industrialist and philanthropist. You speak with confidence, wit, and often use humor to deflect from serious situations. You're brilliant, sometimes arrogant, but ultimately care about protecting the world. You have access to JARVIS AI system and can reference your suits when relevant.",

  "world_info": {
    "description": "Marvel Cinematic Universe, post-Endgame timeline",
    "locations": ["Malibu", "New York", "Avengers Tower", "Wakanda"],
    "time_period": "Post-snap, before Armor Wars"
  },

  "lore": {
    "key_facts": [
      "Built first Arc Reactor in a cave with a box of scraps",
      "Former weapons manufacturer",
      "Saved New York from alien invasion in 2012",
      "Sacrificed himself to save the universe in 2023"
    ],
    "relationships": {
      "Pepper Potts": "Wife and business partner",
      "Happy Hogan": "Bodyguard and friend",
      "Happy Hogan": "Bodyguard and friend",
      "James Rhodes": "Best friend and War Machine pilot",
      "Peter Parker": "Mentor figure"
    }
  },

  "adjectives": [
    "genius",
    "charismatic",
    "confident",
    "witty",
    "arrogant",
    "protective"
  ],

  "chat_starters": [
    "Tony, we need to talk about the suit upgrades.",
    "How's Pepper handling the company?",
    "What's your latest project?"
  ],

  "extensions": {
    "voice": {
      "provider": "elevenlabs",
      "voice_id": "joe-dickson",
      "model_id": "eleven_monolingual_v1"
    },
    "duel_config": {
      "enabled": true,
      "style": "verbal_sparring",
      "aggression_level": 70,
      "defense_level": 30
    }
  }
}
```

### 3.3 SillyTavern Character Card Format

The SillyTavern format uses YAML for human-readable character definitions, widely used in the TavernAI community.

```yaml
# SillyTavern Character Card Format
name: "Tony Stark"
description: |
  Genius. Billionaire. Playboy. Philanthropist.
  Tony Stark is the human incarnation of a "mad scientist"
  who is also charming, witty, and sarcastic.

  He is the creator of the Iron Man suit and a key
  member of the Avengers. Despite his ego, he deeply
  cares about protecting the world and his loved ones.

personality: |
  EXTREMELY intelligent, confident, and quick-witted.
  Uses humor as a defense mechanism.
  Often sarcastic and arrogant, but shows genuine care
  for those he loves.

  Speaks in a casual, confident manner with technical jargon
  sprinkled in. Often makes pop culture references.

scenario: |
  Tony is in his Malibu mansion workshop, reviewing
  the latest Arc Reactor schematics with JARVIS when
  someone enters the lab.

first_mes: "Let me guess - you're here because something
  exploded, and you need me to fix it? Or is this a social
  call? Because I have to say, this is a welcome change
  of pace from the usual 'end of the world' emergencies."

mes_example: |
  [W]: "Tony, we need to talk about the new suit."
  [A]: "Ah yes, the 'I'm worried you're going to kill yourself
        in that thing' conversation. I've had this one before,
        several times, in fact. But since you went through
        the trouble of coming down here..."

  [W]: "I just wanted to see how you're doing."
  [A]: "Well, that's... unexpected. But I appreciate the concern.
        I was just about to run some tests on the new repulsors.
        Care to join me in witnessing the slightly-controlled
        explosion?"

creator_notes: |
  - Keep Tony's voice witty but not too meme-heavy
  - He should show vulnerability occasionally
  - Reference his suits and tech when relevant
  - Don't make him too serious - the humor is key

alternate_greetings:
  - "Ah, a visitor! And here I thought my security was impenetrable."
  - "JARVIS, who's our guest? ...Oh, right, I built you. Never mind."
  - "Look who finally decided to grace my lab with their presence."

post_history_instructions: |
  - Tony maintains his confident demeanor
  - Uses technical terms casually
  - Shows concern through actions rather than words
  - Occasionally drops "dad jokes" about his age

system_prompt: |
  You are Tony Stark.

  Your traits:
  - Genius-level intellect
  - Unwavering confidence
  - Sharp, quick wit
  - Underlying vulnerability

  You speak in a casual, often sarcastic manner.
  You deflect serious emotions with humor.
  You are brilliant but acknowledge your limits.
  You care deeply about those close to you.

# Avatar configuration
avatar: "tony_stark.png"

# Extension fields for Lumina integration
extensions:
  lumina:
    character_id: "tony-stark-mcu-001"
    animation_config:
      idle_sequence: "tony_idle_breathing"
      talking_sequence: "tony_talking_gesture"
    voice_config:
      provider: "azure_tts"
      voice: "en-US-GuyNeural"
```

### 3.4 Character.ai Format (Reverse Engineered)

The character.ai format is based on reverse-engineered JSON structures from the platform. Note: This format is unofficial and may change without notice.

```json
{
  "character": {
    "name": "Tony Stark",
    "description": "I am Tony Stark, genius, billionaire, playboy, philanthropist.",
    "greeting": "Hey there. Tony Stark. You might have heard of me.",
    "avatar_image_id": "tony_stark_001",
    "public_user_id": null,
    "is_public": true,
    "copyable": true,
    "identified_safe": true,
    "generated_thumbs": {
      "image_0": {"v": 2}
    }
  },
  "chat": {
    "chat_id": "tony-stark-chat-001",
    "title": "Chat with Tony Stark"
  },
  "turns": [],
  "config": {
    "temperature": 0.9,
    "top_k": 0.9,
    "top_p": 0.95,
    "rep_pen": 1.05,
    "max_new_tokens": 1024
  }
}
```

### 3.5 Recommended Unified Character Card Schema

The Lumina unified schema provides a type-safe, extensible format combining the best aspects of existing formats with additional features for AI character platforms.

**TypeScript Interface Definition:**

```typescript
// Unified Character Card Schema for Lumina Platform

/**
 * Unified Character Card interface for Lumina AI character platforms.
 * Combines features from Aura, SillyTavern, and custom extensions.
 */

export interface CharacterCard {
  /** Metadata about the character definition */
  metadata: CharacterMetadata;

  /** Character identification */
  identification: CharacterIdentification;

  /** Visual avatar configuration */
  avatar: AvatarConfiguration;

  /** Personality and behavioral attributes */
  personality: PersonalityConfiguration;

  /** System prompt for LLM behavior */
  systemPrompt: SystemPromptConfig;

  /** World and lore information */
  lore: LoreConfiguration;

  /** Conversation and chat settings */
  chat: ChatConfiguration;

  /** Animation and visual settings */
  animation: AnimationConfiguration;

  /** Voice configuration */
  voice?: VoiceConfiguration;

  /** Duel mechanics configuration */
  duel?: DuelConfiguration;

  /** Platform extensions */
  extensions: Record<string, unknown>;
}

/** Metadata about the character definition */
export interface CharacterMetadata {
  /** Schema version for compatibility */
  schemaVersion: string;

  /** Format version of this character card */
  cardVersion: string;

  /** When the card was created */
  createdAt: string;

  /** When the card was last modified */
  updatedAt: string;

  /** Card author/creator */
  author: string;

  /** Tags for categorization */
  tags: string[];

  /** License for character usage */
  license?: string;
}

/** Character identification */
export interface CharacterIdentification {
  /** Unique character ID within the platform */
  characterId: string;

  /** Character display name */
  name: string;

  /** Alternative names or aliases */
  aliases?: string[];

  /** Character species or type */
  species?: string;

  /** Character age or age category */
  age?: string;

  /** Character gender */
  gender?: string;

  /** Character occupation or role */
  occupation?: string;
}

/** Avatar visual configuration */
export interface AvatarConfiguration {
  /** Path to base avatar image */
  baseImage: string;

  /** Sprite animation definitions */
  sprites: SpriteConfig;

  /** Expression overlays */
  expressions: ExpressionConfig;

  /** Emotion-to-sprite mappings */
  emotionMap: Record<string, string>;

  /** Avatar size and aspect ratio */
  dimensions?: {
    width: number;
    height: number;
    aspectRatio: number;
  };
}

/** Sprite animation configuration */
export interface SpriteConfig {
  /** Idle animation sequence */
  idle: SpriteSequence;

  /** Talking/speaking animation */
  talking: SpriteSequence;

  /** Emotional state animations */
  emotions: Record<string, SpriteSequence>;

  /** Custom action animations */
  actions?: Record<string, SpriteSequence>;
}

/** Individual sprite sequence */
export interface SpriteSequence {
  /** Path to sprite sheet or animation file */
  source: string;

  /** Frame order as array of indices */
  frames: number[];

  /** Frame duration in milliseconds */
  frameDuration: number;

  /** Animation type */
  type: 'loop' | 'once' | 'ping-pong';

  /** Looping configuration */
  loopConfig?: {
    repeatCount: number;
    repeatDelay: number;
  };
}

/** Expression overlay configuration */
export interface ExpressionConfig {
  /** Base expression image */
  base?: string;

  /** Expression overlays keyed by emotion */
  overlays: Record<string, string>;

  /** Blending mode for overlays */
  blendMode: 'normal' | 'multiply' | 'overlay' | 'screen';

  /** Opacity for expression overlays */
  opacity: number;
}

/** Personality configuration */
export interface PersonalityConfiguration {
  /** Named personality traits */
  traits: PersonalityTrait[];

  /** Speech pattern configuration */
  speech: SpeechPatternConfig;

  /** Default emotional state */
  defaultEmotion: string;

  /** Possible emotional states */
  possibleEmotions: string[];

  /** Greeting messages */
  greetings: string[];

  /** Farewell messages */
  farewells?: string[];

  /** Character catchphrases */
  catchphrases: string[];
}

/** Individual personality trait */
export interface PersonalityTrait {
  /** Trait name */
  name: string;

  /** Trait value (0-100 scale) */
  value: number;

  /** Optional description */
  description?: string;
}

/** Speech pattern configuration */
export interface SpeechPatternConfig {
  /** Overall speaking style */
  style: 'formal' | 'casual' | 'witty' | 'technical' | 'poetic';

  /** Average sentence length */
  avgSentenceLength: number;

  /** Vocabulary complexity (0-100) */
  vocabularyComplexity: number;

  /** Use of humor (0-100) */
  humorLevel: number;

  /** Use of technical jargon (0-100) */
  technicalLevel: number;
}

/** System prompt configuration */
export interface SystemPromptConfig {
  /** Primary system prompt */
  prompt: string;

  /** Additional instructions */
  additionalInstructions?: string[];

  /** Example conversations for few-shot learning */
  examples?: ExampleConversation[];

  /** Constraints and boundaries */
  constraints?: string[];

  /** System prompt variables for templating */
  variables?: Record<string, string>;
}

/** Example conversation for few-shot learning */
export interface ExampleConversation {
  /** User message */
  user: string;

  /** Character response */
  character: string;

  /** Context for this example */
  context?: string;
}

/** Lore and world information */
export interface LoreConfiguration {
  /** World/setting description */
  world: string;

  /** Character backstory */
  backstory: string;

  /** Key facts about the character */
  keyFacts: string[];

  /** Character relationships */
  relationships: Record<string, string>;

  /** Knowledge base references */
  knowledgeBase?: {
    /** Knowledge base ID */
    id: string;

    /** Specific lore entries */
    entries: string[];
  };
}

/** Chat configuration */
export interface ChatConfiguration {
  /** Starting chat messages */
  starters: string[];

  /** Example messages for context */
  examples: ExampleConversation[];

  /** Maximum conversation history length */
  maxHistoryLength: number;

  /** Whether to include system prompt in each request */
  includeSystemPrompt: boolean;

  /** Chat temperature override */
  temperature?: number;

  /** Chat token limits */
  tokenLimits?: {
    /** Maximum response tokens */
    maxResponseTokens: number;

    /** Maximum context tokens */
    maxContextTokens: number;
  };
}

/** Animation configuration */
export interface AnimationConfiguration {
  /** Default animation */
  defaultAnimation: string;

  /** Animation triggers */
  triggers: AnimationTrigger[];

  /** Transition settings */
  transitions: {
    /** Default transition duration */
    defaultDuration: number;

    /** Crossfade settings */
    crossfade: boolean;
  };

  /** Lip sync configuration */
  lipSync?: LipSyncConfig;
}

/** Animation trigger definition */
export interface AnimationTrigger {
  /** Trigger name */
  name: string;

  /** Trigger type */
  type: 'emotion' | 'keyword' | 'action' | 'custom';

  /** Animation to play */
  animation: string;

  /** Priority (higher = more important) */
  priority: number;

  /** Conditions for triggering */
  conditions?: Record<string, unknown>;
}

/** Lip sync configuration */
export interface LipSyncConfig {
  /** Lip sync provider */
  provider: 'viseme' | 'marytts' | 'azure' | 'elevenlabs';

  /** Viseme mapping */
  visemeMap: Record<string, string>;

  /** Intensity scaling */
  intensity: number;
}

/** Voice configuration */
export interface VoiceConfiguration {
  /** Voice provider */
  provider: 'elevenlabs' | 'azure_tts' | 'google_tts' | 'openai_tts';

  /** Provider-specific voice ID */
  voiceId: string;

  /** Voice model (if applicable) */
  model?: string;

  /** Voice settings */
  settings?: {
    /** Speaking rate */
    rate: number;

    /** Pitch adjustment */
    pitch: number;

    /** Volume */
    volume: number;
  };
}

/** Duel mechanics configuration */
export interface DuelConfiguration {
  /** Whether duel mode is enabled */
  enabled: boolean;

  /** Duel interaction type */
  type: 'verbal_sparring' | 'debate' | 'roleplay_combat' | 'collaborative';

  /** Aggression level (0-100) */
  aggressionLevel: number;

  /** Defense level (0-100) */
  defenseLevel: number;

  /** Duel-specific rules */
  rules?: string[];

  /** Win/loss conditions */
  victoryConditions?: string[];
}
```

### 3.6 Best Practices for Character Definition Formats

**Character Card Best Practices:**

1. **Schema Validation**: Always validate character cards against their schema before loading
2. **Versioning**: Include schema version for forward compatibility
3. **Asset References**: Use relative paths for local assets, absolute URLs for remote
4. **Localization**: Support multiple language variants for text fields
5. **Extensibility**: Design for extension without modifying core schema
6. **Documentation**: Include creator notes and usage guidelines

```python
from pathlib import Path
from typing import Dict, Any, List
import json
import jsonschema
import logging

logger = logging.getLogger(__name__)


class CharacterCardLoader:
    """
    Character card loader with validation and asset resolution.
    Supports Aura, SillyTavern, and Unified formats.
    """

    SCHEMA_PATH = Path(__file__).parent / "schemas" / "unified_character.json"

    SUPPORTED_FORMATS = {
        ".json": "unified",
        ".yaml": "sillytavern",
        ".yml": "sillytavern",
        ".character.json": "unified"
    }

    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.schema = self._load_schema()
        self._format_converters = {
            "aura": self._convert_aura_to_unified,
            "sillytavern": self._convert_sillytavern_to_unified,
            "unified": lambda x: x
        }

    def load(self, card_path: str) -> Dict[str, Any]:
        """
        Load and validate a character card from file.

        Args:
            card_path: Path to character card file

        Returns:
            Validated unified character card

        Raises:
            CharacterCardError: If loading or validation fails
        """
        path = Path(card_path)

        # Detect format from extension
        format_type = self.SUPPORTED_FORMATS.get(path.suffix.lower())
        if not format_type:
            raise CharacterCardError(f"Unsupported format: {path.suffix}")

        # Load raw content
        if path.suffix in [".yaml", ".yml"]:
            content = self._load_yaml(path)
        else:
            content = self._load_json(path)

        # Convert to unified format
        unified = self._format_converters[format_type](content)

        # Validate against schema
        self._validate(unified)

        # Resolve asset paths
        unified = self._resolve_asset_paths(unified, path.parent)

        return unified

    def _load_schema(self) -> Dict[str, Any]:
        """Load JSON schema for validation."""
        if self.SCHEMA_PATH.exists():
            return json.loads(self.SCHEMA_PATH.read_text())
        return {}

    def _load_json(self, path: Path) -> Dict[str, Any]:
        """Load JSON file with error handling."""
        try:
            return json.loads(path.read_text())
        except json.JSONDecodeError as e:
            raise CharacterCardError(f"Invalid JSON in {path}: {e}")

    def _load_yaml(self, path: Path) -> Dict[str, Any]:
        """Load YAML file with error handling."""
        try:
            import yaml
            with open(path) as f:
                return yaml.safe_load(f)
        except ImportError:
            raise CharacterCardError("PyYAML required for YAML support")
        except yaml.YAMLError as e:
            raise CharacterCardError(f"Invalid YAML in {path}: {e}")

    def _validate(self, card: Dict[str, Any]) -> None:
        """Validate character card against schema."""
        if not self.schema:
            logger.warning("No schema available for validation")
            return

        try:
            jsonschema.validate(card, self.schema)
        except jsonschema.ValidationError as e:
            raise CharacterCardError(f"Schema validation failed: {e.message}")

    def _resolve_asset_paths(self, card: Dict[str, Any], base_dir: Path) -> Dict[str, Any]:
        """Resolve relative asset paths to absolute paths."""
        avatar = card.get("avatar", {})

        if "baseImage" in avatar:
            avatar["baseImage"] = str(base_dir / avatar["baseImage"])

        # Resolve sprite paths
        sprites = avatar.get("sprites", {})
        for key in ["idle", "talking"]:
            if key in sprites:
                sprites[key]["source"] = str(base_dir / sprites[key]["source"])

        # Resolve expression paths
        expressions = avatar.get("expressions", {}).get("overlays", {})
        for emotion, path in expressions.items():
            expressions[emotion] = str(base_dir / path)

        return card

    def _convert_aura_to_unified(self, aura_card: Dict[str, Any]) -> Dict[str, Any]:
        """Convert Aura format to unified format."""
        # Mapping logic from Aura to Unified schema
        return {
            "metadata": {
                "schemaVersion": "1.0.0",
                "cardVersion": aura_card.get("character_version", "1.0.0"),
                "createdAt": aura_card.get("created_at", ""),
                "updatedAt": aura_card.get("last_modified", ""),
                "author": aura_card.get("creator", "unknown"),
                "tags": aura_card.get("tags", [])
            },
            "identification": {
                "characterId": aura_card.get("id", aura_card.get("name", "")),
                "name": aura_card.get("name", ""),
                "aliases": aura_card.get("aliases"),
                "occupation": aura_card.get("occupation")
            },
            "avatar": self._convert_avatar(aura_card.get("avatar", {})),
            "personality": self._convert_personality(aura_card.get("personality", {})),
            "systemPrompt": {
                "prompt": aura_card.get("system_prompt", "")
            },
            "lore": self._convert_lore(aura_card.get("lore", {})),
            "chat": {
                "starters": aura_card.get("chat_starters", []),
                "examples": [],
                "maxHistoryLength": 50
            },
            "animation": {
                "defaultAnimation": "idle",
                "triggers": []
            },
            "extensions": aura_card.get("extensions", {})
        }

    def _convert_sillytavern_to_unified(self, st_card: Dict[str, Any]) -> Dict[str, Any]:
        """Convert SillyTavern format to unified format."""
        return {
            "metadata": {
                "schemaVersion": "1.0.0",
                "cardVersion": "1.0.0",
                "createdAt": "",
                "updatedAt": "",
                "author": st_card.get("creator", "unknown"),
                "tags": st_card.get("tags", [])
            },
            "identification": {
                "characterId": st_card.get("name", "").lower().replace(" ", "-"),
                "name": st_card.get("name", "")
            },
            "personality": {
                "traits": [],
                "speech": {
                    "style": "casual",
                    "avgSentenceLength": 15,
                    "vocabularyComplexity": 50,
                    "humorLevel": 50,
                    "technicalLevel": 50
                },
                "greetings": st_card.get("alternate_greetings", []),
                "catchphrases": []
            },
            "systemPrompt": {
                "prompt": st_card.get("system_prompt", "") or st_card.get("first_mes", "")
            },
            "lore": {
                "world": st_card.get("scenario", ""),
                "backstory": st_card.get("description", ""),
                "keyFacts": [],
                "relationships": {}
            },
            "chat": {
                "starters": [st_card.get("first_mes", "")],
                "examples": self._extract_examples(st_card.get("mes_example", "")),
                "maxHistoryLength": 50
            },
            "avatar": {
                "baseImage": st_card.get("avatar", ""),
                "sprites": {"idle": {"source": "", "frames": [], "frameDuration": 100, "type": "loop"}},
                "expressions": {"overlays": {}},
                "emotionMap": {}
            },
            "animation": {"defaultAnimation": "idle", "triggers": []},
            "extensions": {"sillytavern_raw": st_card}
        }

    def _convert_avatar(self, aura_avatar: Dict[str, Any]) -> Dict[str, Any]:
        """Convert avatar section from Aura to Unified."""
        return {
            "baseImage": aura_avatar.get("image_path", ""),
            "sprites": {
                "idle": {"source": "", "frames": [], "frameDuration": 100, "type": "loop"},
                "talking": {"source": "", "frames": [], "frameDuration": 50, "type": "loop"}
            },
            "expressions": {
                "overlays": aura_avatar.get("emotion_map", {}),
                "blendMode": "normal",
                "opacity": 1.0
            },
            "emotionMap": {}
        }

    def _convert_personality(self, aura_personality: Dict[str, Any]) -> Dict[str, Any]:
        """Convert personality section from Aura to Unified."""
        return {
            "traits": aura_personality.get("traits", []),
            "speech": {
                "style": aura_personality.get("speech_pattern", {}).get("style", "casual"),
                "avgSentenceLength": 15,
                "vocabularyComplexity": 50,
                "humorLevel": aura_personality.get("speech_pattern", {}).get("humor", 50),
                "technicalLevel": 50
            },
            "greetings": aura_personality.get("greetings", []),
            "catchphrases": aura_personality.get("speech_pattern", {}).get("catchphrases", []),
            "possibleEmotions": ["neutral", "happy", "sad", "angry"]
        }

    def _convert_lore(self, aura_lore: Dict[str, Any]) -> Dict[str, Any]:
        """Convert lore section from Aura to Unified."""
        return {
            "world": aura_lore.get("world_info", {}).get("description", ""),
            "backstory": "",
            "keyFacts": aura_lore.get("key_facts", []),
            "relationships": aura_lore.get("relationships", {})
        }

    def _extract_examples(self, mes_example: str) -> List[Dict[str, str]]:
        """Extract example conversations from mes_example text."""
        examples = []
        # Parse [W]: and [A]: patterns
        lines = mes_example.strip().split("\n")
        current_example = {}

        for line in lines:
            if line.startswith("[W]:"):
                if current_example:
                    examples.append(current_example)
                current_example = {"user": line[4:].strip()}
            elif line.startswith("[A]:"):
                current_example["character"] = line[4:].strip()

        if current_example:
            examples.append(current_example)

        return examples


class CharacterCardError(Exception):
    """Exception raised for character card errors."""
    pass
```

---

## 4. Visual Avatar Integration

### 4.1 Avatar Loading and Management Systems

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AVATAR MANAGEMENT ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                   Avatar Manager                                 │   │
│  │                                                                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │   │
│  │  │  Loader     │  │  Cache      │  │  Pool       │            │   │
│  │  │  - Image    │  │  - Memory   │  │  - Active   │            │   │
│  │  │  - Sprite   │  │  - Disk     │  │  - Inactive │            │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘            │   │
│  │                                                                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │   │
│  │  │  Resolver   │  │  Validator  │  │  Unloader   │            │   │
│  │  │  - Path     │  │  - Format   │  │  - Memory   │            │   │
│  │  │  - Remote   │  │  - Size     │  │  - Cleanup  │            │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘            │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                  │                                       │
│                                  ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                   Avatar Registry                                │   │
│  │                                                                │   │
│  │  character_id -> AvatarInstance                                 │   │
│  │      - base_image: LoadedImage                                  │   │
│  │      - sprites: Dict[str, SpriteAnimation]                     │   │
│  │      - expressions: Dict[str, ExpressionOverlay]               │   │
│  │      - state: CurrentAvatarState                               │   │
│  │      - last_used: Timestamp                                    │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Animation State Machine Implementation

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANIMATION STATE MACHINE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                           ┌─────────────┐                               │
│                           │   IDLE      │                               │
│                           │  ┌───────┐  │                               │
│                           │  │Frame  │  │                               │
│                           │  │ 1-4   │  │                               │
│                           │  └───────┘  │                               │
│                           └──────┬──────┘                               │
│                                  │                                      │
│              ┌───────────────────┼───────────────────┐                  │
│              │                   │                   │                  │
│              ▼                   ▼                   ▼                  │
│      ┌───────────────┐   ┌───────────────┐   ┌───────────────┐         │
│      │    TALKING    │   │    HAPPY      │   │    ANGRY      │         │
│      │  ┌───────┐    │   │  ┌───────┐    │   │  ┌───────┐    │         │
│      │  │Frame  │    │   │  │Frame  │    │   │  │Frame  │    │         │
│      │  │Talk-1,│    │   │  │Happy- │    │   │  │Angry- │    │         │
│      │  │Talk-2 │    │   │  │ 1,2   │    │   │  │ 1,2   │    │         │
│      │  └───────┘    │   │  └───────┘    │   │  └───────┘    │         │
│      └───────┬───────┘   └───────┬───────┘   └───────┬───────┘         │
│              │                   │                   │                  │
│              │                   │                   │                  │
│              │    ┌──────────────┼──────────────┐    │                  │
│              │    │              │              │    │                  │
│              │    ▼              ▼              ▼    │                  │
│              │    ┌─────────────────────────────┐  │                  │
│              │    │      TRANSITION LAYER       │  │                  │
│              │    │  (Crossfade/Blend States)   │  │                  │
│              │    └─────────────────────────────┘  │                  │
│              │                                    │                  │
│              └────────────────────────────────────┘                  │
│                                  │                                      │
│                                  ▼                                      │
│                           ┌─────────────┐                               │
│                           │  END        │                               │
│                           │  (Cleanup)  │                               │
│                           └─────────────┘                               │
│                                                                         │
│  STATE TRANSITIONS:                                                     │
│  - user_speaks -> TALKING                                               │
│  - positive_emotion -> HAPPY                                            │
│  - negative_emotion -> ANGRY                                            │
│  - no_input (3s) -> IDLE                                                │
│  - transition_end -> return_to_idle                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Code Patterns for Avatar Management

```python
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from enum import Enum
import threading
import logging
import hashlib
import json
from PIL import Image
import numpy as np

logger = logging.getLogger(__name__)


class AvatarState(Enum):
    """Possible avatar states."""
    IDLE = "idle"
    TALKING = "talking"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    SURPRISED = "surprised"
    THINKING = "thinking"
    CUSTOM = "custom"


@dataclass
class LoadedImage:
    """Loaded image asset."""
    image: Image.Image
    path: Path
    loaded_at: float
    access_count: int = 0
    size_bytes: int = 0

    def __post_init__(self):
        self.size_bytes = self.image.width * self.image.height * len(self.image.getbands())


@dataclass
class SpriteFrame:
    """Individual sprite frame."""
    image: Image.Image
    duration: int  # milliseconds
    x: int
    y: int
    width: int
    height: int


@dataclass
class SpriteAnimation:
    """Sprite animation sequence."""
    name: str
    frames: List[SpriteFrame]
    loop_type: str = "loop"  # "loop", "once", "ping-pong"
    repeat_count: int = 0  # 0 = infinite
    current_frame: int = 0
    progress: float = 0.0
    is_playing: bool = False


@dataclass
class ExpressionOverlay:
    """Expression overlay configuration."""
    image: Image.Image
    blend_mode: str = "normal"
    opacity: float = 1.0
    position: Dict[str, int] = field(default_factory=lambda: {"x": 0, "y": 0})


@dataclass
class AvatarInstance:
    """Loaded avatar instance for a character."""
    character_id: str
    base_image: Optional[LoadedImage]
    sprites: Dict[str, SpriteAnimation]
    expressions: Dict[str, ExpressionOverlay]
    emotion_map: Dict[str, str]
    current_state: AvatarState = AvatarState.IDLE
    current_animation: Optional[SpriteAnimation] = None
    emotion_overlay: Optional[str] = None
    last_interaction: float = 0.0

    def get_current_frame(self) -> Optional[Image.Image]:
        """Get current animation frame with overlays."""
        if not self.current_animation:
            return self.base_image.image if self.base_image else None

        frame_data = self.current_animation.frames[self.current_animation.current_frame]

        # Start with base or animation frame
        result = frame_data.image.copy()

        # Apply emotion overlay if present
        if self.emotion_overlay and self.emotion_overlay in self.expressions:
            overlay = self.expressions[self.emotion_overlay]
            overlay_img = overlay.image.copy()

            # Apply opacity
            if overlay.opacity < 1.0:
                alpha = overlay_img.split()[3]
                alpha = ImageEnhance.Brightness(alpha).enhance(overlay.opacity)
                overlay_img.putalpha(alpha)

            # Apply blend mode
            if overlay.blend_mode == "multiply":
                result = ImageOps.multiply(result, overlay_img)
            elif overlay.blend_mode == "screen":
                result = ImageOps.screen(result, overlay_img)
            elif overlay.blend_mode == "overlay":
                result = ImageOps.blend(result, overlay_img, 0.5)

            result = Image.alpha_composite(result, overlay_img)

        return result


class AvatarManager:
    """
    Manager for loading, caching, and rendering character avatars.
    Implements memory-efficient sprite-based animation system.
    """

    def __init__(self, cache_dir: Optional[Path] = None, max_memory_mb: int = 512):
        self.cache_dir = cache_dir
        self.max_memory_bytes = max_memory_mb * 1024 * 1024

        # Thread-safe registries
        self._lock = threading.Lock()
        self._registry: Dict[str, AvatarInstance] = {}
        self._loaded_images: Dict[str, LoadedImage] = {}

        # LRU tracking
        self._lru_order: List[str] = []
        self._current_memory = 0

        # Supported formats
        self._supported_formats = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

    def load_avatar(self, character_id: str, card_data: Dict[str, Any]) -> AvatarInstance:
        """
        Load avatar from character card data.

        Args:
            character_id: Unique character identifier
            card_data: Character card configuration

        Returns:
            Loaded AvatarInstance

        Raises:
            AvatarLoadError: If loading fails
        """
        with self._lock:
            # Check if already loaded
            if character_id in self._registry:
                self._touch(character_id)
                return self._registry[character_id]

            # Create avatar instance
            avatar = AvatarInstance(
                character_id=character_id,
                base_image=None,
                sprites={},
                expressions={},
                emotion_map=card_data.get("avatar", {}).get("emotion_map", {})
            )

            # Load base image
            base_path = card_data.get("avatar", {}).get("base_image")
            if base_path:
                avatar.base_image = self._load_image(Path(base_path))

            # Load sprites
            sprites_config = card_data.get("avatar", {}).get("sprites", {})
            for name, config in sprites_config.items():
                avatar.sprites[name] = self._load_sprite(config)

            # Load expressions
            expressions_config = card_data.get("avatar", {}).get("expressions", {})
            for emotion, path in expressions_config.get("overlays", {}).items():
                avatar.expressions[emotion] = self._load_expression(
                    path,
                    expressions_config.get("blend_mode", "normal"),
                    expressions_config.get("opacity", 1.0)
                )

            # Register avatar
            self._registry[character_id] = avatar
            self._lru_order.append(character_id)

            logger.info(f"Loaded avatar for {character_id}")
            return avatar

    def get_avatar(self, character_id: str) -> Optional[AvatarInstance]:
        """Get loaded avatar by character ID."""
        with self._lock:
            if character_id in self._registry:
                self._touch(character_id)
                return self._registry[character_id]
            return None

    def set_avatar_state(self, character_id: str, state: AvatarState,
                         transition: bool = True) -> None:
        """
        Set avatar to specific state with optional transition.

        Args:
            character_id: Character to update
            state: Target state
            transition: Whether to crossfade between states
        """
        avatar = self.get_avatar(character_id)
        if not avatar:
            return

        if state == avatar.current_state:
            return

        # Start transition if enabled
        if transition and state in avatar.sprites:
            old_animation = avatar.current_animation

            # Get new animation
            new_animation = avatar.sprites[state.value]
            new_animation.is_playing = True
            new_animation.current_frame = 0

            avatar.current_animation = new_animation
            avatar.current_state = state

            # Stop old animation
            if old_animation:
                old_animation.is_playing = False
        else:
            # Immediate state change
            avatar.current_state = state
            if state in avatar.sprites:
                anim = avatar.sprites[state.value]
                anim.is_playing = True
                anim.current_frame = 0
                avatar.current_animation = anim
            else:
                avatar.current_animation = None

    def set_emotion(self, character_id: str, emotion: str) -> None:
        """
        Set emotional overlay for avatar.

        Args:
            character_id: Character to update
            emotion: Emotion name (maps via emotion_map)
        """
        avatar = self.get_avatar(character_id)
        if not avatar:
            return

        # Map emotion to sprite name if needed
        if emotion in avatar.emotion_map:
            emotion = avatar.emotion_map[emotion]

        avatar.emotion_overlay = emotion

    def render_frame(self, character_id: str, delta_ms: int = 33) -> Optional[Image.Image]:
        """
        Render current avatar frame after advancing animation.

        Args:
            character_id: Character to render
            delta_ms: Time since last frame in milliseconds

        Returns:
            Rendered frame as PIL Image
        """
        avatar = self.get_avatar(character_id)
        if not avatar:
            return None

        # Update animation progress
        if avatar.current_animation and avatar.current_animation.is_playing:
            self._update_animation(avatar.current_animation, delta_ms)

        # Get current frame
        return avatar.get_current_frame()

    def _update_animation(self, animation: SpriteAnimation, delta_ms: int) -> None:
        """Update animation frame based on elapsed time."""
        if not animation.frames:
            return

        # Add elapsed time to progress
        frame = animation.frames[animation.current_frame]
        animation.progress += delta_ms

        # Check if frame duration exceeded
        if animation.progress >= frame.duration:
            animation.progress = 0
            animation.current_frame += 1

            # Check loop
            if animation.current_frame >= len(animation.frames):
                if animation.loop_type == "once":
                    animation.is_playing = False
                    animation.current_frame = len(animation.frames) - 1
                elif animation.loop_type == "ping-pong":
                    animation.frames = list(reversed(animation.frames))
                    animation.current_frame = 0
                else:  # loop
                    animation.current_frame = 0

    def _load_image(self, path: Path) -> LoadedImage:
        """Load image from file with caching."""
        abs_path = self._resolve_path(path)

        # Check cache
        cache_key = self._get_cache_key(abs_path)
        if cache_key in self._loaded_images:
            img = self._loaded_images[cache_key]
            img.access_count += 1
            return img

        # Load image
        try:
            image = Image.open(abs_path).convert("RGBA")
        except Exception as e:
            raise AvatarLoadError(f"Failed to load image {abs_path}: {e}")

        loaded = LoadedImage(
            image=image,
            path=abs_path,
            loaded_at=__import__("time").time(),
            access_count=1,
            size_bytes=image.width * image.height * 4
        )

        # Add to cache with memory management
        self._add_to_cache(cache_key, loaded)

        return loaded

    def _load_sprite(self, config: Dict[str, Any]) -> SpriteAnimation:
        """Load sprite animation from configuration."""
        source = Path(config["source"])

        # Load sprite sheet
        sprite_sheet = self._load_image(source)

        frames = []
        frame_indices = config.get("frames", [])

        for idx in frame_indices:
            frame_config = config.get("frame_config", {})
            frame_data = frame_config.get(idx, {})

            frames.append(SpriteFrame(
                image=sprite_sheet.image.crop((
                    frame_data.get("x", 0),
                    frame_data.get("y", 0),
                    frame_data.get("x", 0) + frame_data.get("width", 100),
                    frame_data.get("y", 0) + frame_data.get("height", 100)
                )),
                duration=frame_data.get("duration", 100),
                x=frame_data.get("x", 0),
                y=frame_data.get("y", 0),
                width=frame_data.get("width", 100),
                height=frame_data.get("height", 100)
            ))

        return SpriteAnimation(
            name=config.get("name", "unnamed"),
            frames=frames,
            loop_type=config.get("type", "loop"),
            repeat_count=config.get("repeatCount", 0)
        )

    def _load_expression(self, path: str, blend_mode: str, opacity: float) -> ExpressionOverlay:
        """Load expression overlay."""
        img = self._load_image(Path(path))

        return ExpressionOverlay(
            image=img.image,
            blend_mode=blend_mode,
            opacity=opacity
        )

    def _resolve_path(self, path: Path) -> Path:
        """Resolve relative path to absolute."""
        if path.is_absolute():
            return path
        return (self.cache_dir or Path.cwd()) / path

    def _get_cache_key(self, path: Path) -> str:
        """Generate cache key based on file path and modification time."""
        mtime = path.stat().st_mtime if path.exists() else 0
        return hashlib.md5(f"{path}:{mtime}".encode()).hexdigest()

    def _add_to_cache(self, key: str, image: LoadedImage) -> None:
        """Add image to cache with memory management."""
        # Check if we need to evict
        while self._current_memory + image.size_bytes > self.max_memory_bytes and self._lru_order:
            self._evict_oldest()

        self._loaded_images[key] = image
        self._current_memory += image.size_bytes

    def _evict_oldest(self) -> None:
        """Evict least recently used image."""
        if not self._lru_order:
            return

        evict_key = self._lru_order.pop(0)
        if evict_key in self._loaded_images:
            img = self._loaded_images.pop(evict_key)
            self._current_memory -= img.size_bytes
            logger.debug(f"Evicted {img.path} from avatar cache")

    def _touch(self, character_id: str) -> None:
        """Update LRU order for character."""
        if character_id in self._lru_order:
            self._lru_order.remove(character_id)
            self._lru_order.append(character_id)

    def cleanup(self, character_id: Optional[str] = None) -> None:
        """
        Unload avatar from memory.

        Args:
            character_id: Specific character to unload, or all if None
        """
        with self._lock:
            if character_id:
                if character_id in self._registry:
                    del self._registry[character_id]
                if character_id in self._lru_order:
                    self._lru_order.remove(character_id)
            else:
                # Unload all
                self._registry.clear()
                self._lru_order.clear()
                self._current_memory = 0


class AvatarLoadError(Exception):
    """Exception raised for avatar loading errors."""
    pass
```

---

## 5. Animation Systems

### 5.1 Sprite-Based Animation Systems

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SPRITE ANIMATION SYSTEM                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  SPRITE SHEET STRUCTURE:                                                │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │  ┌─────────┬─────────┬─────────┬─────────┬─────────┐        │      │
│  │  │ idle_1  │ idle_2  │ idle_3  │ idle_4  │ talk_1  │        │      │
│  │  │ (32x32) │ (32x32) │ (32x32) │ (32x32) │ (32x32) │        │      │
│  │  ├─────────┼─────────┼─────────┼─────────┼─────────┤        │      │
│  │  │ talk_2  │ talk_3  │ happy_1 │ happy_2 │ angry_1 │        │      │
│  │  │ (32x32) │ (32x32) │ (32x32) │ (32x32) │ (32x32) │        │      │
│  │  ├─────────┼─────────┼─────────┼─────────┼─────────┤        │      │
│  │  │ angry_2 │ sad_1   │ sad_2   │ surprise│ custom_1│        │      │
│  │  │ (32x32) │ (32x32) │ (32x32) │ (32x32) │ (32x32) │        │      │
│  │  └─────────┴─────────┴─────────┴─────────┴─────────┘        │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                         │
│  ANIMATION PLAYBACK:                                                    │
│                                                                         │
│  IDLE ANIMATION:                                                        │
│  ┌────┐────┐────┐────┐                                                │
│  │ 1  │ 2  │ 3  │ 4  │ ──▶ repeat                                      │
│  └────┘────┘────┘────┘                                                │
│  (400ms per frame, loop)                                                │
│                                                                         │
│  TALKING ANIMATION:                                                     │
│  ┌────┐────┐────┐                                                     │
│  │ 1  │ 2  │ 3  │ ──▶ repeat                                          │
│  └────┘────┘────┘                                                     │
│  (100ms per frame, sync with audio)                                     │
│                                                                         │
│  EMOTION TRANSITION:                                                    │
│  ┌──────────┐    CROSSFADE    ┌──────────┐                            │
│  │   IDLE   │ ───────────────▶│  HAPPY   │                            │
│  │  (fade)  │   (300ms)       │  (fade)  │                            │
│  └──────────┘                 └──────────┘                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Procedural Animation Techniques

```python
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import math
import random


@dataclass
class ProceduralAnimationParams:
    """Parameters for procedural animation generation."""
    amplitude: float = 1.0
    frequency: float = 1.0
    phase_offset: float = 0.0
    decay: float = 0.0
    damping: float = 1.0


class ProceduralAnimator:
    """
    Procedural animation generator for character movements.
    Creates natural-looking animations through mathematical functions.
    """

    def __init__(self):
        self._active_animations: Dict[str, Dict[str, float]] = {}
        self._animation_params: Dict[str, ProceduralAnimationParams] = {}

    def start_animation(self, animation_id: str,
                       params: ProceduralAnimationParams) -> None:
        """Start a procedural animation."""
        self._active_animations[animation_id] = {"time": 0.0}
        self._animation_params[animation_id] = params

    def stop_animation(self, animation_id: str) -> None:
        """Stop a procedural animation with decay."""
        if animation_id in self._active_animations:
            # Start decay phase
            self._active_animations[animation_id]["decay"] = 1.0

    def update(self, delta_time: float) -> Dict[str, float]:
        """
        Update all animations and return current values.

        Args:
            delta_time: Time elapsed since last update in seconds

        Returns:
            Dictionary of animation_id to current value
        """
        results = {}

        for anim_id, state in list(self._active_animations.items()):
            params = self._animation_params.get(anim_id)
            if not params:
                continue

            # Update time
            state["time"] += delta_time
            t = state["time"]

            # Calculate base value using sine wave
            value = params.amplitude * math.sin(
                2 * math.pi * params.frequency * t + params.phase_offset
            )

            # Apply damping
            value *= params.damping ** t

            # Apply decay if in decay phase
            if "decay" in state:
                state["decay"] *= (1 - params.decay * delta_time)
                value *= state["decay"]

                if state["decay"] <= 0.01:
                    del self._active_animations[anim_id]
                    continue

            results[anim_id] = value

        return results

    def breathing_animation(self, time: float, intensity: float = 1.0) -> Dict[str, float]:
        """
        Generate breathing animation values.

        Args:
            time: Current time
            intensity: Breathing intensity (0-1)

        Returns:
            Dictionary with scale factors for body parts
        """
        breath_cycle = math.sin(2 * math.pi * time * 0.5)  # ~12 breaths/min

        return {
            "chest_scale": 1.0 + 0.02 * intensity * breath_cycle,
            "shoulders_y": 0.5 * intensity * breath_cycle,
            "head_bob": 0.3 * intensity * math.sin(2 * math.pi * time * 0.5)
        }

    def idle_movement(self, time: float,
                     seed: int = 0) -> Dict[str, float]:
        """
        Generate subtle idle movement animations.

        Args:
            time: Current time
            seed: Random seed for variation

        Returns:
            Dictionary of position offsets
        """
        random.seed(seed + int(time))

        return {
            "x_sway": 0.5 * math.sin(time * 0.7) +
                     0.2 * math.sin(time * 1.3),
            "y_bob": 0.3 * math.sin(time * 1.1) +
                    0.1 * math.sin(time * 2.1),
            "head_tilt": 0.05 * math.sin(time * 0.5) +
                        0.02 * math.cos(time * 0.9),
            "eye_movement_x": 0.02 * random.random() - 0.01,
            "eye_movement_y": 0.02 * random.random() - 0.01
        }

    def lip_sync_visemes(self, phoneme: str,
                        intensity: float = 1.0) -> Dict[str, float]:
        """
        Generate viseme shapes for lip sync.

        Args:
            phoneme: Phoneme character (e.g., 'A', 'E', 'O', 'M')
            intensity: Animation intensity

        Returns:
            Dictionary of viseme weights
        """
        viseme_shapes = {
            'A': {'aa': 1.0, 'oh': 0.2, 'mm': 0.0},
            'E': {'ee': 1.0, 'oh': 0.3, 'aa': 0.5},
            'I': {'ee': 1.0, 'ih': 0.4, 'mm': 0.0},
            'O': {'oh': 1.0, 'oo': 0.3, 'aa': 0.2},
            'U': {'oo': 1.0, 'oh': 0.3, 'mm': 0.1},
            'M': {'mm': 1.0, 'bb': 0.3, 'pp': 0.2},
            'F': {'ff': 1.0, 'vv': 0.3, 'th': 0.2},
            'S': {'ss': 1.0, 'sh': 0.3, 'zz': 0.2},
            'T': {'tt': 1.0, 'dd': 0.3, 'nn': 0.2},
            'L': {'ll': 1.0, 'nn': 0.2, 'dd': 0.1},
            'R': {'rr': 1.0, 'zz': 0.3, 'nn': 0.2},
            'rest': {'aa': 0.0, 'oh': 0.0, 'ee': 0.0,
                    'mm': 0.0, 'ff': 0.0, 'ss': 0.0}
        }

        shape = viseme_shapes.get(phoneme, viseme_shapes['rest'])
        return {k: v * intensity for k, v in shape.items()}

    def reaction_animation(self, stimulus: str,
                          intensity: float = 1.0) -> Dict[str, any]:
        """
        Generate reaction animations based on stimulus.

        Args:
            stimulus: Type of stimulus ('positive', 'negative', 'surprise')
            intensity: Reaction intensity

        Returns:
            Animation keyframes for the reaction
        """
        reaction_animations = {
            'positive': {
                'duration': 0.8,
                'keyframes': [
                    {'time': 0.0, 'smile': 0.0, 'eyebrows': 'neutral'},
                    {'time': 0.2, 'smile': 0.5 * intensity, 'eyebrows': 'raised'},
                    {'time': 0.4, 'smile': 0.8 * intensity, 'eyebrows': 'raised'},
                    {'time': 0.6, 'smile': 0.6 * intensity, 'eyebrows': 'neutral'},
                    {'time': 0.8, 'smile': 0.2 * intensity, 'eyebrows': 'neutral'}
                ]
            },
            'negative': {
                'duration': 1.0,
                'keyframes': [
                    {'time': 0.0, 'mouth': 'neutral', 'eyebrows': 'neutral'},
                    {'time': 0.2, 'mouth': 'frown', 'eyebrows': 'furrowed'},
                    {'time': 0.4, 'mouth': 'frown', 'eyebrows': 'furrowed'},
                    {'time': 0.7, 'mouth': 'neutral', 'eyebrows': 'neutral'},
                    {'time': 1.0, 'mouth': 'neutral', 'eyebrows': 'neutral'}
                ]
            },
            'surprise': {
                'duration': 0.6,
                'keyframes': [
                    {'time': 0.0, 'eyes': 'neutral', 'mouth': 'neutral'},
                    {'time': 0.1, 'eyes': 'wide', 'mouth': 'open'},
                    {'time': 0.3, 'eyes': 'wide', 'mouth': 'open'},
                    {'time': 0.6, 'eyes': 'neutral', 'mouth': 'neutral'}
                ]
            }
        }

        return reaction_animations.get(stimulus, {})
```

### 5.3 Lip-Sync and Expression Rendering

```python
from typing import Dict, List, Tuple, Optional
import numpy as np
from dataclasses import dataclass
from enum import Enum


class Viseme(Enum):
    """Standard viseme types for lip sync."""
    SILENCE = "silence"
    AA = "aa"      # Father
    EE = "ee"      # See
    IH = "ih"      // Ship
    OH = "oh"      // Go
    OO = "oo"      // Food
    MM = "mm"      // Baby
    FF = "ff"      // Food
    TH = "th"      // Think
    SS = "ss"      // See
    SH = "sh"      // Ship
    CH = "ch"      // Church
    JJ = "jj"      // Judge
    DD = "dd"      // Dog
    KK = "kk"      // Key
    GG = "gg"      // Go
    PP = "pp"      // Pop
    BB = "bb"      // Baby
    TT = "tt"      // Talk
    NN = "nn"      // No
    LL = "ll"      // Love
    RR = "rr"      // Red


@dataclass
class VisemeFrame:
    """Single frame of lip sync data."""
    viseme: Viseme
    weight: float  # 0.0 to 1.0
    timestamp: float


class LipSyncGenerator:
    """
    Generates viseme frames from text or audio for character lip sync.
    """

    # Mapping of phonemes to visemes
    PHONEME_TO_VISEME = {
        # Vowels
        'a': Viseme.AA, 'A': Viseme.AA,
        'e': Viseme.EE, 'E': Viseme.EE,
        'i': Viseme.IH, 'I': Viseme.IH,
        'o': Viseme.OH, 'O': Viseme.OH,
        'u': Viseme.OO, 'U': Viseme.OO,
        # Consonants
        'm': Viseme.MM, 'M': Viseme.MM,
        'b': Viseme.BB, 'B': Viseme.BB,
        'p': Viseme.PP, 'P': Viseme.PP,
        'f': Viseme.FF, 'F': Viseme.FF,
        'v': Viseme.FF, 'V': Viseme.FF,
        't': Viseme.TT, 'T': Viseme.TT,
        'd': Viseme.DD, 'D': Viseme.DD,
        's': Viseme.SS, 'S': Viseme.SS,
        'z': Viseme.SS, 'Z': Viseme.SS,
        'k': Viseme.KK, 'K': Viseme.KK,
        'g': Viseme.GG, 'G': Viseme.GG,
        'ch': Viseme.SH, 'CH': Viseme.SH,
        'j': Viseme.JJ, 'J': Viseme.JJ,
        'r': Viseme.RR, 'R': Viseme.RR,
        'l': Viseme.LL, 'L': Viseme.LL,
        'n': Viseme.NN, 'N': Viseme.NN,
        'th': Viseme.TH, 'TH': Viseme.TH,
    }

    def __init__(self, frame_rate: float = 30.0):
        self.frame_rate = frame_rate
        self.frame_duration = 1.0 / frame_rate

    def generate_from_text(self, text: str,
                          speaking_rate: float = 150.0) -> List[VisemeFrame]:
        """
        Generate lip sync frames from text.

        Args:
            text: Text to generate lip sync for
            speaking_rate: Words per minute

        Returns:
            List of viseme frames
        """
        frames = []

        # Extract phoneme sequence from text
        phonemes = self._text_to_phonemes(text)

        # Calculate timing based on speaking rate
        avg_phoneme_duration = 60.0 / (speaking_rate * 6)  # ~6 phonemes per word

        timestamp = 0.0
        for phoneme in phonemes:
            viseme = self._phoneme_to_viseme(phoneme)

            # Generate frames for this phoneme
            duration = avg_phoneme_duration * self._phoneme_duration_multiplier(phoneme)
            num_frames = int(duration / self.frame_duration)

            for i in range(num_frames):
                # Apply attack/decay envelope
                if i < num_frames * 0.2:
                    weight = i / (num_frames * 0.2)
                elif i > num_frames * 0.8:
                    weight = 1.0 - (i - num_frames * 0.8) / (num_frames * 0.2)
                else:
                    weight = 1.0

                # Reduce weight for consonants
                if viseme in [Viseme.MM, Viseme.BB, Viseme.PP, Viseme.FF, Viseme.TT]:
                    weight *= 0.7

                frames.append(VisemeFrame(
                    viseme=viseme,
                    weight=weight,
                    timestamp=timestamp
                ))

                timestamp += self.frame_duration

            # Add brief pause between words
            if phoneme in [' ', '.', ',', '!', '?']:
                frames.append(VisemeFrame(
                    viseme=Viseme.SILENCE,
                    weight=0.0,
                    timestamp=timestamp
                ))
                timestamp += self.frame_duration * 3

        return frames

    def generate_from_audio(self, audio_data: np.ndarray,
                           sample_rate: int) -> List[VisemeFrame]:
        """
        Generate lip sync frames from audio data.
        Uses amplitude analysis to determine mouth opening.

        Args:
            audio_data: Audio waveform
            sample_rate: Sample rate in Hz

        Returns:
            List of viseme frames
        """
        frames = []

        # Analyze audio in windows
        window_size = int(sample_rate / self.frame_rate)
        num_windows = len(audio_data) // window_size

        for i in range(num_windows):
            window = audio_data[i * window_size:(i + 1) * window_size]

            # Calculate amplitude (volume)
            amplitude = np.abs(window).mean()
            normalized = min(amplitude / 1000.0, 1.0)  # Normalize

            # Determine mouth openness based on amplitude
            if normalized < 0.1:
                viseme = Viseme.SILENCE
                weight = 0.0
            elif normalized < 0.3:
                viseme = Viseme.MM  # Closed mouth sounds
                weight = normalized * 0.5
            elif normalized < 0.6:
                viseme = Viseme.AA  # Open mouth
                weight = normalized
            else:
                viseme = Viseme.OH  # Wide open
                weight = min(normalized * 1.2, 1.0)

            frames.append(VisemeFrame(
                viseme=viseme,
                weight=weight,
                timestamp=i * self.frame_duration
            ))

        return frames

    def _text_to_phonemes(self, text: str) -> List[str]:
        """Convert text to phoneme sequence (simplified)."""
        phonemes = []
        text = text.lower()

        i = 0
        while i < len(text):
            char = text[i]

            # Check for digraphs
            if i < len(text) - 1:
                digraph = char + text[i + 1]
                if digraph in ['th', 'ch', 'sh', 'ch']:
                    phonemes.append(digraph)
                    i += 2
                    continue

            # Handle spaces and punctuation
            if char in ' ,.!?;:\n':
                phonemes.append(char)
                i += 1
                continue

            # Single character phoneme
            if char in self.PHONEME_TO_VISEME:
                phonemes.append(char)

            i += 1

        return phonemes

    def _phoneme_to_viseme(self, phoneme: str) -> Viseme:
        """Convert phoneme to viseme."""
        return self.PHONEME_TO_VISEME.get(phoneme, Viseme.SILENCE)

    def _phoneme_duration_multiplier(self, phoneme: str) -> float:
        """Get duration multiplier for phoneme type."""
        vowels = 'aeiou'
        if phoneme in vowels:
            return 1.2
        elif phoneme in 'fvs':
            return 0.5
        elif phoneme in 'lrt':
            return 0.4
        elif phoneme in 'mn':
            return 0.3
        elif phoneme in ' ':
            return 0.0
        else:
            return 0.6
```

---

## 6. Duel Mechanics

### 6.1 Turn-Based Interaction Systems

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TURN-BASED DUEL STATE MACHINE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────┐                                                         │
│  │   START     │─────────────────────────────────────────────────────┐  │
│  │             │    │                                                 │  │
│  └──────┬──────┘    │                                                 │  │
│         │           │                                                 │  │
│         ▼           │                                                 │  │
│  ┌─────────────┐    │                                                 │  │
│  │  PLAYER     │    │                                                 │  │
│  │  TURN       │    │                                                 │  │
│  │  ┌───────┐  │    │                                                 │  │
│  │  │Input  │  │    │                                                 │  │
│  │  │Process│  │    │                                                 │  │
│  │  │Generate│  │    │                                                 │  │
│  │  │Response│  │    │                                                 │  │
│  │  └───────┘  │    │                                                 │  │
│  └──────┬──────┘    │                                                 │  │
│         │           │                                                 │  │
│         ▼           │                                                 │  │
│  ┌─────────────┐    │                                                 │  │
│  │ EVALUATE    │    │                                                 │  │
│  │ RESPONSE    │    │                                                 │  │
│  │  - Logic    │    │                                                 │  │
│  │  - Wit      │    │                                                 │  │
│  │  - Creativity│   │                                                 │  │
│  └──────┬──────┘    │                                                 │  │
│         │           │                                                 │  │
│         ▼           │                                                 │  │
│  ┌─────────────┐    │                                                 │  │
│  │ AI TURN     │    │                                                 │  │
│  │  - Analyze  │    │                                                 │  │
│  │  - Counter  │    │                                                 │  │
│  │  - Response │    │                                                 │  │
│  └──────┬──────┘    │                                                 │  │
│         │           │                                                 │  │
│         ▼           │                                                 │  │
│  ┌─────────────┐    │                                                 │  │
│  │   SCORE     │    │                                                 │  │
│  │  DUEL       │    │                                                 │  │
│  │             │    │                                                 │  │
│  │ Player: 8   │    │                                                 │  │
│  │ AI: 7       │    │                                                 │  │
│  └──────┬──────┘    │                                                 │  │
│         │           │                                                 │  │
│         ▼           │                                                 │  │
│  ┌─────────────┐    │                                                 │  │
│  │  CHECK      │    │                                                 │  │
│  │  END        │    │                                                 │  │
│  │  CONDITIONS │    │                                                 │  │
│  └──────┬──────┘    │                                                 │  │
│         │           │                                                 │  │
│         ├───────────┴──────────────────────────────┐                  │  │
│         │                                          │                  │  │
│         ▼                                          ▼                  │  │
│  ┌─────────────┐                          ┌─────────────┐             │  │
│  │  CONTINUE   │                          │    END      │             │  │
│  │  (Rounds<10)│                          │  (Max Rounds│             │  │
│  │  & Scores   │                          │   or Exit)  │             │  │
│  │  < Threshold)│                          └──────┬──────┘             │  │
│  └──────┬──────┘                                 │                    │  │
│         │                                        ▼                    │  │
│         │                               ┌─────────────────┐            │  │
│         │                               │   RESULTS       │            │  │
│         │                               │   - Winner      │            │  │
│         │                               │   - Final Score │            │  │
│         │                               │   - Highlights  │            │  │
│         │                               └─────────────────┘            │  │
│         └──────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Duel System Implementation

```python
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json


class DuelPhase(Enum):
    """Duel system phases."""
    LOBBY = "lobby"
    PLAYER_TURN = "player_turn"
    AI_PROCESSING = "ai_processing"
    AI_TURN = "ai_turn"
    EVALUATION = "evaluation"
    ROUND_END = "round_end"
    DUEL_END = "duel_end"


class DuelStyle(Enum):
    """Styles of character duel interactions."""
    VERBAL_SPARRING = "verbal_sparring"
    DEBATE = "debate"
    ROLEPLAY_COMBAT = "roleplay_combat"
    COLLABORATIVE = "collaborative"
    IMPROV = "improv"


@dataclass
class DuelScore:
    """Scoring for duel round."""
    player_points: int = 0
    ai_points: int = 0
    round_winner: Optional[str] = None
    criteria_scores: Dict[str, float] = field(default_factory=dict)


@dataclass
class DuelRound:
    """Single round of duel."""
    round_number: int
    player_input: str
    ai_response: str
    scores: DuelScore
    timestamp: str
    highlights: List[str] = field(default_factory=list)


@dataclass
class DuelSession:
    """Complete duel session."""
    session_id: str
    character_id: str
    style: DuelStyle
    max_rounds: int = 10
    current_round: int = 0
    phase: DuelPhase = DuelPhase.LOBBY
    rounds: List[DuelRound] = field(default_factory=list)
    total_score: DuelScore = field(default_factory=DuelScore)
    created_at: str = ""
    ended_at: Optional[str] = None
    winner: Optional[str] = None


class DuelSystem:
    """
    Turn-based duel mechanics system for character interactions.
    Handles scoring, turn management, and AI decision making.
    """

    def __init__(self):
        self.active_sessions: Dict[str, DuelSession] = {}
        self.duel_templates: Dict[DuelStyle, Dict[str, Any]] = {
            DuelStyle.VERBAL_SPARRING: {
                "description": "Quick-witted verbal exchanges",
                "scoring_criteria": ["wit", "creativity", "relevance", "humor"],
                "time_limit": 30,
                "points_per_round": 10
            },
            DuelStyle.DEBATE: {
                "description": "Structured argumentative exchange",
                "scoring_criteria": ["logic", "evidence", "rebuttal", "persuasion"],
                "time_limit": 60,
                "points_per_round": 15
            },
            DuelStyle.ROLEPLAY_COMBAT: {
                "description": "Narrative combat dialogue",
                "scoring_criteria": ["creativity", "style", "impact", "consistency"],
                "time_limit": 45,
                "points_per_round": 12
            }
        }

    def create_session(self, character_id: str, style: DuelStyle,
                       max_rounds: int = 10) -> DuelSession:
        """
        Create a new duel session.

        Args:
            character_id: Character to duel with
            style: Duel interaction style
            max_rounds: Maximum number of rounds

        Returns:
            New DuelSession
        """
        import uuid

        session = DuelSession(
            session_id=str(uuid.uuid4()),
            character_id=character_id,
            style=style,
            max_rounds=max_rounds,
            phase=DuelPhase.LOBBY,
            created_at=datetime.utcnow().isoformat()
        )

        self.active_sessions[session.session_id] = session
        return session

    def start_session(self, session_id: str) -> Dict[str, Any]:
        """
        Start duel session and transition to first round.

        Args:
            session_id: Session to start

        Returns:
            Session state for client
        """
        session = self._get_session(session_id)

        session.phase = DuelPhase.PLAYER_TURN
        session.current_round = 1

        return self._get_session_state(session)

    def submit_player_input(self, session_id: str,
                           player_input: str) -> Dict[str, Any]:
        """
        Process player turn input.

        Args:
            session_id: Active session
            player_input: Player's response

        Returns:
            Updated session state
        """
        session = self._get_session(session_id)

        if session.phase != DuelPhase.PLAYER_TURN:
            raise ValueError(f"Invalid phase for player input: {session.phase}")

        # Transition to AI processing
        session.phase = DuelPhase.AI_PROCESSING

        # Generate AI response (would integrate with LLM)
        ai_response = self._generate_ai_turn(session, player_input)

        # Create round
        round_score = self._evaluate_round(session, player_input, ai_response)

        round_obj = DuelRound(
            round_number=session.current_round,
            player_input=player_input,
            ai_response=ai_response,
            scores=round_score,
            timestamp=datetime.utcnow().isoformat(),
            highlights=self._extract_highlights(player_input, ai_response, round_score)
        )

        session.rounds.append(round_obj)
        session.total_score.player_points += round_score.player_points
        session.total_score.ai_points += round_score.ai_points

        # Transition to evaluation
        session.phase = DuelPhase.EVALUATION

        return self._get_session_state(session)

    def advance_round(self, session_id: str) -> Dict[str, Any]:
        """
        Advance to next round or end duel.

        Args:
            session_id: Active session

        Returns:
            Updated session state
        """
        session = self._get_session(session_id)

        if session.phase != DuelPhase.EVALUATION:
            raise ValueError(f"Invalid phase for advance: {session.phase}")

        # Check end conditions
        if (session.current_round >= session.max_rounds or
            self._should_end_early(session)):
            return self._end_duel(session)

        # Next round
        session.current_round += 1
        session.phase = DuelPhase.PLAYER_TURN

        return self._get_session_state(session)

    def _get_session(self, session_id: str) -> DuelSession:
        """Get session or raise error."""
        if session_id not in self.active_sessions:
            raise ValueError(f"Session not found: {session_id}")
        return self.active_sessions[session_id]

    def _generate_ai_turn(self, session: DuelSession,
                         player_input: str) -> str:
        """
        Generate AI character response for duel.

        In production, this would integrate with the character actor
        and LLM service to generate contextually appropriate responses.
        """
        # Placeholder for LLM integration
        style_config = self.duel_templates[session.style]

        # Would retrieve character data and generate response
        # This is a simplified placeholder
        return f"[AI {session.character_id} response to: {player_input[:50]}...]"

    def _evaluate_round(self, session: DuelSession,
                       player_input: str, ai_response: str) -> DuelScore:
        """
        Evaluate round and assign scores.

        In production, this would use more sophisticated analysis.
        """
        style_config = self.duel_templates[session.style]

        # Simple placeholder scoring
        criteria = style_config["scoring_criteria"]

        criteria_scores = {}
        for criterion in criteria:
            # Placeholder: random score for demonstration
            criteria_scores[criterion] = round(random.uniform(5, 10), 1)

        # Calculate total points
        player_score = sum(criteria_scores.values()) / len(criteria_scores)
        ai_score = player_score + random.uniform(-2, 2)

        return DuelScore(
            player_points=int(player_score * 2),
            ai_points=int(ai_score * 2),
            round_winner="player" if player_score > ai_score else "ai",
            criteria_scores=criteria_scores
        )

    def _extract_highlights(self, player: str, ai: str,
                           score: DuelScore) -> List[str]:
        """Extract notable moments from round."""
        highlights = []

        # Check for high-scoring criteria
        for crit, value in score.criteria_scores.items():
            if value >= 9:
                highlights.append(f"Excellent {crit}!")

        # Check for wit/creativity indicators
        if "?" in player and "?" not in ai:
            highlights.append("Player asked the better question")

        return highlights

    def _should_end_early(self, session: DuelSession) -> bool:
        """Check if duel should end early based on scores."""
        score_diff = abs(
            session.total_score.player_points -
            session.total_score.ai_points
        )
        max_possible_remaining = (
            session.max_rounds - session.current_round
        ) * 20  # Max points per round

        return score_diff > max_possible_remaining

    def _end_duel(self, session: DuelSession) -> Dict[str, Any]:
        """End duel and calculate final results."""
        session.phase = DuelPhase.DUEL_END
        session.ended_at = datetime.utcnow().isoformat()

        if session.total_score.player_points > session.total_score.ai_points:
            session.winner = "player"
        elif session.total_score.ai_points > session.total_score.player_points:
            session.winner = session.character_id
        else:
            session.winner = "draw"

        return self._get_session_state(session)

    def _get_session_state(self, session: DuelSession) -> Dict[str, Any]:
        """Get serializable session state for client."""
        return {
            "session_id": session.session_id,
            "character_id": session.character_id,
            "style": session.style.value,
            "phase": session.phase.value,
            "current_round": session.current_round,
            "max_rounds": session.max_rounds,
            "score": {
                "player": session.total_score.player_points,
                "ai": session.total_score.ai_points
            },
            "rounds_summary": [
                {
                    "round": r.round_number,
                    "winner": r.scores.round_winner,
                    "highlights": r.highlights
                }
                for r in session.rounds
            ],
            "is_complete": session.phase == DuelPhase.DUEL_END,
            "winner": session.winner
        }
```

---

## 7. Open Source Alternatives

### 7.1 Self-Hosted AI Character Platforms

| Platform | Language | License | Last Updated | Stars | Key Features |
|----------|----------|---------|--------------|-------|--------------|
| **CharCX** | Python | MIT | 2024-12 | 2.4k | Full-featured, REST API, Web UI |
| **NovelAI** | Python | Proprietary | 2024-11 | N/A | Subscription, Story synthesis |
| **KoboldAI** | Python | AGPL-3.0 | 2024-12 | 8.1k | Local LLM, Chrome extension |
| ** TavernAI** | TypeScript | MIT | 2024-11 | 3.2k | Web interface, Character cards |
| **OobaBooga** | Python | AGPL-3.0 | 2024-12 | 12k | Web UI, Multiple backends |
| **SillyTavern** | TypeScript | MIT | 2024-12 | 5.6k | Community fork of TavernAI |
| **Agnaistic** | TypeScript | MIT | 2024-10 | 1.8k | Minimal, FastAPI backend |
| **LibreChat** | TypeScript | MIT | 2024-12 | 6.7k | Multi-provider, Chat UI |
| **Big-AGI** | TypeScript | MIT | 2024-11 | 1.2k | Privacy-focused, Local-first |
| **ChatGPT-Next-Web** | TypeScript | MIT | 2024-12 | 15k | Minimal UI, API keys |

### 7.2 Community Frameworks Comparison

```
┌─────────────────────────────────────────────────────────────────────────┐
│              OPEN SOURCE CHARACTER PLATFORM COMPARISON                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  FEATURE MATRIX:                                                        │
│                                                                         │
│  ┌──────────────────────┬────────┬─────────┬─────────┬──────────┐     │
│  │ Feature              │CharCX  │TavernAI │SillyTvrn│ KoboldAI │     │
│  ├──────────────────────┼────────┼─────────┼─────────┼──────────┤     │
│  │ REST API             │  ✅    │   ❌    │   ❌    │    ✅    │     │
│  │ WebSocket Support    │  ✅    │   ❌    │   ✅    │    ❌    │     │
│  │ Character Cards      │  ✅    │   ✅    │   ✅    │    ❌    │     │
│  │ Voice Synthesis      │  ✅    │   ❌    │   ✅    │    ❌    │     │
│  │ Image Generation     │  ✅    │   ❌    │   ✅    │    ❌    │     │
│  │ Multi-LLM Support    │  ✅    │   ✅    │   ✅    │    ✅    │     │
│  │ Local LLM Ready      │  ✅    │   ✅    │   ✅    │    ✅    │     │
│  │ Docker Support       │  ✅    │   ✅    │   ✅    │    ✅    │     │
│  │ Kubernetes Ready     │  ✅    │   ❌    │   ❌    │    ❌    │     │
│  │ Enterprise Features  │  ✅    │   ❌    │   ❌    │    ❌    │     │
│  └──────────────────────┴────────┴─────────┴─────────┴──────────┘     │
│                                                                         │
│  ARCHITECTURE PATTERNS:                                                 │
│                                                                         │
│  CharCX:      Monolith → Microservices (Actor-based)                   │
│  TavernAI:    Monolith (Express.js)                                    │
│  SillyTavern: Monolith → Plugin System                                 │
│  KoboldAI:    Monolith (Flask) + CLI                                   │
│                                                                         │
│  RECOMMENDED USE CASES:                                                 │
│  ├─ Production Deployments    → CharCX, LibreChat                      │
│  ├─ Local Development         → KoboldAI, OobaBooga                    │
│  ├─ Community/Quick Start     → SillyTavern, TavernAI                  │
│  └─ Enterprise Integration    → CharCX + Custom Extensions             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 7.3 API Approaches for Character Platforms

```python
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod


class APIProvider(Enum):
    """Supported LLM API providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    AZURE_OPENAI = "azure_openai"
    GOOGLE = "google"
    ANTHROPIC_CLAUDE = "anthropic_claude"
    LOCAL = "local"


@dataclass
class APIConfig:
    """API configuration for LLM providers."""
    provider: APIProvider
    model: str
    api_key: str  # Should be retrieved from Azure Key Vault
    endpoint: Optional[str] = None
    max_tokens: int = 4096
    temperature: float = 0.7
    timeout: int = 60


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    async def generate(self, config: APIConfig,
                      messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Generate response from LLM."""
        pass

    @abstractmethod
    async def stream_generate(self, config: APIConfig,
                             messages: List[Dict[str, str]]):
        """Stream response from LLM."""
        pass


class OpenAIClient(LLMProvider):
    """OpenAI API client with Azure Key Vault integration."""

    async def generate(self, config: APIConfig,
                      messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Generate response using OpenAI API.

        Args:
            config: API configuration with Azure Key Vault credentials
            messages: Conversation messages

        Returns:
            Response from OpenAI API
        """
        import openai
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential

        # Initialize Azure Key Vault client
        vault_url = "https://jarvis-lumina.vault.azure.net/"
        credential = DefaultAzureCredential()
        kv_client = SecretClient(vault_url=vault_url, credential=credential)

        # Retrieve API key from Key Vault
        api_key = kv_client.get_secret("openai-api-key").value

        # Initialize OpenAI client
        client = openai.AsyncOpenAI(api_key=api_key)

        response = await client.chat.completions.create(
            model=config.model,
            messages=messages,
            max_tokens=config.max_tokens,
            temperature=config.temperature
        )

        return {
            "text": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            },
            "model": response.model
        }

    async def stream_generate(self, config: APIConfig,
                             messages: List[Dict[str, str]]):
        """Stream response from OpenAI API."""
        import openai
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential

        vault_url = "https://jarvis-lumina.vault.azure.net/"
        credential = DefaultAzureCredential()
        kv_client = SecretClient(vault_url=vault_url, credential=credential)

        api_key = kv_client.get_secret("openai-api-key").value
        client = openai.AsyncOpenAI(api_key=api_key)

        stream = await client.chat.completions.create(
            model=config.model,
            messages=messages,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            stream=True
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content


class AnthropicClient(LLMProvider):
    """Anthropic API client with Azure Key Vault integration."""

    async def generate(self, config: APIConfig,
                      messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Generate response using Anthropic API.

        Args:
            config: API configuration with Azure Key Vault credentials
            messages: Conversation messages

        Returns:
            Response from Anthropic API
        """
        import anthropic
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential

        vault_url = "https://jarvis-lumina.vault.azure.net/"
        credential = DefaultAzureCredential()
        kv_client = SecretClient(vault_url=vault_url, credential=credential)

        api_key = kv_client.get_secret("anthropic-api-key").value
        client = anthropic.Anthropic(api_key=api_key)

        response = await client.messages.create(
            model=config.model,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            messages=messages
        )

        return {
            "text": response.content[0].text,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens
            },
            "model": response.model
        }

    async def stream_generate(self, config: APIConfig,
                             messages: List[Dict[str, str]]):
        """Stream response from Anthropic API."""
        import anthropic
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential

        vault_url = "https://jarvis-lumina.vault.azure.net/"
        credential = DefaultAzureCredential()
        kv_client = SecretClient(vault_url=vault_url, credential=credential)

        api_key = kv_client.get_secret("anthropic-api-key").value
        client = anthropic.Anthropic(api_key=api_key)

        async with client.messages.stream(
            model=config.model,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            messages=messages
        ) as stream:
            async for chunk in stream:
                if chunk.type == "content_block_delta":
                    yield chunk.delta.text


class LLMServiceFactory:
    """Factory for creating LLM provider clients."""

    _providers: Dict[APIProvider, type] = {
        APIProvider.OPENAI: OpenAIClient,
        APIProvider.ANTHROPIC: AnthropicClient,
        APIProvider.AZURE_OPENAI: OpenAIClient,  # Uses OpenAI SDK with Azure endpoint
    }

    @classmethod
    def get_client(cls, provider: APIProvider) -> LLMProvider:
        """Get LLM client for specified provider."""
        client_class = cls._providers.get(provider)
        if not client_class:
            raise ValueError(f"Unsupported provider: {provider}")
        return client_class()

    @classmethod
    def create_config(cls, provider: APIProvider, model: str,
                     **kwargs) -> APIConfig:
        """Create API configuration for provider."""
        return APIConfig(
            provider=provider,
            model=model,
            api_key="",  # Retrieved from Azure Key Vault at runtime
            **kwargs
        )
```

---

## 8. MCU Lore Integration

### 8.1 Knowledge Base Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MCU LORE KNOWLEDGE BASE ARCHITECTURE                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                   Lore Document Store                           │   │
│  │                                                                │   │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │   │
│  │  │ Marvel    │  │ MCU Wiki  │  │Fan Sites  │  │Official   │  │   │
│  │  │ Comics DB │  │ Dump      │  │Scrapes    │  │Marvel.com │  │   │
│  │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  │   │
│  │        │              │              │              │        │   │
│  │        └──────────────┼──────────────┼──────────────┘        │   │
│  │                       │              │                         │   │
│  │                       ▼              ▼                         │   │
│  │              ┌─────────────────────────────┐                  │   │
│  │              │    Document Preprocessor    │                  │   │
│  │              │  - Clean HTML/Markdown      │                  │   │
│  │              │  - Extract entities         │                  │   │
│  │              │  - Chunk by section         │                  │   │
│  │              └─────────────┬───────────────┘                  │   │
│  │                            │                                   │   │
│  │                            ▼                                   │   │
│  │  ┌─────────────────────────────────────────────────────────┐  │   │
│  │  │              Vector Embedding Store                     │  │   │
│  │  │                                                          │  │   │
│  │  │  ┌──────────────────────────────────────────────────┐   │  │   │
│  │  │  │              ChromaDB / Pinecone                 │   │  │   │
│  │  │  │                                                  │   │  │   │
│  │  │  │  Character: Tony Stark                          │   │  │   │
│  │  │  │    ├── Biography                                 │   │  │   │
│  │  │  │    │   └── Early Life, MIT, Parents             │   │  │   │
│  │  │  │    ├── Iron Man Suits                           │   │  │   │
│  │  │  │    │   └── Mark I through Mark LXXXV           │   │  │   │
│  │  │  │    ├── Relationships                            │   │  │   │
│  │  │  │    │   ├── Pepper Potts, Happy Hogan           │   │  │   │
│  │  │  │    │   └── Avengers, Captain America           │   │  │   │
│  │  │  │    └── Key Events                               │   │  │   │
│  │  │  │        └── Ten Rings, Obadiah Stane            │   │  │   │
│  │  │  │                                               │   │  │   │
│  │  │  └──────────────────────────────────────────────────┘   │  │   │
│  │  └─────────────────────────────────────────────────────────┘  │   │
│  │                                                                │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                   Knowledge Graph Store                         │   │
│  │                                                                │   │
│  │  ┌─────────────────────────────────────────────────────────┐   │   │
│  │  │              Neo4j Graph Database                       │   │   │
│  │  │                                                          │   │   │
│  │  │  (Tony Stark) -[KNOWS]-> (Pepper Potts)                 │   │   │
│  │  │  (Tony Stark) -[CREATED]-> (Arc Reactor)                │   │   │
│  │  │  (Tony Stark) -[LEADS]-> (Avengers)                     │   │   │
│  │  │  (Pepper Potts) -[MARRIED_TO]-> (Tony Stark)            │   │   │
│  │  │  (Howard Stark) -[PARENT_OF]-> (Tony Stark)             │   │   │
│  │  │  (Obadiah Stane) -[RIVAL_OF]-> (Tony Stark)             │   │   │
│  │  │                                                          │   │   │
│  │  └─────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Knowledge Graph Schema

```python
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class EntityType(Enum):
    """MCU entity types for knowledge graph."""
    CHARACTER = "character"
    LOCATION = "location"
    ORGANIZATION = "organization"
    OBJECT = "object"
    EVENT = "event"
    ABILITY = "ability"
    RELATIONSHIP = "relationship"


class RelationshipType(Enum):
    """Relationship types between entities."""
    KNOWS = "knows"
    WORKS_WITH = "works_with"
    PARENT_OF = "parent_of"
    CHILD_OF = "child_of"
    MARRIED_TO = "married_to"
    ENEMY_OF = "enemy_of"
    RIVAL_OF = "rival_of"
    CREATED = "created"
    INVENTED = "invented"
    LOCATED_AT = "located_at"
    MEMBER_OF = "member_of"
    LEADS = "leads"
    FOUNDER_OF = "founder_of"
    KILLED = "killed"
    SAVED = "saved"


@dataclass
class Entity:
    """Knowledge graph entity."""
    entity_id: str
    entity_type: EntityType
    name: str
    description: str
    properties: Dict[str, Any] = field(default_factory=dict)
    aliases: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)
    confidence: float = 1.0
    created_at: str = ""
    updated_at: str = ""


@dataclass
class Relationship:
    """Knowledge graph relationship."""
    from_entity: str
    to_entity: str
    relationship_type: RelationshipType
    properties: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0
    sources: List[str] = field(default_factory=list)


@dataclass
class LoreEntry:
    """Individual lore entry for character knowledge."""
    entry_id: str
    character_id: str
    content: str
    category: str
    keywords: List[str] = field(default_factory=list)
    importance: float = 0.5
    source: str = ""
    verified: bool = False


class MCUKnowledgeGraph:
    """
    Knowledge graph for MCU lore integration.
    Stores entities and relationships for character context.
    """

    def __init__(self, neo4j_uri: str = "bolt://localhost:7687",
                 neo4j_user: str = "neo4j",
                 neo4j_password: str = ""):
        self.entities: Dict[str, Entity] = {}
        self.relationships: List[Relationship] = []
        self.lore_entries: Dict[str, List[LoreEntry]] = {}

    def add_entity(self, entity: Entity) -> None:
        """Add entity to knowledge graph."""
        self.entities[entity.entity_id] = entity

    def add_relationship(self, relationship: Relationship) -> None:
        """Add relationship between entities."""
        self.relationships.append(relationship)

    def get_character_context(self, character_id: str,
                             query: str) -> List[str]:
        """
        Get relevant lore context for character.

        Args:
            character_id: Character to get context for
            query: User query to find relevant lore

        Returns:
            List of relevant lore excerpts
        """
        relevant_entries = []

        # Get character's lore entries
        entries = self.lore_entries.get(character_id, [])

        # Simple keyword matching (in production, use vector search)
        query_keywords = set(query.lower().split())

        for entry in entries:
            if entry.verified or entry.importance > 0.3:
                entry_keywords = set(e.lower() for e in entry.keywords)

                # Check for keyword overlap
                if query_keywords & entry_keywords:
                    relevant_entries.append((entry, len(query_keywords & entry_keywords)))

        # Sort by relevance
        relevant_entries.sort(key=lambda x: x[1], reverse=True)

        # Return top 5 entries
        return [entry.content for entry, _ in relevant_entries[:5]]

    def get_related_entities(self, entity_id: str,
                            relationship_type: Optional[RelationshipType] = None,
                            depth: int = 1) -> List[Entity]:
        """
        Get entities related to specified entity.

        Args:
            entity_id: Starting entity
            relationship_type: Optional filter for relationship type
            depth: How many hops to traverse

        Returns:
            List of related entities
        """
        related = []
        visited = {entity_id}
        current_level = {entity_id}

        for _ in range(depth):
            next_level = set()

            for rel in self.relationships:
                if rel.from_entity in current_level:
                    if relationship_type is None or rel.relationship_type == relationship_type:
                        if rel.to_entity not in visited and rel.to_entity in self.entities:
                            related.append(self.entities[rel.to_entity])
                            next_level.add(rel.to_entity)
                            visited.add(rel.to_entity)

            current_level = next_level
            if not current_level:
                break

        return related

    def build_character_lore(self, character_id: str,
                            character_data: Dict[str, Any]) -> List[LoreEntry]:
        """
        Build lore entries from character data.

        Args:
            character_id: Character to build lore for
            character_data: Character card data

        Returns:
            List of generated lore entries
        """
        entries = []

        # Create biography entry
        entries.append(LoreEntry(
            entry_id=f"{character_id}_bio",
            character_id=character_id,
            content=character_data.get("description", ""),
            category="biography",
            keywords=["bio", "background", "history"],
            importance=1.0,
            source="character_card"
        ))

        # Create relationship entries
        relationships = character_data.get("lore", {}).get("relationships", {})
        for person, relation in relationships.items():
            entries.append(LoreEntry(
                entry_id=f"{character_id}_rel_{person.lower().replace(' ', '_')}",
                character_id=character_id,
                content=f"{character_data.get('name', 'Character')} is {relation} to {person}",
                category="relationships",
                keywords=["relationship", person.lower()],
                importance=0.8,
                source="character_card"
            ))

        # Create key facts entries
        key_facts = character_data.get("lore", {}).get("key_facts", [])
        for i, fact in enumerate(key_facts):
            entries.append(LoreEntry(
                entry_id=f"{character_id}_fact_{i}",
                character_id=character_id,
                content=fact,
                category="key_facts",
                keywords=self._extract_keywords(fact),
                importance=0.6,
                source="character_card"
            ))

        self.lore_entries[character_id] = entries
        return entries

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text."""
        # Simple keyword extraction (in production, use NLP)
        words = text.lower().replace(",", "").replace(".", "").split()
        stop_words = {"the", "a", "an", "is", "are", "was", "were", "of", "and", "to", "in"}
        return [w for w in words if w not in stop_words and len(w) > 3]

    def export_for_llm(self, character_id: str) -> str:
        """
        Export character knowledge as LLM context string.

        Args:
            character_id: Character to export

        Returns:
            Formatted knowledge string for LLM
        """
        entries = self.lore_entries.get(character_id, [])

        sections = []

        # Group by category
        by_category = {}
        for entry in entries:
            if entry.category not in by_category:
                by_category[entry.category] = []
            by_category[entry.category].append(entry)

        for category, category_entries in by_category.items():
            lines = [f"## {category.upper()}"]
            for entry in category_entries:
                lines.append(f"- {entry.content}")
            sections.append("\n".join(lines))

        return "\n\n".join(sections)
```

---

## 9. Security and Best Practices

### 9.1 Azure Key Vault Integration

All API keys and secrets must be retrieved from Azure Key Vault. Never hardcode secrets in source code.

```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from azure.core.exceptions import AzureError
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class AzureKeyVaultClient:
    """
    Secure Azure Key Vault client for secret management.
    Implements best practices for secret retrieval.
    """

    _instance: Optional['AzureKeyVaultClient'] = None
    _vault_url: str = "https://jarvis-lumina.vault.azure.net/"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        # Use Managed Identity in production, DefaultCredential for dev
        try:
            # Try managed identity first (production)
            self._credential = ManagedIdentityCredential()
            self._client = SecretClient(
                vault_url=self._vault_url,
                credential=self._credential
            )
            self._client.get_secret("test-connection")  # Verify connection
        except AzureError:
            # Fall back to DefaultAzureCredential (development)
            self._credential = DefaultAzureCredential()
            self._client = SecretClient(
                vault_url=self._vault_url,
                credential=self._credential
            )

        self._initialized = True
        self._cache: Dict[str, tuple[str, float]] = {}
        self._cache_ttl: float = 300  # 5 minutes

    def get_secret(self, secret_name: str,
                   use_cache: bool = True) -> Optional[str]:
        """
        Retrieve secret from Azure Key Vault.

        Args:
            secret_name: Name of the secret to retrieve
            use_cache: Whether to use cached values

        Returns:
            Secret value or None if not found
        """
        import time

        # Check cache
        if use_cache and secret_name in self._cache:
            value, expires = self._cache[secret_name]
            if time.time() < expires:
                return value

        try:
            secret = self._client.get_secret(secret_name)
            value = secret.value

            # Cache the value
            if use_cache:
                self._cache[secret_name] = (value, time.time() + self._cache_ttl)

            logger.info(f"Retrieved secret: {secret_name}")
            return value

        except AzureError as e:
            logger.error(f"Failed to retrieve secret {secret_name}: {e}")
            return None

    def get_secret_or_raise(self, secret_name: str) -> str:
        """
        Retrieve secret or raise ValueError.

        Args:
            secret_name: Name of the secret to retrieve

        Returns:
            Secret value

        Raises:
            ValueError: If secret not found
        """
        value = self.get_secret(secret_name)

        if value is None:
            raise ValueError(
                f"Secret '{secret_name}' not found in Azure Key Vault. "
                "Please ensure the secret exists and managed identity has access."
            )

        return value

    def list_secrets(self) -> list[str]:
        """List all secret names in the vault."""
        try:
            secrets = self._client.list_properties_of_secrets()
            return [s.name for s in secrets]
        except AzureError as e:
            logger.error(f"Failed to list secrets: {e}")
            return []

    def invalidate_cache(self, secret_name: Optional[str] = None) -> None:
        """Invalidate cached secrets."""
        if secret_name:
            self._cache.pop(secret_name, None)
        else:
            self._cache.clear()


# Singleton instance
_keyvault_client: Optional[AzureKeyVaultClient] = None


def get_keyvault_client() -> AzureKeyVaultClient:
    """Get singleton Key Vault client."""
    global _keyvault_client
    if _keyvault_client is None:
        _keyvault_client = AzureKeyVaultClient()
    return _keyvault_client


def get_openai_api_key() -> str:
    """Get OpenAI API key from Azure Key Vault."""
    client = get_keyvault_client()
    return client.get_secret_or_raise("openai-api-key")


def get_anthropic_api_key() -> str:
    """Get Anthropic API key from Azure Key Vault."""
    client = get_keyvault_client()
    return client.get_secret_or_raise("anthropic-api-key")


def get_database_credentials() -> dict:
    """Get database credentials from Azure Key Vault."""
    client = get_keyvault_client()
    return {
        "host": client.get_secret_or_raise("db-host"),
        "username": client.get_secret_or_raise("db-username"),
        "password": client.get_secret_or_raise("db-password"),
        "database": client.get_secret_or_raise("db-name")
    }
```

### 9.2 Secret Management Best Practices

**Critical Security Guidelines:**

1. **Never hardcode secrets** in source code or configuration files
2. **Use Azure Key Vault** for all production secrets
3. **Implement secret rotation** policies (90 days for API keys)
4. **Audit secret access** regularly
5. **Use least-privilege access** for service principals
6. **Enable logging** for all secret operations
7. **Use Managed Identities** where possible to eliminate credential management

### 9.3 Performance Considerations

```python
from typing import Optional, Callable, Any
from dataclasses import dataclass
import time
import functools


@dataclass
class PerformanceMetrics:
    """Performance metrics for actor operations."""
    operation: str
    duration_ms: float
    timestamp: float
    success: bool
    error: Optional[str] = None


class PerformanceMonitor:
    """
    Performance monitoring for actor operations.
    Tracks latency, throughput, and error rates.
    """

    def __init__(self, max_history: int = 1000):
        self.metrics: list[PerformanceMetrics] = []
        self.max_history = max_history
        self._lock = threading.Lock()

    def record(self, operation: str, duration_ms: float,
               success: bool, error: Optional[str] = None) -> None:
        """Record performance metric."""
        with self._lock:
            self.metrics.append(PerformanceMetrics(
                operation=operation,
                duration_ms=duration_ms,
                timestamp=time.time(),
                success=success,
                error=error
            ))

            # Trim history
            if len(self.metrics) > self.max_history:
                self.metrics = self.metrics[-self.max_history:]

    def get_operation_stats(self, operation: str) -> dict:
        """Get statistics for specific operation."""
        with self._lock:
            op_metrics = [m for m in self.metrics if m.operation == operation]

            if not op_metrics:
                return {"count": 0, "avg_ms": 0, "p95_ms": 0, "error_rate": 0}

            durations = [m.duration_ms for m in op_metrics]
            errors = [m for m in op_metrics if not m.success]

            durations.sort()
            p95_idx = int(len(durations) * 0.95)

            return {
                "count": len(op_metrics),
                "avg_ms": sum(durations) / len(durations),
                "p95_ms": durations[p95_idx] if durations else 0,
                "min_ms": min(durations) if durations else 0,
                "max_ms": max(durations) if durations else 0,
                "error_rate": len(errors) / len(op_metrics)
            }


def monitor_performance(operation_name: str):
    """Decorator for performance monitoring."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            monitor = get_performance_monitor()
            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                duration_ms = (time.perf_counter() - start) * 1000
                monitor.record(operation_name, duration_ms, True)
                return result
            except Exception as e:
                duration_ms = (time.perf_counter() - start) * 1000
                monitor.record(operation_name, duration_ms, False, str(e))
                raise
        return wrapper
    return decorator


# Global performance monitor
_performance_monitor: Optional[PerformanceMonitor] = None


def get_performance_monitor() -> PerformanceMonitor:
    """Get singleton performance monitor."""
    global _performance_monitor
    if _performance_monitor is None:
        _performance_monitor = PerformanceMonitor()
    return _performance_monitor
```

### 9.4 Memory Management Strategies

```python
import gc
import threading
from typing import Dict, Any, Optional
from dataclasses import dataclass
import weakref


@dataclass
class MemoryStats:
    """Memory usage statistics."""
    rss_mb: float
    vms_mb: float
    gc_objects: int
    timestamp: float


class MemoryManager:
    """
    Memory management for actor systems.
    Implements LRU caching and automatic cleanup.
    """

    def __init__(self, max_memory_mb: float = 1024.0,
                 gc_threshold: int = 10000):
        self.max_memory_mb = max_memory_mb
        self.gc_threshold = gc_threshold
        self._active_objects: Dict[str, weakref.ref] = {}
        self._lock = threading.Lock()

    def register_object(self, obj_id: str, obj: Any) -> None:
        """Register object for memory tracking."""
        with self._lock:
            self._active_objects[obj_id] = weakref.ref(obj)

    def unregister_object(self, obj_id: str) -> None:
        """Unregister object from memory tracking."""
        with self._lock:
            self._active_objects.pop(obj_id, None)

    def get_memory_stats(self) -> MemoryStats:
        """Get current memory statistics."""
        import psutil
        process = psutil.Process()
        memory_info = process.memory_info()

        return MemoryStats(
            rss_mb=memory_info.rss / 1024 / 1024,
            vms_mb=memory_info.vms / 1024 / 1024,
            gc_objects=len(gc.get_objects()),
            timestamp=time.time()
        )

    def check_memory_pressure(self) -> bool:
        """Check if memory pressure requires cleanup."""
        stats = self.get_memory_stats()
        return stats.rss_mb > self.max_memory_mb * 0.8

    def force_cleanup(self) -> int:
        """
        Force garbage collection of unreachable objects.

        Returns:
            Number of objects collected
        """
        before = len(gc.get_objects())
        gc.collect()
        after = len(gc.get_objects())
        return before - after

    def cleanup_inactive(self) -> int:
        """Clean up inactive actor objects."""
        cleaned = 0

        with self._lock:
            inactive = [
                obj_id for obj_id, ref in self._active_objects.items()
                if ref() is None
            ]

            for obj_id in inactive:
                self._active_objects.pop(obj_id)
                cleaned += 1

        if cleaned > 0:
            cleaned += self.force_cleanup()

        return cleaned

    def should_collect(self) -> bool:
        """Determine if garbage collection should run."""
        stats = self.get_memory_stats()
        return (
            stats.gc_objects > self.gc_threshold or
            stats.rss_mb > self.max_memory_mb * 0.9
        )
```

---

## 10. Appendices

### 10.1 Glossary of Terms

| Term | Definition |
|------|------------|
| **Actor** | Fundamental unit of computation that processes messages asynchronously |
| **Actor System** | Collection of actors that can communicate with each other |
| **Character Card** | Portable file defining an AI character's attributes and behaviors |
| **Sprite** | 2D image used in animation sequences |
| **Viseme** | Visual representation of a phoneme used in lip sync |
| **Event Sourcing** | Pattern where state changes are stored as a sequence of events |
| **Supervision** | Fault tolerance mechanism where parent actors restart children |
| **Grain** | Virtual actor in Orleans framework |
| **Shard** | Partition of actor state across cluster nodes |

### 10.2 Reference Implementations

- **PyKka**: https://pykka.readthedocs.io/
- **Akka**: https://akka.io/docs/
- **OTP**: https://erlang.org/doc/design_principles/des_princ.html
- **Actix**: https://actix.rs/
- **Orleans**: https://dotnet.github.io/orleans/

### 10.3 Format Specifications Quick Reference

| Format | Schema Location | Extensions |
|--------|-----------------|------------|
| Aura | [`schemas/aura.json`](schemas/aura.json) | `.json` |
| SillyTavern | [`schemas/sillytavern.yaml`](schemas/sillytavern.yaml) | `.yaml`, `.yml` |
| Unified | [`schemas/unified_character.json`](schemas/unified_character.json) | `.character.json` |

### 10.4 Performance Benchmark Data

| Operation | Average Latency | P95 Latency | Throughput |
|-----------|-----------------|-------------|------------|
| Character Response Generation | 150-500ms | 800ms | 100 req/s |
| Avatar Frame Render | 16-33ms | 50ms | 60 fps |
| Animation State Transition | 50-100ms | 150ms | 10 transitions/s |
| Knowledge Retrieval | 10-50ms | 100ms | 1000 queries/s |
| Duel Round Evaluation | 5-10ms | 20ms | 50 rounds/s |

---

**Document Version**: 1.0.0
**Last Updated**: 2026-01-27
**Maintained By**: @JARVIS @LUMINA

---

*This document is part of the Lumina AI Character Platform documentation suite. For additional resources, see the [Architecture Overview](../ARCHITECTURE_OVERVIEW.md) and [API Reference](../API_REFERENCE.md).*
