# Modules in the service catalog

It is crucial to provide ownership information for modules. Every module has to be registered as a service in [SIT](https://sit.adform.zone/services/services/all) and a correct owning team has to be indicated.

Below are the guidelines for registering a service for a module.

## Project specific modules

Modules in different AAP projects have different requirements for corresponding service in SIT. These requirements are listed below.

### Schema Module Catalog module

A service for a module must be registered in SIT under the product/scope that represents module's domain area.

Service category must be `GraphQL Schema Module`, technology must be `GraphQL`. Service title must derive from module name in Schema Module Catalog and end with `-SCHEMA-MODULE`.

Example service titles: `CAMPAIGNS-SCHEMA-MODULE`, `DIRECT-LINE-ITEM-FEES-INPUT-MODE-SCHEMA-MODULE`.

### Schema Module Catalog relations module

A service must be registered in SIT for module under the product/scope that represents domain area of the type that the module extends with relation.

Service category must be `GraphQL Schema Module`, technology must be `GraphQL`. Service title must derive from module name in Schema Module Catalog and end with `-RELATIONS-MODULE`.

Example service titles: `RTB-LINE-ITEM-RELATIONS-MODULE`, `AGENCY-ENTITY-LIST-RELATIONS-MODULE`.

### Bulk Service module

A service for a module must be registered in SIT under the product/scope that represents module's domain area.

Service category must be `GraphQL Bulk Module`, technology must be `Node.JS`. Service title must derive from module name in Bulk Service and end with `-BULK-MODULE`.

Example service titles: `ORDER-BULK-MODULE`, `RTB-TARGETING-LIST-DOMAINS-REMOVE-BULK-MODULE`.

### Listener Platform module

A service for a module must be registered in SIT under the product/scope that represents module's domain area.

Service category must be `AAP Listener Module`, technology must be `Node.JS`. Service title must derive from module name in Listener Platform and end with `-LISTENER-MODULE`.

Example service titles: `CIAM-NOTIFICATION-LISTENER-MODULE`, `ENTITY-EXPORT-NOTIFICATION-LISTENER-MODULE`.

### AAP Middleware Server module

A service for a module must be registered in SIT under `AAP-MIDDLEWARE-SERVER` product/scope.

Service category must be `GraphQL Schema Module`, technology must be `GraphQL`. Service title must derive from module name in AAP Middleware Server and end with `-SCHEMA-MODULE`.

Example service titles: `AUTH-OPERATIONS-SCHEMA-MODULE`, `SUBSCRIPTIONS-SCHEMA-MODULE`.

## URLs and dependencies

URL to module's directory in git respository in its primary branch must be provided for a service in SIT. Its kind must be `Code`.

URL to the latest module's external review page must be provided for a service in SIT. Its kind must be `Other`, title must be `Review`.

A project the module is a part of must be listed as "depends on" for module's service in SIT.
