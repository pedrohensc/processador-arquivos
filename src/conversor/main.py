import typer
from pathlib import Path
from PIL import Image
import magic

app = typer.Typer(help="Conversor de imagens – converte arquivos entre formatos como JPG, PNG, WEBP, etc.")


@app.command()
def converter(
    entrada: str = typer.Argument(..., help="Caminho do arquivo de entrada"),
    saida: str = typer.Argument(..., help="Caminho do arquivo convertido (com extensão desejada)")
):
    """
    Converte uma imagem para outro formato.
    Exemplo:
        conversor imagem.jpg imagem.png
    """

    caminho_entrada = Path(entrada)
    caminho_saida = Path(saida)

    # 1. Verificar se existe
    if not caminho_entrada.exists():
        typer.secho("❌ Arquivo de entrada não encontrado.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # 2. Detectar tipo de arquivo com python-magic
    tipo = magic.from_file(str(caminho_entrada), mime=True)
    typer.echo(f"🔎 Tipo detectado: {tipo}")

    # 3. Abrir imagem
    try:
        img = Image.open(caminho_entrada)
    except Exception as e:
        typer.secho(f"❌ Erro ao abrir imagem: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # 4. Converter e salvar
    try:
        img.convert("RGB").save(caminho_saida)
        typer.secho(f"✅ Imagem convertida com sucesso!\n➡ Arquivo salvo em: {caminho_saida}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Erro ao salvar imagem convertida: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
