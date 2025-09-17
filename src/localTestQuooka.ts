const data = [
    {
        "ID Entrega": "TRK-3000",
        "Data Saída": "2025-08-01",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Rio de Janeiro - RJ",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 1300,
        "Custo Frete": "R$ 1.950,00"
    },
    {
        "ID Entrega": "TRK-3001",
        "Data Saída": "2025-08-01",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Recife - PE",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.250,00"
    },
    {
        "ID Entrega": "TRK-3002",
        "Data Saída": "2025-08-02",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Fortaleza - CE",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 500,
        "Custo Frete": "R$ 950,00"
    },
    {
        "ID Entrega": "TRK-3003",
        "Data Saída": "2025-08-02",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Brasília - DF",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 1400,
        "Custo Frete": "R$ 2.750,00"
    },
    {
        "ID Entrega": "TRK-3004",
        "Data Saída": "2025-08-03",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Aracaju - SE",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 850,
        "Custo Frete": "R$ 1.400,00"
    },
    {
        "ID Entrega": "TRK-3005",
        "Data Saída": "2025-08-03",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Natal - RN",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 700,
        "Custo Frete": "R$ 1.200,00"
    },
    {
        "ID Entrega": "TRK-3006",
        "Data Saída": "2025-08-04",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Macapá - AP",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 750,
        "Custo Frete": "R$ 1.800,00"
    },
    {
        "ID Entrega": "TRK-3007",
        "Data Saída": "2025-08-04",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Campinas - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 900,
        "Custo Frete": "R$ 1.700,00"
    },
    {
        "ID Entrega": "TRK-3008",
        "Data Saída": "2025-08-04",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Maceió - AL",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 2000,
        "Custo Frete": "R$ 3.400,00"
    },
    {
        "ID Entrega": "TRK-3009",
        "Data Saída": "2025-08-05",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Vitória - ES",
        "Tipo de Carga": "Alimentos",
        "Peso (kg)": 1200,
        "Custo Frete": "R$ 2.100,00"
    },
    {
        "ID Entrega": "TRK-3010",
        "Data Saída": "2025-08-05",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Joinville - SC",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 1600,
        "Custo Frete": "R$ 2.800,00"
    },
    {
        "ID Entrega": "TRK-3011",
        "Data Saída": "2025-08-05",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Ribeirão Preto - SP",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 400,
        "Custo Frete": "R$ 900,00"
    },
    {
        "ID Entrega": "TRK-3012",
        "Data Saída": "2025-08-06",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São José dos Campos - SP",
        "Tipo de Carga": "Eletrodomésticos",
        "Peso (kg)": 1200,
        "Custo Frete": "R$ 2.400,00"
    },
    {
        "ID Entrega": "TRK-3013",
        "Data Saída": "2025-08-06",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Caxias do Sul - RS",
        "Tipo de Carga": "Materiais de Construção",
        "Peso (kg)": 2500,
        "Custo Frete": "R$ 4.000,00"
    },
    {
        "ID Entrega": "TRK-3014",
        "Data Saída": "2025-08-06",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Florianópolis - SC",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 800,
        "Custo Frete": "R$ 1.500,00"
    },
    {
        "ID Entrega": "TRK-3015",
        "Data Saída": "2025-08-07",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Natal - RN",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 450,
        "Custo Frete": "R$ 1.000,00"
    },
    {
        "ID Entrega": "TRK-3016",
        "Data Saída": "2025-08-07",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Belém - PA",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 900,
        "Custo Frete": "R$ 1.700,00"
    },
    {
        "ID Entrega": "TRK-3017",
        "Data Saída": "2025-08-07",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Aracaju - SE",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 2100,
        "Custo Frete": "R$ 3.200,00"
    },
    {
        "ID Entrega": "TRK-3018",
        "Data Saída": "2025-08-07",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Sorocaba - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 650,
        "Custo Frete": "R$ 1.250,00"
    },
    {
        "ID Entrega": "TRK-3019",
        "Data Saída": "2025-08-07",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Uberlândia - MG",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 500,
        "Custo Frete": "R$ 950,00"
    },
    {
        "ID Entrega": "TRK-3020",
        "Data Saída": "2025-08-08",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Anápolis - GO",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.300,00"
    },
    {
        "ID Entrega": "TRK-3021",
        "Data Saída": "2025-08-08",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São Paulo - SP",
        "Tipo de Carga": "Materiais de Construção",
        "Peso (kg)": 2300,
        "Custo Frete": "R$ 3.800,00"
    },
    {
        "ID Entrega": "TRK-3022",
        "Data Saída": "2025-08-08",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Pelotas - RS",
        "Tipo de Carga": "Eletrodomésticos",
        "Peso (kg)": 1500,
        "Custo Frete": "R$ 2.600,00"
    },
    {
        "ID Entrega": "TRK-3023",
        "Data Saída": "2025-08-08",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Macapá - AP",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 750,
        "Custo Frete": "R$ 1.850,00"
    },
    {
        "ID Entrega": "TRK-3024",
        "Data Saída": "2025-08-08",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Feira de Santana - BA",
        "Tipo de Carga": "Alimentos",
        "Peso (kg)": 1600,
        "Custo Frete": "R$ 2.600,00"
    },
    {
        "ID Entrega": "TRK-3025",
        "Data Saída": "2025-08-09",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Maringá - PR",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 400,
        "Custo Frete": "R$ 850,00"
    },
    {
        "ID Entrega": "TRK-3026",
        "Data Saída": "2025-08-09",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Campinas - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 550,
        "Custo Frete": "R$ 1.050,00"
    },
    {
        "ID Entrega": "TRK-3027",
        "Data Saída": "2025-08-09",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Novo Hamburgo - RS",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 1900,
        "Custo Frete": "R$ 3.200,00"
    },
    {
        "ID Entrega": "TRK-3028",
        "Data Saída": "2025-08-09",
        "Centro de Distribuição": "CD Recife",
        "Destino": "João Pessoa - PB",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 700,
        "Custo Frete": "R$ 1.600,00"
    },
    {
        "ID Entrega": "TRK-3029",
        "Data Saída": "2025-08-10",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Boa Vista - RR",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 950,
        "Custo Frete": "R$ 2.000,00"
    },
    {
        "ID Entrega": "TRK-3030",
        "Data Saída": "2025-08-10",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Santos - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 700,
        "Custo Frete": "R$ 1.400,00"
    },
    {
        "ID Entrega": "TRK-3031",
        "Data Saída": "2025-08-10",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Curitiba - PR",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 1300,
        "Custo Frete": "R$ 2.600,00"
    },
    {
        "ID Entrega": "TRK-3032",
        "Data Saída": "2025-08-10",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Belo Horizonte - MG",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.250,00"
    },
    {
        "ID Entrega": "TRK-3033",
        "Data Saída": "2025-08-11",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Recife - PE",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 1800,
        "Custo Frete": "R$ 3.100,00"
    },
    {
        "ID Entrega": "TRK-3034",
        "Data Saída": "2025-08-11",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Salvador - BA",
        "Tipo de Carga": "Alimentos",
        "Peso (kg)": 1700,
        "Custo Frete": "R$ 2.900,00"
    },
    {
        "ID Entrega": "TRK-3035",
        "Data Saída": "2025-08-11",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Porto Alegre - RS",
        "Tipo de Carga": "Materiais de Construção",
        "Peso (kg)": 2600,
        "Custo Frete": "R$ 4.200,00"
    },
    {
        "ID Entrega": "TRK-3036",
        "Data Saída": "2025-08-12",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São Paulo - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 650,
        "Custo Frete": "R$ 1.350,00"
    },
    {
        "ID Entrega": "TRK-3037",
        "Data Saída": "2025-08-12",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Joinville - SC",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 500,
        "Custo Frete": "R$ 1.100,00"
    },
    {
        "ID Entrega": "TRK-3038",
        "Data Saída": "2025-08-12",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Macapá - AP",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 800,
        "Custo Frete": "R$ 1.900,00"
    },
    {
        "ID Entrega": "TRK-3039",
        "Data Saída": "2025-08-13",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Vitória - ES",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 550,
        "Custo Frete": "R$ 1.100,00"
    },
    {
        "ID Entrega": "TRK-3040",
        "Data Saída": "2025-08-13",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Campinas - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 900,
        "Custo Frete": "R$ 1.750,00"
    },
    {
        "ID Entrega": "TRK-3041",
        "Data Saída": "2025-08-13",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Maceió - AL",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 2200,
        "Custo Frete": "R$ 3.700,00"
    },
    {
        "ID Entrega": "TRK-3042",
        "Data Saída": "2025-08-14",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Brasília - DF",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 1500,
        "Custo Frete": "R$ 2.900,00"
    },
    {
        "ID Entrega": "TRK-3043",
        "Data Saída": "2025-08-14",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Caxias do Sul - RS",
        "Tipo de Carga": "Materiais de Construção",
        "Peso (kg)": 2700,
        "Custo Frete": "R$ 4.500,00"
    },
    {
        "ID Entrega": "TRK-3044",
        "Data Saída": "2025-08-14",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São José dos Campos - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 700,
        "Custo Frete": "R$ 1.450,00"
    },
    {
        "ID Entrega": "TRK-3045",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Florianópolis - SC",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.200,00"
    },
    {
        "ID Entrega": "TRK-3046",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Macapá - AP",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 850,
        "Custo Frete": "R$ 2.000,00"
    },
    {
        "ID Entrega": "TRK-3047",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Fortaleza - CE",
        "Tipo de Carga": "Alimentos",
        "Peso (kg)": 1900,
        "Custo Frete": "R$ 3.000,00"
    },
    {
        "ID Entrega": "TRK-3048",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Sorocaba - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 750,
        "Custo Frete": "R$ 1.500,00"
    },
    {
        "ID Entrega": "TRK-3049",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Uberlândia - MG",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 650,
        "Custo Frete": "R$ 1.350,00"
    },
    {
        "ID Entrega": "TRK-4001",
        "Data Saída": "2025-08-10",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Rio de Janeiro - RJ",
        "Tipo de Carga": "Eletrodomésticos",
        "Peso (kg)": 1200,
        "Custo Frete": "R$ 2.400,00"
    },
    {
        "ID Entrega": "TRK-4002",
        "Data Saída": "2025-08-11",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Rio de Janeiro - RJ",
        "Tipo de Carga": "Eletrodomésticos",
        "Peso (kg)": 1300,
        "Custo Frete": "R$ 2.600,00"
    },
    {
        "ID Entrega": "TRK-4003",
        "Data Saída": "2025-08-12",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São Paulo - SP",
        "Tipo de Carga": "Eletrodomésticos",
        "Peso (kg)": 1100,
        "Custo Frete": "R$ 2.200,00"
    },
    {
        "ID Entrega": "TRK-4004",
        "Data Saída": "2025-08-10",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Vitória - ES",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 300,
        "Custo Frete": "R$ 950,00"
    },
    {
        "ID Entrega": "TRK-4005",
        "Data Saída": "2025-08-11",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Vitória - ES",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 350,
        "Custo Frete": "R$ 1.100,00"
    },
    {
        "ID Entrega": "TRK-4006",
        "Data Saída": "2025-08-13",
        "Centro de Distribuição": "CD Belo Horizonte",
        "Destino": "Uberlândia - MG",
        "Tipo de Carga": "Medicamentos",
        "Peso (kg)": 280,
        "Custo Frete": "R$ 900,00"
    },
    {
        "ID Entrega": "TRK-4007",
        "Data Saída": "2025-08-12",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Fortaleza - CE",
        "Tipo de Carga": "Alimentos",
        "Peso (kg)": 1800,
        "Custo Frete": "R$ 3.200,00"
    },
    {
        "ID Entrega": "TRK-4008",
        "Data Saída": "2025-08-14",
        "Centro de Distribuição": "CD Salvador",
        "Destino": "Recife - PE",
        "Tipo de Carga": "Alimentos",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.200,00"
    },
    {
        "ID Entrega": "TRK-4009",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Joinville - SC",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 500,
        "Custo Frete": "R$ 1.150,00"
    },
    {
        "ID Entrega": "TRK-4010",
        "Data Saída": "2025-08-13",
        "Centro de Distribuição": "CD Curitiba",
        "Destino": "Florianópolis - SC",
        "Tipo de Carga": "Papelaria",
        "Peso (kg)": 450,
        "Custo Frete": "R$ 1.100,00"
    },
    {
        "ID Entrega": "TRK-4011",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Campinas - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 850,
        "Custo Frete": "R$ 1.800,00"
    },
    {
        "ID Entrega": "TRK-4012",
        "Data Saída": "2025-08-16",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Ribeirão Preto - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 400,
        "Custo Frete": "R$ 900,00"
    },
    {
        "ID Entrega": "TRK-4013",
        "Data Saída": "2025-08-17",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Brasília - DF",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 1400,
        "Custo Frete": "R$ 2.750,00"
    },
    {
        "ID Entrega": "TRK-4014",
        "Data Saída": "2025-08-18",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Anápolis - GO",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.200,00"
    },
    {
        "ID Entrega": "TRK-4015",
        "Data Saída": "2025-08-19",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Maceió - AL",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 2100,
        "Custo Frete": "R$ 3.600,00"
    },
    {
        "ID Entrega": "TRK-4016",
        "Data Saída": "2025-08-20",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Aracaju - SE",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 900,
        "Custo Frete": "R$ 1.800,00"
    },
    {
        "ID Entrega": "TRK-4017",
        "Data Saída": "2025-08-21",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Caxias do Sul - RS",
        "Tipo de Carga": "Materiais de Construção",
        "Peso (kg)": 2500,
        "Custo Frete": "R$ 4.000,00"
    },
    {
        "ID Entrega": "TRK-4018",
        "Data Saída": "2025-08-22",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São José dos Campos - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.300,00"
    },
    {
        "ID Entrega": "TRK-4019",
        "Data Saída": "2025-08-23",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Santos - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 400,
        "Custo Frete": "R$ 900,00"
    },
    {
        "ID Entrega": "TRK-4020",
        "Data Saída": "2025-08-24",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Macapá - AP",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 750,
        "Custo Frete": "R$ 1.800,00"
    },
    {
        "ID Entrega": "TRK-4011",
        "Data Saída": "2025-08-15",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Campinas - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 850,
        "Custo Frete": "R$ 1.800,00"
    },
    {
        "ID Entrega": "TRK-4012",
        "Data Saída": "2025-08-16",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Ribeirão Preto - SP",
        "Tipo de Carga": "Eletrônicos",
        "Peso (kg)": 400,
        "Custo Frete": "R$ 900,00"
    },
    {
        "ID Entrega": "TRK-4013",
        "Data Saída": "2025-08-17",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Brasília - DF",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 1400,
        "Custo Frete": "R$ 2.750,00"
    },
    {
        "ID Entrega": "TRK-4014",
        "Data Saída": "2025-08-18",
        "Centro de Distribuição": "CD Goiânia",
        "Destino": "Anápolis - GO",
        "Tipo de Carga": "Autopeças",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.200,00"
    },
    {
        "ID Entrega": "TRK-4015",
        "Data Saída": "2025-08-19",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Maceió - AL",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 2100,
        "Custo Frete": "R$ 3.600,00"
    },
    {
        "ID Entrega": "TRK-4016",
        "Data Saída": "2025-08-20",
        "Centro de Distribuição": "CD Recife",
        "Destino": "Aracaju - SE",
        "Tipo de Carga": "Bebidas",
        "Peso (kg)": 900,
        "Custo Frete": "R$ 1.800,00"
    },
    {
        "ID Entrega": "TRK-4017",
        "Data Saída": "2025-08-21",
        "Centro de Distribuição": "CD Porto Alegre",
        "Destino": "Caxias do Sul - RS",
        "Tipo de Carga": "Materiais de Construção",
        "Peso (kg)": 2500,
        "Custo Frete": "R$ 4.000,00"
    },
    {
        "ID Entrega": "TRK-4018",
        "Data Saída": "2025-08-22",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "São José dos Campos - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 600,
        "Custo Frete": "R$ 1.300,00"
    },
    {
        "ID Entrega": "TRK-4019",
        "Data Saída": "2025-08-23",
        "Centro de Distribuição": "CD São Paulo",
        "Destino": "Santos - SP",
        "Tipo de Carga": "Vestuário",
        "Peso (kg)": 400,
        "Custo Frete": "R$ 900,00"
    },
    {
        "ID Entrega": "TRK-4020",
        "Data Saída": "2025-08-24",
        "Centro de Distribuição": "CD Belém",
        "Destino": "Macapá - AP",
        "Tipo de Carga": "Produtos de Higiene",
        "Peso (kg)": 750,
        "Custo Frete": "R$ 1.800,00"
    }
]

const dataVendas = [
    {
        "Código Venda": "65056",
        "Data": "12/1/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Calça",
        "Quantidade": "2",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 340.00"
    },
    {
        "Código Venda": "65501",
        "Data": "12/3/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Camisa",
        "Quantidade": "3",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 300.00"
    },
    {
        "Código Venda": "65707",
        "Data": "12/4/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Bermuda",
        "Quantidade": "1",
        "Valor Unitário": "R$ 150.00",
        "Valor Final": "R$ 150.00"
    },
    {
        "Código Venda": "65750",
        "Data": "12/4/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Bermuda",
        "Quantidade": "4",
        "Valor Unitário": "R$ 150.00",
        "Valor Final": "R$ 600.00"
    },
    {
        "Código Venda": "65810",
        "Data": "12/5/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Chinelo",
        "Quantidade": "1",
        "Valor Unitário": "R$ 60.00",
        "Valor Final": "R$ 60.00"
    },
    {
        "Código Venda": "65830",
        "Data": "12/5/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Gorro",
        "Quantidade": "2",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 160.00"
    },
    {
        "Código Venda": "65859",
        "Data": "12/5/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Bermuda",
        "Quantidade": "4",
        "Valor Unitário": "R$ 150.00",
        "Valor Final": "R$ 600.00"
    },
    {
        "Código Venda": "65893",
        "Data": "12/5/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Gorro",
        "Quantidade": "3",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 240.00"
    },
    {
        "Código Venda": "66029",
        "Data": "12/6/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Cinto",
        "Quantidade": "2",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 400.00"
    },
    {
        "Código Venda": "66040",
        "Data": "12/6/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Chinelo",
        "Quantidade": "1",
        "Valor Unitário": "R$ 60.00",
        "Valor Final": "R$ 60.00"
    },
    {
        "Código Venda": "66240",
        "Data": "12/7/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Bermuda",
        "Quantidade": "3",
        "Valor Unitário": "R$ 150.00",
        "Valor Final": "R$ 450.00"
    },
    {
        "Código Venda": "66304",
        "Data": "12/7/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Gorro",
        "Quantidade": "1",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 80.00"
    },
    {
        "Código Venda": "66321",
        "Data": "12/7/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Camisa",
        "Quantidade": "1",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 100.00"
    },
    {
        "Código Venda": "66404",
        "Data": "12/8/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Calça",
        "Quantidade": "5",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 850.00"
    },
    {
        "Código Venda": "66637",
        "Data": "12/9/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Calça",
        "Quantidade": "3",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 510.00"
    },
    {
        "Código Venda": "66672",
        "Data": "12/9/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Cinto",
        "Quantidade": "3",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 600.00"
    },
    {
        "Código Venda": "66713",
        "Data": "12/9/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Camisa",
        "Quantidade": "2",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "66724",
        "Data": "12/10/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Cinto",
        "Quantidade": "3",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 600.00"
    },
    {
        "Código Venda": "66945",
        "Data": "12/11/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Calça",
        "Quantidade": "1",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 170.00"
    },
    {
        "Código Venda": "67063",
        "Data": "12/11/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Gorro",
        "Quantidade": "3",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 240.00"
    },
    {
        "Código Venda": "67469",
        "Data": "12/13/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Chinelo",
        "Quantidade": "1",
        "Valor Unitário": "R$ 60.00",
        "Valor Final": "R$ 60.00"
    },
    {
        "Código Venda": "67571",
        "Data": "12/14/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Camisa",
        "Quantidade": "3",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 300.00"
    },
    {
        "Código Venda": "67907",
        "Data": "12/15/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Camisa",
        "Quantidade": "5",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 500.00"
    },
    {
        "Código Venda": "68113",
        "Data": "12/16/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Calça",
        "Quantidade": "1",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 170.00"
    },
    {
        "Código Venda": "68217",
        "Data": "12/17/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Camisa",
        "Quantidade": "1",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 100.00"
    },
    {
        "Código Venda": "68226",
        "Data": "12/17/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Camisa",
        "Quantidade": "2",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "68275",
        "Data": "12/17/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Bermuda",
        "Quantidade": "2",
        "Valor Unitário": "R$ 150.00",
        "Valor Final": "R$ 300.00"
    },
    {
        "Código Venda": "68409",
        "Data": "12/17/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Calça",
        "Quantidade": "1",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 170.00"
    },
    {
        "Código Venda": "68480",
        "Data": "12/18/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Gorro",
        "Quantidade": "1",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 80.00"
    },
    {
        "Código Venda": "68753",
        "Data": "12/19/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Camisa",
        "Quantidade": "2",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "68989",
        "Data": "12/20/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Gorro",
        "Quantidade": "1",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 80.00"
    },
    {
        "Código Venda": "69104",
        "Data": "12/21/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Camisa",
        "Quantidade": "1",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 100.00"
    },
    {
        "Código Venda": "69104",
        "Data": "12/21/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Camisa",
        "Quantidade": "3",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 300.00"
    },
    {
        "Código Venda": "69115",
        "Data": "12/21/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Camisa",
        "Quantidade": "1",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 100.00"
    },
    {
        "Código Venda": "69145",
        "Data": "12/21/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Cinto",
        "Quantidade": "2",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 400.00"
    },
    {
        "Código Venda": "69184",
        "Data": "12/21/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Camisa",
        "Quantidade": "2",
        "Valor Unitário": "R$ 100.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "69220",
        "Data": "12/22/19",
        "ID Loja": "Iguatemi Esplanada",
        "Produto": "Cinto",
        "Quantidade": "1",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "69286",
        "Data": "12/22/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Gorro",
        "Quantidade": "2",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 160.00"
    },
    {
        "Código Venda": "69676",
        "Data": "12/24/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Gorro",
        "Quantidade": "4",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 320.00"
    },
    {
        "Código Venda": "69714",
        "Data": "12/24/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Cinto",
        "Quantidade": "2",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 400.00"
    },
    {
        "Código Venda": "69730",
        "Data": "12/24/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Gorro",
        "Quantidade": "2",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 160.00"
    },
    {
        "Código Venda": "69917",
        "Data": "12/25/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Calça",
        "Quantidade": "2",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 340.00"
    },
    {
        "Código Venda": "69286",
        "Data": "12/22/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Gorro",
        "Quantidade": "2",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 160.00"
    },
    {
        "Código Venda": "69676",
        "Data": "12/24/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Gorro",
        "Quantidade": "4",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 320.00"
    },
    {
        "Código Venda": "69714",
        "Data": "12/24/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Cinto",
        "Quantidade": "2",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 400.00"
    },
    {
        "Código Venda": "69730",
        "Data": "12/24/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Gorro",
        "Quantidade": "2",
        "Valor Unitário": "R$ 80.00",
        "Valor Final": "R$ 160.00"
    },
    {
        "Código Venda": "69917",
        "Data": "12/25/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Calça",
        "Quantidade": "2",
        "Valor Unitário": "R$ 170.00",
        "Valor Final": "R$ 340.00"
    },
    {
        "Código Venda": "69999",
        "Data": "12/26/19",
        "ID Loja": "Shopping Eldorado",
        "Produto": "Camisa",
        "Quantidade": "3",
        "Valor Unitário": "R$ 120.00",
        "Valor Final": "R$ 360.00"
    },
    {
        "Código Venda": "70012",
        "Data": "12/27/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Tênis",
        "Quantidade": "1",
        "Valor Unitário": "R$ 250.00",
        "Valor Final": "R$ 250.00"
    },
    {
        "Código Venda": "70045",
        "Data": "12/28/19",
        "ID Loja": "BH Shopping",
        "Produto": "Jaqueta",
        "Quantidade": "1",
        "Valor Unitário": "R$ 350.00",
        "Valor Final": "R$ 350.00"
    },
    {
        "Código Venda": "70070",
        "Data": "12/28/19",
        "ID Loja": "Iguatemi Porto Alegre",
        "Produto": "Vestido",
        "Quantidade": "2",
        "Valor Unitário": "R$ 180.00",
        "Valor Final": "R$ 360.00"
    },
    {
        "Código Venda": "70101",
        "Data": "12/29/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Tênis",
        "Quantidade": "2",
        "Valor Unitário": "R$ 250.00",
        "Valor Final": "R$ 500.00"
    },
    {
        "Código Venda": "70130",
        "Data": "12/29/19",
        "ID Loja": "Shopping Eldorado",
        "Produto": "Cinto",
        "Quantidade": "1",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "70165",
        "Data": "12/30/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Gorro",
        "Quantidade": "3",
        "Valor Unitário": "R$ 75.00",
        "Valor Final": "R$ 225.00"
    },
    {
        "Código Venda": "70192",
        "Data": "12/30/19",
        "ID Loja": "BH Shopping",
        "Produto": "Camisa",
        "Quantidade": "2",
        "Valor Unitário": "R$ 120.00",
        "Valor Final": "R$ 240.00"
    },
    {
        "Código Venda": "70220",
        "Data": "12/31/19",
        "ID Loja": "Iguatemi Porto Alegre",
        "Produto": "Jaqueta",
        "Quantidade": "1",
        "Valor Unitário": "R$ 380.00",
        "Valor Final": "R$ 380.00"
    },
    {
        "Código Venda": "70250",
        "Data": "12/31/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Vestido",
        "Quantidade": "1",
        "Valor Unitário": "R$ 190.00",
        "Valor Final": "R$ 190.00"
    },
    {
        "Código Venda": "70300",
        "Data": "12/24/19",
        "ID Loja": "Shopping Eldorado",
        "Produto": "Jaqueta",
        "Quantidade": "5",
        "Valor Unitário": "R$ 350.00",
        "Valor Final": "R$ 1750.00"
    },
    {
        "Código Venda": "70301",
        "Data": "12/29/19",
        "ID Loja": "Shopping Eldorado",
        "Produto": "Meia",
        "Quantidade": "3",
        "Valor Unitário": "R$ 40.00",
        "Valor Final": "R$ 120.00"
    },
    {
        "Código Venda": "70302",
        "Data": "12/29/19",
        "ID Loja": "BH Shopping",
        "Produto": "Cinto",
        "Quantidade": "2",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 400.00"
    },
    {
        "Código Venda": "70303",
        "Data": "12/28/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Jaqueta",
        "Quantidade": "1",
        "Valor Unitário": "R$ 350.00",
        "Valor Final": "R$ 350.00"
    },
    {
        "Código Venda": "70304",
        "Data": "12/27/19",
        "ID Loja": "BH Shopping",
        "Produto": "Tênis",
        "Quantidade": "2",
        "Valor Unitário": "R$ 250.00",
        "Valor Final": "R$ 500.00"
    },
    {
        "Código Venda": "70305",
        "Data": "12/31/19",
        "ID Loja": "Iguatemi Porto Alegre",
        "Produto": "Calça",
        "Quantidade": "4",
        "Valor Unitário": "R$ 180.00",
        "Valor Final": "R$ 720.00"
    },
    {
        "Código Venda": "70306",
        "Data": "12/27/19",
        "ID Loja": "Shopping Eldorado",
        "Produto": "Camisa",
        "Quantidade": "1",
        "Valor Unitário": "R$ 120.00",
        "Valor Final": "R$ 120.00"
    },
    {
        "Código Venda": "70307",
        "Data": "12/25/19",
        "ID Loja": "Iguatemi Porto Alegre",
        "Produto": "Jaqueta",
        "Quantidade": "2",
        "Valor Unitário": "R$ 350.00",
        "Valor Final": "R$ 700.00"
    },
    {
        "Código Venda": "70308",
        "Data": "12/24/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Vestido",
        "Quantidade": "3",
        "Valor Unitário": "R$ 190.00",
        "Valor Final": "R$ 570.00"
    },
    {
        "Código Venda": "70309",
        "Data": "12/31/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Tênis",
        "Quantidade": "3",
        "Valor Unitário": "R$ 250.00",
        "Valor Final": "R$ 750.00"
    },
    {
        "Código Venda": "70310",
        "Data": "12/23/19",
        "ID Loja": "BH Shopping",
        "Produto": "Camisa",
        "Quantidade": "2",
        "Valor Unitário": "R$ 120.00",
        "Valor Final": "R$ 240.00"
    },
    {
        "Código Venda": "70311",
        "Data": "12/25/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Cinto",
        "Quantidade": "1",
        "Valor Unitário": "R$ 200.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "70312",
        "Data": "12/24/19",
        "ID Loja": "Shopping Recife",
        "Produto": "Sapato",
        "Quantidade": "2",
        "Valor Unitário": "R$ 300.00",
        "Valor Final": "R$ 600.00"
    },
    {
        "Código Venda": "70313",
        "Data": "12/26/19",
        "ID Loja": "Iguatemi Porto Alegre",
        "Produto": "Blusa",
        "Quantidade": "4",
        "Valor Unitário": "R$ 150.00",
        "Valor Final": "R$ 600.00"
    },
    {
        "Código Venda": "70314",
        "Data": "12/27/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Meia",
        "Quantidade": "5",
        "Valor Unitário": "R$ 40.00",
        "Valor Final": "R$ 200.00"
    },
    {
        "Código Venda": "70315",
        "Data": "12/27/19",
        "ID Loja": "Bourbon Shopping SP",
        "Produto": "Gorro",
        "Quantidade": "2",
        "Valor Unitário": "R$ 70.00",
        "Valor Final": "R$ 140.00"
    },
    {
        "Código Venda": "70316",
        "Data": "12/26/19",
        "ID Loja": "Shopping Eldorado",
        "Produto": "Vestido",
        "Quantidade": "1",
        "Valor Unitário": "R$ 190.00",
        "Valor Final": "R$ 190.00"
    },
    {
        "Código Venda": "70317",
        "Data": "12/30/19",
        "ID Loja": "Center Shopping Uberlândia",
        "Produto": "Tênis",
        "Quantidade": "1",
        "Valor Unitário": "R$ 250.00",
        "Valor Final": "R$ 250.00"
    },
    {
        "Código Venda": "70318",
        "Data": "12/30/19",
        "ID Loja": "Iguatemi Campinas",
        "Produto": "Sapato",
        "Quantidade": "3",
        "Valor Unitário": "R$ 300.00",
        "Valor Final": "R$ 900.00"
    },
    {
        "Código Venda": "70319",
        "Data": "12/24/19",
        "ID Loja": "BH Shopping",
        "Produto": "Camisa",
        "Quantidade": "4",
        "Valor Unitário": "R$ 120.00",
        "Valor Final": "R$ 480.00"
    }
]

console.log(
    data.filter(e => e["Centro de Distribuição"] === "CD Porto Alegre" && e["Tipo de Carga"] === "Materiais de Construção").reduce((acc, curr) => acc + curr["Peso (kg)"], 0)
)

console.log(
    data.filter(e => e["Centro de Distribuição"] === "CD Recife" && e["Tipo de Carga"] === "Bebidas").reduce((acc, curr) => acc + curr["Peso (kg)"], 0)
)

console.log(
    data.filter(e => e['Tipo de Carga'] === 'Alimentos').reduce((acc, curr) => acc + curr['Peso (kg)'], 0)
)

console.log(
    dataVendas.filter(e => e['Produto'] === 'Calça').reduce((acc, curr) => {
        const valorNumerico = parseFloat(
            curr['Valor Final'].replace('R$', '').replace(',', '.')
        );
        return acc + valorNumerico;
    }, 0)
)