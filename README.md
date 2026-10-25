# CloudPilot — Intelligent Infrastructure Monitoring & Self-Healing

CloudPilot is an infrastructure monitoring and automated remediation project designed to monitor servers and containers, detect operational problems, generate alerts, and prepare controlled remediation actions.

The goal is to improve infrastructure reliability, reduce manual intervention, and provide better visibility into system health.

## Project Objectives

- Monitor server availability and infrastructure health.
- Track CPU, memory, and disk usage.
- Detect infrastructure failures and abnormal resource consumption.
- Generate alerts when predefined conditions are met.
- Centralize metrics and visualize monitoring data.
- Implement a Python-based remediation worker.
- Prepare controlled automated recovery actions.
- Explore future integration with Ansible and Kubernetes.

## Architecture

CloudPilot uses a monitoring stack based on Prometheus, Grafana, Alertmanager, Node Exporter, and Python.

```text
                 Infrastructure
                        |
             +----------+----------+
             |                     |
        Node Exporter 1       Node Exporter 2
             |                     |
             +----------+----------+
                        |
                    Prometheus
                        |
             +----------+----------+
             |                     |
          Grafana              Alertmanager
          Dashboards              |
                                  v
                         Remediation Worker
                              (Python)
                                  |
                         Controlled Actions
```

*The diagram represents the intended workflow. The exact alert-to-remediation integration depends on the current configuration.*

## Technology Stack

| Technology | Purpose |
|---|---|
| Docker & Docker Compose | Containerization and service orchestration |
| Prometheus | Metrics collection and monitoring |
| Grafana | Monitoring dashboards and visualization |
| Alertmanager | Alert management |
| Node Exporter | Server metrics collection |
| Python | Remediation worker and automation logic |
| Git & GitHub | Version control |
| Ansible | Planned infrastructure automation |
| Kubernetes | Potential future extension |

## Project Structure

```text
CloudPilot/
├── docker-compose.yml
├── .gitignore
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.yml
├── alertmanager/
│   └── alertmanager.yml
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── prometheus.yml
└── remediation/
    └── worker.py
```

## Getting Started

### Prerequisites

- Windows with Docker Desktop installed and running.
- Docker Engine and Docker Compose.
- Git.
- Python for local development of the remediation worker, if needed.

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CloudPilot
```

Replace the placeholder with the actual repository URL.

### 2. Start the infrastructure

From the project directory, run:

```powershell
docker compose up -d
```

### 3. Check running containers

```powershell
docker compose ps
```

### 4. View service logs

```powershell
docker compose logs -f
```

To inspect a specific service:

```powershell
docker compose logs -f remediation-worker
```

### 5. Stop the infrastructure

```powershell
docker compose down
```

## Monitoring and Alerts

CloudPilot currently includes Prometheus monitoring and alert rules for:

- `ServerExporterDown`: detects when a monitored Node Exporter becomes unavailable.
- `HighCPUUsage`: detects high CPU usage according to the configured threshold.

Prometheus collects metrics and evaluates the configured rules. Alertmanager is included for alert handling.

## Remediation Worker

The project includes a Python remediation worker exposed on port `5001`.

Its purpose is to provide a foundation for controlled infrastructure recovery actions in response to monitoring events.

The next development steps include:

- Validating incoming alerts.
- Defining permitted remediation actions.
- Adding execution logging.
- Implementing safeguards against repeated or unsafe actions.
- Testing the complete alert-to-remediation workflow.

## Current Project Status

**Implemented**
- Docker Compose monitoring environment.
- Prometheus, Grafana, Alertmanager and two Node Exporters.
- Prometheus configuration and alert rules.
- Grafana Prometheus datasource provisioning.
- Python remediation worker.
- Successful startup of the monitoring services.
- Prometheus targets verified as UP after testing.
- Alert rules loaded by Prometheus.

**Next Steps**
1. Verify the complete Alertmanager configuration.
2. Connect Prometheus alerts to the remediation worker.
3. Test alert reception and handling.
4. Implement and test safe remediation actions.
5. Improve Grafana dashboards.
6. Add automated tests and execution logs.
7. Document deployment and operational security.
8. Explore Ansible integration and Kubernetes support.

## Security Considerations

CloudPilot is a development project. Before production deployment:

- Restrict access to monitoring interfaces and APIs.
- Avoid exposing management endpoints publicly.
- Validate all incoming alert payloads.
- Limit remediation actions to an explicit allowlist.
- Store credentials outside the source code.
- Log remediation attempts and their results.
- Test recovery actions in an isolated environment.

## Project Vision

CloudPilot aims to evolve into an intelligent infrastructure operations platform combining monitoring, alerting, automation, and controlled self-healing capabilities.

The long-term objective is to reduce downtime and simplify infrastructure management through observable, testable, and secure automation.
