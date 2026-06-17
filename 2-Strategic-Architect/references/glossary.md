# IIOS Glossary v1.0
## Standardisierte Begriffsdefinitionen

---

## Cornerstone (Eckstein)

**Definition:** Das unverrückbare, vom Anwender wählbare Fundamentprinzip eines Systems, aus dem alle weiteren Regeln, Standards und Architekturentscheidungen abgeleitet werden.

**Eigenschaften:**
- Domänenspezifisch wählbar
- Unveränderlich während des Systemlebenszyklus
- Normativer Anker für alle Ableitungen
- Messbar durch Cornerstone Score

**Beispiele:**
- Ethische Systeme: Menschenwürde, Barmherzigkeit, Gerechtigkeit, Freiheit
- Technische Systeme: Zuverlässigkeit, Sicherheit, Konsistenz, Effizienz

**ISO-Style Definition:**
> Der Eckstein ist das primäre normative Prinzip (Layer 0) der IIOS-Architektur, das als unveränderliche Grundlage für alle weiteren Ableitungen dient und durch den Cornerstone Score (0-100) quantifiziert wird.

---

## Cornerstone Score

**Definition:** Eine quantitative Metrik (0-100), die die Einhaltung des gewählten Ecksteins und seiner Ableitungen misst.

**Gewichtung im IGOS Gesamtscore:** 20%

**Berechnung:**
```
Cornerstone Score = Σ(Kriterium_i × Gewichtung_i)
```

**Kriterien (Beispiel Barmherzigkeit):**
| Kriterium | Gewichtung |
|-----------|------------|
| Menschenwürdeschutz | 30% |
| Verhältnismäßigkeit | 25% |
| Transparenz | 25% |
| Wohlwollen | 20% |

---

## IGOS (Intelligence Governance Operating System)

**Definition:** Das Gesamtsystem zur Steuerung, Bewertung und Zertifizierung intelligenter Infrastrukturen basierend auf der Cornerstone Methodology.

**Komponenten:**
- IIOS Constitution (Verfassung)
- Technical Specification (Technische Spezifikation)
- Visual Design Standard (Design-Standard)
- Governance Standard (Governance-Standard)
- Certification Framework (Zertifizierungsrahmen)
- IGOS Scorecard (Bewertungsinstrument)

---

## IGOS Scorecard

**Definition:** Das zentrale Bewertungsinstrument zur quantitativen Erfassung der Systemkonformität mit der IIOS Constitution.

**Scores:**
- Cornerstone Score (20%)
- Integrity Score (20%)
- Compliance Score (20%)
- Risk Score (15%)
- Governance Score (15%)
- Development Score (10%)

**Ausgabe:** Gesamtscore (0-100) und Zertifizierungslevel

---

## Integrity Score

**Definition:** Eine quantitative Metrik (0-100), die die Qualität, Verlässlichkeit und Integrität von Daten und Informationen misst (Alignment mit Wahrheit).

**Gewichtung:** 20%

**Kriterien:**
| Kriterium | Gewichtung |
|-----------|------------|
| Datenintegrität | 40% |
| Quellen-Verifizierung | 30% |
| Datenaktualität | 30% |

---

## Compliance Score

**Definition:** Eine quantitative Metrik (0-100), die die Einhaltung rechtlicher, regulatorischer und ethischer Standards misst (Alignment mit Recht/Ordnung).

**Gewichtung:** 20%

**Kriterien:**
| Kriterium | Gewichtung |
|-----------|------------|
| Gesetzeseinhaltung | 40% |
| Interne Richtlinien | 30% |
| Auditierbarkeit | 30% |

---

## Risk Score

**Definition:** Eine quantitative Metrik (0-100), die die Effektivität von Sicherheits- und Resilienzmaßnahmen misst (Alignment mit Sicherheit/Fundament).

**Gewichtung:** 15%

**Kriterien:**
| Kriterium | Gewichtung |
|-----------|------------|
| Bedrohungsabwehr | 40% |
| Resilienz | 35% |
| Zugriffskontrolle | 25% |

---

## Governance Score

**Definition:** Eine quantitative Metrik (0-100), die die Gesamteffektivität der Governance-Strukturen und Nachhaltigkeit misst (Alignment mit Nachhaltigkeit/Fundament).

**Gewichtung:** 15%

**Kriterien:**
| Kriterium | Gewichtung |
|-----------|------------|
| Rollen & Verantwortlichkeiten | 35% |
| Entscheidungsprozesse | 35% |
| Nachhaltigkeitsaspekte | 30% |

---

## Development Score

**Definition:** Eine quantitative Metrik (0-100), die den Beitrag zur Entwicklung, Innovation und Problemlösung misst (Alignment mit Entwicklung/Ziel).

**Gewichtung:** 10%

**Kriterien:**
| Kriterium | Gewichtung |
|-----------|------------|
| Innovationsgrad | 40% |
| Wissensgenerierung | 30% |
| Lebensbedingungen | 30% |

---

## Radikale Verdichtung

**Definition:** Der Kernprozess der Cornerstone Methodology zur systematischen Reduktion von Komplexität (1000 → 100 → 10 → 1).

**Phasen:**
1. **Erfassung (~1000):** Sammeln aller Details, Regeln, Anforderungen
2. **Strukturierung (~100):** Gruppierung in funktionale Prinzipien
3. **Destillation (~10):** Synthese zu Kernprinzipien
4. **Fundamentierung (1):** Identifikation des Ecksteins

**Denkmodell:** Die numerische Progression dient als Heuristik, nicht als starre quantitative Regel.

---

## Normative Ableitung

**Definition:** Der top-down-Prozess der Herleitung technischer und organisatorischer Standards aus dem philosophischen Eckstein.

**Hierarchie:**
```
Eckstein (Layer 0)
    ↓
Constitution (Layer 1)
    ↓
Principles (Layer 2)
    ↓
Governance (Layer 3)
    ↓
Technical Standards (Layer 4)
    ↓
Implementation (Layer 5)
    ↓
Audit (Layer 6)
    ↓
Continuous Improvement (Layer 7)
```

---

## Pflichtfeld zur Eckstein-Validierung

**Definition:** Ein in Templates integriertes Pflichtfeld, das eine begründete Verbindung zwischen technischen/organisatorischen Entscheidungen und dem gewählten Eckstein herstellt.

**Funktion:**
- Verhindert Template-Verwässerung
- Sichert philosophische Konsistenz
- Ermöglicht Nachweisbarkeit

**Format:**
```markdown
### Pflichtfeld: Eckstein-Validierung

**Begründung:** [Explizite Begründung, wie diese Komponente dem Eckstein dient]
```

---

## Verhältnismäßigkeit

**Definition:** Das Prinzip, dass Eingriffe und Entscheidungen des Systems stets im angemessenen Verhältnis zu den angestrebten Zielen und potenziellen Auswirkungen stehen müssen.

**Anwendung:**
- Technische Maßnahmen
- Datenerhebung
- Zugriffsbeschränkungen
- Algorithmische Entscheidungen

---

## Menschenwürde

**Definition:** Die unantastbare Würde jedes Menschen, die oberste normative Instanz ethischer Systeme und zentraler Bestandteil des Barmherzigkeits-Ecksteins.

**Schutzaspekte:**
- Autonomie
- Privatsphäre
- Rechte
- Freiheit
- Integrität

---

## Auditierbarkeit

**Definition:** Die Eigenschaft eines Systems, vollständig nachvollziehbar und extern prüfbar zu sein.

**Anforderungen:**
- Immutable Logs
- Vollständige Dokumentation
- Transparenz der Prozesse
- Zugängliche Governance-Strukturen

---

## Resilienz

**Definition:** Die Fähigkeit eines Systems, bei Störungen, Angriffen oder Ausfällen seine Funktionsfähigkeit aufrechtzuerhalten oder schnell wiederherzustellen.

**Dimensionen:**
- Technische Resilienz (Redundanz, Failover)
- Organisatorische Resilienz (Prozesse, Kommunikation)
- Datenresilienz (Backups, Recovery)

---

## Zertifizierungsstufen

**Definition:** Die vier Qualitätsstufen der IIOS-Zertifizierung, basierend auf dem IGOS Gesamtscore.

| Stufe | Score | Charakteristik |
|-------|-------|----------------|
| Platinum | 95-100 | Exzellenz, Best-in-Class |
| Gold | 90-94 | Hervorragend, überdurchschnittlich |
| Silver | 80-89 | Gut, solide Umsetzung |
| Bronze | 70-79 | Basis, Mindestanforderungen |

---

## Cornerstone Steward

**Definition:** Die Rolle, die für die Wahrung und Entwicklung des Ecksteins verantwortlich ist.

**Aufgaben:**
- Eckstein-Validierung
- Philosophische Konsistenz
- Weiterentwicklung der Ableitungen

---

## Governance Officer

**Definition:** Die Rolle, die für die operative Governance und Einhaltung der Verfassung verantwortlich ist.

**Aufgaben:**
- Prozessüberwachung
- Compliance-Prüfung
- Reporting

---

## Technical Architect

**Definition:** Die Rolle, die für die technische Umsetzung der Standards verantwortlich ist.

**Aufgaben:**
- Architekturentwurf
- Implementierungsplanung
- Technische Qualitätssicherung

---

## Compliance Auditor

**Definition:** Die Rolle, die für die unabhängige Überprüfung der Konformität verantwortlich ist.

**Aufgaben:**
- Unabhängige Audits
- Score-Berechnung
- Zertifizierungsempfehlung

---

## Certification Reviewer

**Definition:** Die Rolle, die für die endgültige Zertifizierungsentscheidung verantwortlich ist.

**Aufgaben:**
- Gesamtbewertung
- Zertifizierungsvergabe
- Re-Zertifizierungsplanung

---

## Verwendete Abkürzungen

| Abkürzung | Bedeutung |
|-----------|-----------|
| IIOS | Intelligence Infrastructure Operating System |
| IGOS | Intelligence Governance Operating System |
| CS | Cornerstone Score |
| IS | Integrity Score |
| CoS | Compliance Score |
| RS | Risk Score |
| GS | Governance Score |
| DS | Development Score |

---

**Version:** 1.0.0  
**Stand:** 17. Juni 2026  
**Gültigkeit:** Unbefristet
