# 4. Operations

## 4.1 Queries

Queries are defined as fields in `type Query`.

### 4.1.1 Query SHOULD be named as noun

Queries return objects, thus quries SHOULD be named as noun. When query returns a single object its name SHOULD be a singular noun. For example, `campaign`. When query returns a list of objects, its name SHOULD be a plural noun. For example, `campaigns`.

When single object represents multiple values or corresponding noun has only plural form query name MAY be a noun in plural. For example, `settings`, `statistics`, `savings`.

### 4.1.2 The common type "FilterInput" SHOULD be used for filtering

`FilterInput` type provides a universal way to specify a field, an operation and values for filtering.
Filters parameter SHOULD be named `filters`.

Example:
```graphql
type Query {
  bankAccounts(filters: [FilterInput!]): BankAccountList!
}
```

### 4.1.3 Parameters representing matching entity properties MAY be used for filtering when query has limited filtering capabilities

When query implements filtering by matching only few entity properties they MAY be represented by individual parameters of matching type.

Example:
```graphql
type Query {
  bankAccounts(status: BankAccountStatus, ownerId: ID): BankAccountList!
}
```

### 4.1.4 Parameter for search string SHOULD be named "search"

If query has a parameter for a search string it SHOULD be named `search`.

Example:
```graphql
type Query {
  customers(search: String): CustomerList!
}
```

### 4.1.5 The common type "SortInput" MUST be used for sorting

`SortInput` type provides a universal way to specify a field and an order for sorting.
Sorting parameter SHOULD be named `sortBy`.

Example:
```graphql
type Query {
  bankAccounts(sortBy: [SortInput!]): BankAccountList!
}
```

### 4.1.6 The common type "PaginationInput" MUST be used for pagination

`PaginationInput` type provides a universal way to specify an offset and a limit for pagination.
Pagination parameter SHOULD be named `pagination`.

Example:
```graphql
type Query {
  bankAccounts(pagination: PaginationInput): BankAccountList!
}
```

### 4.1.7 Filtering, sorting and pagination parameters MUST be defined in this order

When querying entities first filtering is applied, then sorting and then pagination. This defines natural order of these parameters in the query.

Examples:
```graphql
type Query {
  bankAccounts(
    filters: [FilterInput!],
    sortBy: [SortInput!],
    pagination: PaginationInput): BankAccountList!
}
```

```graphql
type Query {
  bankAccounts(
    status: BankAccountStatus, ownerId: ID, search: String,
    sortBy: [SortInput!],
    pagination: PaginationInput): BankAccountList!
}
```

### 4.1.8 When module doesn't need a query it SHOULD define a "dummy" query

GraphQL pipeline requires a query to be defined in the module. In order to minimise such dummy queries in the composite schema an identical query SHOULD be used in all such modules. When module schemas are merged into the single composite schema GraphQL merges identical query definitions into single one.

Following dummy query SHOULD be used:
```graphql
type Query {
  dummy: String
}
```

## 4.2 Mutations

Mutations are defined as fields in `type Mutation`.

### 4.2.1 Mutation SHOULD be named as verb

Mutation name SHOULD be in the form `<verb><entity>` or `<verb><entity><field>`. `verb` MAY be `create`, `update`, `delete`, `set`, `upsert`, `add`, `remove`, etc.

For example, `createBankAccount`, `setBankAccountStatus`.

### 4.2.2 Mutation SHOULD return a resulting entity it created or mutated

When mutation creates or updates an entity it SHOULD return a resulting entity.

Example:
```graphql
type Mutation {
  createBankAccount(bankAccount: CreateBankAccountInput!): BankAccount!
  updateBankAccount(id: ID!, bankAccount: UpdateBankAccountInput!): BankAccount!
}
```

### 4.2.3 Mutation SHOULD return Void when it yields no result

When mutaton inherently doesn't return a value, for example, when underlying API returns no content, mutation SHOULD return custom scalar `Void`.

GraphQL does not allow mutation to return nothing because technically mutation is a field and a field must have its type.

Example:
```graphql
type Mutation {
  setBankAccountStatus(id: ID!, status: BankAccountStatus!): Void
  deleteBankAccount(id: ID!): Void
}
```

### 4.2.4 Mutation MAY return entity id

When returning full entity is not feasible or returning `Void` is not suitable, mutation MAY return identifier of affected entity.

### 4.2.5 Custom type "Upload" MUST be used in mutations that upload file

Custom type `Upload` provides support for file upload and MUST be used when file upload is needed. Custom resolver is needed for file upload. Returned type with uploaded file data is specific to a business domain.

Example:
```graphql
type Mutation {
  uploadTransactionsData(file: Upload!): TransactionsFile!
}
```

## 4.3 Subscriptions

Subscription allows client to get an event stream as a result of a particular operation. Upon execution of GraphQL subscription client establishes a channel through which events are delivered.
Subscriptions are defined as fields in `type Subscription`.

### 4.3.1 Architects MUST be consulted with before introducing new subscription

New subscriptions are rarely introduced in Adform GraphQL schema thus architects MUST be contacted before doing so.

### 4.3.2 Subscription MUST be used to get results of asynchronous operation

Instead of implementing query for polling results or other similar approach a GraphQL subscription MUST be used.

### 4.3.3 Operations that produce events to "entityEvent" subscription MUST have parameter named "subscriptionId"

Subscription `entityEvent` is most versatile and most widely used in Adform GraphQL schema. It is used to observe status of asynchronous long running entity based operations, such as creation or update of entities, including bulk updates, import, export.

Subscription `entityEvent` accepts parameter `operationEventId` that uniquely identifies subscription and is used for routing events to a particular client. Operations that produce entity events MUST have corresponding parameter that accepts the same subscription id and that parameter MUST be named `subscriptionId`, as this name better represents its meaning.

Parameter `subscriptionId` MUST be the first one in a mutation or a query.

Example:
```graphql
type Mutation {
  validateBankAccount(subscriptionId: ID!, id: ID!): ID!
}
```

## 4.4 Asynchronous operations

When operation by design takes considerable amount of time to complete it must be implemented as an asynchronous operation. Examples of such operations are import, export, creation of entities when result cannot be provided in real time, and so on.

### 4.4.1 Status and outcome of asynchronous operation MUST be provided via subscription

Asynchronous operation MUST accept parameter `subscriptionId` of type `ID`.

Asynchronous operation MUST provide its status and/or outcome as event(s) published to subscription stream with given `subscriptionId`.

Description of asynchronous operation in the schema MUST indicate which subscription it publishes events to.
