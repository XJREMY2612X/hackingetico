# 2. Clase Vulnerability[cite: 10]
class Vulnerability:
    def __init__(self, title, owasp_category, severity):
        self.title = title
        self.owasp_category = owasp_category
        self.severity = severity

    def summary(self):
        return f"[{self.severity}] {self.title} (Categoría: {self.owasp_category})"
