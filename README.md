# :money_with_wings: Calculadora de Droga e Lavagem

Uma aplicação gráfica em **Python + PyQt6** que calcula quantos "bonecos" (unidades) e quanto dinheiro limpo pode ser obtido a partir da quantidade de drogas informada, considerando o processo de lavagem de dinheiro em servidores RP (roleplay) ou simulações.

Ideal para simular recursos e verificar rapidamente os valores finais depois da lavagem, facilitando organização e tomada de decisões nos servidores.

---

## :clipboard: O que este projeto faz

- Permite inserir as quantidades disponíveis de drogas (**Metanfetamina**, **Cocaína**, **Erva**) em gramas.
- Permite adicionar bonecos extras e o valor manual de dinheiro sujo (caso queira sobrescrever o cálculo padrão).
- Define a taxa (%) retirada durante a lavagem de dinheiro.
- Calcula automaticamente:
  - Bonecos por drogas.
  - Bonecos extras informados manualmente.
  - Total de bonecos.
  - Dinheiro sujo (calculado ou manual).
  - Dinheiro limpo após aplicar a porcentagem de lavagem.
- Interface moderna, limpa e interativa feita com **PyQt6**.
- Visualização detalhada dos resultados, incluindo destaques em cores para cada tipo de valor.

---

## :gear: Requisitos

- **Python 3.7+**
- **PyQt6**

---

## :wrench: Instalação

1. Instale o PyQt6 (caso não tenha):
   ```bash
   pip install PyQt6
   ```

2. Baixe ou copie o arquivo do projeto e salve como `calculadora_droga.py`.

---

## :rocket: Como executar

```bash
python calculadora_droga.py
```

---

## :book: Como funciona o cálculo

- **Bonecos por drogas:** Cada 100g de qualquer droga corresponde a 1 boneco.
- **Dinheiro sujo:** Cada boneco rende R$32.000.
- **Dinheiro limpo:** Dinheiro sujo após aplicar a taxa de lavagem (%).

Se o campo de dinheiro sujo manual for preenchido, esse valor é utilizado no lugar do calculado automaticamente.

---

## :pencil: Licença

Distribuído sem garantia, para fins didáticos e roleplay apenas.

```
MIT License
```