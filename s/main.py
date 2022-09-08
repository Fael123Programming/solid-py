from s.classes.report_creator import ReportCreator

# ReportCompile is liable for fetching and processing the data.
# ReportPrinter is liable for showing it in a specified way.

if __name__ == "__main__":
    report_creator = ReportCreator()
    report_creator.compile()
    report_creator.print()
