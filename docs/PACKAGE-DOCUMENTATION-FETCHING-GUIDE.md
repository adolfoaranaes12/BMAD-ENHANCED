# Package Documentation Fetching Guide

**How to ensure agents use current package APIs**

Version: 2.0
Last Updated: 2025-11-05

---

## Problem Statement

**Common Issue:** Agents produce outdated code when using external packages because they rely on training data instead of checking current documentation.

**Example Problems:**
- Using deprecated methods that were removed in newer versions
- Incorrect parameter types or counts
- Missing required configuration
- Using old API patterns that have been replaced

**Impact:**
- Code doesn't compile or run
- Runtime errors
- Security vulnerabilities from outdated patterns
- Time wasted debugging and fixing

---

## Solution: Always Fetch Documentation First

### The Golden Rule

**Before writing code that uses any external package:**
1. ✅ Identify the package and its installed version
2. ✅ Fetch official documentation for that version
3. ✅ Verify API methods, parameters, return types
4. ✅ Use documentation examples, not training data
5. ✅ Reference docs in code comments

---

## Implementation in BMAD Enhanced

### For Users

**When creating task specifications**, mention packages explicitly:

```markdown
## Technical Specifications

### External Dependencies
- axios@1.6.0 for HTTP requests
- zod@3.22.0 for schema validation
- prisma@5.7.0 for database access

### Package Documentation
- Fetch axios docs before implementing HTTP client
- Verify zod schema syntax for validation
- Check Prisma Client API for database queries
```

**When invoking James:**

```bash
# Correct - James will see package usage and fetch docs
/james *implement task-http-client-001

# The skill will automatically:
# 1. Parse task spec
# 2. Identify axios package
# 3. Fetch axios documentation
# 4. Verify API methods
# 5. Implement using current docs
```

---

### For Agent (Built-In)

James now includes **Package/Library Usage Guardrails**:

```
**Package/Library Usage Guardrails:**
- CRITICAL: When using external packages, ALWAYS fetch current documentation first
- Check package version in package.json/requirements.txt/go.mod
- Fetch documentation from official sources
- Verify API syntax matches current package version
- Never rely solely on training data for package APIs
```

The `implement-v2` skill includes **Step 0.5: Check for External Packages**:
1. Identify external packages
2. Check installed versions
3. Fetch official documentation
4. Verify API compatibility
5. Document findings

---

## How to Fetch Documentation

### JavaScript/TypeScript Packages

**Method 1: NPM Package Page**
```bash
WebFetch(
  url: "https://www.npmjs.com/package/axios",
  prompt: "Extract: installation, main API methods, usage examples, version compatibility"
)
```

**Method 2: Official Documentation**
```bash
WebFetch(
  url: "https://axios-http.com/docs/api_intro",
  prompt: "Extract: API reference for axios.get(), axios.post(), configuration options"
)
```

**Method 3: TypeScript Definitions**
```bash
# Read type definitions for exact signatures
Read(file_path: "node_modules/axios/index.d.ts")
```

**Example Output:**
```typescript
// Axios@1.6.0 Documentation Reference
// Source: https://axios-http.com/docs/api_intro
//
// axios.get(url, config?)
//   - url: string
//   - config?: AxiosRequestConfig
//   - returns: Promise<AxiosResponse<T>>
//
// axios.post(url, data, config?)
//   - url: string
//   - data: any
//   - config?: AxiosRequestConfig
//   - returns: Promise<AxiosResponse<T>>

import axios from 'axios';

const response = await axios.get('/api/users');
```

---

### Python Packages

**Method 1: PyPI**
```bash
WebFetch(
  url: "https://pypi.org/project/requests/",
  prompt: "Extract: API reference, usage examples for version 2.31.0"
)
```

**Method 2: Read the Docs**
```bash
WebFetch(
  url: "https://requests.readthedocs.io/en/stable/",
  prompt: "Extract: requests.get() signature, parameters, return type, examples"
)
```

**Example Output:**
```python
# Requests@2.31.0 Documentation Reference
# Source: https://requests.readthedocs.io/en/stable/
#
# requests.get(url, params=None, **kwargs)
#   - url: str
#   - params: Optional[Dict[str, str]]
#   - returns: requests.Response
#
# Response attributes:
#   - .status_code: int
#   - .text: str
#   - .json(): Dict

import requests

response = requests.get('https://api.github.com/users/octocat')
data = response.json()
```

---

### Go Modules

**Method: pkg.go.dev**
```bash
WebFetch(
  url: "https://pkg.go.dev/github.com/gin-gonic/gin",
  prompt: "Extract: package documentation, function signatures, examples for gin.Engine"
)
```

**Example Output:**
```go
// Gin@1.9.1 Documentation Reference
// Source: https://pkg.go.dev/github.com/gin-gonic/gin
//
// gin.Default() creates Engine with Logger and Recovery middleware
// gin.New() creates blank Engine without middleware
//
// Engine methods:
//   - GET(relativePath string, handlers ...HandlerFunc)
//   - POST(relativePath string, handlers ...HandlerFunc)
//   - Run(addr ...string) error

package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{"message": "pong"})
    })
    r.Run() // listen on 0.0.0.0:8080
}
```

---

### Java Dependencies

**Method: Maven Central + Javadoc**
```bash
WebFetch(
  url: "https://search.maven.org/artifact/com.google.code.gson/gson",
  prompt: "Extract: latest version, Javadoc link"
)

WebFetch(
  url: "https://www.javadoc.io/doc/com.google.code.gson/gson/latest/",
  prompt: "Extract: Gson class methods, fromJson() and toJson() signatures"
)
```

---

### Rust Crates

**Method: docs.rs**
```bash
WebFetch(
  url: "https://docs.rs/serde/latest/serde/",
  prompt: "Extract: Serialize and Deserialize trait documentation, derive macros"
)
```

---

### .NET Packages

**Method: NuGet + Microsoft Docs**
```bash
WebFetch(
  url: "https://www.nuget.org/packages/Newtonsoft.Json/",
  prompt: "Extract: version, documentation link"
)

WebFetch(
  url: "https://www.newtonsoft.com/json/help/html/SerializingJSON.htm",
  prompt: "Extract: JsonConvert.SerializeObject() and DeserializeObject() examples"
)
```

---

## Verification Checklist

Before implementing code with external packages:

### ✅ Version Check
```bash
# JavaScript
grep "package-name" package.json
grep "package-name" package-lock.json

# Python
grep "package-name" requirements.txt
pip show package-name

# Go
grep "package-name" go.mod

# Rust
grep "package-name" Cargo.toml

# Java
grep "groupId\|artifactId" pom.xml
```

### ✅ Documentation Fetch
- [ ] Found official documentation
- [ ] Documentation matches installed version
- [ ] API methods verified
- [ ] Parameter types confirmed
- [ ] Return types confirmed
- [ ] Example code reviewed

### ✅ Code Implementation
- [ ] Used API from documentation, not training data
- [ ] Added comments referencing docs
- [ ] Included version number in comments
- [ ] Tested with actual package version

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Using Training Data

```typescript
// ❌ WRONG - Using training data from 2021
// This API changed in axios 1.0
const response = await axios({
  method: 'get',
  url: '/api/users',
  transformResponse: [function (data) { return data; }]
});

// ✅ CORRECT - Using current axios@1.6.0 docs
// Docs: https://axios-http.com/docs/api_intro
const response = await axios.get('/api/users');
```

---

### ❌ Mistake 2: Assuming Old Patterns Work

```python
# ❌ WRONG - Old requests pattern (pre-2.0)
import requests
r = requests.get('https://api.github.com/events', prefetch=True)

# ✅ CORRECT - Current requests@2.31.0
# Docs: https://requests.readthedocs.io/en/stable/
import requests
r = requests.get('https://api.github.com/events')
```

---

### ❌ Mistake 3: Not Checking Version-Specific Changes

```typescript
// ❌ WRONG - This changed between versions
// Prisma 4.x vs 5.x have different APIs

// ✅ CORRECT - Check installed version first
// package.json shows: "prisma": "^5.7.0"
// Docs: https://www.prisma.io/docs/orm/prisma-client
// Version 5.x uses: prisma.$queryRaw``
const users = await prisma.$queryRaw`SELECT * FROM User`;
```

---

## Best Practices

### 1. Document Version in Comments

```typescript
// Using zod@3.22.0
// Docs: https://zod.dev/?id=primitives
// z.string() creates string schema
import { z } from 'zod';

const userSchema = z.object({
  email: z.string().email(),
  age: z.number().min(18)
});
```

---

### 2. Prefer Official Examples

```python
# From requests documentation:
# https://requests.readthedocs.io/en/stable/user/quickstart/#passing-parameters-in-urls

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)  # https://httpbin.org/get?key1=value1&key2=value2
```

---

### 3. Keep Documentation Links

```go
// Package: github.com/gin-gonic/gin@v1.9.1
// Docs: https://pkg.go.dev/github.com/gin-gonic/gin#readme-api-examples
// Example from official docs: Basic routing

package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run() // 0.0.0.0:8080
}
```

---

### 4. Update Comments When Upgrading

```typescript
// BEFORE UPGRADE:
// Using axios@1.4.0
// ...

// AFTER UPGRADE:
// Using axios@1.6.0
// Docs: https://axios-http.com/docs/api_intro
// BREAKING CHANGE: axios.defaults.transformResponse removed
// Migration: Use response interceptors instead
```

---

## Integration with BMAD Enhanced

### Automatic in implement-v2 Skill

The skill now includes Step 0.5 that automatically:
1. Scans task spec for package mentions
2. Checks installed versions
3. Fetches official documentation
4. Verifies API compatibility
5. Documents findings in code

### Manual Invocation

If implementing without a skill, follow this pattern:

```bash
# 1. Identify package and version
cat package.json | grep express

# 2. Fetch documentation
WebFetch(
  url: "https://expressjs.com/en/5x/api.html",
  prompt: "Extract: express() app creation, app.get() routing, middleware usage"
)

# 3. Verify before implementing
# Check that methods exist and signatures match

# 4. Implement with references
# Add comments linking to docs
```

---

## Summary

### The Rule

**NEVER implement code using external packages without fetching current documentation first.**

### The Process

1. ✅ Identify packages from task spec
2. ✅ Check installed versions
3. ✅ Fetch official documentation
4. ✅ Verify API compatibility
5. ✅ Reference docs in comments
6. ✅ Use documentation examples
7. ✅ Test with actual version

### The Benefit

- ✅ Code works on first try
- ✅ No runtime errors from API changes
- ✅ Secure, up-to-date patterns
- ✅ Easy to maintain and update
- ✅ Clear documentation trail

---

**See Also:**
- [BEST-PRACTICES.md](./BEST-PRACTICES.md) - Development patterns
- [HOW-TO-USE-AGENTS-CORRECTLY.md](./HOW-TO-USE-AGENTS-CORRECTLY.md) - Command syntax
- [CRITICAL-SKILL-LOADING-ISSUE.md](./CRITICAL-SKILL-LOADING-ISSUE.md) - Skill loading

---

**Version:** 2.0
**Status:** Production Ready
**Last Updated:** 2025-11-05
