# Enterprise Security Audit & Compliance Platform (Flask Demo)

Minimal, modular starter showing authentication with MFA, RBAC, basic auditing, encryption helper, and stubbed security features you can extend.

## Quick start
- Install Python 3.10+.
- `python -m venv .venv && .venv\\Scripts\\activate` (Windows) or `source .venv/bin/activate` (Unix).
- `pip install -r requirements.txt`
- `flask --app run run` then open http://127.0.0.1:5000

Default admin seed: email `admin@example.com`, password `Admin@123`.

## Features included
- User register/login with bcrypt hashing, email-style OTP MFA (console print), session management via Flask-Login.
- RBAC with `admin` and `user` roles and a `role_required` decorator.
- Audit log writes on auth and sensitive actions.
- Simple firewall rule simulator endpoint.
- File/content encryption helper with Fernet (AES-128 GCM).
- Stubs for vulnerability scan, DLP policy checks, phishing/spam checks to extend.

## Next steps
- Replace console OTP with real email/SMS provider.
- Swap SQLite for MySQL by updating `SQLALCHEMY_DATABASE_URI` in `app/config.py`.
- Add real scanners (e.g., bandit, zap) and telemetry exporters.

