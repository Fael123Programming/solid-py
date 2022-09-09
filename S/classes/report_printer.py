from S.classes.print_mode import PrintMode


class ReportPrinter:

    @staticmethod
    def print(report: str, mode: PrintMode):
        match mode:
            case PrintMode.TERMINAL:
                print(report)
            case PrintMode.TXT_FILE:
                with open('report.txt', 'w') as file:
                    file.write(report)
