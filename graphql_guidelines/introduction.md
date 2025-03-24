# How to use this documentation

Numbered pages contain the requirements where each requirement is in its numbered section. These numbered requirements must be implemented by developer and checked by reviewer.

It is highly recommended to read all requirements while your GraphQL schema is in design stage, before actual development.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) [[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)] [[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)] when, and only when, they appear in all capitals, as shown here.

# GraphQL schema

Adform composite GraphQL schema provides a contract for Adform business entities, their relations, operations. It consists of multiple domain specific schemas merged into a single one. All types and operations from multiple modules reside in a single namespace.

The composite schema should be consistent across its schema modules, consistent with [Business Entity Model](https://gitz.adform.com/adform/business-entity-foundation), with [DDP contracts](https://gitz.adform.com/ddp/contracts).

Entire composite schema is exposed via a single endpoint by [AAP Middleware Server (MS)](https://gitz.adform.com/AAP/AAP-middleware-server). Middleware Server combines schemas from multiple services such as:
  - [Schema Server](https://gitz.adform.com/AAP/AAP-schema-server)
  - [Bulk Service](https://gitz.adform.com/AAP/AAP-bulk-service)
  - [Notification Server](https://gitz.adform.com/AAP/AAP-listener-platform/tree/develop/packages/graphql/aap-notification-server)
  - [Configuration Service](https://gitz.adform.com/AAP/AAP-configuration-service)
  - [Recents Service](https://gitz.adform.com/AAP/AAP-recents-service)
  - [Favorites Service](https://gitz.adform.com/AAP/AAP-favorites-service)
  - [Product Updates Service](https://gitz.adform.com/AAP/AAP-product-updates-service)
  - and [other](https://gitz.adform.com/AAP/AAP-middleware-server/blob/develop/config/prod.js).

AAP Schema Server (SS) in its turn merges schema modules from [AAP Schema Module Catalog (SMC)](https://gitz.adform.com/AAP/AAP-schema-module-catalog), where modules implement GraphQL contracts over Adform APIs.

These guidelines describe requirements and best practices for GraphQL schemas in order to have homogeneous consistent composite GraphQL schema for easy and smooth consumption and further development.

These guidelines apply to all schema modules that are part of the composite schema.

Visit following resources for learning material about GraphQL:
  - https://graphql.org/learn
  - https://www.howtographql.com
  - https://www.apollographql.com/tutorials
  - https://principledgraphql.com

# How to contribute

Initiate a discussion in a *#graphql-committee* Slack channel or in guidelines github [repository](https://gitz.adform.com/AAP/graphql-guidelines/discussions). After reaching a general consensus create a pull request with proposed changes, share pull request link in the discussion. Pull request must be approved and merged by the architect.
