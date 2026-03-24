import json
import re

with open('Gamma_model.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

html_parts = []

html_parts.append('''<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Html</title>
<style>
  body { font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 20px; background: #fff; }
  .cell { margin-bottom: 30px; }
  .code-block { background: #f5f5f5; border-left: 4px solid #ccc; padding: 10px; border-radius: 4px; overflow-x: auto; }
  pre { margin: 0; white-space: pre-wrap; }
  .toggle-btn { background: #4CAF50; color: white; border: none; padding: 5px 12px; cursor: pointer; border-radius: 4px; margin-bottom: 6px; font-size: 13px; }
  .toggle-btn:hover { background: #45a049; }
  .output { background: #fff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; margin-top: 6px; overflow-x: auto; }
  img { max-width: 100%; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ddd; padding: 6px; text-align: left; }
  th { background: #f0f0f0; }
  .markdown-cell { line-height: 1.6; }
  h1,h2,h3 { color: #333; }
</style>
</head>
<body>
''')

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        src = ''.join(cell['source'])
        src = re.sub(r'^### (.+)$', r'<h3>\1</h3>', src, flags=re.MULTILINE)
        src = re.sub(r'^## (.+)$', r'<h2>\1</h2>', src, flags=re.MULTILINE)
        src = re.sub(r'^# (.+)$', r'<h1>\1</h1>', src, flags=re.MULTILINE)
        src = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', src)
        src = src.replace('\n', '<br>')
        html_parts.append(f'<div class="cell markdown-cell">{src}</div>')

    elif cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        html_parts.append(f'''<div class="cell">
  <button class="toggle-btn" onclick="toggleCode(this)">▶ Mostrar código</button>
  <div class="code-block" style="display:none;">
    <pre><code>{source}</code></pre>
  </div>''')

        for output in cell.get('outputs', []):
            if output.get('output_type') in ['stream']:
                text = ''.join(output.get('text', []))
                html_parts.append(f'<div class="output"><pre>{text}</pre></div>')
            elif output.get('output_type') in ['execute_result', 'display_data']:
                data = output.get('data', {})
                if 'text/html' in data:
                    html_parts.append(f'<div class="output">{"".join(data["text/html"])}</div>')
                elif 'image/png' in data:
                    img = data['image/png']
                    html_parts.append(f'<div class="output"><img src="data:image/png;base64,{img}"/></div>')
                elif 'text/plain' in data:
                    text = ''.join(data['text/plain'])
                    html_parts.append(f'<div class="output"><pre>{text}</pre></div>')

        html_parts.append('</div>')

html_parts.append('''<script>
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
</body></html>
''')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_parts))

print('Pronto!')