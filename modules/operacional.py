# Nome do Aluno: [Seu Nome Aqui]
# Módulo: Operacional
# Descrição: Gerencia o cadastro de produção diária e gera relatórios estatísticos.

from modules import data_manager

def cadastrar_producao():
    """
    Cadastra a produção diária de cada turno por 7 dias.
    Retorna uma lista de dicionários com os dados.
    """
    producao_semanal = []
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    turnos = ["Manhã", "Tarde", "Noite"]

    print("--- Cadastro de Produção Semanal ---")
    for dia in dias_semana:
        dados_dia = {"dia": dia, "turnos": {}}
        print(f"\nDia: {dia}")
        for turno in turnos:
            while True:
                try:
                    qtd = int(input(f"Produção do turno {turno}: "))
                    if qtd < 0:
                        print("A quantidade não pode ser negativa.")
                    else:
                        dados_dia["turnos"][turno] = qtd
                        break
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")
        producao_semanal.append(dados_dia)
    
    # Save to JSON
    # We append new weekly data or overwrite? Requirement implies "Cadastro de Produção".
    # For simplicity and to match the "Weekly" nature, let's append to a history or just save the current week.
    # Given the structure, let's save the current week as 'producao.json' overwriting for now, 
    # or better, append to a list of weeks? 
    # The web app treats 'producao' as a flat list of records.
    # Let's adapt: The terminal module creates a structured week. The web app creates flat records.
    # To share data, we should probably standardize.
    # Web App: [{'dia': 'Segunda', 'turno': 'Manhã', 'quantidade': 10}, ...]
    # Terminal: [{'dia': 'Segunda', 'turnos': {'Manhã': 10...}}]
    
    # Let's convert Terminal input to Flat format for consistency with Web App DB structure (which we are replacing with JSON)
    flat_data = []
    for day_data in producao_semanal:
        for turno, qtd in day_data['turnos'].items():
            flat_data.append({
                'dia': day_data['dia'],
                'turno': turno,
                'quantidade': qtd
            })
            
    # Load existing to append?
    existing_data = data_manager.load_data('producao.json')
    existing_data.extend(flat_data)
    data_manager.save_data('producao.json', existing_data)
    
    return producao_semanal

def calcular_estatisticas(dados):
    """
    Calcula produção total semanal, média por dia e por turno.
    Retorna um dicionário com as estatísticas.
    """
    total_semanal = 0
    total_turnos = {"Manhã": 0, "Tarde": 0, "Noite": 0}
    
    for dia in dados:
        for turno, qtd in dia["turnos"].items():
            total_semanal += qtd
            total_turnos[turno] += qtd
            
    media_diaria = total_semanal / 7
    media_por_turno = {t: qtd / 7 for t, qtd in total_turnos.items()}
    
    return {
        "total_semanal": total_semanal,
        "media_diaria": media_diaria,
        "media_por_turno": media_por_turno,
        "total_por_turno": total_turnos
    }

def simular_producao(total_semanal):
    """
    Simula a produção mensal e anual com base na produção semanal.
    """
    mensal = total_semanal * 4
    anual = total_semanal * 52
    return mensal, anual

def calcular_capacidade_ideal():
    """
    Calcula a produção ideal com 100% da capacidade.
    Capacidade padrão: 500 unidades/mês com 2 turnos.
    Terceiro turno aumenta 50%.
    """
    # Capacidade base (2 turnos) = 500/mês
    # 3 turnos = 500 + 50% = 750/mês
    cap_mensal_ideal = 750
    cap_semanal_ideal = cap_mensal_ideal / 4
    cap_anual_ideal = cap_mensal_ideal * 12
    
    return {
        "semanal": cap_semanal_ideal,
        "mensal": cap_mensal_ideal,
        "anual": cap_anual_ideal
    }

def gerar_relatorio(dados, estatisticas, ideal):
    """
    Emite um relatório comparativo entre produção real e ideal.
    """
    print("\n" + "="*40)
    print("RELATÓRIO OPERACIONAL - CARANGOS S/A")
    print("="*40)
    
    print(f"Produção Total Semanal: {estatisticas['total_semanal']}")
    print(f"Média Diária: {estatisticas['media_diaria']:.2f}")
    
    print("\nMédia por Turno:")
    for turno, media in estatisticas['media_por_turno'].items():
        print(f"  {turno}: {media:.2f}")

    mensal_est, anual_est = simular_producao(estatisticas['total_semanal'])
    
    print("\n--- Simulação ---")
    print(f"Estimativa Mensal (Real): {mensal_est}")
    print(f"Estimativa Anual (Real): {anual_est}")
    
    print("\n--- Comparativo com Ideal (100% Capacidade) ---")
    print(f"Ideal Semanal: {ideal['semanal']:.2f} | Real: {estatisticas['total_semanal']} | Diferença: {estatisticas['total_semanal'] - ideal['semanal']:.2f}")
    print(f"Ideal Mensal: {ideal['mensal']} | Real: {mensal_est} | Diferença: {mensal_est - ideal['mensal']}")
    print(f"Ideal Anual: {ideal['anual']} | Real: {anual_est} | Diferença: {anual_est - ideal['anual']}")
    print("="*40)

if __name__ == "__main__":
    # Teste manual simples
    print("Iniciando módulo Operacional...")
    # Para teste rápido, vou criar dados fictícios se não quiser digitar tudo
    # dados = cadastrar_producao() 
    
    # Mock de dados para teste sem input
    dados_mock = [
        {"dia": "Segunda", "turnos": {"Manhã": 10, "Tarde": 10, "Noite": 5}},
        {"dia": "Terça", "turnos": {"Manhã": 10, "Tarde": 10, "Noite": 5}},
        {"dia": "Quarta", "turnos": {"Manhã": 10, "Tarde": 10, "Noite": 5}},
        {"dia": "Quinta", "turnos": {"Manhã": 10, "Tarde": 10, "Noite": 5}},
        {"dia": "Sexta", "turnos": {"Manhã": 10, "Tarde": 10, "Noite": 5}},
        {"dia": "Sábado", "turnos": {"Manhã": 5, "Tarde": 5, "Noite": 0}},
        {"dia": "Domingo", "turnos": {"Manhã": 0, "Tarde": 0, "Noite": 0}},
    ]
    
    stats = calcular_estatisticas(dados_mock)
    ideal = calcular_capacidade_ideal()
    gerar_relatorio(dados_mock, stats, ideal)
