def auth_headers(request):
    token = request.session.get('token')

    if not token:
        return {}

    return {
        "Authorization": f"Bearer {token}"
    }
