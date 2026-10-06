from pathlib import Path
import html,json
root=Path(__file__).resolve().parents[1]
documents=json.loads((root/"content/documents.json").read_text())
rows=[]
for doc in documents:
    esc=lambda key:html.escape(doc[key],quote=True)
    tags="".join("<span>"+html.escape(item)+"</span>" for item in doc["items"])
    rows.append('<a class="document-row" href="'+esc("url")+'"><span class="document-number">'+esc("id")+'</span><div class="document-copy"><p class="document-label">'+esc("label")+'</p><h2>'+esc("title")+'</h2><p>'+esc("description")+'</p><div class="document-tags">'+tags+'</div></div><span class="document-arrow" aria-hidden="true">↗</span></a>')
template=(root/"content/index.template.html").read_text()
(root/"index.html").write_text(template.replace("{{DOCUMENTS}}",chr(10).join(rows)).replace("{{COUNT}}",str(len(documents))))
print("Generated document index:",len(documents))
