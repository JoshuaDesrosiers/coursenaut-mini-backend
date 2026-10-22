## Coursenaut reimagined

> Github repo dedicated to redifining Coursenaut with a proper scope

### What is Coursenaut?

At its core Coursenaut is an AI accelerated platform that can be used to generate courses, or as a digital classroom space.

> Coursenaut currently looks like this:

| Category | Component | Details |
|---|---|---|
| Language | TypeScript | Node 20+, ES modules, compiled with `tsc` |
| Framework | Express 4 | REST API, `helmet`, `express-rate-limit`, `zod` validation |
| Hosting | Google Cloud Run | Service `coursenaut-api`, region `us-central1`, stateless container, scales to zero |
| Secrets | GCP Secret Manager | Gemini, Stripe, and webhook keys |
| Scheduled jobs | Cloud Scheduler | Calls `/internal` endpoints using a shared-secret check |
| Database | Firestore | Orgs, users, courses (modules embedded), enrollments, submissions, AppLabs, rubrics, certificates, focus sessions, credit balances, kill switch |
| Auth | Firebase Auth | Custom claims: `role` (`org_admin` / `student`) + `orgId` |
| App verification | Firebase App Check | Confirms requests come from the real app |
| File storage | Firebase Storage | Uploaded files |
| AI (primary) | Gemini (`@google/genai`) | Course and AppLab generation, AI grading, chat; model chosen per org |
| AI (optional) | Grok (xAI) | Second provider, active only if `XAI_API_KEY` is set |
| Payments | Stripe | Subscriptions and AI credit purchases |
| Email | Resend | Outbound email and inbound email via webhook (`svix` signatures) |
| Images | Pexels API | Image search for course content |
| PDFs | `pdf-lib` | Certificate and course PDF generation |
| External AI integration | MCP server (`@modelcontextprotocol/sdk`) | Lets orgs connect Claude, Cursor, etc. to author courses, with per-org API keys |


The problem with coursenaut as of now, market wise, is that it competes with digital classroom tools, and AI course generators, both pretty saturated departments! Coursenaut focuses on two big existing pieces and frankly doesn't deliver on either of them well!

`What if we can narrow the scope?`
`what if instead of fighting digital classrooms we work with them?`

The problem with Coursenaut, architecture wise, is that while the site promises analytics, using a document & collection-based database limits the analytics we can pull and can be costly.

`what if we switch to an SQL based database to deliver on our promise?`
`could switching to SQL enhance our devops page by giving us more meaningful analytics to pull from?`

> What if we can get Coursenaut to look like this:

| Category | Component | Technical Details |
|---|---|---|
| **Language & Environment** | Python 3.11+ | Type hints, `venv`, modular package structure |
| **Framework & Web Stack** | Flask | App Factory pattern, Blueprints for modular routes |
| **Production Server** | Gunicorn | High-performance container WSGI server |
| **Hosting & Infrastructure** | Google Cloud Run | Stateless container, auto-scaling, scale-to-zero |
| **Database** | PostgreSQL (GCP Cloud SQL) | Relational modeling for assignments, submissions, retries |
| **Database ORM** | Flask-SQLAlchemy | ORM, strict foreign keys, cascade deletes, transactions |
| **Database Migrations** | Flask-Migrate (Alembic) | Version-controlled schema migrations |
| **AI Generation Engine** | Gemini API (`google-genai`) | AI pipeline for AppLab steps and grading rubrics |
| **LMS Integration** | Google Classroom API | Syncs assignments and auto-pushes student grades |
| **Testing & Rigor** | pytest | Automated unit testing with in-memory SQLite fixtures |
| **Configuration** | `python-dotenv` & GCP Secrets | 12-Factor App config and environment variable injection |
| **Containerization** | Docker | Environment parity via lightweight containerization |

In this repo you will find the redefined backend for Coursenaut in a first attempt to address the overshooting and underperformance of some features.
