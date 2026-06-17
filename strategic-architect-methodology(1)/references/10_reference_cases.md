# IIOS Reference Cases v1.0
## 10 vollständig ausgearbeitete Praxisfälle

---

## Überblick

Diese 10 Referenzfälle demonstrieren die vollständige Anwendung der IIOS Methodik auf reale Probleme. Jeder Fall zeigt:

```
Problem → Analyse → Bewertung → Governance Review → Entscheidung → Dokumentation → Visualisierung → Audit
```

---

## Fall 1: Krankenhaus-Patientendaten-Management (Unternehmen)

### Problemstellung
Ein 800-Betten-Krankenhaus muss sein Patientendaten-Management-System modernisieren. 50.000 Patientenakten, sensible Gesundheitsdaten, Compliance mit HIPAA und DSGVO erforderlich.

### Analyse

**~1000 Details:**
- Alte Papierakten (30%)
- Verschiedene IT-Systeme (25%)
- Mitarbeiter-Workflows (20%)
- Compliance-Anforderungen (15%)
- Integration mit Laboren/Pharmazie (10%)

**~100 Prinzipien:**
- Datenintegrität, Zugriffskontrolle, Audit-Trails
- Patientenautonomie, Einwilligungsmanagement
- Notfallzugriff, Datenminimalisierung

**~10 Kernprinzipien:**
- Schutz der Patientenwürde (Eckstein: Barmherzigkeit)
- Medizinische Datenintegrität (Maßstab: Wahrheit)
- Gesetzliche Compliance (Ordnung: Recht)
- System-Sicherheit (Fundament: Sicherheit)
- Langzeitarchivierung (Fundament: Nachhaltigkeit)
- Medizinischer Fortschritt (Ziel: Entwicklung)

**Eckstein:** Barmherzigkeit
> "Barmherzigkeit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."

### Bewertung (IGOS Scorecard)

| Score | Wert | Begründung |
|-------|------|------------|
| Cornerstone Score | 94/100 | Starker Patientenschutz, Verhältnismäßigkeit beachtet |
| Integrity Score | 91/100 | Hash-Validierung, ACID-Compliance |
| Compliance Score | 96/100 | HIPAA, DSGVO, ISO 27001 |
| Risk Score | 88/100 | TDE, Multi-Faktor, Redundanz |
| Governance Score | 85/100 | Klare Rollen, Trainings |
| Development Score | 82/100 | Innovation: KI-gestützte Diagnoseunterstützung |

**IGOS Gesamtscore: 90.4/100 → GOLD**

### Governance Review

**Rollen:**
- Cornerstone Steward: Chefarzt Ethik-Kommission
- Governance Officer: Datenschutzbeauftragter
- Technical Architect: IT-Direktor
- Compliance Auditor: Externer HIPAA-Auditor
- Certification Reviewer: Krankenhausleitung

**Entscheidungsprozess:**
1. Ethik-Kommission prüft Patientenschutz
2. Datenschutz prüft DSGVO-Konformität
3. IT implementiert technische Maßnahmen
4. Externer Auditor validiert HIPAA
5. Leitung genehmigt Gold-Zertifizierung

### Entscheidung
**Zertifizierung:** GOLD
**System:** PostgreSQL mit TDE, FHIR-API, Blockchain-Audit-Trail
**Pflichtfeld-Validierung:** ✓ Jede Komponente begründet Patientenschutz

### Dokumentation
- IIOS Constitution (Patientenwürde als Eckstein)
- Technical Spec (FHIR-Architektur)
- Governance Standard (Klinik-Prozesse)
- IGOS Scorecard (90.4/100)

### Visualisierung
- Radar-Chart: Cornerstone Score 94 (höchster Wert)
- Trend: Steigend von 75 (Bronze) auf 90.4 (Gold)

### Audit
**Externer HIPAA-Audit:** Bestanden
**Re-Zertifizierung:** Halbjährlich

---

## Fall 2: Bürgerportal einer Stadtverwaltung (Behörde)

### Problemstellung
Eine 500.000-Einwohner-Stadt entwickelt ein digitales Bürgerportal. 200+ Services, verschiedene Ämter, hohe Barrierefreiheitsanforderungen.

### Analyse

**~1000 Details:**
- 15 Fachämter mit eigenen Systemen
- 50+ Antragsarten
- Identitätsmanagement (eID)
- Barrierefreiheit (WCAG 2.1 AAA)

**~100 Prinzipien:**
- Zugänglichkeit, Transparenz, Gleichbehandlung
- Datenschutz, Bürgerautonomie
- Effizienz, Service-Qualität

**~10 Kernprinzipien:**
- Gleichbehandlung aller Bürger (Eckstein: Gerechtigkeit)
- Transparente Verwaltung (Maßstab: Wahrheit)
- Rechtsstaatlichkeit (Ordnung: Recht)
- Datensicherheit (Fundament: Sicherheit)
- Langfristige Verfügbarkeit (Fundament: Nachhaltigkeit)
- Verwaltungsmodernisierung (Ziel: Entwicklung)

**Eckstein:** Gerechtigkeit
> "Gerechtigkeit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."

### Bewertung

| Score | Wert | Begründung |
|-------|------|------------|
| Cornerstone Score | 89/100 | Gleichbehandlung, Zugänglichkeit |
| Integrity Score | 87/100 | Transparente Prozesse |
| Compliance Score | 92/100 | DSGVO, SGB, WCAG 2.1 AAA |
| Risk Score | 85/100 | eIDAS, BSI-Grundschutz |
| Governance Score | 88/100 | Klare Amtsstrukturen |
| Development Score | 84/100 | Moderne UX, AI-Chatbot |

**IGOS Gesamtscore: 87.6/100 → SILVER**

### Governance Review
**Besonderheit:** Öffentlicher Sektor mit politischer Aufsicht

**Zertifizierung:** SILVER
**System:** Microservices, Kubernetes, API-Gateway, eIDAS-Integration

---

## Fall 3: Autonomes Fahrzeug-Entscheidungssystem (KI-System)

### Problemstellung
Hersteller entwickelt KI für autonome Fahrzeuge. Ethik-Dilemma: Notbremsung-Algorithmus muss unter Zeitdruck Entscheidungen treffen.

### Analyse

**~1000 Details:**
- Sensor-Fusion (Lidar, Kamera, Radar)
- Objekterkennung (Pedestrian, Fahrrad, Auto)
- Trajektorien-Planung
- Notfallprotokolle

**~100 Prinzipien:**
- Lebensschutz, Minimierung von Verletzungen
- Verhältnismäßigkeit, Vorhersehbarkeit
- Transparenz der Entscheidung

**~10 Kernprinzipien:**
- Menschenleben hat Priorität (Eckstein: Menschenwürde)
- Präzise Situationsanalyse (Maßstab: Wahrheit)
- Gesetzeskonformität (Ordnung: Recht)
- Systemsicherheit (Fundament: Sicherheit)
- Algorithmus-Stabilität (Fundament: Nachhaltigkeit)
- KI-Fortschritt (Ziel: Entwicklung)

**Eckstein:** Menschenwürde
> "Menschenwürde ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."

### Bewertung

| Score | Wert | Begründung |
|-------|------|------------|
| Cornerstone Score | 96/100 | Lebensschutz-Priorisierung |
| Integrity Score | 88/100 | Sensor-Validierung |
| Compliance Score | 85/100 | UN-R79, StVZO |
| Risk Score | 90/100 | Redundante Systeme |
| Governance Score | 82/100 | Ethik-Beirat |
| Development Score | 91/100 | Cutting-Edge KI |

**IGOS Gesamtscore: 88.7/100 → SILVER**

### Besonderheit: Trolley-Problem-Dokumentation
**Pflichtfeld-Validierung:**
```
Der Algorithmus priorisiert Menschenleben über Sachschäden.
Bei unvermeidbarer Kollision: Zufällige Auswahl (keine Diskriminierung).
Entscheidung ist dokumentiert und nachvollziehbar.
```

---

## Fall 4: Kryptowährungs-Exchange (Finanzsystem)

### Problemstellung
Neue Exchange für 1M+ Nutzer. Hohe Sicherheitsanforderungen, regulatorische Unsicherheit, schnelle Transaktionen.

### Analyse

**~1000 Details:**
- Cold/Hot Wallet-Architektur
- Order-Matching-Engine
- KYC/AML-Prozesse
- Multi-Sig-Sicherheit

**~100 Prinzipien:**
- Fonds-Sicherheit, Transaktionsintegrität
- Regulatorische Agilität, Nutzertransparenz
- Liquiditätsmanagement

**~10 Kernprinzipien:**
- Vertrauen durch Sicherheit (Eckstein: Sicherheit)
- Unverfälschte Transaktionen (Maßstab: Wahrheit)
- Regulatorische Compliance (Ordnung: Recht)
- Systemsicherheit (Fundament: Sicherheit)
- Langfristige Stabilität (Fundament: Nachhaltigkeit)
- Finanz-Innovation (Ziel: Entwicklung)

**Eckstein:** Sicherheit
> "Sicherheit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."

### Bewertung

| Score | Wert | Begründung |
|-------|------|------------|
| Cornerstone Score | 93/100 | 98% Cold Storage, Multi-Sig |
| Integrity Score | 94/100 | Blockchain-Verifizierung |
| Compliance Score | 78/100 | MiCA im Implementierung |
| Risk Score | 95/100 | HSM, Insurance, Bug Bounty |
| Governance Score | 81/100 | Treasury-Management |
| Development Score | 89/100 | DeFi-Integration |

**IGOS Gesamtscore: 86.7/100 → SILVER**

---

## Fall 5: Smart City Energienetz (Infrastrukturprojekt)

### Problemstellung
Stadt baut Smart Grid für 100.000 Haushalte. Integration erneuerbarer Energien, Echtzeit-Optimierung, Cybersecurity.

### Analyse

**~1000 Details:**
- Smart Meter (100k+ Endpunkte)
- Lastmanagement, Peak-Shaving
- Erneuerbare Integration (Solar, Wind)
- SCADA-Sicherheit

**~100 Prinzipien:**
- Nachhaltigkeit, Energieeffizienz
- Netzstabilität, Cyber-Resilienz
- Verbraucherautonomie

**~10 Kernprinzipien:**
- Nachhaltige Energie (Eckstein: Nachhaltigkeit)
- Präzise Lastprognose (Maßstab: Wahrheit)
- Regulatorische Einbindung (Ordnung: Recht)
- Kritische Infrastruktursicherheit (Fundament: Sicherheit)
- Langfristige Planung (Fundament: Nachhaltigkeit)
- Energiewende (Ziel: Entwicklung)

**Eckstein:** Nachhaltigkeit
> "Nachhaltigkeit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."

### Bewertung

| Score | Wert | Begründung |
|-------|------|------------|
| Cornerstone Score | 92/100 | 60% erneuerbar, CO2-Reduktion |
| Integrity Score | 89/100 | Smart Meter Accuracy |
| Compliance Score | 86/100 | BNetzA, BSI-KritisV |
| Risk Score | 91/100 | Air-Gapped SCADA |
| Governance Score | 84/100 | Stadtwerke-Struktur |
| Development Score | 90/100 | AI-Optimierung |

**IGOS Gesamtscore: 88.6/100 → SILVER**

---

## Fall 6: E-Learning-Plattform (Bildung)

### Problemstellung
Universität mit 50.000 Studenten braucht moderne Lernplattform. Personalisierung, Prüfungsintegrität, Barrierefreiheit.

### Analyse

**~1000 Details:**
- 5000 Kurse, 50.000 Nutzer
- Proctoring für Prüfungen
- Adaptive Lernpfade
- Accessibility (Screenreader)

**~100 Prinzipien:**
- Chancengleichheit, Bildungszugang
- Prüfungsgerechtigkeit, Lernfortschritt
- Datenschutz junger Erwachsener

**~10 Kernprinzipien:**
- Bildungsgerechtigkeit (Eckstein: Gerechtigkeit)
- Wissensvermittlung (Maßstab: Wahrheit)
- Prüfungsordnungen (Ordnung: Recht)
- Plattformsicherheit (Fundament: Sicherheit)
- Langfristige Archivierung (Fundament: Nachhaltigkeit)
- Pädagogische Innovation (Ziel: Entwicklung)

**Eckstein:** Gerechtigkeit

### Bewertung

| Score | Wert |
|-------|------|
| Cornerstone Score | 87/100 |
| Integrity Score | 90/100 |
| Compliance Score | 88/100 |
| Risk Score | 82/100 |
| Governance Score | 85/100 |
| Development Score | 86/100 |

**IGOS Gesamtscore: 86.5/100 → SILVER**

---

## Fall 7: Luftfracht-Logistiksystem (Supply Chain)

### Problemstellung
Frachtfluggesellschaft optimiert Frachtraum-Nutzung in 100+ Flugzeugen. Echtzeit-Tracking, Zoll-Integration, Temperaturkontrolle.

### Analyse

**~1000 Details:**
- 50.000 Shipments/Tag
- IoT-Sensoren (Temperatur, Schock)
- Zoll-Dokumentation (automated)
- ULD-Optimierung

**~100 Prinzipien:**
- Sendungsintegrität, Transparenz
- Regulatorische Compliance
- Effizienz, Nachvollziehbarkeit

**~10 Kernprinzipien:**
- Zuverlässigkeit (Eckstein: Zuverlässigkeit)
- Tracking-Genauigkeit (Maßstab: Wahrheit)
- Zollkonformität (Ordnung: Recht)
- Frachtsicherheit (Fundament: Sicherheit)
- System-Stabilität (Fundament: Nachhaltigkeit)
- Logistik-Innovation (Ziel: Entwicklung)

**Eckstein:** Zuverlässigkeit
> "Zuverlässigkeit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."

### Bewertung

| Score | Wert |
|-------|------|
| Cornerstone Score | 91/100 |
| Integrity Score | 93/100 |
| Compliance Score | 89/100 |
| Risk Score | 87/100 |
| Governance Score | 83/100 |
| Development Score | 85/100 |

**IGOS Gesamtscore: 88.3/100 → SILVER**

---

## Fall 8: Gesichtserkennung im öffentlichen Raum (Überwachung)

### Problemstellung
Stadt plant Gesichtserkennung zur Verbrechensbekämpfung. Hohe Datenschutz-Bedenken, öffentliche Debatte.

### Analyse

**~1000 Details:**
- 500 Kameras in öffentlichen Bereichen
- Echtzeit-Erkennung
- Datenretention-Politik
- Fehlerrate/Bias

**~100 Prinzipien:**
- Datenschutz, Verhältnismäßigkeit
- Transparenz, Bürgerbeteiligung
- Sicherheit vs. Freiheit

**~10 Kernprinzipien:**
- Verhältnismäßigkeit (Eckstein: Barmherzigkeit)
- Akkurate Erkennung (Maßstab: Wahrheit)
- Rechtskonformität (Ordnung: Recht)
- Daten-Sicherheit (Fundament: Sicherheit)
- Langfristige Auswirkungen (Fundament: Nachhaltigkeit)
- Balance Sicherheit/Freiheit (Ziel: Entwicklung)

**Eckstein:** Barmherzigkeit (mit strikten Auflagen)

### Bewertung

| Score | Wert | Anmerkung |
|-------|------|-----------|
| Cornerstone Score | 72/100 | Nur mit Auflagen akzeptabel |
| Integrity Score | 81/100 | 99.2% Accuracy |
| Compliance Score | 85/100 | DSGVO, BVerfG |
| Risk Score | 78/100 | Missbrauchspotenzial |
| Governance Score | 76/100 | Bürgerbeirat |
| Development Score | 68/100 | Ethisch bedenklich |

**IGOS Gesamtscore: 76.5/100 → BRONZE**

### Besonderheit: Kritische Eckstein-Bewertung
**Pflichtfeld:**
```
Eckstein-Validierung: Kritisch. System berührt fundamentale Rechte.
Auflagen:
- Keine Echtzeit-Speicherung
- 30-Tage-Löschung
- Keine automatische Polizei-Alerts
- Jährliche öffentliche Evaluation
Zertifizierung: BRONZE (maximal erreichbar für Überwachungssysteme)
```

---

## Fall 9: Cloud-Native Banking-App (Fintech)

### Problemstellung
Neobank mit 2M Kunden migriert zu cloud-native. Microservices, Zero-Trust, 99.99% SLA.

### Analyse

**~1000 Details:**
- 50 Microservices
- Event-Sourcing, CQRS
- PSD2, KYC, AML
- Multi-Region, Active-Active

**~100 Prinzipien:**
- Transaktionsintegrität, Verfügbarkeit
- Regulatorische Agilität
- Kundenschutz, Transparenz

**~10 Kernprinzipien:**
- Verlässlichkeit (Eckstein: Zuverlässigkeit)
- Transaktionswahrheit (Maßstab: Wahrheit)
- Bankenaufsicht (Ordnung: Recht)
- Finanz-Sicherheit (Fundament: Sicherheit)
- Langfristige Stabilität (Fundament: Nachhaltigkeit)
- Banking-Innovation (Ziel: Entwicklung)

**Eckstein:** Zuverlässigkeit

### Bewertung

| Score | Wert |
|-------|------|
| Cornerstone Score | 95/100 |
| Integrity Score | 94/100 |
| Compliance Score | 93/100 |
| Risk Score | 92/100 |
| Governance Score | 89/100 |
| Development Score | 88/100 |

**IGOS Gesamtscore: 92.6/100 → GOLD**

---

## Fall 10: KI-gestützte Krebsdiagnose (Medizinische KI)

### Problemstellung
Klinik implementiert KI zur Mammographie-Analyse. False-Positive/Negative haben schwerwiegende Folgen.

### Analyse

**~1000 Details:**
- Deep-Learning-Modell (CNN)
- 10.000 historische Fälle
- Radiologen-Interface
- Befundungs-Workflow

**~100 Prinzipien:**
- Diagnosegenauigkeit, Patientenschutz
- Mensch-KI-Kollaboration
- Erklärbarkeit der KI-Entscheidungen

**~10 Kernprinzipien:**
- Patientenwohl (Eckstein: Barmherzigkeit)
- Diagnosewahrheit (Maßstab: Wahrheit)
- Medizinische Standards (Ordnung: Recht)
- Daten-Sicherheit (Fundament: Sicherheit)
- Langzeitstudien (Fundament: Nachhaltigkeit)
- Medizinischer Fortschritt (Ziel: Entwicklung)

**Eckstein:** Barmherzigkeit

### Bewertung

| Score | Wert |
|-------|------|
| Cornerstone Score | 97/100 |
| Integrity Score | 91/100 |
| Compliance Score | 89/100 |
| Risk Score | 86/100 |
| Governance Score | 84/100 |
| Development Score | 90/100 |

**IGOS Gesamtscore: 90.6/100 → GOLD**

### Besonderheit: Mensch-KI-Verhältnis
**Pflichtfeld:**
```
KI unterstützt, ersetzt nicht den Radiologen.
Jede KI-Befundung wird von Facharzt validiert.
Patient wird über KI-Nutzung informiert (Einwilligung).
Fehler werden in Feedback-Loop für Modell-Improvement genutzt.
```

---

## Zusammenfassung der 10 Fälle

| # | Domäne | Eckstein | IGOS Score | Level |
|---|--------|----------|------------|-------|
| 1 | Krankenhaus | Barmherzigkeit | 90.4 | GOLD |
| 2 | Bürgerportal | Gerechtigkeit | 87.6 | SILVER |
| 3 | Autonomes Fahren | Menschenwürde | 88.7 | SILVER |
| 4 | Krypto-Exchange | Sicherheit | 86.7 | SILVER |
| 5 | Smart Grid | Nachhaltigkeit | 88.6 | SILVER |
| 6 | E-Learning | Gerechtigkeit | 86.5 | SILVER |
| 7 | Luftfracht | Zuverlässigkeit | 88.3 | SILVER |
| 8 | Gesichtserkennung | Barmherzigkeit | 76.5 | BRONZE |
| 9 | Neobank | Zuverlässigkeit | 92.6 | GOLD |
| 10 | Medizinische KI | Barmherzigkeit | 90.6 | GOLD |

### Durchschnittliche Scores

| Score | Durchschnitt |
|-------|-------------|
| Cornerstone Score | 87.0 |
| Integrity Score | 89.3 |
| Compliance Score | 86.9 |
| Risk Score | 86.8 |
| Governance Score | 84.1 |
| Development Score | 85.1 |
| **IGOS Gesamt** | **86.6** |

---

**Version:** 1.0.0  
**Stand:** 17. Juni 2026  
**Referenz:** Alle IIOS Framework Dokumente
