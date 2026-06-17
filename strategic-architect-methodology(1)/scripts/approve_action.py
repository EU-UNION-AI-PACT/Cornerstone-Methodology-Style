#!/usr/bin/env python3
"""
SystemHeaven Action Approval Script
====================================

Interaktives Skript für Bestätigungen vor kritischen Aktionen.
Erfordert explizite Zustimmung (Ja/Nein) mit Sicherheitsabfragen.

Verwendung:
    python approve_action.py [aktion] [optionen]

Aktionen:
    push        Git Push mit Bestätigung
    install     Framework Installation mit Bestätigung
    sync        Template Synchronisation mit Bestätigung
    validate    Validierung mit Bestätigung
    delete      Löschung von Dateien mit Bestätigung
    deploy      Deployment mit Bestätigung

Beispiele:
    python approve_action.py push
    python approve_action.py install --target-dir /path/to/dir
    python approve_action.py sync --force
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, Callable
import subprocess


class Colors:
    """ANSI Farbcodes für Terminalausgabe."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_header(text: str) -> None:
    """Printt formatierten Header."""
    print(f"\n{Colors.HEADER}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{text}{Colors.END}")
    print(f"{Colors.HEADER}{'='*70}{Colors.END}\n")


def print_warning(text: str) -> None:
    """Printt Warnung."""
    print(f"{Colors.WARNING}⚠️  {text}{Colors.END}")


def print_success(text: str) -> None:
    """Printt Erfolg."""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")


def print_error(text: str) -> None:
    """Printt Fehler."""
    print(f"{Colors.FAIL}❌ {text}{Colors.END}")


def print_info(text: str) -> None:
    """Printt Info."""
    print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")


def ask_confirmation(
    question: str,
    default: bool = False,
    critical: bool = False
) -> bool:
    """
    Fragt nach Bestätigung (Ja/Nein).
    
    Args:
        question: Die Frage an den Benutzer
        default: Standard-Antwort bei Enter (True=Ja, False=Nein)
        critical: Bei kritischen Aktionen wird eine zusätzliche Sicherheitsabfrage gestellt
    
    Returns:
        True wenn bestätigt, False wenn abgelehnt
    """
    if critical:
        print_warning("DIES IST EINE KRITISCHE AKTION!")
        print_warning("Diese Aktion kann nicht rückgängig gemacht werden.")
        print()
        # Bei kritischen Aktionen: Schreibe "BESTÄTIGEN"
        safety_check = input(f"{Colors.FAIL}Zur Bestätigung schreibe 'BESTÄTIGEN': {Colors.END}").strip()
        if safety_check != "BESTÄTIGEN":
            print_error("Sicherheitsabfrage nicht bestanden. Abbruch.")
            return False
        print()
    
    if default:
        prompt = f"{question} [Ja/nein]: "
    else:
        prompt = f"{question} [ja/Nein]: "
    
    while True:
        answer = input(f"{Colors.BOLD}{prompt}{Colors.END}").strip().lower()
        
        if answer == '':
            return default
        elif answer in ['j', 'ja', 'y', 'yes']:
            return True
        elif answer in ['n', 'nein', 'no']:
            return False
        else:
            print_warning("Bitte antworte mit 'ja' oder 'nein'")


def confirm_and_execute(
    action_name: str,
    description: str,
    command: list,
    cwd: Optional[Path] = None,
    critical: bool = False
) -> bool:
    """
    Bestätigt Aktion und führt sie aus.
    
    Args:
        action_name: Name der Aktion
        description: Beschreibung was passieren wird
        command: Auszuführendes Kommando als Liste
        cwd: Arbeitsverzeichnis
        critical: Ob es eine kritische Aktion ist
    
    Returns:
        True wenn erfolgreich, False bei Abbruch oder Fehler
    """
    print_header(f"AKTION: {action_name}")
    print_info(f"Beschreibung: {description}")
    print_info(f"Kommando: {' '.join(command)}")
    if cwd:
        print_info(f"Verzeichnis: {cwd}")
    print()
    
    if not ask_confirmation("Möchtest du diese Aktion ausführen?", default=False, critical=critical):
        print_error("Aktion abgebrochen durch Benutzer.")
        return False
    
    print()
    print_info("Führe Aktion aus...")
    print()
    
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        print_success(f"Aktion '{action_name}' erfolgreich ausgeführt!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Aktion '{action_name}' fehlgeschlagen!")
        if e.stderr:
            print_error(f"Fehler: {e.stderr}")
        return False
    except FileNotFoundError:
        print_error(f"Kommando nicht gefunden: {command[0]}")
        return False


def action_push(args) -> bool:
    """Git Push mit Bestätigung."""
    base_path = Path(args.base_path) if args.base_path else Path.cwd()
    
    return confirm_and_execute(
        action_name="Git Push",
        description="Pusht alle lokalen Änderungen zu GitHub (origin main)",
        command=["git", "push", "-u", "origin", "main"] + (["--force"] if args.force else []),
        cwd=base_path,
        critical=args.force  # Force-Push ist kritisch
    )


def action_install(args) -> bool:
    """Framework Installation mit Bestätigung."""
    base_path = Path(args.target_dir) if args.target_dir else Path.cwd()
    
    # Prüfe ob Verzeichnis bereits existiert
    if base_path.exists() and any(base_path.iterdir()):
        print_warning(f"Zielverzeichnis {base_path} existiert bereits und ist nicht leer!")
        if not ask_confirmation("Trotzdem fortfahren?", default=False, critical=True):
            return False
    
    installer_path = Path(__file__).parent.parent / "systemheaven.py"
    
    if not installer_path.exists():
        print_error(f"Installer nicht gefunden: {installer_path}")
        return False
    
    return confirm_and_execute(
        action_name="SystemHeaven Installation",
        description=f"Installiert SystemHeaven Framework in {base_path}",
        command=["python3", str(installer_path), "--target-dir", str(base_path)],
        critical=False
    )


def action_sync(args) -> bool:
    """Template Synchronisation mit Bestätigung."""
    base_path = Path(args.base_path) if args.base_path else Path.cwd()
    builder_path = Path(__file__).parent / "build_framework.py"
    
    if not builder_path.exists():
        print_error(f"Build-Skript nicht gefunden: {builder_path}")
        return False
    
    return confirm_and_execute(
        action_name="Template Synchronisation",
        description="Synchronisiert Templates über alle Packages (Single Source of Truth)",
        command=["python3", str(builder_path), "sync", "--base-path", str(base_path)],
        cwd=base_path,
        critical=False
    )


def action_validate(args) -> bool:
    """Validierung mit Bestätigung."""
    base_path = Path(args.base_path) if args.base_path else Path.cwd()
    validator_path = Path(__file__).parent / "dynamic_validation_engine.py"
    
    if not validator_path.exists():
        print_error(f"Validator nicht gefunden: {validator_path}")
        return False
    
    return confirm_and_execute(
        action_name="Framework Validierung",
        description="Validiert alle Framework-Komponenten gegen die Eckstein-Prinzipien",
        command=["python3", str(validator_path), "parse"],
        cwd=base_path,
        critical=False
    )


def action_delete(args) -> bool:
    """Löschung mit Bestätigung."""
    target = Path(args.target)
    
    if not target.exists():
        print_error(f"Ziel existiert nicht: {target}")
        return False
    
    print_warning(f"Folgendes wird gelöscht: {target}")
    
    if target.is_dir():
        # Zeige was drin ist
        files = list(target.rglob("*"))
        print_info(f"Enthält {len(files)} Dateien/Ordner")
        if len(files) > 0:
            print_info("Erste 10 Einträge:")
            for f in files[:10]:
                print(f"  - {f}")
            if len(files) > 10:
                print(f"  ... und {len(files) - 10} weitere")
    
    return confirm_and_execute(
        action_name="Datei/Ordner Löschung",
        description=f"Löscht permanent: {target}",
        command=["rm", "-rf", str(target)],
        critical=True  # Löschen ist immer kritisch
    )


def main():
    """Hauptfunktion für CLI."""
    parser = argparse.ArgumentParser(
        description="SystemHeaven Action Approval - Bestätigung für kritische Aktionen",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
    python approve_action.py push                    # Push mit Bestätigung
    python approve_action.py push --force            # Force push (kritisch)
    python approve_action.py install               # Installation
    python approve_action.py install --target-dir /path
    python approve_action.py sync                    # Synchronisation
    python approve_action.py validate                # Validierung
    python approve_action.py delete --target ./dir   # Löschung (kritisch)
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Verfügbare Aktionen")
    
    # Push
    push_parser = subparsers.add_parser("push", help="Git Push mit Bestätigung")
    push_parser.add_argument("--base-path", "-b", help="Repository-Pfad")
    push_parser.add_argument("--force", "-f", action="store_true", help="Force push (kritisch)")
    
    # Install
    install_parser = subparsers.add_parser("install", help="Framework Installation")
    install_parser.add_argument("--target-dir", "-t", help="Zielverzeichnis")
    
    # Sync
    sync_parser = subparsers.add_parser("sync", help="Template Synchronisation")
    sync_parser.add_argument("--base-path", "-b", help="Framework-Base-Pfad")
    
    # Validate
    validate_parser = subparsers.add_parser("validate", help="Framework Validierung")
    validate_parser.add_argument("--base-path", "-b", help="Framework-Base-Pfad")
    
    # Delete
    delete_parser = subparsers.add_parser("delete", help="Löschung mit Bestätigung")
    delete_parser.add_argument("--target", "-t", required=True, help="Zu löschendes Ziel")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Führe gewählte Aktion aus
    actions = {
        "push": action_push,
        "install": action_install,
        "sync": action_sync,
        "validate": action_validate,
        "delete": action_delete,
    }
    
    success = actions[args.command](args)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
