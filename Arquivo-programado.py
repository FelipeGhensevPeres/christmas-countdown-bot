from datetime import datetime
from twilio.rest import Client


def chegando_natal():


    sid_conta = "ACff4a8ea25e11dcdcbdc2ec838dccc257"
    token = "f6fef2a69f7e2036932cb856009dfa29"

    cliente = Client(sid_conta,token)

    data_hoje = datetime.now()
    data_hoje_limpa = data_hoje.replace(second=0,microsecond=0)
    data_natal = datetime(2025,12,25, 0,0,0)

    dias_natal = data_natal - data_hoje_limpa
    passou_natal = data_hoje_limpa - data_natal

    if dias_natal.days > 1:
       mensagem = cliente.messages.create(
           to="+5511943436836",
           from_="+12173975391",
           body= f'Faltam {dias_natal.days} dias para o natal chegar, quando chegar rode este codigo e eu te avisarei!')
       
    elif dias_natal.days == 1:
       mensagem = cliente.messages.create(
           to="+5511943436836",
           from_="+12173975391",
           body= 'FALTA 1 DIA PARA O NATAL!!!')

    elif dias_natal.days == 0:
        mensagem = cliente.messages.create(
            to="+5511943436836",
            from_="+12173975391",
            body= 'HOJE TEM NATAL AS 00:00!!!!!')

    else:
        mensagem = cliente.messages.create(
            to="+5511943436836",
            from_="+12173975391",
            body= f'O natal ja passou faz {passou_natal} dias')
           
    
chegando_natal()











