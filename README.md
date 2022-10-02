# Prova de ABD

# User Story

## 1 - Cadastro de Produtos
  Como um usuário do sistema na parte da logística, eu quero ter todos os produtos dentros do sistema para controlar a entrada e saída dos itens, e assim, poder melhorar a logística e compra dos mesmos.

## 2 - Cadastro de Usuários
  Como um usuário do sistema na parte de vendas, é necessário ter todos os usuários cadastrados em uma base de dados e apartir dos dados, analisar o que eles gostam e entregar o produto que eles mais gostam e aumentar o número de vendas.

## 3 - Venda dos Produtos - Relação entre Usuários e Produtos
  Como um usuário do sistema na parte de análise de vendas, é preciso ter uma análise se a estratégia da cadastro de usuários no sentido de aumentar as vendas está ou não funcionando, e para isso um cadastro de cada venda efetuada é obrigatória.
  
# Critérios de Aceitação
  + 1.1 - Não é possível ter uma quantidade negativa de produtos.
  + 1.2 - Todo ID é único.
  + 1.3 - Todo produto deve estar SEMPRE anexada a um usuário.
  + 1.4 - Não pode haver um produto vazio.
  
  + 2.1 - Todo usuário deve ter um CPF, e o mesmo será usado como identificação do usuário.
  + 2.2 - Não pode haver um usuário vazio.
  + 2.3 - Deve ter uma data de admissão do cadastro do usuário.
  + 2.4 - Um endereço só pode estar atrelado a um usuário
  
  + 3.1 - Todo ID da venda é único.
  + 3.2 - Uma venda só pode estar atrelada a um usuário.
  + 3.3 - Não pode haver uma venda vazia cadastrada.
  
# Definition of Done
  + 1 - Para cada funcionalidade do projeto será necessário entregar um relatório de como foi feito tal *feature* explicando todos os detalhes.
  
  + 2 - É necessário entregar testes de qualidade do código se ele é eficaz ou não.

  + 3 - Para melhor entendimento da funcionalidade, é obrigatório apresentar em uma reunião todos os dados relevantes para o item número 2(dois) em forma de slides.

# Modelo Entidade Relacionamento

![mer_diagram_abd](https://user-images.githubusercontent.com/97915231/193430853-71093034-e084-43d4-9e41-943f15dadefc.JPG)

# Diagrama de Classes

![class_diagram_abd](https://user-images.githubusercontent.com/97915231/193430855-42b6fff9-f2cf-4c2b-997f-e3918a02145b.JPG)
