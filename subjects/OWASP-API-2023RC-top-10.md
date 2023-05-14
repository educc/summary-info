# OWASP API TOP 10 2013

- [OWASP API TOP 10 2013](#owasp-api-top-10-2013)
- [1. Broken Object Level Authorization (BOLA)](#1-broken-object-level-authorization-bola)
- [2. Broken Authentication](#2-broken-authentication)
- [3. Broken Object Property Level Authorization](#3-broken-object-property-level-authorization)
- [4. Unrestricted Resource Consumption](#4-unrestricted-resource-consumption)
- [5. Broken Function Level Authorization](#5-broken-function-level-authorization)
- [6. Server-Side Request Forgery (SSRF)](#6-server-side-request-forgery-ssrf)
- [7. Security Misconfiguration](#7-security-misconfiguration)
- [8. Lack of Protection from Automated Threats](#8-lack-of-protection-from-automated-threats)
- [9. Improper Asset Management](#9-improper-asset-management)
- [10. Unsafe Consumption of APIs](#10-unsafe-consumption-of-apis)


# 1. Broken Object Level Authorization (BOLA)

* **What is this?**

BOLA is a vulnerability that allows attackers to access resources that they are not authorized to access. This can be exploited to steal data, modify data, or perform other unauthorized actions.

* **Attack Scenarios**

  * An attacker could use a SQL injection attack to gain access to sensitive data that is stored in a database.
  * An attacker could use a brute-force attack to guess a user's password.
  * An attacker could exploit a misconfigured firewall to gain access to an API.

* **How to Prevent**

  * Use strong authentication mechanisms, such as OAuth 2.0 or OpenID Connect.
  * Implement role-based access control (RBAC).
  * Use input validation to prevent SQL injection and other attacks.
  * Monitor your APIs for suspicious activity.

# 2. Broken Authentication

* **What is this?**

Broken authentication is a vulnerability that allows attackers to gain unauthorized access to APIs. This can be exploited to steal data, modify data, or perform other unauthorized actions.

* **Attack Scenarios**

  * An attacker could use a brute-force attack to guess a user's password.
  * An attacker could exploit a misconfigured password reset mechanism.
  * An attacker could exploit a session fixation attack.

* **How to Prevent**

  * Use strong passwords and password policies.
  * Implement two-factor authentication (2FA).
  * Use a secure password reset mechanism.
  * Use a session management framework.

# 3. Broken Object Property Level Authorization

* **What is this?**

Broken object property level authorization is a vulnerability that allows attackers to access sensitive properties of objects that they are not authorized to access. This can be exploited to steal data, modify data, or perform other unauthorized actions.

* **Attack Scenarios**

  * An attacker could use a SQL injection attack to gain access to sensitive data that is stored in a database.
  * An attacker could use a brute-force attack to guess a user's password.
  * An attacker could exploit a misconfigured firewall to gain access to an API.

* **How to Prevent**

  * Use strong authentication mechanisms, such as OAuth 2.0 or OpenID Connect.
  * Implement role-based access control (RBAC).
  * Use input validation to prevent SQL injection and other attacks.
  * Monitor your APIs for suspicious activity.

# 4. Unrestricted Resource Consumption

* **What is this?**

Unrestricted resource consumption is a vulnerability that allows attackers to consume an excessive amount of resources, such as CPU time, memory, or bandwidth. This can be exploited to deny service to legitimate users.

* **Attack Scenarios**

  * An attacker could use a denial-of-service (DoS) attack to overwhelm an API with requests.
  * An attacker could use a distributed denial-of-service (DDoS) attack to overwhelm an API with requests from multiple sources.
  * An attacker could use a resource exhaustion attack to consume all of the resources of an API, such as CPU time or memory.

* **How to Prevent**

  * Implement rate limiting to prevent attackers from consuming too many resources.
  * Use a load balancer to distribute traffic across multiple servers.
  * Monitor your APIs for suspicious activity.

# 5. Broken Function Level Authorization

* **What is this?**

Broken function level authorization is a vulnerability that allows attackers to call functions that they are not authorized to call. This can be exploited to steal data, modify data, or perform other unauthorized actions.

* **Attack Scenarios**

  * An attacker could use a SQL injection attack to gain access to sensitive data that is stored in a database.
  * An attacker could use a brute-force attack to guess a user's password.
  * An attacker could exploit a misconfigured firewall to gain access to an API.

* **How to Prevent**

  * Use strong authentication mechanisms, such as OAuth 2.0 or OpenID Connect.
  * Implement role-based access control (RBAC).
  * Use input validation to prevent SQL injection and other attacks.
  * Monitor your APIs for suspicious activity.

# 6. Server-Side Request Forgery (SSRF)

* **What is this?**

SSRF is a vulnerability that allows attackers to make requests to arbitrary URLs on the server that hosts the API. This can be exploited to steal data, modify data, or perform other unauthorized actions.

* **Attack Scenarios**

  * An attacker could use SSRF to make requests to internal systems that are not exposed to the public.
  * An attacker could use SSRF to make requests to systems that are not intended to be accessed by the public, such as systems that contain sensitive data.
  * An attacker could use SSRF to perform actions on behalf of a user, such as making a purchase or transferring money.

* **How to Prevent**

  * Validate all input before making requests to external systems.
  * Use a white list of allowed domains for requests.
  * Use a proxy server to make requests to external systems.

# 7. Security Misconfiguration

* **What is this?**

Security misconfiguration is a vulnerability that is caused by incorrect or incomplete security settings. This can be exploited by attackers to gain unauthorized access to systems or data.

* **Attack Scenarios**

  * An attacker could exploit a misconfigured firewall to gain access to a system.
  * An attacker could exploit a misconfigured web server to gain access to sensitive data.
  * An attacker could exploit a misconfigured database to gain access to sensitive data.

* **How to Prevent**

  * Use a security configuration management tool to manage security settings.
  * Use a security scanner to identify misconfigured security settings.
  * Follow security best practices.

# 8. Lack of Protection from Automated Threats

* **What is this?**

Lack of protection from automated threats is a vulnerability that is caused by not taking steps to protect systems from automated attacks. This can be exploited by attackers to launch large-scale attacks that can overwhelm systems and cause denial-of-service.

* **Attack Scenarios**

  * An attacker could use a denial-of-service (DoS) attack to overwhelm a system with requests.
  * An attacker could use a distributed denial-of-service (DDoS) attack to overwhelm a system with requests from multiple sources.
  * An attacker could use a brute-force attack to guess passwords or other sensitive data.

* **How to Prevent**

  * Use a firewall to block unwanted traffic.
  * Use a load balancer to distribute traffic across multiple servers.
  * Use a web application firewall (WAF) to block malicious traffic.
  * Implement rate limiting to prevent attackers from making too many requests.

# 9. Improper Asset Management

* **What is this?**

Improper asset management is a vulnerability that is caused by not properly managing sensitive assets, such as passwords, keys, and certificates. This can be exploited by attackers to gain unauthorized access to systems or data.

* **Attack Scenarios**

  * An attacker could steal a password or key and use it to gain unauthorized access to a system.
  * An attacker could steal a certificate and use it to impersonate a legitimate user.
  * An attacker could exploit a vulnerability in an asset management system to gain unauthorized access to assets.

* **How to Prevent**

  * Use strong passwords and keys.
  * Store passwords and keys in a secure location.
  * Use a certificate authority (CA) to issue and revoke certificates.
  * Implement asset management policies and procedures.

# 10. Unsafe Consumption of APIs

* **What is this?**

Unsafe consumption of APIs is a vulnerability that is caused by not using APIs safely. This can be exploited by attackers to gain unauthorized access to systems or data.

* **Attack Scenarios**

  * An attacker could use an API to make unauthorized requests to a system.
  * An attacker could use an API to inject malicious code into a system.
  * An attacker could use an API to exploit a vulnerability in a system.

* **How to Prevent**

  * Use APIs only for authorized purposes.
  * Validate all input before making requests to APIs.
  * Use a proxy server to make requests to APIs.
  * Implement API security policies and procedures.
