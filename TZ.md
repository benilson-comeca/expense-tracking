# Projeto: Vacancy Analyzer

## 1. Objetivo
Criar um web-serviço para estudantes de IT que permite analisar salários de vagas de emprego.

## 2. Público-alvo
- Estudantes de programação
- Pessoas procurando emprego na área IT

## 3. Modelos de Dados

### Category
- name (nome da categoria)

### Vacancy
- title (título da vaga)
- company (empresa)
- salary (salário)
- category (ligação com Category)

### SavedVacancy
- user (usuário)
- vacancy (vaga salva)

## 4. Funcionalidades
- Listar vagas
- Calcular média salarial
- Mostrar gráfico de salários
- Integração com API externa
- Sistema de login

## 5. Tecnologias
- Python
- Django
- SQLite
- Matplotlib (gráficos)