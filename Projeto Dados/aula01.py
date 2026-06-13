import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("aluno.csv", encoding="utf-8")
print(df.head())
print(df.describe())
df["MÉDIA"] = df["MÉDIA"].str.replace(",", ".").astype(float)
# grafico de barras 
plt.hist(df["MÉDIA"], bins=10, edgecolor="black")
plt.title("Distribuição das médias dos Alunos")
plt.xlabel("Média")
plt.ylabel("Frequência")
plt.grid(axis="y", alpha=0.75)
plt.show()
# grafico de pizza
labels = ["Aprovados", "Reprovados"]
sizes = [len(df[df["MÉDIA"] >= 6]), len(df[df["MÉDIA"] < 6])]
colors = ["#4CAF50", "#F44336"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
plt.title("Proporção de Alunos Aprovados e Reprovados")
plt.axis("equal")
plt.show()  
# DISPERSAO
plt.figure(figsize=(8, 5))
plt.scatter(df["MÉDIA"], df["N2"], alpha=0.7)
plt.title("Relação entre Média e N2")
plt.xlabel("MÉDIA")
plt.ylabel("N2")
plt.grid(True)

plt.show()