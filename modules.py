import socket
import requests


def whois_lookup(target):
    """Retorna as informações WHOIS de um domínio ou IP (usando conexão raw ao servidor WHOIS padrão)."""
    server = "whois.iana.org"
    port = 43

    if not target.replace(".", "").isdigit():
        if target.lower().endswith(".br"):
            server = "whois.registro.br"
        else:
            server = "whois.verisign-grs.com"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, port))
            s.send((target + "\r\n").encode())
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
        return response.decode(errors="ignore")
    except Exception as e:
        return f"[ERRO] WHOIS lookup falhou: {e}"


def dns_lookup(domain):
    """Resolve DNS básicos: A, AAAA, MX, NS, TXT"""
    results = {}
    try:
        results["IPV4"] = socket.gethostbyname(domain)
    except Exception:
        results["IPV4"] = "Não encontrado"
    try:
        results["IPV6"] = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
    except Exception:
        results["IPV6"] = "Não encontrado"
    return results


def subdomain_scan(domain, wordlist=None):
    """Testa subdomínios de uma wordlist externa"""
    if wordlist is None:
        wordlist = [
            "www",
            "mail",
            "mail2",
            "localhost",
            "static",
            "mobile",
            "acesso",
            "pt",
            "ftp",
            "test",
            "blog",
            "webmail",
            "admin",
            "api",
            "docs",
            "dev",
            "home",
        ]
    found = []
    for prefix in wordlist:
        sub = f"{prefix}.{domain}"
        try:
            ip = socket.gethostbyname(sub)
            found.append((sub, ip))
        except Exception:
            continue
    return found


def get_http_headers(target):
    """Busca e retorna os headers HTTP de um site (básico para fingerprinting)."""
    url = "http://" + target if not target.startswith("http") else target
    try:
        resp = requests.get(url, timeout=3)
        return resp.headers
    except Exception as e:
        return f"[ERRO] Fetch headers falhou: {e}"
