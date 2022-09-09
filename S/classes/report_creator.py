from S.classes.print_mode import PrintMode
from S.classes.report_compiler import ReportCompiler
from S.classes.report_printer import ReportPrinter


class ReportCreator:

    def __init__(self):
        self._report = None

    def compile(self):
        with ReportCompiler() as rc:
            self._report = rc.compile()

    def print(self):
        rp = ReportPrinter()
        rp.print(self._report, PrintMode.TXT_FILE)
