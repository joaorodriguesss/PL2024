#1/user/bin/env python3
import re

f = open("C:/Users/35193/Documents/GitHub/PL2024/AulasTP/musica2024/musica/_-cantaCanta.lyr") 
txt = f.read()

metadados, body = re.split('\n\n', txt, maxsplit=1)
metadados = dict(re.findall (r'(\w+)\s*:\s*(.+)\s',txt))
# metadados = dict([(g[0], g[1]) for g in re.findall (r'(\w+)\s*:\s*(.+)\s',txt)])
print(metadados)

out = open('out/' + re.sub(r'.lyr'))

print(
    f"""
<body>
    <h1> {metadados} 'title' </h1>
    <pre> {body} </pre>
</body>
    """
)