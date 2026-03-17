import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Entrada
capital   = float(input('Capital inicial: '))
aporte    = float(input('Aporte mensal: '))
meses     = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual %: '))/100    
perc_cdb  = float(input('Percentual do CDI - CDB (%): '))/100
perc_lci  = float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii  = float(input('Rentabilidade do FII (%): '))/100
Meta      = float(input('Meta financeira (R$): '))

#Conversão CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1

#Total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb             = cdi_mensal * perc_cdb
montante_cdb         = (capital * math.pow((1+taxa_cdb),meses))+ (aporte * meses)
lucro_cdb            = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI/LCA
taxa_lci     = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses))+(aporte * meses)

#Poupança
taxa_poupanca       = 0.005
montante_poupanca   = (capital * math.pow((1+taxa_poupanca),meses)) + (aporte * meses)

#FII
montante_fii_base = (capital * math.pow((1+taxa_fii),meses)) + (aporte * meses)

#Simulações de risco - FII
fii1 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii2 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii3 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii4 = montante_fii_base * (1 + random.uniform(-0.03,0.03))
fii5 = montante_fii_base * (1 + random.uniform(-0.03,0.03))

#Lista para estatística - FII
simulacoes_fii = [fii1,fii2,fii3,fii4,fii5]

#Indicadores estatísticos - FII
media_fii   = statistics.mean(simulacoes_fii)
mediana_fii = statistics.median(simulacoes_fii)
desvio_fii  = statistics.stdev(simulacoes_fii)

#Data atual - Data de Resgate
data_atual = datetime.datetime.now()

#Converter meses em dias (30 dias por mês) - Data de Resgate
dias_investimento = meses * 30

#Data estimada de resgate - Data de Resgate
data_resgate = data_atual + datetime.timedelta(days=dias_investimento)

#Formatar valores em moeda brasileira
total_fmt      = locale.currency(total_investido, grouping=True)
cdb_fmt        = locale.currency(montante_cdb_liquido, grouping=True)
lci_fmt        = locale.currency(montante_lci, grouping=True)
poupanca_fmt   = locale.currency(montante_poupanca, grouping=True)
fii_fmt        = locale.currency(media_fii, grouping=True)

#Formatar datas
data_simulacao   = data_atual.strftime('%d/%m/%Y')
data_resgate_fmt = data_resgate.strftime('%d/%m/%Y')

#Meta financeira
meta_atingida = media_fii >= Meta

print('\n========================================')
print(' PyInvest - Simulador de Investimentos')
print('========================================')
print(f'Data da simulação: {data_atual.strftime("%d/%m/%Y")}')
print(f'Data estimada de resgate: {data_resgate.strftime("%d/%m/%Y")}')
print('========================================\n')

print(f'Total investido: {locale.currency(total_investido, grouping=True)}')

print('\n--- RESULTADOS FINANCEIROS ---')

#CDB
print(f'CDB: {locale.currency(montante_cdb_liquido, grouping=True)}')
print('█' * int(montante_cdb_liquido / 1000))

#LCI/LCA
print(f'\nLCI/LCA: {locale.currency(montante_lci, grouping=True)}')
print('█' * int(montante_lci / 1000))

#Poupança
print(f'\nPoupança: {locale.currency(montante_poupanca, grouping=True)}')
print('█' * int(montante_poupanca / 1000))

#FII
print(f'\nFII (média): {locale.currency(media_fii, grouping=True)}')
print('█' * int(media_fii / 1000))

print('\n--- ESTATÍSTICAS FII ---')
print(f'Mediana: {locale.currency(mediana_fii, grouping=True)}')
print(f'Desvio padrão: {locale.currency(desvio_fii, grouping=True)}')

print(f'\nMeta atingida? {meta_atingida}')
print('========================================')
