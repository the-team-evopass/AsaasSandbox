import requests

def DeleteSubscriptions(id_assinatura):
    url = f'https://sandbox.asaas.com/api/v3/subscriptions/{id_assinatura}'
    headers = {
        "accept": "application/json",
        "access_token": "$aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAwNTg2MTM6OiRhYWNoXzViZjJiMzRmLTU5MDEtNGFjOC1iOGFjLTUwYTIyYWU3NjRjOQ==" 
    }
    resposta_delete_assiantura = requests.delete(url, headers=headers)

    if resposta_delete_assiantura.status_code == 200:
        print(f"A assinatura do id {id_assinatura} foi apagada")
    else:
        print(f"Falha ao apagar a assinatura do id {id_assinatura}")

def ListAndDeleteSubscriptions():
    url = 'https://sandbox.asaas.com/api/v3/subscriptions'
    headers = {
        "accept": "application/json",
        "access_token": "$aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAwNTg2MTM6OiRhYWNoXzViZjJiMzRmLTU5MDEtNGFjOC1iOGFjLTUwYTIyYWU3NjRjOQ=="  
    }

    limite_pag = 100
    offset = 0

    while True:
        params = {
            'limit': limite_pag,
            'offset': offset
        }
        response_list = requests.get(url, headers=headers, params=params)

        if response_list.status_code == 200:
            data = response_list.json()['data']
            if not data:
                print('Sem cobranças no Asaas Sandbox')
                break
            for assinatura in data:
                id_assinatura = assinatura['id']
                DeleteSubscriptions(id_assinatura)
            offset += limite_pag
        else:
            print("Falha ao obter a lista de cobranças")
            break

ListAndDeleteSubscriptions()