# Nome do Aluno: [Seu Nome Aqui]
# Módulo: Estoque
# Descrição: Gerencia o cadastro de produtos e cálculo de custos de estoque.

from modules import data_manager

# Load initial data
produtos = data_manager.load_data('produtos.json')

def cadastrar_produto(codigo, nome, data_fab, fornecedor, quantidade, valor_compra):
    """
    Cadastra um novo produto na lista de produtos.
    Verifica duplicidade de código antes de inserir.
    """
    # Reload to ensure fresh data
    global produtos
    produtos = data_manager.load_data('produtos.json')
    
    if verificar_duplicidade(codigo):
        print(f"Erro: Produto com código {codigo} já existe!")
        return False
    
    produto = {
        "codigo": codigo,
        "nome": nome,
        "data_fabricacao": data_fab,
        "fornecedor": fornecedor,
        "quantidade": quantidade,
        "valor_compra": valor_compra
    }
    produtos.append(produto)
    data_manager.save_data('produtos.json', produtos)
    print(f"Produto '{nome}' cadastrado com sucesso.")
    return True

def verificar_duplicidade(codigo):
    """
    Verifica se já existe um produto com o código informado.
    Retorna True se existir, False caso contrário.
    """
    for p in produtos:
        if p["codigo"] == codigo:
            return True
    return False

def pesquisar_produto(termo):
    """
    Pesquisa produto por nome ou código.
    Retorna uma lista de produtos encontrados.
    """
    resultados = []
    termo = str(termo).lower()
    for p in produtos:
        if termo in str(p["codigo"]).lower() or termo in p["nome"].lower():
            resultados.append(p)
    return resultados

def calcular_custos(lista_produtos=None):
    """
    Calcula o custo total do estoque (semanal, mensal, anual).
    Aceita uma lista opcional de produtos. Se não fornecida, usa a global.
    """
    if lista_produtos is None:
        lista_produtos = produtos

    custo_total_atual = sum(p["quantidade"] * p["valor_compra"] for p in lista_produtos)
    
    # Projeção
    custo_mensal = custo_total_atual * 4
    custo_anual = custo_total_atual * 52
    
    return {
        "total_atual": custo_total_atual,
        "mensal_projetado": custo_mensal,
        "anual_projetado": custo_anual
    }

def listar_produtos():
    """
    Lista todos os produtos cadastrados.
    """
    print("\n--- Lista de Produtos ---")
    for p in produtos:
        print(f"Cód: {p['codigo']} | Nome: {p['nome']} | Qtd: {p['quantidade']} | Valor: R${p['valor_compra']:.2f}")

if __name__ == "__main__":
    # Teste manual
    print("Iniciando módulo Estoque...")
    
    # Cadastrando 10 produtos fictícios
    cadastrar_produto(1, "Pneu", "01/01/2024", "Pirelli", 100, 200.0)
    cadastrar_produto(2, "Motor", "02/01/2024", "Ford", 10, 5000.0)
    cadastrar_produto(3, "Volante", "03/01/2024", "Logitech", 50, 150.0)
    cadastrar_produto(4, "Banco", "04/01/2024", "CouroBom", 40, 300.0)
    cadastrar_produto(5, "Vidro", "05/01/2024", "Blindex", 80, 100.0)
    cadastrar_produto(6, "Farol", "06/01/2024", "LuzMax", 60, 80.0)
    cadastrar_produto(7, "Parachoque", "07/01/2024", "PlastCar", 30, 250.0)
    cadastrar_produto(8, "Freio", "08/01/2024", "Brembo", 100, 120.0)
    cadastrar_produto(9, "Embreagem", "09/01/2024", "Luk", 20, 400.0)
    cadastrar_produto(10, "Radio", "10/01/2024", "Sony", 50, 180.0)
    
    # Teste duplicidade
    cadastrar_produto(1, "Pneu Duplicado", "01/01/2024", "X", 1, 1.0)
    
    # Pesquisa
    print("\nPesquisando 'Motor':", pesquisar_produto("Motor"))
    
    # Custos
    custos = calcular_custos()
    print("\nCustos do Estoque:")
    print(f"Total Atual (Semanal): R${custos['total_atual']:.2f}")
    print(f"Projeção Mensal: R${custos['mensal_projetado']:.2f}")
    print(f"Projeção Anual: R${custos['anual_projetado']:.2f}")
