# Nome do Aluno: [Seu Nome Aqui]
# Módulo: Financeiro
# Descrição: Gerencia cálculo de custos e formação de preço de venda.

from modules import data_manager

def cadastrar_despesas_fixas():
    """
    Solicita a entrada manual de despesas fixas.
    Retorna o valor total das despesas.
    """
    print("\n--- Cadastro de Despesas Fixas ---")
    try:
        agua = float(input("Custo de Água: R$ "))
        luz = float(input("Custo de Luz: R$ "))
        salarios = float(input("Custo de Salários: R$ "))
        impostos = float(input("Custo de Impostos: R$ "))
        
        despesas = [
            {"tipo": "Agua", "valor": agua},
            {"tipo": "Luz", "valor": luz},
            {"tipo": "Salarios", "valor": salarios},
            {"tipo": "Impostos", "valor": impostos}
        ]
        data_manager.save_data('despesas.json', despesas)
        
        total_fixo = agua + luz + salarios + impostos
        return total_fixo
    except ValueError:
        print("Erro: Digite apenas valores numéricos.")
        return 0.0

def calcular_custo_producao(despesas_fixas, custo_insumos_total):
    """
    Calcula o custo total de produção (Fixas + Variáveis/Insumos).
    """
    custo_total = despesas_fixas + custo_insumos_total
    return custo_total

def calcular_custo_por_carro(custo_total_producao, qtd_carros_produzidos):
    """
    Calcula o custo unitário por carro.
    """
    if qtd_carros_produzidos <= 0:
        return 0.0
    return custo_total_producao / qtd_carros_produzidos

def calcular_preco_venda(custo_unitario):
    """
    Calcula o preço de venda com 50% de lucro sobre o custo unitário.
    """
    margem_lucro = 0.50
    preco_venda = custo_unitario * (1 + margem_lucro)
    return preco_venda

if __name__ == "__main__":
    print("Iniciando módulo Financeiro...")
    
    # Simulação
    # despesas = cadastrar_despesas_fixas() # Comentado para não bloquear teste automático
    despesas_mock = 50000.0 # Exemplo: 50 mil de despesas fixas
    
    # Supondo que o custo de insumos venha do módulo Estoque (ex: R$ 200.000)
    custo_insumos = 200000.0
    
    # Supondo produção de 100 carros (do módulo Operacional)
    qtd_carros = 100
    
    custo_total = calcular_custo_producao(despesas_mock, custo_insumos)
    custo_unitario = calcular_custo_por_carro(custo_total, qtd_carros)
    preco_venda = calcular_preco_venda(custo_unitario)
    
    print(f"\n--- Relatório Financeiro (Simulação) ---")
    print(f"Despesas Fixas: R$ {despesas_mock:.2f}")
    print(f"Custo Insumos: R$ {custo_insumos:.2f}")
    print(f"Custo Total Produção: R$ {custo_total:.2f}")
    print(f"Quantidade Produzida: {qtd_carros}")
    print(f"Custo por Carro: R$ {custo_unitario:.2f}")
    print(f"Preço de Venda Sugerido (+50%): R$ {preco_venda:.2f}")
