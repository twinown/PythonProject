def remove_url_anchor(url):
    return url if url.find('#')==-1 else url[0:url.find('#')]