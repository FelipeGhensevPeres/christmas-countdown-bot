from datetime import datetime
from twilio.rest import Client


def chegando_natal():


    sid_conta = "SEU SID DA CONTA TWILLIO"
    token = "SEU TOKEN DA CONTA TWILLIO"

    cliente = Client(sid_conta,token)

    data_hoje = datetime.now()
    data_hoje_limpa = data_hoje.replace(second=0,microsecond=0)
    data_natal = datetime(2025,12,25, 0,0,0)

    dias_natal = data_natal - data_hoje_limpa
    passou_natal = data_hoje_limpa - data_natal

    if dias_natal.days > 1:
       mensagem = cliente.messages.create(
           to="+SEU NUMERO DE TELEFONE",
           from_="+NUMERO FORNECIDO PELO TWILLIO",
           body= f'Faltam {dias_natal.days} dias para o natal chegar, quando chegar rode este codigo e eu te avisarei!')
       
    elif dias_natal.days == 1:
       mensagem = cliente.messages.create(
           to="+SEU NUMERO DE TELEFONE",
           from_="+NUMERO FORNECIDO PELO TWILLIO",
           body= 'FALTA 1 DIA PARA O NATAL!!!')

    elif dias_natal.days == 0:
        mensagem = cliente.messages.create(
            to="+SEU NUMERO DE TELEFONE",
            from_="+NUMERO FORNECIDO PELO TWILLIO",
            body= 'HOJE TEM NATAL AS 00:00!!!!!')

    else:
        mensagem = cliente.messages.create(
            to="+SEU NUMERO DE TELEFONE",
            from_="+NUMERO FORNECIDO PELO TWILLIO",
            body= f'O natal ja passou faz {passou_natal} dias')
           
    
chegando_natal()












