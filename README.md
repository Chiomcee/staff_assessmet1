# Patient Data JSON Exploration

## 📄 Overview

This project explores a JSON file that contains detailed **patient information**, including:

- Personal details
- Insurance information
- Emergency contact
- Medical history
- Appointment schedule
- Medical notes

---

## 🔑 Keys in the JSON Data

The JSON file contains **6 main keys**:

1. `patient`
2. `insurance`
3. `emergencyContact`
4. `medicalHistory`
5. `appointments`
6. `notes`

---

## 🏥 Insurance Details

The `insurance` key holds an object with the following information:

```json
{
  "provider": "Health Insurance Co.",
  "policyNumber": "HIC123456789",
  "coverageStart": "2020-01-01",
  "coverageEnd": "2025-01-01",
  "premium": 200.00,
  "deductible": 1000.00,
  "coPay": 20.00
}
```

---


## 🏷️ Insurance Provider

The **insurance provider** is: **Health Insurance Co.**

---

## 📂 Project Structure

staff_assessment1/
├── patient_data.json # JSON file with patient records
├── patient_data.py # Python script for data exploration
└── README.md # Project documentation (this file)