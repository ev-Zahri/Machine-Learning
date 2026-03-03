import requests
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def fetch_and_plot_cot():
    url = "https://www.cftc.gov/dea/futures/deanybtsf.htm"
    response = requests.get(url)
    text = response.text

    # 1. Mencari blok data "USD INDEX"
    # Kita ambil teks mulai dari USD INDEX sampai garis pembatas berikutnya
    pattern = re.compile(r"USD INDEX - ICE FUTURES U.S\..*?TOTAL TRADERS:", re.DOTALL)
    match = pattern.search(text)
    
    if not match:
        print("Data USD INDEX tidak ditemukan.")
        return

    block = match.group(0)

    # 2. Ekstrak Open Interest
    oi_match = re.search(r"OPEN INTEREST:\s+([\d,]+)", block)
    open_interest = int(oi_match.group(1).replace(',', '')) if oi_match else 0

    # 3. Ekstrak Baris "COMMITMENTS" (Baris angka pertama di bawah header)
    # Kita cari baris yang berisi deretan angka setelah kata COMMITMENTS
    lines = block.split('\n')
    commitments_row = ""
    for i, line in enumerate(lines):
        if "COMMITMENTS" in line:
            commitments_row = lines[i+1]
            break
    
    # Ambil semua angka dari baris tersebut
    values = re.findall(r'(\d{1,3}(?:,\d{3})*)', commitments_row)
    values = [int(v.replace(',', '')) for v in values]

    # Pemetaan berdasarkan struktur laporan CFTC:
    # 0: Non-Comm Long, 1: Non-Comm Short, 2: Spreads
    # 3: Comm Long, 4: Comm Short
    # 5: Total Long, 6: Total Short
    # 7: Non-Rept Long, 8: Non-Rept Short
    
    data = {
        'Category': ['Non-Commercial', 'Non-Commercial', 'Commercial', 'Commercial', 'Non-Reportable', 'Non-Reportable'],
        'Position': ['Long', 'Short', 'Long', 'Short', 'Long', 'Short'],
        'Contracts': [values[0], values[1], values[3], values[4], values[7], values[8]]
    }

    df = pd.DataFrame(data)
    
    # Hitung Net Position untuk informasi tambahan
    print(f"USD INDEX - Open Interest: {open_interest:,}")
    print("-" * 30)
    for cat in ['Non-Commercial', 'Commercial', 'Non-Reportable']:
        long = df[(df['Category'] == cat) & (df['Position'] == 'Long')]['Contracts'].values[0]
        short = df[(df['Category'] == cat) & (df['Position'] == 'Short')]['Contracts'].values[0]
        print(f"{cat} Net Position: {long - short:,}")

    # 4. Visualisasi dengan Seaborn
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    plot = sns.barplot(
        data=df, 
        x='Category', 
        y='Contracts', 
        hue='Position', 
        palette={'Long': '#2ecc71', 'Short': '#e74c3c'}
    )
    
    plt.title(f'USD INDEX Commitment of Traders - Open Interest: {open_interest:,}', fontsize=15)
    plt.ylabel('Number of Contracts')
    plt.xlabel('Trader Category')
    
    # Tambahkan label angka di atas bar
    for p in plot.patches:
        plot.annotate(format(p.get_height(), ',.0f'), 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha = 'center', va = 'center', 
                      xytext = (0, 9), 
                      textcoords = 'offset points')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    fetch_and_plot_cot()