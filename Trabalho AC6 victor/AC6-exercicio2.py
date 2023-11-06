import json

alunos = {
    "1234": {
        "nome": "André Guimarães",
        "e-mail": "andre.guim@gmail.com"
    },
    "5678": {
        "nome": "Vanessa Barboza",
        "e-mail": "vbarboza@yahoo.com"
    },
    "9012": {
        "nome": "Renato Amorim",
        "e-mail": "ream@hotmail.com"
    }
}

with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)