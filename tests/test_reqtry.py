from reqtry import request, get, post, put, patch, delete, options, head


def test_request():
    r = request("GET", 'https://httpbin.org/get')
    assert r.status_code == 200


def test_get():
    r = get('https://httpbin.org/get')
    assert r.status_code == 200


def test_post():
    r = post('https://httpbin.org/post', data={"hello": "world"})
    assert r.status_code == 200


def test_put():
    r = put('https://httpbin.org/put', data={"hello": "world"})
    assert r.status_code == 200


def test_patch():
    r = patch('https://httpbin.org/patch', data={"hello": "world"})
    assert r.status_code == 200


def test_delete():
    r = delete('https://httpbin.org/delete')
    assert r.status_code == 200
