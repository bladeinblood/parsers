import requests

value_question = ['whsOnd zHQkBf': 'value']

r = requests.post('https://docs.google.com/forms/d/e/1FAIpQLSeZVH8NA1tRss2pqIOuU586wj4kqcE46Sf4NDhBwE-LlMLoOA/viewform', data=value_question)
print(r.text)
