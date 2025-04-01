def main():
    aprovados = 0
    reprovados = 0
    total_alunos = 0

    while True:
        try:
            nota = input("Digite a nota do aluno (ou 'sair' para finalizar): ")
            if nota.lower() == 'sair':
                break
            nota = float(nota)
            total_alunos += 1
            if nota >= 5:
                aprovados += 1
            else:
                reprovados += 1
        except ValueError:
            print("Entrada inválida. Por favor, insira um número ou 'sair'.")

    print("\nResumo:")
    print(f"Quantidade de alunos aprovados: {aprovados}")
    print(f"Quantidade de alunos reprovados: {reprovados}")
    print(f"Quantidade total de alunos: {total_alunos}")

if __name__ == "__main__":
    main()