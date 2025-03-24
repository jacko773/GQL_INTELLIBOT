# 5. Documentation

GraphQL schema MUST be well documented.
Comments in GraphQL schema are implemented with block strings, i.e., strings wrapped in triple-quotes (`"""`), that appear immediately before the type, field, operation. These comments appear in schema explorer in GraphQL playground. Documentation supports markdown syntax.

## 5.1 Schema MUST have non-trivial documentation

Add descriptions that explain meaning and purpose of the type, field, operation. Avoid trivial descriptions that just repeat type or field name. Such trivial descriptions only clutter the source code.

## 5.2 Documentation SHOULD be compact

For short descriptions triple-quotes and string content SHOULD be on the same line. Otherwise it makes difficult to read the schema in source code.

## 5.3 Documentation MUST be adapted for GraphQL use

When documentation is copied from underlying API's Swagger it may contain text that makes little sense in GraphQL context. Such text MUST be adapted for GraphQL.

Bad example:
```graphql
type BankAccount {
  """ Gets or sets bank account name """
  name: String!
}
```

In above example comment that makes sense for .Net property doesn't make sense in GraphQL.
