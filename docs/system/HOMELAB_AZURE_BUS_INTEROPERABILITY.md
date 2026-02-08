# Homelab Azure Service Bus Interoperability

## Overview

Comprehensive async Azure Service Bus interoperability system for all @HOMELAB assets at multiple infrastructure and inference layers, coordinating interconnectivity, security, network, and system engineering teams.

## Assets

### @FALC
- **Type**: System
- **Topics**: `falc.workflows`, `falc.events`, `falc.commands`
- **Queues**: `falc-command-queue`, `falc-response-queue`
- **Infrastructure Topics**: `infrastructure.falc.system`, `infrastructure.falc.monitoring`, `infrastructure.falc.health`
- **Inference Topics**: `inference.falc.ai`, `inference.falc.llm`, `inference.falc.decision`

### @NAS (10.17.17.32)
- **Type**: Storage
- **Topics**: `nas.storage`, `nas.backup`, `nas.monitoring`, `nas.file_operations`
- **Queues**: `nas-storage-queue`, `nas-backup-queue`, `nas-monitoring-queue`
- **Infrastructure Topics**: `infrastructure.nas.storage`, `infrastructure.nas.network`, `infrastructure.nas.health`
- **Inference Topics**: `inference.nas.cache`, `inference.nas.data`, `inference.nas.physics`

### @PFSENSEFW (10.17.17.1)
- **Type**: Firewall
- **Topics**: `pfsense.network`, `pfsense.firewall`, `pfsense.monitoring`, `pfsense.security`
- **Queues**: `pfsense-network-queue`, `pfsense-firewall-queue`, `pfsense-security-queue`
- **Infrastructure Topics**: `infrastructure.pfsense.network`, `infrastructure.pfsense.routing`, `infrastructure.pfsense.security`
- **Inference Topics**: `inference.pfsense.traffic`, `inference.pfsense.patterns`, `inference.pfsense.threats`

### @KAIJU_NO_8 (10.17.17.11)
- **Type**: Workstation
- **Topics**: `kaiju.workflows`, `kaiju.compute`, `kaiju.mcp`, `kaiju.monitoring`
- **Queues**: `kaiju-workflow-queue`, `kaiju-compute-queue`, `kaiju-mcp-queue`
- **Infrastructure Topics**: `infrastructure.kaiju.system`, `infrastructure.kaiju.network`, `infrastructure.kaiju.resources`
- **Inference Topics**: `inference.kaiju.llm`, `inference.kaiju.ai`, `inference.kaiju.cluster`

### @HOMELAB
- **Type**: Infrastructure
- **Topics**: `homelab.orchestration`, `homelab.coordination`, `homelab.monitoring`, `homelab.events`
- **Queues**: `homelab-orchestration-queue`, `homelab-coordination-queue`, `homelab-monitoring-queue`
- **Infrastructure Topics**: `infrastructure.homelab.network`, `infrastructure.homelab.security`, `infrastructure.homelab.resources`, `infrastructure.homelab.health`
- **Inference Topics**: `inference.homelab.ai`, `inference.homelab.llm`, `inference.homelab.decision`, `inference.homelab.patterns`

### @COMPANY
- **Type**: Organization
- **Topics**: `company.workflows`, `company.coordination`, `company.security`, `company.compliance`
- **Queues**: `company-workflow-queue`, `company-coordination-queue`, `company-security-queue`
- **Infrastructure Topics**: `infrastructure.company.network`, `infrastructure.company.security`, `infrastructure.company.resources`
- **Inference Topics**: `inference.company.ai`, `inference.company.decision`, `inference.company.strategy`

## Engineering Teams

### Interconnectivity Engineering Team
- **Responsibilities**:
  - Azure Service Bus topology design
  - Message routing and delivery
  - Component integration
  - Interoperability testing
  - Connection management
- **Topics**: `teams.interconnectivity.design`, `teams.interconnectivity.routing`, `teams.interconnectivity.integration`
- **Queues**: `interconnectivity-design-queue`, `interconnectivity-routing-queue`

### Security Engineering Team
- **Responsibilities**:
  - Security policy enforcement
  - Threat detection and response
  - Access control
  - Audit and compliance
  - Security monitoring
- **Topics**: `teams.security.policy`, `teams.security.threats`, `teams.security.audit`
- **Queues**: `security-policy-queue`, `security-threat-queue`, `security-audit-queue`

### Network Engineering Team
- **Responsibilities**:
  - Network topology
  - Routing and switching
  - Firewall management
  - Network monitoring
  - Performance optimization
- **Topics**: `teams.network.topology`, `teams.network.routing`, `teams.network.monitoring`
- **Queues**: `network-topology-queue`, `network-routing-queue`

### System Engineering Team
- **Responsibilities**:
  - System architecture
  - Infrastructure design
  - Resource management
  - System monitoring
  - Performance tuning
- **Topics**: `teams.system.architecture`, `teams.system.infrastructure`, `teams.system.monitoring`
- **Queues**: `system-architecture-queue`, `system-infrastructure-queue`

## Infrastructure Layers

### Layer 1: Physical Infrastructure
- **Description**: Hardware, network, storage
- **Assets**: NAS, PFSENSEFW, KAIJU_NO_8
- **Topics**: `infrastructure.physical.hardware`, `infrastructure.physical.network`, `infrastructure.physical.storage`

### Layer 2: Network Infrastructure
- **Description**: Network topology, routing, firewall
- **Assets**: PFSENSEFW, HOMELAB
- **Topics**: `infrastructure.network.topology`, `infrastructure.network.routing`, `infrastructure.network.security`

### Layer 3: System Infrastructure
- **Description**: Operating systems, services, applications
- **Assets**: KAIJU_NO_8, NAS, HOMELAB
- **Topics**: `infrastructure.system.os`, `infrastructure.system.services`, `infrastructure.system.applications`

### Layer 4: Application Infrastructure
- **Description**: Applications, APIs, services
- **Assets**: FALC, HOMELAB, COMPANY
- **Topics**: `infrastructure.application.apis`, `infrastructure.application.services`, `infrastructure.application.workflows`

## Inference Layers

### Layer 1: Data Inference Layer
- **Description**: Data processing, caching, storage
- **Assets**: NAS, HOMELAB
- **Topics**: `inference.data.processing`, `inference.data.caching`, `inference.data.storage`

### Layer 2: AI Inference Layer
- **Description**: AI models, LLM inference, decision making
- **Assets**: KAIJU_NO_8, FALC, HOMELAB
- **Topics**: `inference.ai.models`, `inference.ai.llm`, `inference.ai.decision`

### Layer 3: Coordination Inference Layer
- **Description**: Workflow orchestration, coordination, intelligence
- **Assets**: HOMELAB, COMPANY
- **Topics**: `inference.coordination.workflow`, `inference.coordination.intelligence`, `inference.coordination.orchestration`

### Layer 4: Strategy Inference Layer
- **Description**: Strategic decision making, planning, optimization
- **Assets**: COMPANY, HOMELAB
- **Topics**: `inference.strategy.planning`, `inference.strategy.optimization`, `inference.strategy.decision`

## Message Routing

### Cross-Asset Routing
- **FALC → NAS**: `falc.workflows` → `nas.storage`
- **NAS → KAIJU_NO_8**: `nas.storage` → `kaiju.compute`
- **PFSENSEFW → HOMELAB**: `pfsense.network` → `homelab.orchestration`
- **KAIJU_NO_8 → COMPANY**: `kaiju.workflows` → `company.workflows`

### Team Routing
- **Interconnectivity Team**: All assets (FALC, NAS, PFSENSEFW, KAIJU_NO_8, HOMELAB)
- **Security Team**: PFSENSEFW, HOMELAB, COMPANY
- **Network Team**: PFSENSEFW, HOMELAB
- **System Engineering Team**: NAS, KAIJU_NO_8, HOMELAB

### Layer Routing
- **Infrastructure → Inference**: `infrastructure.*` → `inference.*`
- **Cross-Layer**: All layers can communicate via topics

## Usage

### Python API

```python
from homelab_azure_bus_interoperability import get_homelab_interoperability

# Get interoperability instance
interop = get_homelab_interoperability()

# Publish message from asset
interop.publish_asset_message(
    asset_id="nas",
    topic="nas.storage",
    message_type=MessageType.WORKFLOW,
    payload={"operation": "backup", "target": "/volume1/backup"}
)

# Publish message from team
interop.publish_team_message(
    team_id="security_team",
    topic="teams.security.policy",
    message_type=MessageType.COORDINATION,
    payload={"policy": "enforce_password_auth"}
)

# Subscribe to topic
def handle_nas_message(message: Dict[str, Any]):
    print(f"Received NAS message: {message}")

interop.subscribe_asset_topic(
    asset_id="nas",
    topic="nas.storage",
    subscription="nas-storage-subscription",
    handler=handle_nas_message
)

# Start async processing
interop.start_async_processing()
```

### CLI

```bash
# Show status
python scripts/python/homelab_azure_bus_interoperability.py --status

# Get asset status
python scripts/python/homelab_azure_bus_interoperability.py --asset nas

# Get team status
python scripts/python/homelab_azure_bus_interoperability.py --team security_team

# Show summary
python scripts/python/homelab_azure_bus_interoperability.py --summary

# Publish message
python scripts/python/homelab_azure_bus_interoperability.py --publish nas:nas.storage:workflow

# Start async processing
python scripts/python/homelab_azure_bus_interoperability.py --start

# Stop async processing
python scripts/python/homelab_azure_bus_interoperability.py --stop
```

## Configuration

Configuration file: `config/homelab_azure_bus_interoperability.json`

### Azure Service Bus
- **Namespace**: `jarvis-lumina-bus.servicebus.windows.net`
- **Connection String**: From Azure Key Vault (`service-bus-connection-string`)
- **Credential**: DefaultAzureCredential

### Security
- **Authentication**: Azure Key Vault
- **Authorization**: RBAC (role-based)
- **Encryption**: TLS 1.2 (in transit), at rest
- **Audit**: Enabled for security events and team actions

## Tags

@FALC @NAS @PFSENSEFW @KAIJU_NO_8 @HOMELAB @COMPANY
#AZURE_SERVICE_BUS #INTEROPERABILITY #INFRASTRUCTURE #INFERENCE #ASYNC
#INTERCONNECTIVITY #SECURITY #NETWORK #SYSTEM_ENGINEERING
