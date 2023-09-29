CONFIG_RACAS = {
    
    "Humano": {

        "Modificadores_atributos":
            {   
                
                'forca_base': 2,
                'destreza_base': 0,
                'constituicao_base': 0,
                'inteligencia_base': 0,
                'sabedoria_base': 0,
                'carisma_base': 0,
                'AC': 8,
            },
        "Modificadores_proficiencia":
            {
                "Armas": 
                    {
                        "arma_teste": 0,
                    },
                "Vestimentas":
                    {
                        "vestimenta_teste": 0,
                    },
                "Itens":
                    {
                        "item_teste": 0,
                    }
            }
    },
    "Rato": {

        "Modificadores_atributos":
            {   
                
                'forca_base': -2,
                'destreza_base': 5,
                'constituicao_base': -3,
                'inteligencia_base': -5,
                'sabedoria_base': -5,
                'carisma_base': -5,
                'AC': 4,
            },
        "Modificadores_proficiencia":
            {
                "Armas": 
                    {
                        "arma_teste": 0,
                    },
                "Vestimentas":
                    {
                        "vestimenta_teste": 0,
                    },
                "Itens":
                    {
                        "item_teste": 0,
                    }
            }
    }  
}

CONFIG_CLASSES = {
    
    "Guerreiro": {

        "Modificadores_atributos":
            {   
                
                'forca_base': 2,
                'destreza_base': 0,
                'constituicao_base': 2,
                'inteligencia_base': 0,
                'sabedoria_base': 0,
                'carisma_base': 0,
                'AC': 3,
            },
        "Modificadores_proficiencia":
            {
                "Armas": 
                    {
                        "arma_teste": 0,
                    },
                "Vestimentas":
                    {
                        "vestimenta_teste": 0,
                    },
                "Itens":
                    {
                        "item_teste": 0,
                    }
            }
    } 
}
   
CONFIG_RARIDADE = {
    "Quebrado": 
        {"chance": 0.2,
         "poder": -2},
        
    "Comum": 
        {"chance": 0.4,
         "poder": 0},
        
    "Incomum": 
        {"chance": 0.2,
         "poder": 1},
    "Raro":
        {"chance": 0.1,
         "poder": 2},
    "Lendario":
        {"chance": 0.07,
         "poder": 3},
    "Mitico":
        {"chance": 0.03,
         "poder": 4},
}
    