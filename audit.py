import platform
import subprocess

def print_header():
    print("=" * 50)
    print("      Security Compliance Checker")
    print("=" * 50)
    print()

def check_filevault():
    result = subprocess.run(
        ["fdesetup", "status"],
        capture_output=True,
        text=True
    )
    return result.stdout

def check_firewall():
    result = subprocess.run(
        ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
        capture_output=True,
        text=True
    )
    return result.stdout

def check_gatekeeper():
    result = subprocess.run(
        ["spctl", "--status"],
        capture_output=True,
        text=True
    )
    return result.stdout

def main():
    print_header()

    computer_name = platform.node()
    macos_version = platform.mac_ver()[0]

    print("🖥️ SYSTEM INFORMATION")
    print("-" * 40)
    print(f"Computer Name : {computer_name}")
    print(f"macOS Version : {macos_version}")
    print()

    # FileVault
    filevault_status = check_filevault()

    if "On" in filevault_status:
        print("FileVault      ✓ PASS")
    else:
        print("FileVault      ✗ FAIL")

    # Firewall
    firewall_status = check_firewall()

    if "enabled" in firewall_status.lower():
        print("Firewall       ✓ PASS")
    else:
        print("Firewall       ✗ FAIL")

    # Gatekeeper
    gatekeeper_status = check_gatekeeper()

    if "assessments enabled" in gatekeeper_status.lower():
        print("Gatekeeper     ✓ PASS")
    else:
        print("Gatekeeper     ✗ FAIL")

    print()
    print("Raw Results")
    print("-" * 40)
    print(filevault_status)
    print(firewall_status)
    print(gatekeeper_status)

if __name__ == "__main__":
    main()