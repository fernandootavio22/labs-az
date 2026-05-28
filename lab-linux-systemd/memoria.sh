#!/bin/bash
while true; do
  echo "Monitoramento - Memória em uso: $(free -m | awk 'NR==2{print $3"MB"}')"
  sleep 10
done
