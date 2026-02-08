# Docker Image Selection Guide
## LUMINA Project - Best Practices & Recommendations

**Last Updated:** 2026-01-14  
**System Specs:** x64-based PC, 64GB RAM  
**Primary Language:** Python 3.11+

---

## 📋 Executive Summary

This guide provides Docker image selection recommendations for the LUMINA project based on:
- System architecture (x64, 64GB RAM)
- Application requirements (Python 3.11+, AI/ML workloads)
- Security considerations
- Resource efficiency
- Compatibility requirements

**Key Recommendation:** Use Debian-based `-slim` variants for Python services (current choice is optimal). Consider Alpine for minimal services where musl compatibility is verified.

---

## 🎯 Image Selection Principles

### 1. **For Most Applications**
- ✅ Use official images (e.g., `python`, `node`, `nginx`)
- ✅ Well-maintained and widely compatible
- ✅ Regular security updates
- ✅ Extensive documentation

### 2. **For Minimal Resource Usage**
- ✅ Alpine-based images (e.g., `python:3.12-alpine`)
- ⚠️ **Consideration:** May require musl libc compatibility testing
- ✅ Significantly smaller disk and memory footprint
- ✅ Good for resource-constrained environments

### 3. **For Maximum Compatibility**
- ✅ Debian-based images (e.g., `python:3.12-slim` or `ubuntu:24.04`)
- ✅ Slightly larger but more compatible
- ✅ Better for complex dependencies
- ✅ **Recommended for LUMINA** (current choice)

### 4. **For Enhanced Security**
- ✅ Docker Hardened Images (DHIs) - minimal, secure
- ✅ Available in both Alpine and Debian flavors
- ✅ Continuously scanned for vulnerabilities
- ✅ Reduced attack surface
- 🔍 **Consider for:** Security-critical services (API gateways, authentication)

---

## 🔍 Current LUMINA Docker Image Analysis

### Python Services (Primary Stack)

**Current Choice:** `python:3.11-slim`

| Service | Dockerfile | Base Image | Status | Recommendation |
|---------|-----------|------------|--------|----------------|
| JARVIS Master Agent API | `Dockerfile` | `python:3.11-slim` | ✅ Optimal | **Keep** - Perfect balance |
| PEAK AI Orchestrator | `containerization/services/peak-ai-orchestrator/Dockerfile` | `python:3.11-slim` | ✅ Optimal | **Keep** - Good compatibility |
| MANUS MCP Server | `containerization/services/manus-mcp-server/Dockerfile` | `python:3.11-slim` | ✅ Optimal | **Keep** - Azure SDK compatibility |
| API Gateway | `docker/api_gateway/Dockerfile` | `python:3.11-slim` | ✅ Optimal | **Keep** - Standard choice |
| AIOS | `docker/aios/Dockerfile` | `python:3.11-slim` | ✅ Optimal | **Keep** - Build tools needed |

**Analysis:**
- ✅ **Excellent choice** - `python:3.11-slim` is Debian-based
- ✅ Good compatibility with Azure SDK, PostgreSQL, and ML libraries
- ✅ Reasonable size (~150-200MB) without sacrificing compatibility
- ✅ Well-maintained official image

**Alternative Consideration:**
- `python:3.11-alpine` - Would save ~50-70MB but requires musl compatibility testing
- **Recommendation:** Only consider if disk space becomes critical

---

### LLM/AI Model Services

**Current Choice:** `ollama/ollama:latest`

| Service | Dockerfile | Base Image | Status | Recommendation |
|---------|-----------|------------|--------|----------------|
| Hardened PEAK AI | `containerization/services/hardened-peak-ai/Dockerfile` | `ollama/ollama:latest` | ⚠️ Review | **Consider DHI variant** |
| Falcon LLM | `containerization/services/ollama/Dockerfile.falcon` | `ollama/ollama:latest` | ✅ Acceptable | **Keep** - Official image |

**Analysis:**
- ✅ Official Ollama image is well-maintained
- ⚠️ For hardened services, consider Docker Hardened Images if available
- ✅ Current choice is acceptable for development/production

**Security Enhancement:**
- Consider multi-stage builds to reduce final image size
- Review security scanning for `ollama/ollama:latest`
- Monitor for DHI variants of Ollama

---

### Database Services

**Current Choice:** `postgres:15-alpine`

| Service | docker-compose.yml | Base Image | Status | Recommendation |
|---------|-------------------|------------|--------|----------------|
| PostgreSQL | `docker-compose.yml` | `postgres:15-alpine` | ✅ Optimal | **Keep** - Minimal & efficient |

**Analysis:**
- ✅ Alpine variant is perfect for PostgreSQL
- ✅ Minimal size with full functionality
- ✅ Well-tested and stable

---

## 📊 Image Size Comparison

| Image | Size (Approx) | Use Case | Recommendation |
|-------|--------------|----------|----------------|
| `python:3.11` | ~900MB | Full Debian | ❌ Too large |
| `python:3.11-slim` | ~150MB | **Current** | ✅ **Optimal** |
| `python:3.11-alpine` | ~50MB | Minimal | ⚠️ Test compatibility |
| `ollama/ollama:latest` | ~1.2GB | LLM runtime | ✅ Acceptable |
| `postgres:15-alpine` | ~250MB | Database | ✅ Optimal |

---

## 🛡️ Security Considerations

### Current Security Posture

1. **Python Services:**
   - ✅ Using official images (regularly updated)
   - ✅ Multi-stage builds where applicable
   - ✅ Non-root users in some services (MANUS MCP Server)
   - ⚠️ **Enhancement Opportunity:** Add non-root users to all services

2. **LLM Services:**
   - ✅ Official Ollama image
   - ✅ Security hardening in hardened-peak-ai Dockerfile
   - ⚠️ **Enhancement Opportunity:** Consider DHI variants

3. **Database:**
   - ✅ Alpine-based (minimal attack surface)
   - ✅ Official PostgreSQL image

### Security Recommendations

1. **Add Non-Root Users:**
   ```dockerfile
   RUN groupadd --gid 1000 appuser && \
       useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser
   USER appuser
   ```

2. **Use Docker Hardened Images (DHIs):**
   - For security-critical services
   - When available for your base images
   - Continuously scanned for vulnerabilities

3. **Regular Security Scanning:**
   - Use `docker scan` or Trivy
   - Integrate into CI/CD pipeline
   - Monitor for CVE updates

---

## 🚀 Performance Optimization

### System Resources (64GB RAM, x64)

**Current Status:** ✅ Plenty of resources available

**Recommendations:**
1. **Size is NOT Critical:** With 64GB RAM, image size is less important than compatibility
2. **Focus on Compatibility:** Debian-based images reduce compatibility issues
3. **Multi-Stage Builds:** Already implemented in main Dockerfile ✅
4. **Layer Caching:** Optimize Dockerfile layer ordering (already good ✅)

### Build Optimization

**Current Best Practices (Already Implemented):**
- ✅ Multi-stage builds (main Dockerfile)
- ✅ Layer caching (requirements.txt copied before code)
- ✅ `.dockerignore` configured
- ✅ Minimal system packages installed

**Additional Recommendations:**
- Use BuildKit for faster builds: `DOCKER_BUILDKIT=1 docker build ...`
- Consider build cache mounts for pip: `--mount=type=cache,target=/root/.cache/pip`

---

## 📝 Dockerfile Template Recommendations

### Python Service Template (Current Best Practice)

```dockerfile
# Multi-stage build for production
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y \
    # Runtime deps only
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Create non-root user
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

# Copy application code
COPY --chown=appuser:appuser . /app

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ✅ Action Items

### Immediate (No Changes Needed)
- ✅ **Keep** `python:3.11-slim` for all Python services
- ✅ **Keep** `postgres:15-alpine` for database
- ✅ **Keep** `ollama/ollama:latest` for LLM services

### Short-Term Enhancements
1. **Add Non-Root Users** to all Dockerfiles (security best practice)
2. **Standardize Health Checks** across all services
3. **Document Image Choices** in Dockerfile comments

### Long-Term Considerations
1. **Monitor for DHI Variants** of base images
2. **Evaluate Alpine** for services where size becomes critical
3. **Security Scanning** integration in CI/CD

---

## 🔗 References

- [Docker Hardened Images (DHIs)](https://docs.docker.com/dhi/explore/what/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Official Python Docker Images](https://hub.docker.com/_/python)
- [Official PostgreSQL Docker Images](https://hub.docker.com/_/postgres)
- [Ollama Docker Image](https://hub.docker.com/r/ollama/ollama)

---

## 📊 Decision Matrix

| Criteria | python:3.11-slim | python:3.11-alpine | python:3.11 |
|----------|-----------------|-------------------|-------------|
| **Size** | Medium (~150MB) | Small (~50MB) | Large (~900MB) |
| **Compatibility** | ✅ Excellent | ⚠️ Good (musl) | ✅ Excellent |
| **Maintenance** | ✅ Official | ✅ Official | ✅ Official |
| **Security** | ✅ Good | ✅ Good | ✅ Good |
| **Build Speed** | ✅ Fast | ✅ Fast | ⚠️ Slower |
| **LUMINA Fit** | ✅ **BEST** | ⚠️ Test needed | ❌ Too large |

**Winner:** `python:3.11-slim` ✅

---

## 🎯 Conclusion

**Current Docker image choices for LUMINA are optimal:**

1. ✅ `python:3.11-slim` - Perfect balance of size and compatibility
2. ✅ `postgres:15-alpine` - Minimal and efficient
3. ✅ `ollama/ollama:latest` - Official and well-maintained

**With 64GB RAM, compatibility > size optimization.**

**Next Steps:**
- Add non-root users to all services (security enhancement)
- Document image choices in Dockerfile comments
- Monitor for Docker Hardened Image variants

---

**Tags:** `#DOCKER` `#DEPLOYMENT` `#SECURITY` `#OPTIMIZATION` `@LUMINA` `@JARVIS`
