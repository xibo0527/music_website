def global_text(request):
    current_url = request.path
    return locals()