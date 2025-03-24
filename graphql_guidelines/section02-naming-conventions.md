# 2. Naming conventions

## 2.1 Character casing

### 2.1.1 Names of types MUST be in Pascal case

Names of object, input object, scalar, enum, interface, union MUST be in Pascal case.

### 2.1.2 Names of fields MUST be in camel case

Names of fields of object, input object, interface MUST be in camel case.

### 2.1.3 Names of operations MUST be in camel case

Names of queries, mutations, subscriptions MUST be in camel case.

### 2.1.4 Names of operation parameters MUST be in camel case

Names of query, mutation and subscription parameters MUST be in camel case.

### 2.1.5 Names of enumeration values MUST be in camel case

Enumeration values MUST be in camel case.

### 2.1.6 Names of directives MUST be in camel case

Names of directives MUST be in camel case prepended by `@` symbol.

## 2.2 Name elements

Requirements in this section apply to names of all GraphQL schema elements unless indicated otherwise.

### 2.2.1 Abbreviations SHOULD be avoided

Abbreviations in names SHOULD be avoided, unless they are business terms or otherwise widely known and accepted terms.

For example, full term `ContextualTargeting` should be used instead of `CT`.

Example of accepted abbreviations: `Url`, `Rtb`, `Cpa`, etc.

### 2.2.2 Acronym / initialism MUST be letter cased as a regular word

Acronym or initialism MUST be letter cased as a regular word. Only the first letter can be in upper case.

For example, term `RTB` MUST be letter cased as `Rtb` or `rtb`:
- `RtbLineItem` (type)
- `rtbLineItems` (query)
- `RtbDmpMapping` (type)
- `cpm` (field name)

### 2.2.3 Names MUST NOT contain version

Versions common in APIs, such as `v1` or `v2` MUST NOT be used in names on permanent basis.

Version specific names MAY be used for limited period of time when implementing breaking changes in multiple phases.

### 2.2.4 Names MUST NOT contain "dto"

Names MUST NOT contain `dto` or similar words. Sometimes these are used in underlying APIs. Instead, use business terms consistent across the composite schema.

### 2.2.5 Query names MUST NOT contain "get", "list"

Query names MUST NOT contain `get`, `list` or similar verbs.

### 2.2.6 Names SHOULD include unit of measurement

Field and type names SHOULD express units of measurement for contained value. Typically these SHOULD be implemented as a suffix such as `Ms` (for milliseconds), `Seconds`, `Hours`, `Days`, `Bytes`, `Mb` (for megabytes).

When value expresses percentage on 0..1 scale name SHOULD be suffixed with `Rate`. For example, `videoCompletionRate`.

When value expresses percentage on 0..100 scale name SHOULD be suffixed with `Percentage`. For example, `deviationPercentage`.

## 2.3 Consistency and uniqueness

Type and operation names MUST represent module's business domain.

Currently type reusage from different module is not supported. When it is necessary to use type from different module, it SHOULD be copied and named according to a business domain of a target module.

### 2.3.1 If module represents business domain of an entity, entity name SHOULD be used in names as is

If module represents business domain of an entity, entity name SHOULD be used in names as is. For example, campaigns module representing campaigns business domain SHOULD use `type Campaign`, `query createCampaign` and similar.

### 2.3.2 If type or operation refers to an entity from a different domain its name SHOULD clearly indicate that

If type or operation refers to an entity from a different domain (i.e., module's business domain doesn't own the entity), its name SHOULD clearly indicate that and MUST NOT interfere with similar entity in original business domain. Typical solution is to use module specific prefix or suffix for such types.

For example:
- `Campaign` - represents original business entity in a business domain module
- `CampaignListItem` - represents campaign read model in a different module.
