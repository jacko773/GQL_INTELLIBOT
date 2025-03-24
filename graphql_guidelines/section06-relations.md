# 6. Relations

Types and operations for different business entities are typically implemented in separate schema modules. Often, such entities are related and can be organised into graph where one entity can be accessed from other entity.

Consider types in following example where each type is defined in a separate schema module.

Campaigns module:
```graphql
type Campaign {
  id: ID!
  name: String!
  advertiserId: ID!
}

type Query {
  campaigns(advertiserId: ID!): CampaignList!
}
```

Advertisers module:
```graphql
type Advertiser {
  id: ID!
  name: String!
}

type Query {
  advertiser(id: ID!): Advertiser!
}
```

It is possible to define relations between these two types using `extend` keyword.

Campaign relations module:
```graphql
extend type Campaign {
  advertiser: Advertiser!
}
```

Advertiser relations module:
```graphql
extend type Advertiser {
  campaigns: CampaignList!
}
```

Object types are extended with additional fields that correspond to queries.

Then, it is necessary to provide information how to resolve these new fields. This is achieved by schema stitching configuration in relation module's `configuration.js` file.

As a result, a client is able to write queries such as:
```graphql
query campaignWithAdvertiser {
  campaign(id: $campaignId) {
    id
    name
    advertiser {
      id
      name
    }
  }
}
```

Such definition of relations (extended types with relation fields added) and schema stitching configuration are placed in relations modules.

## 6.1 Relation to parent entity SHOULD be added when introducing new type

It is quite common for a client to want to access direct entity's parent, thus such relations SHOULD be added when a type is introduced. Relations SHOULD be added in a separate relations module.

Example:
```graphql
extend type Order {
  campaign: Campaign!
}
```

## 6.2 Relation to child entities MAY be added when introducing new type

The need to access entity's child entities is less common. Relation to child entities MAY be added when introducing new type if it is known that client needs such relation.

Example:
```graphql
extend type Order {
  rtbLineItems: RtbLineItemList!
}
```

## 6.3 Other kinds of relations MAY be added when introducing new type

There can be a relation between entities other than parent-child. Such relation MAY be added when a real use case exists.

Example:
```graphql
extend type Targeting {
  country: Country
}
```

## 6.4 Relation is an extension of module whose type the relation extends

Relation field extends a type. Therefore:
- Relation module MUST be named as type's module with word `Relations` in it. For example, `campaignRelationsModule`.
- Owner of original type's module MUST own corresponding relation module.
- In source code relations module MUST be placed in the same directory as the module it extends.
