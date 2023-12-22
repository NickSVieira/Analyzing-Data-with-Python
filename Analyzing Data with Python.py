#!/usr/bin/env python
# coding: utf-8

# # Python Insights - Analisando Dados com Python
# 
# ### Case - Cancelamento de Clientes
# 
# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

# In[1]:


# Pseudocogidico
# Passo 1: Importar a base dados OK
# Passo 2: Visualizar a base de dados OK
# Passo 3: Tratamento de erros (Corrigir os erros da base de dados) OK
# Tratar valorares vazios OK
# Retirar informacoes inuteis (informacao que nao te ajuda, te atrapalha) OK
# Passo 4: Analise inicial da base de dados (entender como estao os cancelamentos)
# Passo 5: Analise profunda da base de dados (encontrando a causa dos canelamentos)


# In[2]:


pip install pandas numpy openpyxl plotly


# In[3]:


# Passo 1 e 2
import pandas
tabela_cancel = pandas.read_csv('cancelamentos.csv')
#Passo 3
# linha --> axis = 0
# coluna --> axis = 1
tabela_cancel = tabela_cancel.drop('CustomerID', axis=1)
display(tabela_cancel)


# In[4]:


# Passo 3 continue
display(tabela_cancel.info())
tabela_cancel = tabela_cancel.dropna()
display(tabela_cancel.info())


# In[5]:


# Passo 4
display(tabela_cancel['cancelou'].value_counts())
display(tabela_cancel['cancelou'].value_counts(normalize=True))


# In[6]:


# Passo 4 continue

display(tabela_cancel.groupby("duracao_contrato").mean())
# Clientes que tem a assinatura Monthly tem 100% de cancelamento


# In[7]:


tabela_cancel = tabela_cancel[tabela_cancel['duracao_contrato']!='Monthly']
display(tabela_cancel['cancelou'].value_counts())
display(tabela_cancel['cancelou'].value_counts(normalize=True))


# In[8]:


# Passo 5
import plotly.express as px
for coluna in tabela_cancel.columns:
    grafico = px.histogram(tabela_cancel, x=coluna, color='cancelou')
    grafico.show()


# In[9]:


# Problema 1: Clientes assima de 51 anos de idade tem 100% de chance de cancelar
tabela_cancel = tabela_cancel[tabela_cancel['ligacoes_callcenter']<=51]
# Problema 2: Clientes que ligam mais de 5 vezes ao callcenter tem 100% de chance de cancelar
tabela_cancel = tabela_cancel[tabela_cancel['ligacoes_callcenter']<5]
# Problema 3: Clientes que atrasam o pagamento a cima de 21 dias tem 100% de chance de cancelar
tabela_cancel = tabela_cancel[tabela_cancel['dias_atraso']<=20]
# Problema 4: Clientes que gastam menos de R$500 tem 100% de chance de cancelar
tabela_cancel = tabela_cancel[tabela_cancel['total_gasto']>500]
# Problema 5: Clientes que adquirem a assinatura Monthly tem 100% de chance de cancelar
tabela_cancel = tabela_cancel[tabela_cancel['duracao_contrato']!='Monthly']
display(tabela_cancel['cancelou'].value_counts())
display(tabela_cancel['cancelou'].value_counts(normalize=True))


# ## Possivel resolucao para os problemas encontrados
# ### Problema 1: Clientes assima de 51 anos de idade tem 100% de chance de cancelar
# Facilidade de uso e acessibilidade: Adaptar a interface dos serviços, aplicativos ou site da empresa para torná-los mais amigáveis e acessíveis aos usuários mais velhos. Considerar a ampliação de fontes, uso de cores de alto contraste e uma navegação intuitiva.
# Ofertas e descontos especiais: Oferecer ofertas, descontos ou programas de fidelidade exclusivos para clientes acima de 51 anos pode incentivá-los a permanecer com a empresa por mais tempo.
# Programas de educação e suporte: Oferecer programas de educação e suporte para ajudar os clientes mais velhos a utilizar melhor os serviços e recursos disponíveis. Isso pode ser feito através de tutoriais, webinars, workshops ou até mesmo suporte técnico especializado.
# Feedback contínuo: Estabelecer um canal de comunicação aberto para receber feedback contínuo dos clientes acima de 51 anos, permitindo que eles expressem suas opiniões e sugestões para melhorias.
# Campanhas de marketing direcionadas: Desenvolver campanhas de marketing direcionadas especificamente para clientes mais velhos, destacando os benefícios do serviço para essa faixa etária.
# Parcerias com organizações e associações: Estabelecer parcerias com organizações ou associações que atendam a pessoas acima de 51 anos, para aumentar a conscientização sobre os serviços e oferecer benefícios exclusivos.
# Monitoramento de métricas: Monitorar regularmente as métricas de satisfação e retenção dos clientes acima de 51 anos para acompanhar o progresso e identificar áreas que precisam de melhorias contínuas.
# ### Problema 2: Clientes que ligam mais de 5 vezes ao callcenter tem 100% de chance de cancelar
# Melhorar o atendimento inicial: Garantir que o atendimento inicial seja rápido, eficiente e resolva o problema do cliente logo na primeira ligação. Treinar os atendentes para entenderem as necessidades do cliente desde o início e fornecer soluções eficazes.
# Atendimento ao cliente de qualidade: Investir em treinamento contínuo para o pessoal do call center, capacitando-os a lidar com situações desafiadoras de forma empática, cortês e profissional.
# Registro de histórico de chamadas: Manter um registro detalhado do histórico de chamadas e interações anteriores com cada cliente. Isso permitirá que os atendentes tenham acesso rápido às informações relevantes quando o cliente ligar novamente, evitando a repetição de perguntas e problemas.
# ### Problema 3: Clientes que atrasam o pagamento a cima de 21 dias tem 100% de chance de cancelar
# Opções de pagamento flexíveis: Oferecer opções de pagamento flexíveis, como parcelamentos ou datas de vencimento personalizadas, para acomodar as diferentes situações financeiras dos clientes.
# Descontos por pagamento antecipado: Oferecer descontos ou benefícios especiais para clientes que pagam suas faturas antes da data de vencimento, incentivando o pagamento pontual.
# Política de tolerância: Implementar uma política de tolerância para atrasos menores, permitindo que os clientes evitem taxas de atraso ou penalidades caso paguem a fatura dentro de um prazo razoável após a data de vencimento.
# Programas de fidelidade: Criar programas de fidelidade ou recompensas para clientes que mantêm um histórico de pagamentos pontuais, oferecendo incentivos para que eles continuem a cumprir com os prazos de pagamento.
# ### Problema 4: Clientes que gastam menos de reais 500 tem 100% de chance de cancelar
# Parcerias estratégicas: Estabelecer parcerias com outras empresas ou estabelecimentos para oferecer benefícios e descontos exclusivos aos clientes que gastam menos, incentivando o uso contínuo dos serviços.
# Ofertas e promoções personalizadas: Analisar o histórico de gastos de cada cliente e oferecer ofertas e promoções personalizadas que atendam às suas necessidades e interesses. Isso pode incentivar os clientes a permanecer com o serviço e aproveitar as vantagens exclusivas.
# Pacotes e planos flexíveis: Oferecer pacotes e planos flexíveis que sejam mais adequados às necessidades e ao orçamento dos clientes que gastam menos. Isso pode incluir opções mais econômicas ou pacotes com serviços essenciais para essa faixa de consumidores.
# ### Problema 5: Clientes que adquirem a assinatura Monthly tem 100% de chance de cancelar
# Oferecer benefícios adicionais: Incluir benefícios ou recursos exclusivos para os assinantes mensais, tornando a assinatura mais atraente e valiosa em relação às opções avulsas ou concorrentes.
# Ofertas de upgrade: Oferecer oportunidades de upgrade para planos com mais benefícios ou serviços adicionais, incentivando os assinantes a permanecerem na empresa.
# Personalização: Personalizar a experiência dos assinantes mensais com recomendações de conteúdo, serviços ou produtos com base em suas preferências e histórico de uso.
# # A implementação das orientações propostas tem o potencial de contribuir significativamente para a redução do problema de cancelamento dos clientes, resultando em uma diminuição substancial na taxa de cancelamento, possivelmente alcançando níveis entre 18% e 9%. No entanto, é importante reconhecer que a eficácia dessas ações pode ser influenciada por uma série de fatores adicionais, incluindo a resposta dos clientes às estratégias implementadas, as condições do mercado e a capacidade da empresa de se adaptar e melhorar continuamente suas práticas de atendimento e retenção de clientes.
