mkdir -p ~/TestFiles/Downloads
mkdir -p ~/TestFiles/Documentos
mkdir -p ~/TestFiles/Imagens
mkdir -p ~/TestFiles/Downloads/temp
mkdir -p ~/TestFiles/Downloads/ArquivosCompactados
mkdir -p ~/TestFiles/Backup_Docs

echo "Diretórios de teste criados."

# 2. Crie arquivos PDF (Regra 1)
# PDF Grande (7MB - para testar tamanho)
dd if=/dev/urandom of=~/TestFiles/Downloads/documento_grande_report.pdf bs=1M count=7
# PDF Pequeno
dd if=/dev/urandom of=~/TestFiles/Downloads/relatorio_semanal.pdf bs=1K count=50
dd if=/dev/urandom of=~/TestFiles/Downloads/proposta_final.pdf bs=1K count=80

echo "Arquivos PDF criados."

# 3. Crie arquivos de imagem (Regra 2)
# Requer ImageMagick (instale com `sudo apt install imagemagick` ou `brew install imagemagick`)
convert -size 100x100 xc:red ~/TestFiles/Downloads/minha_foto_2025.jpeg
convert -size 50x50 xc:blue ~/TestFiles/Downloads/logo_empresa.png

echo "Arquivos de imagem criados."

# 4. Crie arquivos antigos em Downloads 
# Use 'touch -d' para definir uma data de criação antiga (Linux/macOS)
touch -d '2023-05-10 10:00:00' ~/TestFiles/Downloads/backup_antigo.zip
touch -d '2023-11-20 15:30:00' ~/TestFiles/Downloads/relatorio_velho.pdf
touch -d '2023-12-31 23:59:59' ~/TestFiles/Downloads/trabalho_faculdade.docx
# Um arquivo antigo que já está tageado para testar a regra 1 se rodar duas vezes
# A data de modificação real do arquivo será a de 2023-01-01
touch -d '2023-01-01 12:00:00' ~/TestFiles/Downloads/[Downloads]documento_antigo_pdf.pdf

echo "Arquivos antigos criados."

# 5. Crie arquivos de documentos com tamanhos variados
# Pequeno (P): até 100 KB
dd if=/dev/urandom of=~/TestFiles/Downloads/carta_curta.doc bs=1K count=50
dd if=/dev/urandom of=~/TestFiles/Downloads/nota.txt bs=1K count=10
# Médio (M): 101 KB a 1024 KB
dd if=/dev/urandom of=~/TestFiles/Downloads/documento_medio.docx bs=1K count=500
# Grande (G): acima de 1024 KB
dd if=/dev/urandom of=~/TestFiles/Downloads/relatorio_anual.txt bs=1M count=2

echo "Arquivos de documentos com tamanhos variados criados."

# 6. Crie arquivos compactados
# Crie um diretório temporário e depois o compacte
mkdir -p /tmp/temp_zip_content
echo "Conteúdo de um arquivo dentro do zip." > /tmp/temp_zip_content/file1.txt
zip -r ~/TestFiles/Downloads/arquivos_do_projeto.zip /tmp/temp_zip_content
rm -rf /tmp/temp_zip_content # Limpa o diretório temporário

# Para .rar, você precisaria do `rar` instalado e uma licença, então vamos focar no zip para simplicidade
# Se quiser testar .rar, crie um dummy:
dd if=/dev/urandom of=~/TestFiles/Downloads/fotos_viagem.rar bs=1K count=200

echo "Arquivos compactados criados."

# 7. Crie um arquivo com data de criação recente
# A data atual do sistema será usada, ativando a regra se for 2025-07-07 ou posterior
touch ~/TestFiles/Downloads/novo_download_hoje.pdf 

echo "Arquivo de novo download criado."

# 8. Crie arquivos temporários e de log 
dd if=/dev/urandom of=~/TestFiles/Downloads/temp_file_01.tmp bs=1K count=10
dd if=/dev/urandom of=~/TestFiles/Downloads/temp_log_02.log bs=1K count=30
dd if=/dev/urandom of=~/TestFiles/Downloads/big_log_file.log bs=1K count=70 # Não deve ser excluído (tamanho > 50KB)

echo "Arquivos temporários e de log criados."

echo -e "\nTodos os arquivos de teste foram gerados em ~/TestFiles/Downloads/"
ls -lh ~/TestFiles/Downloads/