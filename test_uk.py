from tps import download, Handler
from tps.content.ops import find
from tps.modules import Emphasizer

# mkdir /home/yehor/.tps && cp data/stress.dict /home/yehor/.tps/stress.dict
stress_dict = find("stress.dict", raise_exception=True)

emphasizer = Emphasizer((stress_dict, "plane"))
text = "Режими – це в російських в'язницях. Сказав Матвій.".lower()
x = emphasizer.process_text(text)
print(x)

# handler = Handler("uk")
# text = "Режими – це в російських в'язницях. Сказав Матвій."

# result = handler.process_text(text, keep_delimiters=False)
# print(result)
