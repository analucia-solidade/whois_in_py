import whois

def obter_info_whois(nome_do_domínio):
    try:
        info = whois.whois(nome_do_domínio)
        return info
    except Exception as e:
        return str(e)

def main():
    nome_do_domínio = input("Digite o nome do domínio para pesquisar WHOIS: ")
    info = obter_info_whois(nome_do_domínio)
    print(info)

if __name__ == "__main__":
    main()
