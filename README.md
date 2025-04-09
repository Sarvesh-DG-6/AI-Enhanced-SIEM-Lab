# AI Module for Wazuh-Enhanced SIEM

This module uses Machine Learning (Isolation Forest) to detect anomalies in log data collected by Wazuh.

---

## 📦 Contents

- `train_model.py` – Train ML model
- `predict.py` – Detect anomalies from log data
- `process_wazuh_logs.py` – Convert Wazuh logs (alerts.json) into CSV
- `visualize_results.py` – Plot anomalies
- `test_dataset.csv` – Tentative dataset for testing
- `requirements.txt` – Required Python packages

---

## 🚀 Setup

```bash
pip install -r requirements.txt
