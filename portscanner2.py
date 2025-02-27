import socket
import sys
import argparse
import ipaddress


def scan_tcp(ip, port, family):
    """Escaneia uma porta usando TCP e tenta coletar um banner."""
    sock = socket.socket(family, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((ip, port))
    except Exception as e:
        result = -1
    sock.close()
    return result


def scan_udp(ip, port, family):
    """Escaneia uma porta usando UDP.
    O UDP é intrinsecamente 'silencioso': se não houver resposta, pode estar aberta ou filtrada.
    """
    sock = socket.socket(family, socket.SOCK_DGRAM)
    sock.settimeout(0.5)
    try:
        sock.sendto(b"", (ip, port))
        result = 0  # Recebeu resposta: porta aberta
    except socket.timeout:
        # Timeout: não há resposta
        result = -1
    except Exception:
        result = 1  # Porta fechada ou erro
    sock.close()
    return result


def resolve_domain(domain):
    """Resolve um nome de domínio para um endereço IP."""
    try:
        # Primeiro tentamos resolver como IPv4
        ip_addr = socket.gethostbyname(domain)
        family = socket.AF_INET
        return ip_addr, family
    except socket.gaierror:
        return None, None


def main():
    parser = argparse.ArgumentParser(
        description="Ferramenta de Escaneamento de Portas em Python"
    )
    parser.add_argument(
        "target",
        nargs="?",
        help="Endereço IP (IPv4 ou IPv6) ou domínio do host a ser escaneado",
    )
    parser.add_argument(
        "-p", "--ports", help="Intervalo de portas (ex: 20-80)", default="1-2"
    )
    parser.add_argument(
        "-t", "--tcp", action="store_true", help="Realizar escaneamento TCP"
    )
    parser.add_argument(
        "-u", "--udp", action="store_true", help="Realizar escaneamento UDP"
    )
    args = parser.parse_args()

    # Verifica se o endereço IP ou domínio foi fornecido
    if args.target is None:
        print("ERRO: É necessário fornecer um endereço IP ou nome de domínio!")
        print("\nExemplo de uso:")
        print("  python portscanner2.py 192.168.1.1")
        print("  python portscanner2.py wikipedia.org")
        print("\nArgumentos opcionais:")
        print("  -p, --ports: Intervalo de portas (ex: 20-80)")
        print("  -t, --tcp: Realizar escaneamento TCP")
        print("  -u, --udp: Realizar escaneamento UDP")
        sys.exit(1)

    # Se nenhum dos protocolos for selecionado, escaneia TCP por padrão
    if not args.tcp and not args.udp:
        args.tcp = True

    # Verifica se o endereço é IPv4, IPv6 ou um domínio
    try:
        # Tenta interpretar como um endereço IP
        ip_obj = ipaddress.ip_address(args.target)
        ip_addr = args.target
        if ip_obj.version == 4:
            family = socket.AF_INET
        else:
            family = socket.AF_INET6
    except ValueError:
        # Se não for um IP válido, tenta resolver como um domínio
        print(f"Tentando resolver o domínio: {args.target}")
        ip_addr, family = resolve_domain(args.target)
        if ip_addr is None:
            print(f"Não foi possível resolver o domínio: {args.target}")
            sys.exit(1)
        print(f"Domínio resolvido para: {ip_addr}")

    try:
        port_range = args.ports.split("-")
        start_port = int(port_range[0])
        end_port = int(port_range[1])
    except Exception:
        print("Formato de intervalo inválido. Utilize start-end (ex: 20-80).")
        sys.exit(1)

    well_known = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        111: "RPCbind",
        135: "MSRPC",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "Microsoft-DS",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP",
        8000: "HTTP",
    }
    if start_port == 1 and end_port == 2:
        print(f"Escaneando {args.target} ({ip_addr}) nas portas conhecidas...")
        print(
            "Nenhum intervalo de portas especificado. Escaneando apenas portas conhecidas."
        )
        ports_to_scan = [
            21,
            22,
            23,
            25,
            53,
            80,
            110,
            111,
            135,
            139,
            143,
            443,
            445,
            993,
            995,
            3306,
            3389,
            8000,
        ]
    else:
        print(
            f"Escaneando {args.target} ({ip_addr}) nas portas de {start_port} a {end_port}..."
        )
        ports_to_scan = list(range(start_port, end_port + 1))

    # Varre o intervalo de portas e guarda os resultados
    results = []
    open_ports = []

    for port in ports_to_scan:
        service = well_known.get(port, "Desconhecido")
        port_results = {}

        if args.tcp:
            result = scan_tcp(ip_addr, port, family)
            if result == 0:
                state = "ABERTA (TCP)"
                port_results["tcp"] = state
                open_ports.append((port, service, state))
            else:
                state = "FECHADA ou FILTRADA (TCP)"
                port_results["tcp"] = state

        if args.udp:
            result = scan_udp(ip_addr, port, family)
            if result == 0:
                state = "ABERTA (UDP)"
                port_results["udp"] = state
                open_ports.append((port, service, state))
            elif result == -1:
                state = "ABERTA ou FILTRADA (UDP) SEM RESPOSTA"
                port_results["udp"] = state
            else:
                state = "FECHADA (UDP)"
                port_results["udp"] = state

        results.append((port, service, port_results))

    # Perguntar ao usuário qual tipo de resultado exibir
    print("\nEscaneamento concluído!")
    show_option = (
        input("Deseja exibir todas as portas ou apenas as abertas? (T/A): ")
        .strip()
        .upper()
    )

    if show_option == "A":
        print("\n=== PORTAS ABERTAS ===")
        if not open_ports:
            print("Nenhuma porta aberta encontrada.")
        for port, service, state in open_ports:
            print(f"Porta {port} - {service}: {state}")
    else:
        print("\n=== RESULTADOS DO ESCANEAMENTO ===")
        for port, service, port_results in results:
            if "tcp" in port_results:
                print(f"Porta {port} - {service}: {port_results['tcp']}")
            if "udp" in port_results:
                print(f"Porta {port} - {service}: {port_results['udp']}")


if __name__ == "__main__":
    main()
