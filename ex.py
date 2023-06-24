from re import search

regex = r'[a-zA-Z]{2}\d{6,}'

ex = '/title/tt1564367/?ref_=bo_cso_table_3'

print(search(regex,ex).group(0))