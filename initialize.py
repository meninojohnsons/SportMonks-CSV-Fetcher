import os

def criar_pasta(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"📁 Pasta criada: {caminho}")
    else:
        print(f"📂 Pasta já existe: {caminho}")

def criar_env():
    token = input("🔐 Informe seu API_TOKEN do SportMonks: ").strip()
    if not token:
        print("❌ O token não pode estar vazio.")
        return

    with open('.env', 'w') as f:
        f.write(f"API_TOKEN={token}\n")
    print("✅ Arquivo .env criado com sucesso.")

def instrucoes_uso():
    print("\n📘 Instruções de uso do SportMonks CSV Fetcher:\n")
    print("1. Adicione seus arquivos .csv brutos em: csv/input/")
    print("2. Execute o programa com:")
    print("   ▶️  python main.py")
    print("3. O programa irá gerar os arquivos processados em: csv/output/")
    print("4. Durante a execução, será solicitado:")
    print("   - Nome do time (ex: Flamengo)")
    print("   - ID da liga (ex: 1988)")
    print("   - Temporada (ex: 22_23)\n")
    print("📎 O token da API é carregado automaticamente do arquivo .env")

def main():
    print("🔧 Configurando o projeto SportMonks CSV Fetcher...")

    criar_env()
    criar_pasta('csv/input')
    criar_pasta('csv/output')
    criar_pasta('csv/temp')

    instrucoes_uso()

if __name__ == "__main__":
    main()
