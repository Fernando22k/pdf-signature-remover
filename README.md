# PDF Signature Remover

Script em Python para remover assinaturas digitais de arquivos PDF removendo o objeto **AcroForm**.

⚠️ Importante:
Este script remove apenas a **estrutura de assinatura digital do PDF**, não remove imagens ou marcas visuais da assinatura dentro do documento.

---

## Funcionalidades

* Remove assinaturas digitais baseadas em **AcroForm**
* Processa múltiplos PDFs automaticamente
* Gera novos arquivos sem alterar o original
* Processamento em lote de uma pasta

---

## Tecnologias utilizadas

* Python 3
* pypdf

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/pdf-signature-remover.git
```

Entre na pasta:

```bash
cd pdf-signature-remover
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Como usar

Edite o caminho da pasta no script:

```python
pasta_pdfs = r"C:\Users\SeuUsuario\Downloads\teste"
```

Execute:

```bash
python remover_assinatura.py
```

---

## Resultado

Arquivos com nome:

```
arquivo_assinado.pdf
```

serão convertidos para:

```
arquivo_sem_assinatura.pdf
```

---

## Observação importante

Este script remove apenas a estrutura técnica da assinatura digital no PDF.

Isso pode invalidar a assinatura digital e deve ser utilizado apenas para fins educacionais ou quando permitido legalmente.

---

## Licença

MIT License
