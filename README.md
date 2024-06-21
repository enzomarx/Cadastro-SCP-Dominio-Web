## README - Cadastro-SCP-Dominio-Web

### Descrição

Este script Python utiliza a biblioteca `pyautogui` para automatizar o processo de cadastro de SCPs (Sociedades em Conta de Participação) em um domínio web. O script lê os dados das SCPs a serem cadastradas a partir de um arquivo CSV e preenche os campos do formulário de cadastro no site.

### Pré-requisitos

* Python 3.x instalado
* Biblioteca `pyautogui` instalada: `pip install pyautogui`
* Biblioteca `pandas` instalada: `pip install pandas`
* Arquivo CSV contendo os dados das SCPs com as seguintes colunas:
    * `mat`: Matrícula da SCP
    * `empresa`: Nome da empresa
    * (Outras colunas conforme os campos do formulário de cadastro)

### Configuração

1. **Instalar as bibliotecas:**
    ```bash
    pip install pyautogui pandas
    ```
2. **Criar o arquivo CSV:**
    * Crie um arquivo CSV com as informações das SCPs, utilizando as colunas mencionadas acima.
    * Salve o arquivo CSV em um local acessível pelo script.
3. **Modificar o script:**
    * Abra o script `Cadastro-SCP-Dominio-Web.py` em um editor de texto.
    * Altere o caminho do arquivo CSV na linha 6:
        ```python
        tabela = pd.read_csv(r"C:\Users\PC\Desktop\Guia Erros.csv")
        ```
        Substitua `"C:\Users\PC\Desktop\Guia Erros.csv"` pelo caminho real do seu arquivo CSV.
    * Verifique se os valores de `pyautogui.PAUSE` (linha 2) e das coordenadas de clique (linhas 4-39) estão ajustados de acordo com a resolução da sua tela e o layout do site.

### Uso

1. **Executar o script:**
    * Abra um terminal ou prompt de comando.
    * Navegue até o diretório onde o script está salvo.
    * Execute o seguinte comando:
        ```bash
        python Cadastro-SCP-Dominio-Web.py
        ```
2. **Interação com o script:**
    * O script irá iniciar o processo de cadastro automático.
    * Aguarde a conclusão do processo para cada SCP.
    * O script pode solicitar interação manual em alguns momentos, como para confirmar pop-ups ou resolver CAPTCHAs.

### Observações

* Este script é um exemplo básico e pode precisar ser adaptado de acordo com as especificidades do site de cadastro e do formato do arquivo CSV.
* É importante testar o script com cuidado em um ambiente de teste antes de utilizá-lo em dados reais.
* A automação de tarefas em sites pode violar os termos de serviço, portanto, utilize o script com cautela e responsabilidade.

### Melhorias Futuras

* Implementar tratamento de erros para lidar com falhas no processo de cadastro.
* Adicionar opções para personalizar o script, como seleção de campos a serem preenchidos e configurações de tempo de espera.
* Criar uma interface gráfica para facilitar o uso do script.

### Contribuições

Este script é de código aberto e você pode contribuir com melhorias ou sugestões. Envie suas pull requests para o repositório do GitHub.
