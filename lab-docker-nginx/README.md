## 🛠️ Lab 01: Deploy de Servidor Web Nginx (Customizado)

Neste laboratório, implementei um servidor Nginx via Docker em uma instância Ubuntu ARM na Oracle Cloud, superando desafios de conectividade e segurança.

### 🧠 Desafios e Soluções (Troubleshooting):
* **Arquitetura ARM:** Implementação em processadores Ampere (A1), garantindo alta performance com **custo zero**.
* **Segurança SSH:** Resolução de erro de permissão de chave privada no Windows (`unprotected private key file`) via PowerShell.
* **Redes OCI:** Configuração de **Listas de Segurança (Security Lists)** na VCN para liberar tráfego externo na porta 80 (HTTP).
* **Docker Volumes:** Mapeamento de arquivos locais (`index.html`) para dentro do container, permitindo atualizações em tempo real sem precisar refazer o build da imagem.

### 📦 Tecnologias Utilizadas:
- **Cloud:** Oracle Cloud Infrastructure (OCI) - Pay As You Go (Always Free).
- **SO:** Ubuntu Server 22.04 LTS (ARM64).
- **Containers:** Docker & Docker Compose.
- **Web:** Nginx (Alpine Image).
- **Controle de Versão:** Git & GitHub.

---

## 📂 Estrutura do Lab
* `index.html`: Página customizada do servidor.
* `docker-compose.yml`: Orquestração do container Nginx com mapeamento de porta 80:80 e volumes.
* `README.md`: Documentação técnica do processo.

---
