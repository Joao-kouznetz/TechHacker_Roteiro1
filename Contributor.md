# Contributor.md

## Descrição da Arquitetura e Decisões de Design

O app é estruturado com modularidade e extensibilidade, visando separar claramente a interface do usuário (main.py), as funções utilitárias (modules.py) e componentes independentes como o scanner de portas (portscanner2.py).

### Decisões de Design

- **Menu interativo** centralizado (main.py) facilita o uso e integração de múltiplas funcionalidades sem confundir o usuário.
- **Modularização:** funcionalidades core (WHOIS, DNS, subdomínio e cabeçalhos HTTP) estão em `modules.py`, promovendo reuso de código.
- **Portscanner desacoplado:** `portscanner2.py` pode ser rodado isoladamente ou chamado via menu, permitindo fácil manutenção e extensão futura. Rodando como processo garante que ele terá as mesmas funcionalidades que rodando isoladamente.

---

## Estrutura de Arquivos

- **main.py**  
  Entrada principal da ferramenta. Exibe o menu, recebe as opções do usuário e chama as funções dos módulos correspondentes ou aciona o scanner de portas via subprocesso.

- **modules.py**  
  Contém funções básicas de reconhecimento:  
  - `whois_lookup`: consulta WHOIS para domínios/IPs  
  - `dns_lookup`: resolve registros DNS básicos  
  - `subdomain_scan`: tenta descobrir subdomínios usando uma wordlist  
  - `get_http_headers`: coleta cabeçalhos HTTP de um alvo

- **portscanner2.py**  
  Script independente, especializado em escaneamento de portas (TCP/UDP) em IPV4/IPV6/domínios.
  - Permite range de portas customizável e mostra possíveis serviços associados às portas abertas.

- **Readme.md**  
  Documentação geral do projeto: descrição, funcionalidades disponíveis, exemplos de uso e informações para usuários finais.

- **Contributor.md**  
  Informação destinada a desenvolvedores: arquitetura, decisões de design e explicação/descrição dos arquivos para manutenção, extensão ou análise detalhada.
