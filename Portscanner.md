
# Roteiro 1 portscanner

## Descrição

A ferramenta `portscanner2.py` é uma scanners multiplataforma para TCP e UDP que permite verificar a abertura ou fechadura de portas em um host. Ele suporta endereços IP (IPv4/IPv6) e nomes de domínio, além de fornecer resultados detalhados do escaneamento.

## Funcionalidades Principais

- Escaneamento de TCP
- Escaneamento de UDP
- Suporte a IPv4 e IPv6
- Resolução de domínios para IPs
- Intervalo de portas personalizáveis (formato: start-end)
- Lista de portas bem conhecidas por padrão
- Opção para exibir apenas portas abertas ou todos os resultados
- Timeout de conexão (0.5 segundos)

## Uso

```bash
python portscanner2.py [argumentos]
```

Argumentos:

target: Endereço IP ou domínio do host a ser escaneado.

-p, --ports: Intervalo de portas a serem escaneadas (ex: 20-80).

-t, --tcp: Realizar escaneamento TCP.

-u, --udp: Realizar escaneamento UDP.

Exemplos:

```zsh
# Escaneando um endereço IP na portas conhecidas como padrão
python3 portscanner2.py 10.102.10.151   

# Especificando um intervalo de portas TCP e em um dominio
python3 portscanner2.py -p 20-80 wikipedia.org -t

# Escaneando UDP para um endereço IPv6
python3 portscanner2.py ::1 -u

```

## Funções Principais

```zsh
scan_tcp(ip, port, family)
    Descrição: Escaneia uma porta usando TCP e tenta coletar um banner.
    Parâmetros:
    ip: Endereço IP do host.
    port: Número da porta a ser escaneada.
    family: Família do socket (AF_INET para IPv4 ou AF_INET6 para IPv6).
    Retorno: Retorna 0 se a porta estiver aberta, -1 caso contrário.

scan_udp(ip, port, family)
    Descrição: Escaneia uma porta usando UDP.
    Parâmetros:
    ip: Endereço IP do host.
    port: Número da porta a ser escaneada.
    family: Família do socket (AF_INET para IPv4 ou AF_INET6 para IPv6).
    Retorno: Retorna 0 se a porta estiver aberta, -1 se houver timeout e 1 caso contrário.
resolve_domain(domain)
    Descrição: Resolve um nome de domínio para um endereço IP.
    Parâmetros:
    domain: Nome do domínio a ser resolvido.
    Retorno: Retorna uma tupla com o endereço IP e a família do socket (AF_INET ou AF_INET6) ou None se a resolução falhar.
main()
    Descrição: Função principal que controla todo o fluxo do script, incluindo:
    Análise de argumentos.
    Detecção do tipo de endereço (IP ou domínio).
    Escaneamento das portas especificadas.
    Exibição dos resultados.
```

# Atividades feitas

- [x] Deverá possuir uma interface amigável e de fácil utilização (user-friendly interface); (1
ponto)
- [x] Permitir o escaneamento de um host ou uma rede; (1 ponto)
- [x] Permitir inserir o range (intervalo) de portas a serem escaneadas; (1 ponto)
- [x] Além da função de escaneamento, espera-se que seu código relacione as portas Well-Know Ports e seus serviços, e apresente em sua saída (imprimir) o número da porta e o nome do serviço associado. (2 pontos)
- [x] O código deve indicar se uma porta está aberta, fechada ou filtrada (usando
respostas como RST, TIMEOUT, etc.).(1 ponto)
- [x] Implementar escaneamento de portas UDP além de TCP.(2 pontos)
- [ ] Permitir que a ferramenta tente identificar o sistema operacional pelo banner de resposta.(2 pontos)
- [x] Permitir a entrada de endereços IPv6 e adaptar o socket para suportar essa
funcionalidade.(2 pontos)
