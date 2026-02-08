# Lumina Complete Workflow: Build → Activation → Dev/Test/Prod

**Date**: 2025-01-28  
**Status**: 📋 **COMPLETE WORKFLOW DOCUMENTATION**

---

## Overview

This document provides the complete workflow from building the Lumina extension through activation to deployment in dev, test, and production environments.

---

## Phase 1: Build Process

### 1.1 Prerequisites

- **Node.js**: v16+ (for VS Code extension development)
- **Python**: 3.9+ (for backend scripts)
- **TypeScript**: Latest (for extension code)
- **VS Code Extension Development Tools**: Installed

### 1.2 Build Steps

```bash
# 1. Install dependencies
npm install

# 2. Compile TypeScript
npm run compile
# OR
tsc -p tsconfig.json

# 3. Package extension
npm run package
# OR
vsce package

# 4. Verify build
npm run test
```

### 1.3 Build Artifacts

- `out/` - Compiled JavaScript files
- `*.vsix` - Packaged extension file
- `node_modules/` - Dependencies

### 1.4 Build Verification

```bash
# Check build output
ls -la out/

# Verify extension package
code --install-extension *.vsix --force
```

---

## Phase 2: Development Environment Setup

### 2.1 Local Development

```bash
# 1. Clone repository
git clone <repository-url>
cd lumina

# 2. Install dependencies
npm install
pip install -r requirements.txt

# 3. Configure development environment
cp .env.example .env.dev
# Edit .env.dev with development settings

# 4. Start development services
python scripts/python/deploy_activate_lumina.py
```

### 2.2 Development Workflow

1. **Make Changes**
   - Edit source files in `src/`
   - Edit Python scripts in `scripts/python/`

2. **Test Locally**
   ```bash
   npm run test
   python -m pytest tests/
   ```

3. **Verify Workflow**
   ```bash
   python scripts/python/workflow_completion_verifier.py
   ```

4. **Track Changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

### 2.3 Development Verification

- ✅ Code compiles without errors
- ✅ Tests pass
- ✅ Workflow verification passes
- ✅ No critical linting errors

---

## Phase 3: Testing Environment

### 3.1 Test Environment Setup

```bash
# 1. Create test environment config
cp .env.example .env.test
# Edit .env.test with test settings

# 2. Run tests
npm run test
python -m pytest tests/

# 3. Integration tests
python scripts/python/test_integration.py
```

### 3.2 Test Workflow

1. **Unit Tests**
   - Test individual components
   - Mock external dependencies

2. **Integration Tests**
   - Test component interactions
   - Test workflow execution

3. **End-to-End Tests**
   - Test complete workflows
   - Test extension activation

### 3.3 Test Verification

- ✅ All unit tests pass
- ✅ All integration tests pass
- ✅ All E2E tests pass
- ✅ Code coverage > 80%

---

## Phase 4: Extension Activation

### 4.1 Activation Prerequisites

- ✅ Build completed successfully
- ✅ Tests passed
- ✅ Configuration verified
- ✅ Dependencies installed

### 4.2 Activation Steps

```bash
# 1. Deploy and activate
python scripts/python/deploy_activate_lumina.py

# 2. Register systems
# This creates config/lumina_extensions_integration.json

# 3. Verify activation
python scripts/python/verify_activation.py
```

### 4.3 Activation Verification

- ✅ Extension registered in Lumina
- ✅ All systems operational
- ✅ R5 API server running
- ✅ Droid actor system loaded
- ✅ JARVIS helpdesk integration active

### 4.4 Activation Checklist

- [ ] Systems registered
- [ ] Dependencies verified
- [ ] Configurations verified
- [ ] R5 API server started
- [ ] Components verified operational

---

## Phase 5: Development Environment Deployment

### 5.1 Dev Environment Setup

```bash
# 1. Configure dev environment
cp config/dev.json.example config/dev.json
# Edit config/dev.json

# 2. Set environment variables
export ENVIRONMENT=dev
export DEBUG=true

# 3. Deploy to dev
python scripts/python/deploy_activate_lumina.py --env dev
```

### 5.2 Dev Environment Verification

```bash
# Check services
curl http://localhost:8000/r5/health

# Verify workflows
python scripts/python/test_workflows.py --env dev
```

### 5.3 Dev Environment Features

- Debug logging enabled
- Development API endpoints
- Mock external services
- Hot reload enabled

---

## Phase 6: Test Environment Deployment

### 6.1 Test Environment Setup

```bash
# 1. Configure test environment
cp config/test.json.example config/test.json
# Edit config/test.json

# 2. Set environment variables
export ENVIRONMENT=test
export DEBUG=false

# 3. Deploy to test
python scripts/python/deploy_activate_lumina.py --env test
```

### 6.2 Test Environment Verification

```bash
# Run test suite
npm run test:test
python -m pytest tests/ --env test

# Integration tests
python scripts/python/test_integration.py --env test
```

### 6.3 Test Environment Features

- Production-like configuration
- Test data isolation
- Automated test execution
- Performance monitoring

---

## Phase 7: Production Environment Deployment

### 7.1 Production Prerequisites

- ✅ All tests passed
- ✅ Security audit completed
- ✅ Performance benchmarks met
- ✅ Documentation updated
- ✅ Rollback plan prepared

### 7.2 Production Deployment Steps

```bash
# 1. Configure production environment
cp config/prod.json.example config/prod.json
# Edit config/prod.json with production settings

# 2. Set environment variables
export ENVIRONMENT=prod
export DEBUG=false
export LOG_LEVEL=info

# 3. Pre-deployment checks
python scripts/python/pre_deployment_checks.py

# 4. Deploy to production
python scripts/python/deploy_activate_lumina.py --env prod

# 5. Post-deployment verification
python scripts/python/post_deployment_verification.py
```

### 7.3 Production Verification

```bash
# Health checks
curl https://api.production.com/health

# Service status
python scripts/python/check_production_status.py

# Monitor logs
tail -f data/logs/production.log
```

### 7.4 Production Features

- Production logging
- Error monitoring
- Performance monitoring
- Security hardening
- Backup procedures

---

## Phase 8: Workflow Verification

### 8.1 Workflow Tracking

All workflows are tracked using `workflow_base.py`:

```python
from workflow_base import WorkflowBase

class MyWorkflow(WorkflowBase):
    def __init__(self):
        super().__init__("MyWorkflow", total_steps=5)
    
    async def execute(self):
        self._mark_step(1, "Step 1", "completed")
        # ... workflow logic
```

### 8.2 Workflow Verification

```bash
# Verify workflow completion
python scripts/python/workflow_completion_verifier.py

# Check workflow status
python scripts/python/check_workflow_status.py
```

### 8.3 Workflow Checklist

- [ ] All steps tracked
- [ ] Completion verified
- [ ] Deliverables confirmed
- [ ] No missing steps
- [ ] Verification passed

---

## Phase 9: Monitoring & Maintenance

### 9.1 Monitoring

- **Health Checks**: Automated health monitoring
- **Error Tracking**: Error logging and alerting
- **Performance Metrics**: Performance monitoring
- **Usage Analytics**: Usage tracking

### 9.2 Maintenance

- **Regular Updates**: Scheduled updates
- **Security Patches**: Security updates
- **Backup Procedures**: Regular backups
- **Documentation Updates**: Keep docs current

---

## Complete Workflow Diagram

```
┌─────────────────┐
│   Build Phase   │
│  (npm install)  │
│  (tsc compile)  │
│  (vsce package) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Dev Environment │
│  (Local Testing) │
│  (Development)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Test Environment│
│  (Unit Tests)    │
│  (Integration)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Activation    │
│  (Deploy Script) │
│  (Registration)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Prod Deployment │
│  (Production)    │
│  (Verification)  │
└─────────────────┘
```

---

## Quick Reference Commands

### Build
```bash
npm install && npm run compile && npm run package
```

### Development
```bash
python scripts/python/deploy_activate_lumina.py --env dev
```

### Testing
```bash
npm run test && python -m pytest tests/
```

### Production
```bash
python scripts/python/deploy_activate_lumina.py --env prod
```

### Verification
```bash
python scripts/python/lumina_complete_audit.py
```

---

## Troubleshooting

### Build Fails
- Check Node.js version
- Clear `node_modules` and reinstall
- Check TypeScript errors

### Activation Fails
- Verify configuration files
- Check dependencies
- Review logs in `data/logs/`

### Deployment Fails
- Verify environment variables
- Check network connectivity
- Review deployment logs

---

**Last Updated**: 2025-01-28

