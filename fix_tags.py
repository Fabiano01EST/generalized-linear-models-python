import json
import re
import os

# Garante pasta docs
os.makedirs("docs", exist_ok=True)

with open('Gamma_model.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

html_parts = []

html_parts.append('''<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Relatório</title>

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
  background: #f7f7f7;
  margin: 0;
}

.container {
  max-width: 1000px;
  margin: 40px auto;
  padding: 20px;
}

.card {
  background: white;
  border-radius: 8px;
  padding: 25px;
  margin-bottom: 25px;
  border: 1px solid #e5e5e5;
}

h1 {
  border-bottom: 2px solid #eaeaea;
  padding-bottom: 5px;
}

h2 {
  color: #2c3e50;
}

h3 {
  color: #444;
}

.markdown-cell {
  line-height: 1.6;
  color: #333;
}

/* ===== TABELA ===== */
.markdown-cell table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
  font-size: 14px;
  border-left: 3px solid #3498db;
}

.markdown-cell th {
  background: #f0f0f0;
  padding: 11px;
  text-align: left;
  border-bottom: 2px solid #dcdcdc;
 white-space: nowrap;
}

.markdown-cell td {
  padding: 10px;
  border-bottom: 1px solid #eaeaea;
  vertical-align: top;
  word-break: break-word;
}

.markdown-cell tr:nth-child(even) {
  background: #fafafa;
}

/* ===== OUTPUT ===== */
.output {
  background: #fcfcfc;
  border-left: 3px solid #3498db;
  padding: 10px;
  margin-top: 10px;
  overflow-x: auto;
}

.output table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.output th {
  background: #f0f0f0;
  padding: 6px;
}

.output td {
  padding: 6px;
  border: 1px solid #ddd;
}

/* ===== CÓDIGO ===== */
.code-block {
  background: #f5f5f5;
  border-left: 3px solid #3498db;
  padding: 10px;
  overflow-x: auto;
}

pre {
  margin: 0;
  white-space: pre-wrap;
}

img {
  max-width: 100%;
  border-radius: 6px;
}

/* ===== BOTÃO ===== */
.toggle-btn {
  background: #3498db;
  color: white;
  border: none;
  padding: 5px 12px;
  cursor: pointer;
  border-radius: 4px;
  font-size: 12px;
}

.toggle-btn:hover {
  background: #2c80b4;
}
</style>

</head>

<body>
<div class="container">
''')

# ===== PROCESSADOR MARKDOWN MANUAL =====
def process_markdown(text):

    # TITULOS
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # NEGRITO
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

    lines = text.split("\n")
    html = []
    i = 0

    while i < len(lines):

        # ===== DETECTA TABELA =====
        if "|" in lines[i]:
            table_lines = []

            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1

            if len(table_lines) > 1:
                header = table_lines[0]
                rows = table_lines[2:]

                html.append("<table>")
                html.append("<thead><tr>")

                for col in header.split("|")[1:-1]:
                    html.append(f"<th>{col.strip()}</th>")

                html.append("</tr></thead>")
                html.append("<tbody>")

                for row in rows:
                    html.append("<tr>")
                    for col in row.split("|")[1:-1]:
                        html.append(f"<td>{col.strip()}</td>")
                    html.append("</tr>")

                html.append("</tbody></table>")

        else:
            if lines[i].strip() != "":
                html.append(f"<p>{lines[i]}</p>")
            i += 1

    return "\n".join(html)


# ===== LOOP PRINCIPAL =====
for cell in nb['cells']:

    # MARKDOWN
    if cell['cell_type'] == 'markdown':
        src = ''.join(cell['source'])
        src = process_markdown(src)

        html_parts.append(f'<div class="card markdown-cell">{src}</div>')

    # CODE
    elif cell['cell_type'] == 'code':
        source = ''.join(cell['source'])

        html_parts.append(f'''
        <div class="card">
          <button class="toggle-btn" onclick="toggleCode(this)">▶ Mostrar código</button>
          <div class="code-block" style="display:none;">
            <pre><code>{source}</code></pre>
          </div>
        ''')

        for output in cell.get('outputs', []):

            if output.get('output_type') == 'stream':
                text = ''.join(output.get('text', []))
                html_parts.append(f'<div class="output"><pre>{text}</pre></div>')

            elif output.get('output_type') in ['execute_result', 'display_data']:
                data = output.get('data', {})

                if 'text/html' in data:
                    html_parts.append(f'''
                    <div class="output">
                      {"".join(data['text/html'])}
                    </div>
                    ''')

                elif 'image/png' in data:
                    img = data['image/png']
                    html_parts.append(f'''
                    <div class="output">
                      <img src="data:image/png;base64,{img}">
                    </div>
                    ''')

                elif 'text/plain' in data:
                    text = ''.join(data['text/plain'])
                    html_parts.append(f'<div class="output"><pre>{text}</pre></div>')

        html_parts.append('</div>')

# FINAL HTML
html_parts.append('''
</div>

<script>
function toggleCode(btn) {
  var div = btn.nextElementSibling;
  if (div.style.display === "none") {
    div.style.display = "block";
    btn.textContent = "▼ Ocultar código";
  } else {
    div.style.display = "none";
    btn.textContent = "▶ Mostrar código";
  }
}
</script>

</body>
</html>
''')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_parts))

print("HTML gerado!")