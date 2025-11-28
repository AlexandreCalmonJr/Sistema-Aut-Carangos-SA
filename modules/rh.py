# Nome do Aluno: [Seu Nome Aqui]
# Módulo: Recursos Humanos
# Descrição: Gerencia cadastro de funcionários e folha de pagamento.

from modules import data_manager

# Load initial data
funcionarios = data_manager.load_data('funcionarios.json')

def cadastrar_funcionario(nome, cpf, rg, endereco, telefone, qtd_filhos, cargo, valor_hora):
    """
    Cadastra um funcionário na lista.
    """
    global funcionarios
    funcionarios = data_manager.load_data('funcionarios.json')
    
    func = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "endereco": endereco,
        "telefone": telefone,
        "qtd_filhos": qtd_filhos,
        "cargo": cargo,
        "valor_hora": valor_hora
    }
    funcionarios.append(func)
    data_manager.save_data('funcionarios.json', funcionarios)
    print(f"Funcionário {nome} cadastrado com sucesso.")

def calcular_salario_bruto(horas_trabalhadas, valor_hora):
    """
    Calcula salário bruto base.
    """
    return horas_trabalhadas * valor_hora

def calcular_horas_extras(horas_extras, valor_hora, cargo):
    """
    Calcula valor das horas extras.
    Gerentes e Diretores não recebem hora extra.
    """
    cargos_sem_extra = ["gerente", "diretor"]
    if cargo.lower() in cargos_sem_extra:
        return 0.0
    
    # Adicional de 50% na hora extra (padrão CLT simples para o exercício)
    valor_extra = horas_extras * (valor_hora * 1.5)
    return valor_extra

def calcular_irpf(salario_base):
    """
    Calcula o IRPF com base em tabela simplificada (exemplo 2024).
    """
    # Tabela progressiva simplificada (valores aproximados para exercício)
    if salario_base <= 2259.20:
        return 0.0
    elif salario_base <= 2826.65:
        return (salario_base * 0.075) - 169.44
    elif salario_base <= 3751.05:
        return (salario_base * 0.15) - 381.44
    elif salario_base <= 4664.68:
        return (salario_base * 0.225) - 662.77
    else:
        return (salario_base * 0.275) - 896.00

def calcular_liquido(salario_bruto, irpf):
    """
    Calcula salário líquido (Bruto - IRPF).
    Ignorando INSS para simplificação conforme enunciado foca em IRPF e faixas de desconto.
    """
    return salario_bruto - irpf

def gerar_folha_pagamento():
    """
    Gera relatório final com salários líquidos e IRPF.
    """
    print("\n--- Folha de Pagamento ---")
    
    # Ordenar por nome
    funcionarios_ordenados = sorted(funcionarios, key=lambda x: x["nome"])
    
    for f in funcionarios_ordenados:
        # Simulação de horas para o relatório (em um sistema real, viria de input ou ponto)
        horas_trab = 160 # Mensal padrão
        horas_ext = 10   # Exemplo
        
        bruto = calcular_salario_bruto(horas_trab, f["valor_hora"])
        extra = calcular_horas_extras(horas_ext, f["valor_hora"], f["cargo"])
        total_bruto = bruto + extra
        
        irpf = calcular_irpf(total_bruto)
        liquido = calcular_liquido(total_bruto, irpf)
        
        paga_ir = "Sim" if irpf > 0 else "Não"
        
        print(f"Nome: {f['nome']}")
        print(f"  Cargo: {f['cargo']}")
        print(f"  Salário Bruto: R$ {total_bruto:.2f}")
        print(f"  IRPF: R$ {irpf:.2f} ({paga_ir})")
        print(f"  Salário Líquido: R$ {liquido:.2f}")
        print("-" * 30)

if __name__ == "__main__":
    print("Iniciando módulo RH...")
    
    # Cadastrando 5 funcionários
    cadastrar_funcionario("Carlos Silva", "111", "RG1", "Rua A", "Tel1", 2, "Operario", 20.0)
    cadastrar_funcionario("Ana Souza", "222", "RG2", "Rua B", "Tel2", 1, "Gerente", 50.0)
    cadastrar_funcionario("Bruno Lima", "333", "RG3", "Rua C", "Tel3", 0, "Operario", 20.0)
    cadastrar_funcionario("Daniela Alves", "444", "RG4", "Rua D", "Tel4", 3, "Diretor", 100.0)
    cadastrar_funcionario("Eduardo Costa", "555", "RG5", "Rua E", "Tel5", 1, "Analista", 35.0)
    
    gerar_folha_pagamento()
