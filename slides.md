# Enterprise Security Audit & Compliance Platform
- Flask + HTML/CSS/JS | SQLite (MySQL-ready)
- Auth + MFA, RBAC, Encryption, DLP, Firewall Sim, Audit
- Demo admin: admin@example.com / Admin@123

---

## Problem & Goals
- Fragmented tools → blind spots, weak compliance
- Need unified view: strong auth, data protection, monitoring, education
- Goals: centralize controls; protect data in transit/at rest; audit for compliance

---

## Architecture
- Frontend: HTML/CSS/JS (multi-page UI)
- Backend: Flask, SQLAlchemy, Flask-Login, Flask-Migrate
- Security: bcrypt (passwords), Fernet (AES-GCM), OTP (EmailJS/console)
- DB: SQLite dev; swap to MySQL via `SQLALCHEMY_DATABASE_URI`
- Modules: Auth/MFA, RBAC, Encryption, DLP, Firewall sim, Audit logs

---

## Authentication & MFA
- Login + bcrypt hashing; sessions via Flask-Login
- MFA OTP via EmailJS if configured; UI shows demo OTP fallback
- Seeds admin for bootstrap access

---

## RBAC & Access Control
- Roles: admin, user
- Decorators enforce admin-only (firewall, audit)
- Nav hides admin sections for non-admin
- Audit log captures auth + sensitive actions

---

## Data Protection (Encryption)
- Text encrypt/decrypt via Fernet (AES-GCM)
- File encryption endpoint returns `.enc`
- UI page for encrypt/decrypt with generated key
- Deploy with TLS for transport security

---

## DLP & Threat Simulation
- DLP regex policies; `/dlp/check` flags/blocks content
- Firewall simulator: allow/deny by source/dest/port/proto
- Stubs for vuln scan, phishing/spam awareness (extendable)

---

## Monitoring & Audit
- Audit logs for login, MFA, encryption, DLP, firewall tests
- Admin UI: view last 50 events
- Request logging: method/path/status/ip/duration/user

---

## Roadmap & Deployment
- Roadmap: CSRF + form validation; rule/policy CRUD UI; real email/SMS OTP; tests/CI; containerization; MySQL prod config
- Env vars: SECRET_KEY, DATABASE_URL, ENCRYPTION_KEY, EMAILJS_SERVICE_ID/TEMPLATE_ID/PUBLIC_KEY/PRIVATE_KEY
- Run: `python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt && flask --app run run`

