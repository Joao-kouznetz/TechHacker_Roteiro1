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
