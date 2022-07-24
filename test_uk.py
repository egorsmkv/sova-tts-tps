from tps import download, Handler
from tps.content.ops import find
from tps.modules import Emphasizer

try:
    stress_dict = find("stress_uk.dict", raise_exception=True)
except FileNotFoundError:
    stress_dict = download("stress_uk.dict")

emphasizer = Emphasizer((stress_dict, "plane"))
text = "Режими – це в російських в'язницях. Сказав Матвій.".lower()
x = emphasizer.process_text(text)
print(x)

# handler = Handler("uk")
# text = "Режими – це в російських в'язницях. Сказав Матвій."

# result = handler.process_text(text, keep_delimiters=False)
# print(result)
