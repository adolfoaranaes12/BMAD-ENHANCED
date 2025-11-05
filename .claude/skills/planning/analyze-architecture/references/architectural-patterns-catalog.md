# Architectural Patterns Catalog

## Common Patterns

### Domain-Driven Design (DDD)
**Indicators:**
- domain/entities/ directories
- AggregateRoot classes
- DomainEvent types
- Value objects

### CQRS
**Indicators:**
- Separate command and query handlers
- commands/ and queries/ directories
- CommandHandler/QueryHandler classes

### Layered Architecture
**Indicators:**
- presentation/, application/, domain/, infrastructure/ layers
- controllers/, services/, repositories/ separation

### Microservices
**Indicators:**
- Multiple services/ subdirectories
- Docker compose configurations
- Independent deployment artifacts
