def formaterToNumber(df):
    return df.str.replace('R\$ ?', '', regex=True).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)