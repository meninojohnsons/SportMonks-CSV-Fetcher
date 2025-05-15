# Guia de Contribuição

## 👋 Bem-vindo ao SportMonks CSV Fetcher!

Primeiro de tudo, obrigado por dedicar seu tempo para contribuir com este projeto! Qualquer contribuição que você fizer será refletida no [SportMonks CSV Fetcher](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher) 🎉

Este guia tem como objetivo fornecer uma visão geral de como você pode participar do desenvolvimento deste projeto.

## 🗺️ Índice

- [Código de Conduta](#código-de-conduta)
- [Eu tenho uma pergunta](#eu-tenho-uma-pergunta)
- [Como posso contribuir?](#como-posso-contribuir)
  - [Reportando bugs](#reportando-bugs)
  - [Sugerindo melhorias](#sugerindo-melhorias)
  - [Seu primeiro código](#seu-primeiro-código)
  - [Pull Requests](#pull-requests)
- [Estilo de código](#estilo-de-código)
- [Mensagens de commit](#mensagens-de-commit)
- [Configuração de desenvolvimento](#configuração-de-desenvolvimento)

## 📜 Código de Conduta

Este projeto e todos os participantes são regidos pelo [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, espera-se que você mantenha este código. Por favor, reporte comportamento inaceitável para [davimoreiraf@gmail.com](mailto:davimoreiraf@gmail.com).

## 🤔 Eu tenho uma pergunta

> Se você quer fazer uma pergunta, assumimos que você leu a [documentação](README.md) disponível.

Antes de fazer uma pergunta, é melhor procurar por [Issues existentes](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher/issues) que possam ajudar você. Caso você tenha encontrado um problema adequado e ainda precise de esclarecimentos, você pode escrever sua pergunta nessa issue. Também é aconselhável procurar respostas na internet primeiro.

Se você ainda sentir a necessidade de fazer uma pergunta e precisar de esclarecimentos, recomendamos o seguinte:

- Abra uma [Issue](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher/issues/new).
- Forneça o máximo de contexto possível sobre o que você está enfrentando.
- Forneça versões do projeto e da plataforma (Python, OS, etc), dependendo do que parece relevante.

Então abordaremos seu problema o mais rápido possível.

## 🛠 Como posso contribuir?

### 🐛 Reportando bugs

#### Antes de enviar um relatório de bug

Um bom relatório de bug não deve deixar os outros precisando procurar você para mais informações. Portanto, pedimos que você investigue cuidadosamente, colete informações e descreva o problema em detalhes em sua issue. Siga os passos abaixo antes de enviar um relatório de bug:

- Certifique-se de que você está usando a versão mais recente.
- Determine se seu bug é realmente um bug e não um erro de sua parte, por exemplo, usar componentes/APIs de ambiente incompatíveis (Certifique-se de ter lido a [documentação](README.md). Se você está procurando suporte, talvez queira verificar [esta seção](#eu-tenho-uma-pergunta)).
- Para ver se outros usuários já encontraram (e possivelmente já resolveram) o mesmo problema que você está tendo, verifique se já não existe um relatório de bug para seu bug ou erro no [bug tracker](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher/issues).
- Certifique-se de que você não está reportando um problema duplicado.
- Colete informações sobre o bug:
  - Rastreamento de pilha (Stack trace)
  - Sistema operacional, plataforma e versão (Windows, Linux, macOS, x86, ARM)
  - Versão do interpretador, compilador, SDK, ambiente de execução, gerente de pacotes, dependendo do que parece relevante.
  - Possivelmente sua entrada e a saída
  - Você pode conseguir isolar o problema? Por exemplo, um pequeno código base que reproduza o bug?

#### Como enviar um bom relatório de bug

Usamos issues do GitHub para rastrear bugs e erros. Se você encontrou um problema com o projeto:

- Abra uma [Issue](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher/issues/new).
- Explique o comportamento que você esperava e o comportamento real.
- Por favor, forneça o máximo de contexto possível e descreva as etapas pelas quais podemos reproduzir o problema.
- Forneça as informações que coletou no estágio anterior.

Uma vez que a issue estiver registrada:

- A equipe do projeto vai marcar a issue de acordo com a prioridade.
- Um membro da equipe tentará reproduzir o problema com suas etapas.
- Se reproduzível, a issue será marcada para conserto na próxima versão.

### 🚀 Sugerindo melhorias

Esta seção orienta você no envio de uma sugestão de melhoria para o SportMonks CSV Fetcher, incluindo recursos completamente novos e pequenas melhorias na funcionalidade existente. Seguir estas diretrizes ajudará os mantenedores e a comunidade a entender sua sugestão e encontrar sugestões relacionadas.

#### Antes de enviar uma melhoria

- Certifique-se de que você está usando a versão mais recente.
- Leia a [documentação](README.md) cuidadosamente e descubra se a funcionalidade já está coberta, talvez por uma configuração individual.
- Faça uma [pesquisa](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher/issues) para ver se a melhoria já foi sugerida. Se sim, adicione um comentário à issue existente em vez de abrir uma nova.
- Descubra se sua ideia se encaixa no escopo e objetivos do projeto. Cabe a você fazer um caso forte para convencer os desenvolvedores do projeto dos méritos deste recurso. Tenha em mente que queremos recursos que sejam úteis para a maioria dos usuários e não apenas para um pequeno subconjunto.

#### Como enviar uma boa sugestão de melhoria

As melhorias são rastreadas como [issues do GitHub](https://github.com/meninojohnsons/SportMonks-CSV-Fetcher/issues).

- Use um título claro e descritivo para identificar a sugestão.
- Forneça uma descrição passo a passo da melhoria sugerida em tantos detalhes quanto possível.
- Descreva o comportamento atual e explique qual comportamento você esperava ver e por quê. Neste ponto, você também pode contar quais alternativas não funcionam para você.
- Você pode querer incluir capturas de tela e GIFs animados que ajudam a demonstrar os passos ou apontar a parte à qual a sugestão está relacionada.
- Explique por que essa melhoria seria útil para a maioria dos usuários do SportMonks CSV Fetcher. Você também pode querer apontar outros projetos que resolveram melhor o mesmo problema.

### 👨‍💻 Seu primeiro código

#### Configuração local

Para configurar o SportMonks CSV Fetcher localmente para desenvolvimento:

1. Fork este repositório
2. Clone seu fork localmente
   ```bash
   git clone https://github.com/seu-usuario/SportMonks-CSV-Fetcher.git
   cd SportMonks-CSV-Fetcher
   ```
3. Crie um ambiente virtual
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # OU
   .venv\Scripts\activate     # Windows
   ```
4. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o script de inicialização para configurar a estrutura de diretórios e arquivo .env
   ```bash
   python initialize.py
   ```

#### Ambiente de desenvolvimento

Sugerimos trabalhar com:

- [Visual Studio Code](https://code.visualstudio.com/) com as extensões:
  - Python
  - Pylint
  - Black Formatter
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/)

#### Começando a trabalhar

1. Escolha uma issue para trabalhar
2. Comente na issue que você gostaria de trabalhá-la
3. Crie um branch para sua feature ou correção
   ```bash
   git checkout -b feature/nome-da-feature
   ```
4. Faça suas alterações
5. Teste suas alterações
6. Commit e push
   ```bash
   git add .
   git commit -m "feat: adiciona nova funcionalidade X"
   git push origin feature/nome-da-feature
   ```
7. Abra um Pull Request

### 🔄 Pull Requests

O processo descrito aqui tem vários objetivos:

- Manter a qualidade do projeto
- Fixar problemas que são importantes para os usuários
- Engajar a comunidade no desenvolvimento do projeto
- Permitir uma distribuição sustentável de desenvolvimento para mantenedores

Por favor, siga estes passos para ter seu trabalho considerado:

1. Siga todas as instruções em [o modelo de pull request](PULL_REQUEST_TEMPLATE.md)
2. Siga o [estilo de código](#estilo-de-código)
3. Depois de enviar seu pull request, verifique se todas as [verificações de status](https://help.github.com/articles/about-status-checks/) estão passando

Enquanto os pré-requisitos acima devem ser satisfeitos antes que o pull request seja mesclado, os revisores do projeto podem pedir que você complete testes adicionais, alterações ou outras mudanças antes que seu pull request possa ser aceito.

## 📝 Estilo de código

Seguimos as convenções PEP 8 para Python:

- Use 4 espaços para indentação (sem tabs)
- Use nomes de variáveis em snake_case
- Use nomes de classes em CamelCase
- Limite as linhas a 120 caracteres
- Docstrings para todas as funções, classes e métodos públicos
- Comentários explicativos quando necessário

Recomendamos usar ferramentas como `black` e `pylint` para formatação e verificação de código:

```bash
# Instalar ferramentas
pip install black pylint

# Formatação com black
black .

# Verificação com pylint
pylint sportmonk_facilitator/
```

## 💬 Mensagens de commit

Usamos [mensagens de commit convencionais](https://www.conventionalcommits.org/) para facilitar o registro de alterações:

- `feat:` para novas funcionalidades
- `fix:` para correções de bugs
- `docs:` para alterações na documentação
- `style:` para formatação de código (espaços em branco, ponto e vírgula, etc)
- `refactor:` para refatoração de código
- `test:` para adição ou correção de testes
- `chore:` para tarefas de manutenção

Exemplo:
```
feat: adiciona suporte para filtrar estatísticas por temporada

Adiciona um novo parâmetro na API que permite filtrar estatísticas
de times por temporada específica. Isso resolve a issue #42.
```

## ⚙️ Configuração de desenvolvimento

Para facilitar o desenvolvimento, sugerimos:

1. Configure um ambiente virtual dedicado para o projeto
2. Configure uma cópia separada da API para desenvolvimento/testes
3. Use dados de amostra (incluídos em `/examples`)
4. Execute testes regularmente

### Testes

Planejamos adicionar suporte para testes unitários e integração completos no futuro. Por enquanto, teste manualmente suas alterações:

1. Execute o script principal com diferentes parâmetros
2. Verifique se os CSV são gerados corretamente
3. Confirme se as requisições à API funcionam como esperado

---

## 🎉 Agradecemos sua contribuição para o SportMonks CSV Fetcher!

Qualquer dúvida, entre em contato conosco pelos issues ou por email.
