import pandas as pd

def data_cleaning(df):
    df = df.copy()

    df.columns = ( # normalizuje tylko nazwy kolumn
    df.columns
    .str.strip()      # usuwa spacje
    .str.lower()      # lowercase
    .str.replace(" ", "_")  # snake_case
)
    text_cols = df.select_dtypes(include=["object", "string"]).columns
    if len(text_cols) == 0:
        return df

    # === 3. Normalizacja produktu ===
    if "produkt" in df.columns:
        df["produkt"] = df["produkt"].str.lower()

    # === 4. Normalizacja miast ===
    if "miasto" in df.columns:
        df["miasto"] = df["miasto"].str.title()

    # === 5. Typy danych ===
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], errors="coerce")

    mapa_normalizacyjna_produkt = {
    "apple": "Apple",
    "apple inc": "Apple",
    "samsung": "Samsung",
    "samsung electronics": "Samsung",
    "xiaomi": "Xiaomi"    
}
    mapa_normalizacyjna_miast = {
    "wrocław": "Wrocław",
    "POZNAŃ": "Poznań"
    }
    df["produkt"] = df["produkt"].map(mapa_normalizacyjna_produkt).fillna(df["produkt"])
    df["sklep"] = df["sklep"].map(mapa_normalizacyjna_miast).fillna(df["sklep"])

    # typy
    df["data_sprzedaży"] = pd.to_datetime(df["data_sprzedaży"], errors="coerce")
    df["ilość"] = pd.to_numeric(df["ilość"], errors="coerce")
    df["cena"] = pd.to_numeric(df["cena"], errors="coerce")

# czyszczenie
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def sortowanie(df):
    df = df.sort_values(["data_sprzedaży", "produkt"]).reset_index(drop=True)
    return df