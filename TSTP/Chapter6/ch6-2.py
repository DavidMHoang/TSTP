prompt = """Fill in the blank
Yesterday I wrote a [response_one].
I sent it to [response_two]!
"""

print(prompt)

response_one = input("response_one: ")
response_two = input("response_two: ")

new = """Yesterday I wrote a {}.
I sent it to {}!
""".format(response_one,
           response_two)

print(new)
