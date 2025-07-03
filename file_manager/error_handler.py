# src/file_manager/error_handler.py

class ErrorHandler:
    def __init__(self, output_file="erros.log"):
        self.errors = []
        self.output_file = output_file

    def report_error(self, error_type, message, line=None, column=None):
        """
        Registra um erro encontrado durante a compilação.
        """
        error_info = {
            "type": error_type,
            "message": message,
            "line": line,
            "column": column
        }
        self.errors.append(error_info)

    def has_errors(self):
        """
        Verifica se algum erro foi registrado.
        """
        return len(self.errors) > 0

    def write_errors_to_file(self):
        """
        Escreve todos os erros registrados em um arquivo.
        """
        if not self.has_errors():
            print(f"Nenhum erro encontrado. Nenhum arquivo '{self.output_file}' gerado.")
            return

        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("--- Relatório de Erros do Compilador File Manager ---\n\n")
            for error in self.errors:
                location = ""
                if error["line"] is not None and error["column"] is not None:
                    location = f" (Linha: {error['line']}, Coluna: {error['column']})"
                f.write(f"[{error['type']}]{location}: {error['message']}\n")
            f.write(f"\nTotal de erros encontrados: {len(self.errors)}\n")
        print(f"Erros encontrados. Relatório salvo em '{self.output_file}'.")

    def print_errors(self):
        """
        Imprime os erros no console.
        """
        if self.has_errors():
            print("\n--- ERROS ENCONTRADOS ---")
            for error in self.errors:
                location = ""
                if error["line"] is not None and error["column"] is not None:
                    location = f" (Linha: {error['line']}, Coluna: {error['column']})"
                print(f"[{error['type']}]{location}: {error['message']}")
            print("-------------------------")