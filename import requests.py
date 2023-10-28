import requests

def verificar_conexao(site_url):
    try:
        response = requests.get(site_url)
        if response.status_code == 200:
            return "O site está online e acessível."
        else:
            return f"O site está online, mas retornou o status {response.status_code}."
    except requests.ConnectionError:
        return "Não foi possível conectar ao site. O site pode estar offline ou inacessível."

if __name__ == "__main__":
    site_url = "https://www.example.com"  # Substitua esta linha pela URL desejada
    status = verificar_conexao(site_url)
    print(status)