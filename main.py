from modules import whois_lookup
from modules import dns_lookup
from modules import subdomain_scan
from modules import get_http_headers
import subprocess
import sys


def menu():
    while True:
        print("\n=== MENU DE RECONHECIMENTO ===")
        print("1 - PortScan")
        print("2 - WHOIS Lookup")
        print("3 - DNS Enumeração")
        print("4 - Subdomain Scanner")
        print("5 - HTTP Headers Fetcher")
        print("0 - Sair")
        opt = input("Escolha uma opção: ").strip()
        if opt == "1":
            target = input("Target: ")
            print("\nArgumentos opcionais:")
            print("  -p, --ports: Intervalo de portas (ex: 20-80)")
            print("  -t, --tcp: Realizar escaneamento TCP")
            print("  -u, --udp: Realizar escaneamento UDP")
            print("\n")
            args = input("Argumentos opcionais (ou tecla enter): ")
            cmd = f"python3 portscanner2.py {target} {args}"
            print("\n")
            subprocess.run(cmd, shell=True)
        elif opt == "2":
            target = input("Domínio/IP: ")
            print(whois_lookup(target))
            print("\n")
        elif opt == "3":
            domain = input("Domínio: ")
            print(dns_lookup(domain))
        elif opt == "4":
            domain = input("Domínio: ")
            result = subdomain_scan(domain)
            if not result:
                print("Nenhum subdomínio encontrado.")
            else:
                for sub, ip in result:
                    print(f"{sub} -> {ip}")
        elif opt == "5":
            target = input("Host/Domínio: ")
            headers = get_http_headers(target)
            print(headers)
        elif opt == "0":
            print("Saindo.")
            sys.exit(0)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
