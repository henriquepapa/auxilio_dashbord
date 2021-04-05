import pandas as pd
import os
from tqdm import tqdm


# escrita local
def carga():
    for file in tqdm(os.listdir('base/csv')):
        df = pd.read_csv(('base/csv/' + file), sep=';', encoding='ISO-8859-1',
                         usecols=['MÊS DISPONIBILIZAÇÃO', 'UF', 'CÓDIGO MUNICÍPIO IBGE', 'NOME MUNICÍPIO', 'PARCELA',
                                  'OBSERVAÇÃO', 'VALOR BENEFÍCIO'])
        df.to_parquet('base/parquet/' + file.replace('csv', '.parquet'))
