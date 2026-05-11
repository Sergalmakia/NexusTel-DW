# NexusTel DW
### Automated Telecom Data Warehouse & Analytics System

> Transforming telecom data into actionable insights.

---

## 📌 Overview

NexusTel DW is a telecom data warehouse and analytics platform designed to centralize customer, billing, payment, and network usage data into a unified warehouse architecture for business intelligence and strategic decision-making.

The system integrates multiple telecom-related data sources using ETL pipelines built with Pentaho Data Integration (PDI), applies data quality management processes, supports historical tracking through Slowly Changing Dimensions (SCD Type 2), and delivers interactive analytics dashboards using Power BI.

---

## 🎯 Project Objectives

The primary objectives of NexusTel DW are to:

- Centralize telecom data from multiple operational systems
- Improve reporting and analytics capabilities
- Monitor telecom KPIs and revenue trends
- Analyze customer behavior and service usage
- Support strategic and operational decision-making
- Implement data quality controls during ETL processing
- Enable historical trend analysis over time

---

## 🏗️ System Architecture

The system follows a layered data warehouse architecture:

```text
Data Sources
   ↓
Staging Layer
   ↓
ETL & Data Quality Processing
   ↓
Data Warehouse (Star Schema)
   ↓
Power BI Dashboards & Analytics