# Pergutas

## 1 Além do PortScan, quais são as 5 ferramentas mais úteis para reconhecimento em um pentest?

As ferrementas mais uteis são whois loookup, dns enumeration, subdomain scanner, nikto e scan de vulnerabilidades como nmap. O whois é uma ferramenta importante para encontrar relações de uma pessoa com um site. Em aula o Avelino contou quando ele expos um grupo que tinha feito um site ilegal rastrenando outros sites pelo dns que esse grupo havia feito e mostrando a conecção da pessoa com o site pelo whois.

## 2 Qual a diferença entre um scanner de portas SYN e um TCP Connect Scan?

O TCP connect uma conecção completa enquanto o SYN scan apenas envia pacotes syn permetindo uma varredura mais discreta. A principal diferença é que o SYN não finaliza a coneção

## 3 Como um pentester pode evitar ser detectado por sistemas de prevenção de intrusão (IPS) durante o reconhecimento?

O paintester pode evitar o reconhecimento usando tecnincas que deixam o ataque mais discreto como:

- Utilização de VPNs encaminhado cada requisição por um ip diferente. Com a diversidade de Ips o ip do pentester é  ocultado e dificulta a detecção.  Impacta o tempo do scan adicionando um overhead porque tera que conectar com cada vpn antes de fazer o scan mas não a eficácia a não ser que você coloque uma vpn para um local onde o servidor não atende ou barre requisições como no caso que o Avelino trouxe em aula de que estava sofrendo um ataque DOS ele combateu so permitindo conecções do Brasil.
- Utilização da rede TOR. Novamente como ela encaminha trafego por  ips intermediario (as maquinas da rede interna do tor) é ocultado o ip do pentester. Impacta a o tempo do scan adicionando overhead que é o tempo de transmitir a requisição dentro da rede TOR mas não a eficacia
- Ajustar o tempo entre requisições. Aumentando o tempo entre requisições pode fazer com que tenha menos logs seguidos o que pode deixar o ataque mais discreto. Aumenta o tempo do scan mas não a eficacia.
- Scan mais furtivos como o SYN . Onde não finaliza a conecção ou seja não envia o ACK o que tem o impoacto de deixar mais rápido mas apenas ve se a porta esta aberta ou fechada.
- Fazer um reconhecimento sem tocar no alvo, usando whois, dns .

# App Reconhecimento do Alvo

## Descrição

O App é um utilitário em Python que reúne diversas funções essenciais de reconhecimento e enumeração digital

Através de um menu no terminal, você pode realizar desde escaneamento de portas até consultas WHOIS, enumeração DNS, busca por subdomínios e coleta de cabeçalhos HTTP.

---

## Principais Funcionalidades

Cada funcionalidade pode ser acessada diretamente pelo menu interativo da ferramenta:

### 1. **PortScan**

- Escaneamento de portas TCP e UDP.
- Suporte a IPv4, IPv6 e nomes de domínio.
- Intervalos customizáveis de portas.
- Associação de portas a serviços conhecidos (“Well-Known Ports”).
- Exibe estado das portas: aberta, fechada, ou filtrada.
- Interface prática para seleção de modo (TCP/UDP), faixa de portas e alvo.

### 2. **WHOIS Lookup**

- Consulta de informações WHOIS de domínio ou IP.
- Retorna detalhes do registro do alvo.

### 3. **DNS Enumeração**

- Resolve registros básicos DNS (A e AAAA).
- Permite análise inicial de infraestrutura DNS do alvo.

### 4. **Subdomain Scanner**

- Testa presença de subdomínios comuns a partir de uma wordlist.
- Revela potenciais alvos adicionais e superfícies de ataque.

### 5. **HTTP Headers Fetcher**

- Busca e exibe cabeçalhos HTTP.
- Útil para fingerprinting e análise de tecnologias adotadas no servidor.

---

## Uso

### Executando a ferramenta

No terminal, execute:

```bash
python3 main.py
```

Siga o menu apresentado para escolher a funcionalidade desejada.

## Exemplos de Uso

### PortScan (Scanner de Portas)

Ele foi desenvolvido no roteiro 1 e pode ser acessado por uma ferramenta paralela. A sua documentação esta ao final do documento.

- Digite “1” no menu.
- Informe o alvo (IP ou domínio).
- Especifique um intervalo de portas (ex: 20-80) ou pressione Enter para padrão.
- Siga as instruções para visualizar as portas abertas e os serviços.

### WHOIS Lookup

- Digite “2” no menu.
- Digite o domínio ou IP.
- Verifique as informações de registro apresentadas.

### DNS Enumeração

- Digite “3” no menu.
- Informe o domínio e acompanhe os registros resolvidos.

### Subdomain Scanner

- Digite “4” no menu.
- Informe o domínio e veja a lista de subdomínios encontrados.

### HTTP Headers Fetcher

- Digite “5” no menu.
- Informe o host ou domínio, e visualize os headers HTTP recebidos.

---

## Informações Técnicas e Para Desenvolvedores

Para detalhes sobre arquitetura, decisões de design, e estrutura do projeto, consulte o arquivo: [contributor](Contributor.md)

## Informações Portscanner

Para detalhes sobre o portscanner ler o seguinte arquivo: [portscanner.md](Portscanner.md)

## Referencias

## Pergunta 2

- [syn e tcp](<https://forense.io/glossario/o-que-e-port-scanning-e-sua-importancia-na-seguranca/#:~:text=O%20TCP%20Connect%2C%20por%20exemplo,permitindo%20uma%20varredura%20mais%20discreta>.)

### Whois

- [site para iana de whois](https://www.iana.org/whois?q=wikipeida.org)
- [como funciona o whois da iana](https://www.iana.org/whois?q=.com)
- para registro.br tentei a mesma coisa e deu certo

### DNS

- [documentação gethostbyname](https://pythontic.com/modules/socket/gethostbyname)
- [Documentação getaddrinfo](https://pythontic.com/modules/socket/getaddrinfo)

### Subdoain scan

- [documentação gethostbyname](https://pythontic.com/modules/socket/gethostbyname)
- [Inspiração para word list](https://raw.githubusercontent.com/danTaler/WordLists/refs/heads/master/Subdomain.txt)

# Exemplos de Teste

caso esteja fazendo um peintest no insper:

Para fazer um Portscan

```
1
insper.edu.br
```

Para fazer um whois:

```
2
insper.edu.br
```

para fazer um DNS Enumeration

```
4
insper.edu.br
```

Para fazer um http header fetcher

```
5
insper.edu.br
```
