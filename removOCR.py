import os
from pypdf import PdfReader, PdfWriter


def remover_assinaturas_pdf(input_path, output_path):
    """
    Remove assinaturas digitais de um arquivo PDF removendo o objeto /AcroForm.

    Atenção:
    Isso remove apenas a estrutura de assinatura do PDF,
    não remove imagens ou marcas visuais presentes no documento.
    """

    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Copiar todas as páginas do PDF original
    for page in reader.pages:
        writer.add_page(page)

    # Remover AcroForm (onde ficam campos de assinatura)
    if "/AcroForm" in writer._root_object:
        del writer._root_object["/AcroForm"]

    # Salvar novo arquivo
    with open(output_path, "wb") as f:
        writer.write(f)


def processar_pasta(pasta):
    """
    Procura PDFs assinados dentro de uma pasta
    e gera novas versões sem o campo de assinatura.
    """

    for arquivo in os.listdir(pasta):

        if arquivo.lower().endswith("_assinado.pdf"):

            caminho_entrada = os.path.join(pasta, arquivo)

            novo_nome = arquivo.replace(
                "_assinado.pdf",
                "_sem_assinatura.pdf"
            )

            caminho_saida = os.path.join(pasta, novo_nome)

            print(f"Removendo assinatura de: {arquivo}")

            remover_assinaturas_pdf(
                caminho_entrada,
                caminho_saida
            )


if __name__ == "__main__":

    pasta_pdfs = r"C:\Users\Avell\Downloads\teste" 

    processar_pasta(pasta_pdfs)

    print("Processo finalizado.")
