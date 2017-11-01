import requests
package = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
r = requests.post('http://jsonplaceholder.typicode.com/posts', params=package)

json_data = r.json()
print(r.url)
print(json_data)
