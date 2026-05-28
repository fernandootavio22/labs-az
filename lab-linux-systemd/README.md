
1. *Script Bash (memoria.sh)*: Um script que utiliza o comando free -m e filtros awk para reportar o uso de memória RAM a cada 10 segundos.
2. *Unit File do Systemd*: Criação de um arquivo .service para gerenciar o ciclo de vida do script.

##  Comandos Principais:
- chmod +x: Para dar permissão de execução ao script.
- sudo systemctl daemon-reload: Para atualizar o gerenciador de serviços com a nova unidade.
- sudo systemctl enable: Para garantir que o monitoramento inicie junto com o servidor (Boot).
- journalctl -u -f: Para monitorar os logs em tempo real (NOC Style).

## 📝 Script do Serviço

```bash
#!/bin/bash
while true; do
  echo "Monitoramento - Memória em uso: $(free -m | awk 'NR==2{print $3"MB"}')"
  sleep 10
done
