import requests

res = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(res.status_code)
print(res.text)

res = requests.post('https://jsonplaceholder.typicode.com/posts',{
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  })
print(res)

res = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(res.text)

res = requests.patch('https://jsonplaceholder.typicode.com/posts/1',{'body':'many'})
print(res.text)

res = requests.put('https://jsonplaceholder.typicode.com/posts/1',{'body':'many'})
print(res.text)



