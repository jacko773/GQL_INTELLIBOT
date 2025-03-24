# 3. Types

## 3.1 Scalars

Scalars typically represent primitive types and can be used both in operation responses and in operation parameters. They are defined with `scalar` keyword.

### 3.1.1 Built-in scalars MUST be used

[Built-in scalar types](https://spec.graphql.org/October2021/#sec-Scalars) MUST be used for the purpose they are defined for. Custom scalars SHOULD NOT be defined if they repeat functionality of the built-in scalars.

### 3.1.2 Existing custom scalars MUST be used

There are common custom scalar and object types defined in [AAP library](https://gitz.adform.com/AAP/AAP-libs/tree/develop/packages/aap-types).

Following custom scalars MUST be used when functionality they provide is needed:
- `Any` - represents any primitive or object value.
- `BigInt` - represents integer value between -(2^53)+1 and 2^53-1.
- `CurrencyCode` - represents three letters currency code according to ISO 4217
- `Decimal` - represents decimal value where digits after decimal point are preserved. Typical usage: monetary values, percentage and rate values entered by user.
- `Date` - represents date and time with offset. Typical usage: auditing fields such as `createdAt`, `lastUpdatedAt`.
- `LocalDate` - represents date without time and without offset. Typical usage: period dates of business entities in local time.
- `LocalDateTime` - represents date and time without offset. Typical usage: period dates with time of business entities in local time.
- `Void` - indicates that operation returns no value. It is useful for mutations based on REST API endpoints that return "No content". Its value is serialized as `null`.

Following custom scalars MUST NOT be used:
- `JSONType` - `Any` SHOULD be used instead
- `NonNegativeFloat` - `Float` SHOULD be used instead
- `EmailAddress` - rarely used, its usefulness is doubtful
- `ObjectId` - not used, its usefulness is doubtful
- `URL` - rarely used, its usefulness is doubtful
- `UUID` - `ID` SHOULD be used instead.

### 3.1.3 Custom scalar "Any" SHOULD be avoided

We strive to have a strongly typed GraphQL schema. However, sometimes due to underlying implementation it is too difficult to express a model in strongly typed manner. Then usage of `Any` type may be justified, but it SHOULD be avoided as much as possible.

Below are the examples of justified usage of `Any` type.

Generic value in notification property:
```graphql
type NotificationProperty {
  name: String
  type: NotificationPropertyType
  value: Any
}
```

Generic value for filter input:
```graphql
input FilterInput {
  fieldName: String!
  operation: FilterOperation!
  values: [Any!]!
}
```

### 3.1.4 New custom scalars MAY be introduced

New custom scalar types MAY be introduced, when necessary. Their introduction MUST be aligned with architects. New scalars MUST be introduced in [AAP-libs](https://gitz.adform.com/AAP/AAP-libs) repository. New scalars MUST NOT be introduced in individual schema module.

## 3.2 Enumerations

Enumeration has a name and a set of values. Enumerations are defined with `enum` keyword.

### 3.2.1 Enumeration name MUST be a singular noun

For example, `ServingMethod`, `BuyingType`.

### 3.2.2 Enumeration name MUST NOT contain word "enum"

Enumeration name MUST NOT contain word "enum", "enumeration" or similar to indicate that the type is enumeration.

### 3.2.3 Enumeration values MUST be strings

Enumeration values MUST NOT be numbers.

Example:
```graphql
enum Direction {
  north
  east
  south
  west
}
```

## 3.3 Objects

Object types represent models returned by queries, mutations and subscriptions. They are defined with `type` keyword.

### 3.3.1 Object fields SHOULD NOT have parameters

Object fields typically correspond to the fields retrieved by the query and thus SHOULD NOT contain parameters. 

Relations (stitched fields) are exception. Stitched fields represent GraphQL queries and thus often have parameters.

## 3.4 Input objects

Input object types are used for operation parameters. They are defined with `input` keyword.

### 3.4.1 Input object names MUST have "Input" suffix

For example, `CampaignInput`.

### 3.4.2 Input objects for mutations MUST NOT include entity id field

When necessary, entity id MUST be passed to mutations as a separate parameter.

Example:

```graphql
input CampaignInput {
  name: String!
}

type Mutation {
  updateCampaign(id: ID!, campaign: CampaignInput!): Campaign!
}
```

### 3.4.3 Separate input object types MAY be used for create and for update mutations

When models for entity create and update mutations are identical, single input object type MAY be used. If models differ, separate input object types SHOULD be used.

Example of single input object:

```graphql
input CampaignInput {
  name: String!
}

type Mutation {
  createCampaign(campaign: CampaignInput!): Campaign!
  updateCampaign(id: ID!, campaign: CampaignInput!): Campaign!
}
```

Example of separate input objects:
```graphql
input CreateCampaignInput {
  advertiserId: ID!
  name: String!
}

input UpdateCampaignInput {
  name: String!
}

type Mutation {
  createCampaign(campaign: CreateCampaignInput!): Campaign!
  updateCampaign(id: ID!, campaign: UpdateCampaignInput!): Campaign!
}
```

## 3.5 Lists

Lists are regular object types designed to represent lists of entities returned by queries.

### 3.5.1 Name of list object type MUST be composed of a single object type name with "List" suffix

Entity name in list object type name MUST be in singular. Entity name MAY be in plural when plural form is naturally used to represent a single entity.

For example, `CampaignList`, `SavingsList` (when single entity type is named `Savings` in plural).

### 3.5.2 List object type MUST have a field for a list of entities

The field MUST be named as entity in plural form.

Field type MUST be an array of object type representing a single entity. Both array and its elements MUST be non-nullable.

Example:
```graphql
type CampaignList {
  campaigns: [Campaign!]!
}
```

### 3.5.3 List object type SHOULD have a field representing amount of entities

Purpose of such field is to facilitate implementation of pagination or infinite scroll on the client.

That MAY be a field `totalCount: Int!` that indicates a total amount of entities that can be returned by a query with given filter parameters. Its value MUST NOT depend on sorting or pagination.

Or that MAY be a field `hasMoreItems: Boolean!` that indicates whether there are more entities to be returned by a query with given filter parameters in the next page.

Example:
```graphql
type CampaignList {
  campaigns: [Campaign!]!
  totalCount: Int!
}
```

or
```graphql
type CampaignList {
  campaigns: [Campaign!]!
  hasMoreItems: Boolean!
}
```

### 3.5.4 List object type MAY have other additional fields

There MAY be other fields in list object type representing useful list properties.

For example, list of messages for a given user MAY have following additional fields:
```graphql
readCount: Int!
unreadCount: Int!
```

## 3.6 Fields

Fields comprise object types and input object types. Field has a name and a type.
Object types represent a list of named fields, where each field yields a value of a specific type.
Input object types define a set of named input fields that can accept input values.

### 3.6.1 Non-null fields MUST be marked accordingly

By default, fields are nullable. Non-null fields are marked with exclamation mark `!`. See [specification](https://spec.graphql.org/October2021/#sec-Non-Null) for more details.

Non-null MUST be marked with `!` as much as possible. This allows clients to understand business entities better and to consume GraphQL schema more efficiently.

Examples:
```graphql
type BankAccount {
  iban: ID!       # value cannot be null
  cards: [Card!]  # value can be null, value can be an empty array, array cannot have null values
  transactions: [Transaction!]! # value cannot be null, value can be an empty array, array cannot have null values
}
```

### 3.6.2 Fields that represent entity identifier MUST be of `ID` type

Fields that represent entity identifier MUST be of `ID` type. It is not important whether underlying id is represented by an integer, UUID or other format.

Note that internally `ID` values are represented as strings, they are serialized to JSON as strings. Because of that, underlying JVM based APIs that use integer identifiers produce an error, because JVM parsing is strict and by default it is unable to parse strings to integers. Such problem does not exist with .Net based APIs. Due to this reason entity identifiers in certain schema modules based on JVM APIs need to be converted to integer in pre-resolvers.

Fields representing identifiers of entities in external (non-Adform) systems, when such entities are not represented in Adform GraphQL schema, MAY use other types. For example, field `adGapId` for line items, which contains an identifier for third-party system.

### 3.6.3 Boolean fields MUST NOT have "is", "has", "does" or similar prefix

It is for consistency with [API guidelines](https://gitz.adform.com/pages/ADP/api-guidelines/#/payload?id=_67-boolean-must-be-represented-as-json-boolean-data-type-).

For example, `active`, `verified`.

Prefix MAY be used when lack of such would make field name unclear. For example, `hasSubdomains`.

## 3.7 Interfaces

Interface can only be used as output type. It cannot be used as parameter for query or mutation.

### 3.7.1 Interfaces SHOULD be used with caution

In Adform interfaces are not widely used. If there is a need or an idea for interface usage, it MUST be discussed and agreed with architects in advance.

## 3.8 Unions

Union can only be used as output type. It cannot be used as parameter for query or mutation.

### 3.8.1 Unions SHOULD be used with caution

In Adform unions are not widely used. If there is a need or an idea for union usage, it MUST be discussed and agreed with architects in advance.

## 3.9 Directives

Directives MAY be used for additional functionality. Directives can be of two types:
- schema (or type system) directives - they are applied in schema definition. For example, `@deprecated`, `@cacheControl`.
- query (or executable) directives - they are used by clients and are applied in queries. For example, `@include`, `@skip`.

### 3.9.1 Custom directives SHOULD be introduced with caution

In Adform custom directives are not widely used. If there is a need or an idea for a custom directive, it MUST be discussed and agreed with architects in advance.

### 3.9.2 Deprecated schema elements MUST be marked with @deprecated directive

Operations, their parameters, fields, enum values that should not be used anymore MUST be marked with `@deprecated` directive providing the reason for deprecation and alternatives to use.

## 3.10 Errors

Currently Adform returns errors in a separate untyped field `errors` which is not represented in GraphQL schema. This implementation is according to GraphQL specification and industry standarts, but this may be changed in the future.

### 3.10.1 Types for errors MUST NOT be defined in the schema

Currently errors are returned in untyped manner. If there is a need for typed errors, it MUST be discussed and agreed with architects in advance.
